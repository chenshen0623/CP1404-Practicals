"""
Project Management
Estimate: 60 minutes
Actual:
"""
import datetime
from operator import attrgetter
from prac_07.project import Project

FILENAME = 'projects.txt'
MENU = ('- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n'
        '- (A)dd new project\n- (U)pdate project\n- (Q)uit')
DATE_FORMAT = '%d/%m/%Y'