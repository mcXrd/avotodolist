# AvoTodolist
- API to make it possible to create tasks and a nested list of subtasks for every task (even for subtasks) 
- API is created via djangorestframework
- API documentation is autogenerated via coreapi and can be seen live on http://serverurl:serverport/api/docs/

# installation guide
1) pull this repository and cd into it
2) sudo docker build -t avotodolist_image .
3) sudo docker run -p 80:80 avotodolist_image
4) you should have app running on port 80 now with documentation on /api/docs/ and tasks recourse on /api/tasks/

caveats:
- file db.sqllite3 is already included, therefore there is no need to run django migrations before starting server

