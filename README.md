# uchan - simple imageboard software written in django 
## description 
uchan was written by me in less than a week in around 8hours of coding
time, it could be used as a base
for making your own imageboard like 4chan or 8kun, 
right now it has implemented the following

- boards - you can add as many boards as you want, it also marks nsfw ones
- threads and replies - they can have media in them
- faq, terms of service and news - all added through admin page
- basic html templates for simplicity, css and scss files included
  
## how to setup 

- install required dependencies 
    ```
    pip install -r requirements.txt
    ```
- create the database 
    ```
    python manage.py migrate
    ```
- run the software 
    ```
    python manage.py runserver 
    ```

## problems and todo list 
- make default boards view (currently only catalog view exists)
- make search option for boards
- add statistics display for threads and boards
- implement report system
- fix file upload, so only files of selected types and under specified size can be uploaded 
- make each board has its own unique ids for threads and replies