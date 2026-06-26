# Required Structures
users = {
    'jperez': {
        'password': '1234',
        'rol': 'student',
        'name': 'Juan Pérez'
    },
    'dromo': {
        'password': '1234',
        'rol': 'student',
        'name': 'Daniela Romo'
    },
    'mjuarez': {
        'password': '1234',
        'rol': 'student',
        'name': 'Mauricio Juárez'
    },
    'mlopez': {
        'password': '1234',
        'rol': 'student',
        'name': 'María López'
    },
    'euc': {
        'password': '1234',
        'rol': 'student',
        'name': 'Ernesto Uc'
    },
    'cbalam': {
        'password': '1234',
        'rol': 'student',
        'name': 'Carlos Balam'
    },
    'jpedrozo': {
        'password': '1234',
        'rol': 'professor',
        'name': 'Jorge Pedrozo'
    },
    'dgamboa': {
        'password': '1234',
        'rol': 'coordinator',
        'name': 'Didier Gamboa'
    }
}

subjects = (
    "Discrete Mathematics",
    "Programming",
    "English II",
    "Differential Calculus",
    "Probability and Statistics",
    "Computer and Server Architecture",
    "Socio-Emotional Skills and Conflict Management"
)

notes = {
    'jperez': {
        'Discrete Mathematics': 8.5,
        'Programming': 9.2,
        'English II': 9.0,
        'Differential Calculus': 7.8,
        'Probability and Statistics': 8.3,
        'Computer and Server Architecture': 6.8,
        'Socio-Emotional Skills and Conflict Management': 9.5
    },
    'dromo': {
        'Discrete Mathematics': 9.0,
        'Programming': 6.7,
        'English II': 9.4,
        'Differential Calculus': 6.2,
        'Probability and Statistics': 9.1,
        'Computer and Server Architecture': 6.5,
        'Socio-Emotional Skills and Conflict Management': 9.8
    },
    'mjuarez': {
        'Discrete Mathematics': 7.5,
        'Programming': 8.0,
        'English II': 8.5,
        'Differential Calculus': 7.0,
        'Probability and Statistics': 7.8,
        'Computer and Server Architecture': 6.2,
        'Socio-Emotional Skills and Conflict Management': 8.9
    },
    'mlopez': {
        'Discrete Mathematics': 9.5,
        'Programming': 9.8,
        'English II': 9.2,
        'Differential Calculus': 9.0,
        'Probability and Statistics': 9.6,
        'Computer and Server Architecture': 9.4,
        'Socio-Emotional Skills and Conflict Management': 10.0
    },
    'euc': {
        'Discrete Mathematics': 8.2,
        'Programming': 6.9,
        'English II': 8.8,
        'Differential Calculus': 6.0,
        'Probability and Statistics': 6.4,
        'Computer and Server Architecture': 8.1,
        'Socio-Emotional Skills and Conflict Management': 9.0
    },
    'cbalam': {
        'Discrete Mathematics': 8.8,
        'Programming': 9.0,
        'English II': 8.5,
        'Differential Calculus': 6.6,
        'Probability and Statistics': 8.9,
        'Computer and Server Architecture': 8.7,
        'Socio-Emotional Skills and Conflict Management': 9.2
    }
}

# Paso 1: Autenticación
while True:
    username = input("Username: ")
    password = input("Password: ")
    if username in users and password == users[username]['password']:
        current_role = users[username]['rol']
        break
    else:
        print("Credenciales incorrectas, intenta de nuevo.")

# Paso 2-5: Distribuidor de menús
if current_role == 'student':
    print(f"Welcome, {users[username]['name']}!")
    approved_subjects = set()
    for subject in subjects:
        grade = notes[username][subject]
        print(subject, grade)
        if grade >= 8.0:
            approved_subjects.add(subject)
    pending_subjects = set(subjects) - approved_subjects
    print("Aprobadas:", approved_subjects)
    print("Pendientes:", pending_subjects)

elif current_role == 'professor':
    for user in users:
        if users[user]['rol'] == 'student':
            print(user, users[user]['name'])
    student_choice = input("Student to grade: ")
    subject_choice = input("Subject to grade: ")
    new_grade = float(input("Grade: "))
    notes[student_choice][subject_choice] = new_grade
    print("The grade was updated successfully")

else:
    for user in users:
        if users[user]['rol'] == 'professor':
            print(user, users[user]['name'])
    print(subjects)
    for student, grades in notes.items():
        print(student)
        for subject, grade in grades.items():
            print(subject, grade)
