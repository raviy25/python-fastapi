## Python application to scrape \<website\> and expose Rest API for retrieving top  game.

Webpage to scrape:  http://example.com

### Project structure details:

FastAPI is used to create the REST API with the following folder structure

```bash
app
|- routes # API routes 
|- controller # Controller service logic
|- models # Models directory
|- test # Test cases to be covered
|- utils # Utils directory containing Parser logic
|- services # Service directory contains scrape service
|- app.py # Execution starts with app.py
|- __init__.py # Python package
|- requirements.txt # Python modules required to run the project
```

### Run the application:

```commandline
#cd app
#python app.py
```
