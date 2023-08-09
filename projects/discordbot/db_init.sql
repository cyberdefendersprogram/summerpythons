CREATE TABLE IF NOT EXISTS python_questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    options JSON NOT NULL,
    answer TEXT NOT NULL
);

/* 
  LLM_Query:

  Show me 1 multiple choice style  question which tests Python knowledge on PEP8 . 
  Show in markdown format. Include just the letter of answer and remove preamble text 
  Then give me SQL to insert the question data in table, the format for table is deifned below:

   CREATE TABLE python_questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    options JSON NOT NULL,
    answer TEXT NOT NULL
  );
*/

INSERT INTO python_questions (question, options, answer)
VALUES (
    'According to PEP 8, which of the following represents the recommended way to name a variable holding a constant value in Python?',
    '{"A": "myConstantValue", "B": "my_constant_value", "C": "MY_CONSTANT_VALUE", "D": "my-constant-value"}',
    'C'
);
INSERT INTO python_questions (question, options, answer)
VALUES (
  'Which of the following represents the recommended line length according to PEP8 standards?',
  '{"A": "60 characters", "B": "79 characters", "C": "100 characters", "D": "120 characters"}',
  'B'
);
INSERT INTO python_questions (question, options, answer)
VALUES 
    (
    'What does PEP8 recommend for the naming convention of function names?',
    '{"A": "CamelCase", "B": "snake_case", "C": "kebab-case", "D": "CAPITALS_WITH_UNDERSCORES"}',
    'B'
    ),
    (
    'In Python, according to PEP8, under what circumstances is it acceptable to use a backslash for line continuation?',
    '{"A": "When breaking up a long function call or definition", "B": "When breaking up a long comment", "C": "When breaking up a dictionary or list", "D": "It is discouraged in all circumstances"}',
    'A'
    ),
    (
    'According to PEP8, how many blank lines should be used to separate top-level function and class definitions?',
    '{"A": "0 blank lines", "B": "1 blank line", "C": "2 blank lines", "D": "3 blank lines"}',
    'C'
    ),
    (
    'How should import statements be grouped according to PEP8?',
    '{"A": "Standard libraries, Third-party libraries, Local libraries", "B": "Third-party libraries, Standard libraries, Local libraries", "C": "Local libraries, Standard libraries, Third-party libraries", "D": "Standard libraries, Local libraries, Third-party libraries"}',
    'A'
    ),
    (
    'According to PEP8, what is the maximum number of characters allowed in a single comment line?',
    '{"A": "60", "B": "72", "C": "79", "D": "100"}',
    'B'
    ),
    (
    'According to PEP8, what is the recommended way to write the Boolean constants `True`, `False`, and `None`?',
    '{"A": "true, false, none", "B": "True, false, None", "C": "TRUE, FALSE, NONE", "D": "True, False, None"}',
    'D');
