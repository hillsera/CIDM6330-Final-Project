# CIDM 6330 Final Project
## Sera Hill

### Selected Domain
My selected domain for this project is a Learning Platform employers can provide to their employees so that employers can choose a learning path that let's them build new skills, or pursue paths that will help them in their current role.

The employee should be able to select their path, watch the prescribed videos, save their progress or change paths. 

### Domain Model
My domain model is LearningPath which allows for video ID, Title, Duration, and Progress. 

### Commands
The commands written in this file work directly with the Django ORM for database operations. This is following the assignment for the Barky Refactor 1 assignment.

I have an "add path command" that lets employers add learning paths for their employees. (Ideally, this would be restricted for the appropriate users)
There is also a "list path command" that allows employees to see the list of learning paths allowed for them.
Additionally, there's a command to save your progress in the learning path
The tests in the "projectarch" directory shows these commands working as expected.

### Message Bus with Django Signals
In the Barky Refactor 3 assignment, we used Django Signals to handle the internal messaging system to support an event-driven architecture. 
Firstly, I had to specify the default app in the __init__.py file in the projectapp directory, and I set up the import signals to happen when the app is ready as outlined from Assignment 7.