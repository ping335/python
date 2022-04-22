"""
click.pass_context(f)
    Указывает, что в качестве первого аргумента callback-а будет передан текущий объект контекста.

click.make_pass_decorator(object_type, ensure=False)
    object_type – тип объекта для передачи
    ensure      – если истина, то будет создан новый объект и сохранен в контексте
"""

import hashlib

import click


class Application:
    def __init__(self, source, alg_name='md5', length=None, verbose=False):
        self.source = source
        self.alg_name = alg_name
        self.length = length
        self.verbose = verbose

    def _create_hash_object(self):
        """Возвращает хеш-объект для указанного алгоритма."""
        if self.alg_name in hashlib.algorithms_guaranteed:
            return getattr(hashlib, self.alg_name)() # hashlib.md5()
        return hashlib.new(self.alg_name)

    def check(self, hash_sum):
        """Возвращает истину, если хеш сумма текущего файла совпадает с переданной, иначе ложь."""
        return self.get_hash() == hash_sum

    def get_hash(self):
        """Возвращает хеш сумму по файлу."""
        hash_obj = self._create_hash_object()
        pos = self.source.tell()

        for chunk in iter(lambda: self.source.read(4096), b''):
            hash_obj.update(chunk)

        self.source.seek(pos)

        if self.alg_name.startswith('shake_'):
            return hash_obj.hexdigest(self.length)

        return hash_obj.hexdigest()


pass_app = click.make_pass_decorator(Application)


def validate_length(ctx, param, value):
    alg_name = ctx.params.get('alg', '')

    if not alg_name.startswith('shake_'):
        return None

    if value is None or value <= 0:
        raise click.BadOptionUsage(param, 'For algorithms shake_128 and shake_256 param length is required')

    return value


@click.group()
@click.version_option()
@click.argument('source', type=click.File(mode='rb')) # позиционный аргумент
@click.option(
    '-a', '--alg',
    type=click.Choice(hashlib.algorithms_available),
    default='md5',
    help='Hashing algorithm.',
    is_eager=True
) # именованный аргумент
@click.option(
    '-l', '--length',
    type=int,
    help='Value of variable length digests for shake_128 and shake_256.',
    callback=validate_length
)
@click.option('-v', '--verbose', is_flag=True)
@click.pass_context
def cli(ctx, source, alg, length, verbose):
    ctx.obj = Application(source, alg, length, verbose)


@cli.command()
@pass_app
def create(app):
    """Displays the hash sum of the file."""
    if app.verbose:
        click.echo(f'File: {click.format_filename(app.source.name)}')
        click.echo(f'Used: {app.alg_name}')
        click.echo(f'Hash: ', nl=False)

    click.echo(app.get_hash())


@cli.command()
@click.argument('source_sum')
@pass_app
def check(app, source_sum):
    """Checking the hash sum of the file."""
    if app.verbose:
        click.echo(f'File: {click.format_filename(app.source.name)}')
        click.echo('Status: ', nl=False)

    if app.check(source_sum):
        click.secho('OK', fg='green')
    else:
        click.secho('Error', fg='red')
