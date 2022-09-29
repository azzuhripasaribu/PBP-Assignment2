## What Does CSRF Token Do
CSRF token is used to authenticate the form that is sent and prevents cross site request forgery attacks

## Can we create the <form> element manually (without using a generator?

Yes, we can create a form manually using HTML \<input> tag to get user input

## Describe the data flow process from the submission made by the user through the HTML form, data storage in the database, until the appearance of the data that has been stored in the HTML template. 
when a user submits a form, the client sends a POST request to the server containing the data that has been submitted by the user through the form. then, depending on the implementation in django views, the server either create a new entry in the database or update an existing entry. then,the data in the database can be used as a context for a template when needed. 