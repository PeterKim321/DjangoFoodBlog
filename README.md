# DjangoFoodBlog

The front end is a template sourced online, please see readme.txt in folder 'code' for source.
The project adds additional functionalities through the use of Python's Django framework.

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
- #TODO - a̶d̶d̶ r̶a̶t̶i̶n̶g̶ t̶o̶ p̶o̶s̶t̶ m̶o̶d̶e̶l̶, test standard image size for thumbnail, deploy project