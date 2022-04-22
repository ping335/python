import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, joinedload


@sa.event.listens_for(sa.engine.Engine, 'connect')
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute('PRAGMA case_sensitive_like = 1')
    cursor.close()


engine = sa.create_engine('sqlite://', echo=True)
# engine = sa.create_engine('mysql+pymysql://root:toor@localhost/demo', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(50), nullable=False)
    contacts = relationship('Contact', backref='user', lazy='dynamic')

    def __repr__(self):
        return f'<{self.__class__.__name__}(id={self.id})>'


class Contact(Base):
    __tablename__ = 'contact'
    
    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.ForeignKey('user.id'), nullable=False)
    name = sa.Column(sa.String(50), nullable=False)
    value = sa.Column(sa.String(255), nullable=False)


class GroupStudents(Base):
    __tablename__ = 'group_students'

    group_id = sa.Column(sa.ForeignKey('group.id'), primary_key=True)
    student_id = sa.Column(sa.ForeignKey('student.id'), primary_key=True)
    student = relationship('Student', backref='groups')
    is_active = sa.Column(sa.Boolean, default=True, nullable=False)


class Group(Base):
    __tablename__ = 'group'

    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String(50), nullable=False)
    students = relationship('GroupStudents', backref='group')

    def add_student(self, student):
        """Добавляет студента в группу."""
        self.students.append(GroupStudents(student=student))


class Student(Base):
    __tablename__ = 'student'

    id = sa.Column(sa.Integer, primary_key=True)
    firstname = sa.Column(sa.String(50), nullable=False)
    lastname = sa.Column(sa.String(50), nullable=False)


Base.metadata.create_all(engine)


group_python = Group(title='Python')
group_php = Group(title='PHP')

student_1 = Student(firstname='Василий', lastname='Васильев')
student_2 = Student(firstname='Петр', lastname='Петров')

# group_python.students.append(GroupStudents(student=student_1))
# group_python.students.append(GroupStudents(student=student_2, is_active=False))
group_python.add_student(student_1)
group_python.add_student(student_2)

group_php.add_student(student_2)

session.add_all([group_python, group_php])
session.commit()

for accos in student_2.groups:
    print('=>', accos.group.title)


user_1 = User(name='Вася')
print('=> PK:', user_1.id) # PK: None

email = Contact(name='email', value='vasya@example.com')
vk = Contact(name='vk', value='https://vk.com/vasya')
user_1.contacts.append(email)
user_1.contacts.append(vk)

session.add(user_1)
session.commit()

print('=> PK:', user_1.id) # PK: 1

for c in user_1.contacts:
    print(c.user.name)


# todo: Способы загрузки связных коллекций

session.add_all([
    User(name='Петя', contacts=[
        Contact(name='phone', value='+70123456789'),
        Contact(name='email', value='petya@example.com'),
    ]),
    User(name='Даша', contacts=[
        Contact(name='phone', value='+79876543210'),
        Contact(name='email', value='dasha@example.com'),
    ]),
])
session.commit()

print('===============================>')


for user in session.query(User):
    print('=>', user.name)
    print('=>', type(user.contacts))

    for contact in user.contacts.filter(Contact.name == 'phone'):
        print('=>', contact.name, contact.value)


# todo: API запросов

q = (
    session.query(User)
    .filter(User.id == Contact.user_id)
    .filter_by(name='Петя')
    # .filter(Contact.name == 'email', Contact.name == 'phone')
    # .filter(sa.and_(Contact.name == 'email', Contact.name == 'phone'))
    # .filter(sa.or_(Contact.name == 'email', Contact.name == 'phone'))
    # .filter(Contact.name.in_(['email', 'phone']))
    # .filter(Contact.name.like('ph%'))
)

# .order_by() sa.desc()
# .limit()
# .offset()

# .count()
# .exists()

print(q.all())

# print(q.get(1))
# print(q.get(4))
# print(q.all())
# print(q.first())
# print(q.filter(User.name == 'Кирилл').one())
# print(q.filter(User.name == 'Кирилл').one_or_none())
# print(q.filter(User.name == 'Вася').one_or_none())
# print(q.one_or_none())

# print(session.query(User.id, User.name).filter(User.name == 'Вася').scalar())


print(session.query(Contact).filter_by(name='phone').count())

q = session.query(Contact).filter_by(name='instagram')
print(session.query(q.exists()).scalar())
