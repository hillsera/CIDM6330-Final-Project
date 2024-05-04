# CIDM 6330 Final Project
## Sera Hill

### Selected Domain
My selected domain for this project is a Learning Platform employers can provide to their employees so that employers can choose a learning path that let's them build new skills, or pursue paths that will help them in their current role.

The employee should be able to select their path, watch the prescribed videos, save their progress or change paths. 

### Domain Model
My domain model is LearningPath which allows for video ID, Title, Duration, and Progress. This app was built using Django Rest Framework in my projectapp directory.

### Commands
The commands written in this file work directly with the Django ORM for database operations.

I have an "add path command" that lets employers add learning paths for their employees. (Ideally, this would be restricted for the appropriate users)
There is also a "list path command" that allows employees to see the list of learning paths allowed for them.
Additionally, there's a command to save your progress in the learning path
The tests in the "projectarch" directory shows these commands working as expected.

### Message Bus with Django Signals
In the Barky Refactor 3 assignment, we used Django Signals to handle the internal messaging system to support an event-driven architecture. 
Firstly, I had to specify the default app in the init.py file in the projectapp directory, and I set up the import signals to happen when the app is ready as outlined from Assignment 7.

05/01 - I am getting an error for async_to_sync in my signals.py file, but the csv file is being created in the specified folder as expected.
05/03 I fixed this issue, turns out I didn't have everything set up properly and I was missing the "ID" field for my test_signal_handlers.

### External Message Bus with Django Channels
While the internal messaging system is using signals, channels is handling the external messaging system. I have updated the asgi.py file to accomodate for this. After some hiccups, when I run my tests in my terminal, the learningpath test information is being sent correctly to the redis server.

When adding the dependency injection as the final part of assignment 8, I am running into errors that I'm unsure on how to solve. I am failing a NOT NULL constraint in my progress portion of the learning path, which further leads me to believe I don't have the knowledge on how to set up something like this correctly. However, I believe the overall architecture follows what was outlined in the refactoring assignments, as I have used the refactor 4 code to set up my own project.