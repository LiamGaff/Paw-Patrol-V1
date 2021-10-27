# Testing
As the web page was being built Chrome developer tools were used regularly to ensure that the code was working smoothly. Each section was then tested again every time a new feature was added. Python functions were regularly tested using the print function to ensure the code worked smoothly. Lighthouse in developer tools was also used to check the application's performance. The user stories were always analyzed with each page to ensure the app meet all the requirements.

## Code validation

* At the end of the development process, W3C CSS and Html validator were used to check the code.

* The CSS validator came back with no errors.

* The HTML threw up some errors that were due to the use of flask. These errors are still being looked into but do not seem to have any effect on the application's performance. After further validation testing, errors have been corrected on most templates. The only errors occuring now are due to a materialize form template. I am unable to change the code in these templates to fix said html errors but the form still works as desired.

## Bugs

**Unresolved issues**
* I have not yet set up the functionality for the user to update their profile image/avatar.

* Some data retrieved from the the google books API is still presented as it is in the JSON file which looks messy. Still working on fixing this.

**continued testing**
* I am still trying to find the best way to call the book API data so that it looks more presentable.
* Working on only allowing a user to post one review per book.

# Manual Testing

# Home Page

**Test #1 (Navbar - Logged in)**

Action: Click on each nav button to be redirected to your chosen template.

Before: Nav button clicked on home page(No state change of the button)

After: Redirected to chosen template. This also worked for logging out of session.

Result: Pass

-----------------------------------------------------------------------------------------

**Test #2 (Navbar - Logged out)**

Action: Click on each to be redirected to your chosen template.

Before: Nav button clicked on home page(No state change of the button)

After: Redirected to chosen template.

Result: Pass

-----------------------------------------------------------------------------------------

**Test #1 (Contact-form)**

Action: Type any book title into search box.

Before: Search box is inactive with plain white background.

After: Text fills the search box and shows previously searched words.

Result: Pass

-----------------------------------------------------------------------------------------

# Search page

**Test #1 (Library button - logged out)**

Action: Click on the "Library" button (plus sign) attached to the searched books.

Before: Hover over button causes no state change.

After: Redirected to login page and flashed message "Login to add book"

Result: Pass

-----------------------------------------------------------------------------------------

**Test #2 (Library button - logged in)**

Action: Click on the "Library" button (plus sign) attached to the searched books.

Before: Hover over button causes no state change.

After: Redirected to profile and book is added to library.

Result: Pass

-----------------------------------------------------------------------------------------

**Test #3 (Review button - logged out)**

Action: Click on the "Review" button under featured book.

Before: Hover over button changes state from orange to light orange.

After: Redirect to review page with a flash message "Login to review book".

Result: Pass

-----------------------------------------------------------------------------------------

**Test #4 (Review button - logged In)**

Action: Click on the "Review" button under featured book.

Before: Hover over button changes state from orange to light orange.

After: Redirect to review page where a review can be submitted

Result: Pass

-----------------------------------------------------------------------------------------

**Test #5 (View button)**

Action: Click on the "View Book" button under featured book.

Before: Hover over button changes colour from teal to a lighter shade of teal and adds some box shadow.

After: On click a new window is opened that redirects us to the google books api page.

Result: Pass

-----------------------------------------------------------------------------------------

**Test #5 (Return home link)**

Action: Click on the "Return home: here" link at the bottom of the page.

Before: Hover over blue link. No change in state.

After: On click redirect to home page.

Result: Pass

-----------------------------------------------------------------------------------------

# Submit_review

Test #1 (Reviews button - Logged in)

Action: Click on "Reviews" button below book image.

Before: Hover over button changes state from orange to light orange.

After: Redirect to book_review template for the chosen title. There is an option to submit a review.

Result: Pass

-----------------------------------------------------------------------------------------

**Test #2 (Reviews button - Logged out)**

Action: Click on "Reviews" button below book image.

Before: Hover over button changes state from orange to light orange.

After: Redirect to book_review template for the chosen title. No option to add review and flash message says "Login to add review"

Result: Pass

-----------------------------------------------------------------------------------------

# book_review(Logged in)


**Test #1 (Range/rating field input)**

Action: Use the slider on the form to pick a number from zero to 10.

Before: Slider is stationary showing no values

After: As the slider is moved up or down a value will appear directly above the slider to show your choice of rating.

Result: Pass

-----------------------------------------------------------------------------------------

**Test #2 (Add comment input)**

Action: Click on comment input section of form and add some text.

Before: Filler text on the line saying "comment".

After: "Comment" moves above the input field so text can be entered. You can now type in your comments on the chosen title.

Result: Pass

-----------------------------------------------------------------------------------------

**Test #3 (Submit Review button)**

Action: After form is filled click on "submit review" button.

Before: Hover over button changes colour from teal to a ligther shade of teal and adds some box shadow.

After: On click page refreshes book_review page and the new review can be found in the review section.

Result: Fail - Book review won't submit as it says I have already submitted a review for this title when I have not.

-----------------------------------------------------------------------------------------

**Test #3b (Submit Review button)**

Action: After form is filled click on "submit review" button.

Before: Hover over button changes colour from teal to a lighter shade of teal and adds some box shadow.

After: On click page refreshes book_review page and the new review can be found in the review section.

Result: 

-----------------------------------------------------------------------------------------

**Test #4 (Remove button)**

Action: Click on "remove" button to remove your own comments 

Before: Hover over button changes no state. Button remains a teal colour

After: On click review page is refreshed and chosen review has been removed.

Result: Pass

-----------------------------------------------------------------------------------------

# Profile

**Test #1 (Update button)**

Action: Click on the "Update" button in the top right corner.

Before: Hover over button changes colour from teal to a lighter shade of teal and adds some box shadow.

After: On click page is redirected to the update profile template.

Result: Pass

-----------------------------------------------------------------------------------------

**Test #2 (Remove button)**

Action: Click on "Remove button" below library books.

Before: Hover over button changes state from orange to light orange.

After: Profile page is refreshed and the chosen title has been removed from the user's library.

Result: Pass

-----------------------------------------------------------------------------------------

Test #3 (Home page button)

Action: Click on "Add some books to your collection: search" at the bottom of the page

Before: Hover over blue link. No change in state.

After: On click redirect to home page.

Result: Pass

-----------------------------------------------------------------------------------------

# Update Profile(still under development)

**Test #1 (Profile page button)**

Action: Click on "Return to profile: Profile" at the bottom of the page

Before: Hover over blue link. No change in state.

After: On click redirect to profile page.

Result: Pass

-----------------------------------------------------------------------------------------

**Test #2 (Drop down selection)**

Action: Click on drop down menu on the form.

Before: Hover over drop down arrow where filler text says "choose your option"

After: On click three options drop down and when one is selected it will replace the filler text.

Result: pass

-----------------------------------------------------------------------------------------

**Test #3 (Update button)**

Action: After form is filled click on "Update" button.

Before: Hover over button changes colour from teal to a ligther shade of teal and adds some box shadow.

After: On click redirect to profile page where profile picture is updated.

Result: Fail - This feature has not been fully built yet.

-----------------------------------------------------------------------------------------

# Registration

**Test #1 (Name input)**

Action: Enter name into name input at the top of the form.

Before: Hover over black input line, no change in state.

After: On click input line turns green and text can now be entered

Result: Pass

-----------------------------------------------------------------------------------------

**Test #2 (Email input)**

Action: Enter email into email input in the middle of the form.

Before: Hover over black input line, no change in state.

After: On click input line turns green and text can now be entered

Result: Pass

-----------------------------------------------------------------------------------------

**Test #3 (Password input)**

Action: Enter Password into password input at the end of the form.

Before: Hover over black input line, no change in state.

After: On click input line turns green and text can now be entered. The text here is hidden, presented as black dots.

Result: Pass

-----------------------------------------------------------------------------------------

**Test #4 (Sign up button)**

Action: After form is filled click on "Sign up" button.

Before: Hover over button changes colour from teal to a lighter shade of teal and adds some box shadow.

After: On click redirect to new profile page with an empty library

Result: Pass

-----------------------------------------------------------------------------------------

**Test #4b (Sign up button - existing account)**

Action: After form is filled click on "Sign up" button.

Before: Hover over button changes colour from teal to a ligther shade of teal and adds some box shadow.

After: On click redirect back to the sign up page and flashed message "An account with this email already exists"

Result: Pass.

-----------------------------------------------------------------------------------------

Test #5 (Login page button)

Action: Click on "Have an account? Log In" at the bottom of the page.

Before: Hover over blue link. No change in state.

After: On click redirect to login page.

Result: Pass 

-----------------------------------------------------------------------------------------

# Login

**Test #1 (Email input)**

Action: Enter email into email input in the middle of the form.

Before: Hover over black input line, no change in state.

After: On click input line turns green and text can now be entered

Result: Pass

-----------------------------------------------------------------------------------------

**Test #3 (Password input)**

Action: Enter Password into password input at the end of the form.

Before: Hover over black input line, no change in state.

After: On click input line turns green and text can now be entered. The text here is hidden, presented as black dots.

Result: Pass

-----------------------------------------------------------------------------------------

**Test #4 (login button)**

Action: After form is filled click on "Login" button.

Before: Hover over button changes colour from teal to a lighter shade of teal and adds some box shadow.

After: On click redirect to users profile page.

Result: Pass

-----------------------------------------------------------------------------------------

**Test #4b (Sign up button - wrong credentials)**

Action: After form is filled click on "Login" button.

Before: Hover over button changes colour from teal to a lighter shade of teal and adds some box shadow.

After: On click redirect back to the Login page and flashed message "Incorrect Email and/or Password"

Result: Pass

-----------------------------------------------------------------------------------------

**Test #5 (Sign up page button)**

Action: Click on "Not registered? Sign up" at the bottom of the page.

Before: Hover over blue link. No change in state.

After: On click redirect to sign up page.

Result: Pass