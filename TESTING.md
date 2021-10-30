# Testing
As the web page was being built Chrome developer tools were used regularly to ensure that the code was working smoothly. All apps were retested upon completion. Python functions and models were regularly tested using the print function to ensure the code worked smoothly. Lighthouse in developer tools was also used to check the application's performance. The user stories were always analyzed with each page to ensure the app meet all the requirements.

Due to some functional errors when working with stripe some bugs adn errors remain. Due to having a deadline I was unable to fix these bugs in time but I will continue developing the site constantly improving its funtionality and style. Also further testing is required.

## Code validation

* W3C Markup Validation was used to validate HTML.

* W3C CSS validation was used to validate CSS.

* JSHint was used to validate JavaScript.

* Chrome Devtools to test responsivitiy throughout.

* HTML and CSS Beautifier.

* AutoPrefixer -This project used AutoPrefixer to make sure the css code is valid for all browsers.
 
* Markdown live-preview -This project used markdown previewer to check the rendering of the readme.md file content.
 
* IDLE- to check python code

## Bugs

* The drop down navigation menue wasnt working. This was do to it beeing automatically set to hidden. All I had to do here was remove the hidden class.

* Strip Payment element wouldnt render. This was due to having unessesary code in the JavaScript for handling the stripe payment.

* I am having further issues with the stripe payment API. I an unable to get the amount from the form to submit the donation.

* The edit animals function isnt working. It is giving me an error of 'str' object has no attribute 'get'. 

* On the deployed site for some reason not all the media and static files are loading. I have manually added all the media files again but this problem still persists. This bug was due to my settings.py missing the "django.template.context_processors.media" in the context_processors.Melinda Zhang was a great help figuring this out.

**Unresolved issues**

* The edit function still isnt working in the animals template. I will comment it out for now and continue to work on it.

* The payment form requires a lot more validation and defensive coding but I only completed it the evening before my deadline. Further work will be done to secure it.

**continued testing**

# Manual Testing

# Home Page

**Test #1 (Navbar - Logged in)**

Action: Click on each nav button to be redirected to your chosen page.

Before: Nav button clicked on home page(No state change of the button)

After: Redirected to chosen template. This also worked for logging out of session.

Result: Pass

-----------------------------------------------------------------------------------------

**Test #2 (Navbar - Logged out)**

Action: Click on each to be redirected to your chosen page.

Before: Nav button clicked on home page(No state change of the button)

After: Redirected to chosen template.

Result: Pass

-----------------------------------------------------------------------------------------

**Test #3 (Contact-form)**

Action: Fill in required fields.

Before: Fields are filled or notified to fill out.

After: Page is refreshed and a message pops up informing you that your message has been recieved.

Result: Fail - Toast messages did not displat

-----------------------------------------------------------------------------------------

**Test #3a (Contact-form)**

Action: Fill in required fields.

Before: Fields are filled or notified to fill out.

After: Page is refreshed and a message pops up informing you that your message has been recieved.

Result:

-----------------------------------------------------------------------------------------

# Animal Page

**Test #1 (Add New Animal Link - logged in as admin)**

Action: Click on the "Add New Animal" link at the top of the page

Before: Hover over button causes no state change.

After: Redirected to a page with a form to add new animal.

Result: Pass

-----------------------------------------------------------------------------------------

**Test #2 (Add animal form - logged in as admin)**

Action: Fill in required fields.

Before: Fields are filled or notified to fill out.

After: Redirected back to animal page and a message pops up informing you that the animal has been added to the database.

Result: Fail - Toast messages did not display

-----------------------------------------------------------------------------------------

**Test #2a (Add animal form - logged in as admin)**

Action: Fill in required fields.

Before: Fields are filled or notified to fill out.

After: Page is refreshed and a message pops up informing you that the animal has been added to the database.

Result: 

-----------------------------------------------------------------------------------------

**Test #3 (Donate button)**

Action: Click on the "Donate" button on the animal card.

Before: Hover over button changes state from red to black.

After: Redirect to donate page.

Result: Pass

-----------------------------------------------------------------------------------------

**Test #4 (Edit button - logged in as admin)**

Action: Click on the "Edit" button on the animal card.

Before: Hover over button changes state from red to black.

After: Redirect to Edit animal form.

Result: Fail - The page will not redirect and is giving an error message.

-----------------------------------------------------------------------------------------

**Test #4a (Edit button - logged in as admin)**

Action: Click on the "Edit" button on the animal card.

Before: Hover over button changes state from red to black.

After: Redirect to Edit animal form.

Result: 

-----------------------------------------------------------------------------------------

**Test #5 (Delete animal - logged in as admin)**

Action: Click on the "remove" animal link on the animal card.

Before: Hover over button changes state from red to black.

After: On click the page refreshes and the animal has been removed.

Result: Pass

-----------------------------------------------------------------------------------------

# Blog Page

**Test #1 (Reviews button - Logged in as admin)**

Action: Click on "Add new post" button at the top of the page.

Before: Hover over button changes state adding a white underline.

After: Redirect to redirect to blog form page.

Result: Pass

-----------------------------------------------------------------------------------------

**Test #2 (Blog for - Logged oin as admin)**

Action: Fill in required fields.

Before: Fields are filled or notified to fill out.

After: Page is redirected back to blog page and a new post is added to the page.

Result: pass


-----------------------------------------------------------------------------------------

**Test #3 (Post/Story links)**

Action: Click on the "remove" animal link on the animal card.

Before: Hover over button changes state from orange to white.

After: On click redirect to page to view full blog post.

Result: Pass


-----------------------------------------------------------------------------------------

**Test #4 (Requires further testing)**

Further testing is to be done on the blog page as it is updated and made fully functional.

-----------------------------------------------------------------------------------------

# Profile Page(Logged in)

**Test #1 (Change password button)**

Action: Click on "Change password" link uder the user details.

Before: Hover over button changes state from red to black.

After: On click page redirects to the change passwoed form.

Result: Pass.

-----------------------------------------------------------------------------------------

**Test #2 (Change password form)**

Action: Fill in required fields.

Before: Fields are filled or notified to fill out.

After: Page is refreshed and the password has been changed.

Result: pass

-----------------------------------------------------------------------------------------

**Test #3 (Payment Form)**

Action: Select donation amount and add card details.

Before: Fields are filled or notified to fill out.

After: On click rredirect to succes page and pop up message is shown.

Result: Fail - Payment system isnt working.

-----------------------------------------------------------------------------------------

**Test #3a (Payment Form)**

Action: Select donation amount and add card details.

Before: Fields are filled or notified to fill out.

After: On click rredirect to succes page and pop up message is shown.

Result: Fail - Payment system isnt working.

-----------------------------------------------------------------------------------------

# Donate page

**Test #1 (Payment Form - Logged in)**

Action: Select donation amount and add card details.

Before: Fields are filled or notified to fill out.

After: On click rredirect to succes page and pop up message is shown.

Result: Fail - Payment system isnt working.

-----------------------------------------------------------------------------------------

**Test #2 (Payment Form - Logged out)**

Action: Click on signup link

Before: Hover over button changes state from red to black.

After: On click page redirects to the signup form.

Result: Pass.

-----------------------------------------------------------------------------------------

**Test #3 (Payment Form - Logged out)**

Action: Click on "Login" link.

Before: Hover over button changes state from red to black.

After: On click page redirects to the login form.

Result: Pass.

-----------------------------------------------------------------------------------------

**Test #2 (Profile Page link - logged out)**

Action: Click on "Profile Page" link.

Before: Hover over button changes state from red to black.

After: On click page redirects to the login form.

Result: Pass.

-----------------------------------------------------------------------------------------

**Test #3 (Profile Page link - logged in)**

Action: Click on "Profile Page" link.

Before: Hover over button changes state from red to black.

After: On click page redirects to the profile page.

Result: Pass.

-----------------------------------------------------------------------------------------

# Login

**Test #1 (Email input)**

Action: Enter email/username into email iinto the formform.

Before: Hover over "signin" button, state change from white to black. Required fileds are filled or requested.

After: On click redirect to profile page if user exists

Result: Pass

-----------------------------------------------------------------------------------------

# Logout

**Test #1 (Email input)**

Action: On logout page click on logout button

Before: Hover over "signin" button, state change from white to black.

After: On click redirect to home page and logged out

Result: Pass

-----------------------------------------------------------------------------------------

# Register

**Test #1 (Email input)**

Action: Enter email/username/name/password on the form.

Before: Hover over "signup" button, state change from white to black. Required fileds are filled or requested.

After: On click redirect to new profile page displaying user's details.

Result: Pass

-----------------------------------------------------------------------------------------