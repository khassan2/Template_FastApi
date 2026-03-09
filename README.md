Pre-requisites
UV-> https://docs.astral.sh/uv/getting-started/installation/
CMD-> pip install uv

==============================================================

STEPS to create project from scratch:

1. Create a new UV project for FastApi
CMD -> uv init

2. Install FastApi
CMD -> uv add fastapi

3. Create Python environment
CMD -> uv add python-dotenv

4. Create Auth dependencies
CMD -> uv add fastapi-users[sqlalchemy]

5. Use to handle images/videos
CMD -> uv add imagekitio

6. Install dependency for WebServer
CMD -> uv add uvicorn[standard]

7. Dependency for Database
CMD -> uv add aiosqlite

8. Create new ENVIRONMENT_VARIABLE (.env) file in the project folder
Add following in .env file
=> IMAGEKIT_PRIVATE_KEY=
=> IMAGEKIT_PUBLIC_KEY=
=> IMAGEKIT_URL=

Go to Imagekit.io for create the above 3 variable information, Create Account -> Go to Developer Options -> API Keys -> Create your API keys to use with above environment variable. Make sure you do not share the PRIVATE_KEY with anyone.

9. Create new Folder "app"

10. Create new File "app.py"

and start writing code

========================================

TO START the project: You first need to add uvicorn server details in the main.py file which are already available in it.
Now to run the server go to your terminal (i use command prompt) and type 

-----> uv run ./main.py 

(make sure your command prompt is running in the same folder as main.py)

========================================

To Browse or test your Api
In browser, localhost:8008/docs (this will open Swagger docs for you to test and see the results of your API)

========================================





