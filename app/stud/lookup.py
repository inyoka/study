#!/usr/bin/env python3

'''
Allows lists to be accessed through a generator 'gen'.
For use by the SelectField 'choices' variable etc.
'''

def gen(items):
    for item in items:
        yield(item)

LAPSED = [('Pending', 'Pending'),
    ('Active', 'Active'),
    ('Inactive', 'Inactive')]

TARGET = [('none', 'None'),
        ('spoken', 'Spoken'),
        ('grammar','Grammar'),
        ('reading','Reading'),
        ('listening','Listening'),
        ('writing','Writing'),
        ('exam','Exam'),
        ('conversation','Conversation')]

GOALS = [('none', 'None'),
    ('TOEFL', 'TOEFL'),
    ('IELTS','IELTS'),
    ('iGCSE','iGCSE'),
    ('A-Levels','A-Levels'),
    ('Professional','Professional Development'),
    ('Personal','Personal Development'),
    ('Overseas','Overseas Study')]

DAYS = [('Sunday', 'Sunday'),
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday')]

GENDER = [('Male', 'Male'), ('Female', 'Female')]

STATUS = [('Pending', 'Pending'),
    ('Active', 'Active'),
    ('Inactive', 'Inactive')]

SOURCE = [(1, 'Internet'),
    (2, 'Newspaper'),
    (3, 'Walk-in'),
    (4, 'Friend/Family'),
    (5, 'Flier/Brochure'),
    (6, 'Radio'),
    (7, 'Other...')]

LAPSEDWHY = [(1, 'Cannot contact'),
    (2, 'Schedule change'),
    (3, 'Focus on studies'),
    (4, 'Moved away'),
    (5, 'Delayed entry'),
    (6, 'Dissatisfied'),
    (7, 'Pending'),
    (8, 'No suitable class'),
    (9, 'Non-starter'),
    (10, 'Other...')]

if __name__ == "__main__":
    for item in gen(TARGET):
        print(item)
