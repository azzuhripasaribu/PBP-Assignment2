## Deployment URL
https://pbp-2006489634.herokuapp.com/katalog/



## Why use a virtual environment

A virtual environment is used so that different application may run different version of a module. We can still create a Django web application without a virtual environment. However, applications with conflicting dependencies won't be able to run simultaneously

## Implementation Process

### 1. Creating Function on views.py

The show_katalog function queries the database for every data with the type `CatalogItem` using the following code:  
`data_wishlist = CatalogItem.objects.all()`  
The function then maps the template with the context using the render function. The function returns a HTTP response which contains the template katalog.html that has been mapped.


### 2. Create a Routing to Map the Function in views.py

The routing is done by project_django/urls.py. it routes every request of the path /katalog to katalog/urls.py which then runs the show_katalog function in views.py

### 3. Mapping the Data Into HTML

The data is mapped into HTML by using template and Django Template Language. The data is mapped by the show_katalog function in views.py.

### 4. Deploying to Heroku
To depoloy to heroku, add new repository secrets with key-value pair of heroku api key and heroku app name in the Github repository.