# uchan
 μchan - imageboard written in django

## first setup

1. choose what branch you want to run 

    default is master, there is also development that contains newer code.  
    to run development branch do 
    ```bash
    git fetch && git checkout development 
    ```


1. now after selecting branch you need to migrate changes to db

    to do that you need to run the following command
    ```bash
    python manage.py migrate 
    ```

1. now you can run test server. 

    to do  that simply run this command
    ```bash
    python manage.py runserver 
    ```

1. if everything works you can create admin account. 

    to do that you need to run 
    ```bash
    python manage.py createsuperuser
    ```
    and follow instructions included there

primary #0d46a0
secondary #2196f3