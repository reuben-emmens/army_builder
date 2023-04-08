# Web App - **Army Builder**

### SUMMARY
---
<br>
This project will provide a hosted api for allows you to perform CRUD operations on unit datasheets from the popular Warhammer 40K tabletop wargame.

### <br> USAGE
---

<br> Navigate to 'https://astra-militarum.up.railway.app/'. From there, you can utilise CRUD API methods to interact with the MongoDB database and access information on unit datacards. For more interactive documentation, FastAPI has automatically generated 'https://astra-militarum.up.railway.app/docs' through which you can see the required parameters and schema. Some requests will need a body, which can also be done through the Swagger docs or by using the 'curl' command line tool and library. An example of this would be: 

```bash
curl -X 'GET' \
  'https://astra-militarum.up.railway.app/' \
  -H 'accept: application/json'
```

### <br> ROADMAP
---
<br>

1. ~~Create a MongoDB Atlas cluster and collection for storing unit documents.~~
2. ~~Create a database.py file, using the Motor driver, and containing CRUD operations~~
3. ~~Create CRUD APIs with FastAPI to interact with the class while obfuscating the inner workings of the program.~~
4. ~~Host on Railway infrastructure platform.~~
5. Write code tests using Pytest, and automated API tests using Postman CLI + GitHub Actions. 
4. Implement caching using Redis for faster queries.
5. Create a front-end interface with Javascript and/or React. 

### <br> AUTHORS
---
<br>
@EmmensReuben

![Visualization of the codebase](./diagram.svg)