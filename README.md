# O.dev Test Task  
Test Task for Python Backend Position  

## How to Run the Service:  
1. Clone the repository.  
2. Specify the Ethereum node endpoint in the *docker-compose.yml* file.  
   - The variable is called `REMOTE_NODE_ENDPOINT` (service `cryptocurrency_service`).  
3. Set a password for encrypting wallet private keys in the *docker-compose.yml* file.  
   - The variable is called `PRIVATE_KEY_ENCRYPTION_PASS` (service `cryptocurrency_service`).  
   - **Any string can be used as the password.**  
4. Start the service and the database using `docker-compose up`.  
   - (4.1.) Optionally, you can uncomment the volume for PostgreSQL.  
5. The API will be available at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/).  

### About Private Key Encryption:  
To avoid storing wallet private keys in plaintext, they are encrypted and stored in the database as JSON.  
- To encrypt a private key, a password is required.  
- For simplicity, a single password is used for all private keys.  
- This password is obtained from the environment variable `PRIVATE_KEY_ENCRYPTION_PASS`.  

Using this password, stored keys can also be decrypted. Therefore, it is **not recommended** to change the password after it is set, as this would make it impossible to decrypt private keys associated with existing wallets.  

## Tests:  
Tests are run in the local environment, with a test PostgreSQL database launched in a separate container.  

To run tests locally:  
1. Uncomment the lines in the *requirements.txt* file under the `#for local environment` section and install dependencies using `pip install -r requirements.txt`.  
2. Create a *.env* file (refer to *.env.example*) and specify values for the variables `PRIVATE_KEY_ENCRYPTION_PASS` and `REMOTE_NODE_ENDPOINT`.  
   - Set the environment variables (or configure them in another convenient way).  
3. Launch the test database container:  
   ```bash
   docker-compose run -p 5432:5432 -d postgresql
   ```  
4. From the `server` directory (where the *manage.py* file is located), run the command:  
   ```bash
   pytest
   ```  

## Documentation:  
Documentation is available at: [http://127.0.0.1:8000/api/v1/schema/swagger-ui/](http://127.0.0.1:8000/api/v1/schema/swagger-ui/).  
