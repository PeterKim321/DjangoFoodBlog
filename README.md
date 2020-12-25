# DjangoFoodBlog

The front end is a template sourced online, please see readme.txt in folder 'code' for source.

This project adds additional functionalities in the backend (Django), extending functionality and adapting it for a personal food blog through the use of Python's Django framework.

The basic framework for the Django backend is from the tutorial: https://www.youtube.com/watch?v=HWg3zXWwre8. The blog has been edited and extended for personal use.

# Changelog
## version 1.0
Initial Release (Tutorial + bug fixes and minor url redirections)

## version 1.1
- Addition of location in posts
- orderby of post.all query set in models.py
- fixed few bugs around the code
- Reformatting of index.html for personal use
- Reformatting of footer
- #TODO = C̶a̶t̶e̶g̶o̶r̶y̶ a̶g̶g̶r̶e̶g̶a̶t̶i̶o̶n̶, S̶e̶a̶r̶c̶h̶ R̶e̶s̶u̶l̶t̶s̶ C̶S̶S̶,̶ L̶o̶g̶i̶n̶ a̶n̶d̶ L̶o̶g̶o̶u̶t̶ C̶S̶S̶

## version 1.2
- Addition of search results css
- Fixed sidebar not loading latest posts and catgeories in search results (addition of requrired param in view.py under search)
- Search required added, can't search for none or empty string
- Forced allauth to redirect to templates under ./account/login.html, logout.html, and signup.html.
- Added Login and Logout in navbar
- added heart to footer &#10084;&#65039;
- #TODO a̶d̶d̶ c̶o̶n̶t̶a̶c̶t̶ h̶t̶m̶l̶ p̶a̶g̶e̶

## version 1.3
- Removed secret key for deployment purposes
- Added Alias for media file in apache config
- Standard thumbnail size 640 x 426 px
- Ready for production publication
- #TODO - a̶d̶d̶ r̶a̶t̶i̶n̶g̶ t̶o̶ p̶o̶s̶t̶ m̶o̶d̶e̶l̶, t̶e̶s̶t̶ s̶t̶a̶n̶d̶a̶r̶d̶ i̶m̶a̶g̶e̶ s̶i̶z̶e̶ f̶o̶r̶ t̶h̶u̶m̶b̶n̶a̶i̶l̶,̶ d̶e̶p̶l̶o̶y̶ p̶r̶o̶j̶e̶c̶t̶

## Extentions TODO
- Search by Location around Sydney (Interactive map + search by geo tag)
- Overall ranking of all restaurants visited (By score)
- Image gallery under every post (For extra pictures that is out of context of post)

## SetUp
- Spin up a fresh instance of aws ec2 instance and ssh into it
- create folder 'django' at ~
- cd into 'django' and clone the project
```
git clone https://github.com/<username>/<repo>.git
```
- create virtual env (may have to install python3 virtualenv) through command
```
python3 -m venv venv
source venv/bin/activate
```
- install dependencies (requirements.txt)
```
pip install -r requirements.txt
```
- migrate and make migrations
```
python3 manage.py migrate && python3 manage.py makemigrations
```
- runserver
```
python3 manage.py runserver
```
- Additional: For users to access your website whilst your server is not running in local host, you must install either apache2 or nginx and gunicorn to create your webserver. The steps to do this can be found online.

## Note
- Yes I realise that I leaked the SECRET_KEY in my past commits, and yes I have tried to remove it using bfg or git-filter, which to my detrement DID NOT WORK. Therefore, the project has been reconfigured with a new SECRET_KEY and the old SECRET_KEY will not compromise the security of the project.

@Future_Employers &#10084; &#65039;
