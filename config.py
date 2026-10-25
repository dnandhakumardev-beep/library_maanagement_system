PROJECT_NAME = 'Library Management System'
DESCRIPTION = 'Maintain a book catalogue and track availability.'
TABLE = 'books'
FIELDS = [{'key': 'title', 'label': 'Book title', 'required': True}, {'key': 'author', 'label': 'Author', 'required': True}, {'key': 'isbn', 'label': 'ISBN', 'required': False}, {'key': 'status', 'label': 'Status (Available or Borrowed)', 'required': True}]
SAMPLES = [['Clean Code', 'Robert C. Martin', '9780132350884', 'Available'], ['Python Crash Course', 'Eric Matthes', '9781718502703', 'Borrowed']]
