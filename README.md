# Node.js Cloudant Starter Overview

## Summary
This app displays demonstrates basic CRUD operations, namely: READ, CREATE, UPDATE and DELETE operations using the Bluemix noSQL DB service. Through this app, the user is able to view existing files, upload new ones, or delete existing ones.

## Setup
Simply clone the repository. The app should allow the user to caryr these operations front-end calls. 

## Operation Instructions

1. See app.js for how to obtain and use the Cloudant credentials as well as the file CRUD API
2. All CRUD operations calls are demonstrated in public/scripts/index2.js and public/scripts/util.js:
* The util.js file contains the basic operations that are used in creating these calls
* The loadItems functions in index2.js loads the existing items, by making a call to 'api/favorites' and storing the results in the variable data
* The uploadFile stores the attached file in the form variable. It then checks if an ID is provided. If not, then it assigns it the value -1, as the system will take that as an indication that it's a new file and use the CREATE operation. If an ID is provided, it will overwrite the existing file using an UPDATE file
* The deleteItem function uses the data binding to retrieve the ID of the selected file in te table, and then call the DELETE operation
