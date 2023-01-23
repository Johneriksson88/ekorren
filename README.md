# Magasinet Ekorren


Magasinet Ekorren is a fully responsive web site for renting storage units, as well as acting as a marketing tool for the company. A customer can easily get information about how it works, create an account and rent and manage their storage units.

![Responsice Mockup](https://github.com/lucyrush/readme-template/blob/master/media/love_running_mockup.png)

## Features 

  - The website is structured as a one page website for the home page, where all information can be found in different sections, clearly separated by different background colors.
  - All user-related pages (login/out, orders, user panel etc.) are on their own pages.

### Existing Features

- __Navigation Bar__

  - Featured on all three pages, the full responsive navigation bar includes links to the Logo, Home page, Storage Units (info and links for renting) and an About & Contact section. The navigation bar is the same on all pages.
  - This section will allow the user to easily navigate from page to page across all devices without having to revert back to the previous page via the ‘back’ button. 
  - To the right is a Log In-button, which will change to Log Out if the user is logged in. A welcome message with a link to the user panel page will also show here if the user is logged in.
  - If an admin is logged in there will also be a link to the admin management page here.

![Nav Bar](https://github.com/lucyrush/readme-template/blob/master/media/love_running_nav.png)

- __The hero section__

  - The hero section contains of a right and a left part.
  - On the left is an image of a happy squirrel moving boxes, a logo the company wished to have on the website.
  - On the right is a short introduction as well as a call to action button which takes the visitor to the order form (if logged in, otherwise the user is asked to create an account).


- __Instructions section__

  - The instructions section shows the potential customer the steps which they have to go through to rent a storage unit.
  - There are 5 steps and they are clearly highlighted through the usage of a different background color for the section.
  - The first step has a link to create an account to keep things simple for the visitor.

![Club Ethos](https://github.com/lucyrush/readme-template/blob/master/media/love_running_ethos.png)

- __Product cards section__

  - Here the visitor can learn about the different products and their attributes, such as sizes, prices etc. in the form of cards.
  - Every product card has a link that takes them to the order form if they are logged in (if not logged in they will be sent to the register account form)

![Meetup Times](https://github.com/lucyrush/readme-template/blob/master/media/love_running_times.png)

- __Why us section__ 

  - Here the visitor is presented with 4 "badges" with arguments for why they would want to rent a storage unit from Magasinet Ekorren.
  - Every badge has a corresponding icon to clearify the message.

![Footer](https://github.com/lucyrush/readme-template/blob/master/media/love_running_footer.png)

- __About & Contact section__

  - Here the visitor can find information about the company and storage units, an embedded google map on which they can click for directions, and a contact form.
  - The three parts are divided into their own "cards".
  - Phone number is a direct call link on mobile and email a direct email link. 

![Gallery](https://github.com/lucyrush/readme-template/blob/master/media/love_running_gallery.png)

- __Footer__

  - The footer has a copyright text on the left with a script changing it to the current year.
  - The middle has a small acorn as a nice addition of color.
  - The right has the nav links, dynamic to present links according to if the visitor is logged in or not.

- __Register page__

  - Here the visitor can create an account by simply providing a username and password two times.
  - The design of the Registration page was derived from this youtuber [Dennis Ivanov](https://www.youtube.com/@DennisIvy), provided at this [JSFiddle](https://jsfiddle.net/ivanov11/hzf0jxLg/)

- __Login page__

  - Here the user or admin can sign in to their account to access the user panel where they can manage orders and customer information.
  - The design of the Login page was derived from this youtuber [Dennis Ivanov](https://www.youtube.com/@DennisIvy), provided at this [JSFiddle](https://jsfiddle.net/ivanov11/dghm5cu7/)

- __User panel page__

  - The user panel page is where the customer can create, delete and view their orders, as well as view and update their contact/invoice information.
  - The orders are presented first in a list, and if there are no orders a text will tell them so. Underneith the list is a button for making a new order. The orders can be deleted by clicking the garbage can icon at the end of the listed order.
  - Deleting an order takes the customer to a page where they can confirm that they want to delete the order.
  - Underneith the customers information is displayed. By clicking edit information they will be taken to a form where they can change it, if for example they changed adress, phone number etc.

- __New order page__

  - The new order page contains a form where the customer can order their storage units.
  - First, a list of the different products is displayed, and underneith the customer can pick their storage unit of choice in a dropdown list.
  - Then they will pick a starting date, which cannot be in the past. 
  - When they click 'Next', a modal will be shown where they can confirm their order by clicking 'Confirm'.


### Features Left to Implement

- Ability to rent a storage unit without having to create an account
- Online payment method
- Stock of individual storage units (at the moment the owner of the company wants to process orders manually, so if a customer books a storage unit that is unavailable he can reach out to them and make a deal on another one)
- Order history on user panel
- Identity validation through swedish BankID
- Uniform form validation on all pages

## Testing 

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your project’s features and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.


### Validator Testing 

- HTML
  - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcode-institute-org.github.io%2Flove-running-2.0%2Findex.html)
- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fvalidator.w3.org%2Fnu%2F%3Fdoc%3Dhttps%253A%252F%252Fcode-institute-org.github.io%252Flove-running-2.0%252Findex.html&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en#css)

### Unfixed Bugs

You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed. 

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub) 

- The site was deployed to GitHub pages. The steps to deploy are as follows: 
  - In the GitHub repository, navigate to the Settings tab 
  - From the source section drop-down menu, select the Master Branch
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 

The live link can be found here - https://code-institute-org.github.io/love-running-2.0/index.html 


## Credits 

In this section you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 

You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign up page are from This Open Source site
- The images used for the gallery page were taken from this other open source site


Congratulations on completing your Readme, you have made another big stride in the direction of being a developer! 

## Other General Project Advice

Below you will find a couple of extra tips that may be helpful when completing your project. Remember that each of these projects will become part of your final portfolio so it’s important to allow enough time to showcase your best work! 

- One of the most basic elements of keeping a healthy commit history is with the commit message. When getting started with your project, read through [this article](https://chris.beams.io/posts/git-commit/) by Chris Beams on How to Write  a Git Commit Message 
  - Make sure to keep the messages in the imperative mood 

- When naming the files in your project directory, make sure to consider meaningful naming of files, point to specific names and sections of content.
  - For example, instead of naming an image used ‘image1.png’ consider naming it ‘landing_page_img.png’. This will ensure that there are clear file paths kept. 

- Do some extra research on good and bad coding practices, there are a handful of useful articles to read, consider reviewing the following list when getting started:
  - [Writing Your Best Code](https://learn.shayhowe.com/html-css/writing-your-best-code/)
  - [HTML & CSS Coding Best Practices](https://medium.com/@inceptiondj.info/html-css-coding-best-practice-fadb9870a00f)
  - [Google HTML/CSS Style Guide](https://google.github.io/styleguide/htmlcssguide.html#General)

Getting started with your Portfolio Projects can be daunting, planning your project can make it a lot easier to tackle, take small steps to reach the final outcome and enjoy the process! 