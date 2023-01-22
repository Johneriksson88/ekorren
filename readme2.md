# Magasinet Ekorren

![Magasinet Ekorren - Am I Responsive Image](docs/readme_images/am_i_responsive.png)

This website was created for a company called Magasinet Ekorren ('The Squirrel Warehouse' roughly translated from Swedish to English). 
The company provides storage units in various sizes for rent to persons and businesses. The website provides short and concise information about the storage units and how to rent them. It provides a service for creating an account, and managing the orders and customer information on a user panel page. 
There is also an admin panel where the site owner can manage the database and collect an updated customer registry.

The website can be [found here](https://magasinet-ekorren.herokuapp.com/).

## Table of Contents

- [UX and UI](#ux-and-ui)
  - [Site Owner Goals](#site-owner-goals)
  - [User Stories](#user-stories)
  - [Wireframes](#wireframes)
- [Design](#design)
  - [Imagery](#imagery)
  - [Colours](#colours)
  - [Fonts](#fonts)
  - [Favicon](#favicon)
- [Features](#features)
  - [Header](#header)
  - [Carousel](#carousel)
  - [All Sections](#all-sections)
  - [About Section](#about-section)
  - [Media Section](#media-section)
  - [Events Section](#events-section)
  - [Contact Section](#contact-section)
  - [Footer](#footer)
- [Deployment](#deployment)
- [Testing](#testing)
  - [Validator Testing](#validator-testing)
  - [Manual Testing](#validator-testing)
  - [Bugs](#bugs)
- [Credits](#credits)
  - [Languages](#languages)
  - [Frameworks, Libraries and Tools](#frameworks-libraries-and-tools)
  - [Images](#images)
  - [Content](#content)

#

## UX and UI

- ### Site Owner Goals

  The website was developed together with the site owner to ensure the main goals of the site was met:

  - Provide information as a marketing tool to get new customers
  - Let the customer rent a storage unit online
  - Present information in a professional and accessible way
  - Ease process of updating the customer database for the product owners invoice program
  - Deploy automated emails for confirmation and notification to the customer and the product owner

#

- ### User Stories

Agile development practices such as user stories were managed by using GitHub's "Issues" tab in the GitHub repository.

The GitHub project can be accessed [here](https://github.com/users/Johneriksson88/projects/4/views/1).
The Issues page can be acceessed [here](https://github.com/Johneriksson88/ekorren/issues)

User stories were divided into three categories:

  - Visitor - a prospective customer enquiring information to make a decision to rent a storage unit
  - Customer - a customer which has decided to rent a storage unit from Magasinet Ekorren
  - Admin - the site owner

  - #### Visitor Goals

    1. As a visitor I can access information about contact, directions and practical information so that I can learn more about the company, their products and how to get in touch with them.
    2. As a visitor I can see arguments for why I would want to rent a storage unit from Magasinet Ekorren so that I can make a decision to rent or not to rent a storage unit.
    3. As a visitor I can access information about the different products and their prices so that I can make a decision to rent or not rent a storage unit.

  - #### Customer Goals

    1. As a customer/visitor I can get clear messages on top of the page so that I get feedback on what I've done.
    2. As a customer I can view my orders so that I know what and how many storage units I'm renting.
    3. As a customer I can edit my contact information so that my contact and invoice details are up to date.
    4. As a customer I can delete orders so that I can cancel my rental of storage unit/units.
    5. As a customer I can delete my account so that I can choose not to be a customer any more.
    6. As a customer I can register an account so that I can update my information and manage/make new orders.
    7. As a customer I can rent a storage unit directly from the web site so that I can quickly act on my decision to rent a storage unit from Magasinet Ekorren.

  - #### Admin goals

    1. As an admin I can login to an admin account so that I can access the admin panel.
    2. As an admin I can get an email notification when a new order is submitted so that I can manually process it.
    3. As an admin I can get an email notification when an order is deleted so that I can cancel the invoicing for that order.
    4. As an admin I can download the customer registry so that I can view it and import it to my invoice software.

  #

  ## Wireframes

  The wireframes for this site were created using Balasmiq. The end product ended up a little bit different from the original wireframe, due to considerations and ideas changing as the creative process flowed on. I only made a wireframe for the landing page, as to get a big picture feel of how the website should look and feel.

  ![Wireframe](main/static/readme/magasinet_ekorren_wireframe.png)


## Design

- ## Imagery

  - ### Logo
    The company logo in the left part of the header has an acorn icon from [flaticon.com](https://www.flaticon.com/). Since the squirrel ('ekorre' in Swedish) is part of the company name, and it repesents the nature of storing and collecting things in one place (think of a squirrel gathering acorns), the acorn felt appropriate for part of the logo. It was the lowest common denominator between the business (storage) and the name (ekorre) and felt natural.
  - ### Hero image
      The hero image of cardboard boxes were purchased from [shutterstock](https://www.shutterstock.com/). They are supposed to represent the nature of storing things in boxes, and provide a fairly uniform color without taking up too much visual capital. This image was the closest option to having a monocolor or gradient background, but with the benefit of having appropriate objects for the business.
  - ### Product cards
      The images for the product cards on the landing page was purchased from [shutterstock](https://www.shutterstock.com/). They are possibly temporary as the site owner wanted to create more personal image representations of the different sizes storage units themselves, but has not done so yet.
  - ### Why us section
      The "why us" section contains 4 icons from [flaticon.com](https://www.flaticon.com/). They were chosen to visually represent the 4 given benefits of renting a storage unit from Magasinet Ekorren. If a visitor were to quickly scroll through the page, the icons being circled to give a badge-like appearance catches the visitor eye and tells a clear story of why Magasinet Ekorren would benefit them.



- ## Colours

  From the start the colors were picked from a squirrel themed palette i found [here](https://colorpalettes.net/tag/colour-of-squirrel-coat/) to represent the colors of the squirrel. At the end of the project when doing the lighthouse testing, I realized that the contrasts using these colors did not pass through the availabilaty-test. After playing around with the Chrome developer tools for testing contrast and availability, i found completely different colors that felt modern, fresh and most of all accessable to the visually impaired and color blind. So essentially accessability dictated the color choices of the entire website.

  Inspiration for color choices can come from a million different places, and I think this shows that a simple thing as playing around with an accessability tool can work at least as well as looking at a color palette.

  To separate the sections on the landing page i chose to have every other section (Get started and Why rent from us) have a contrasting background color of #74cfbf to the other white ones. I did this to clearly signal that the visitor is looking at another section.

- ## Fonts

  The fonts Cinzel Decorative, Bevan and Lato were chosen from the options available from Google Fonts.

  [Cinzel Decorative](https://fonts.google.com/specimen/Cinzel+Decorative?query=cinzel) is only used for the company logo in the header. I thought it looked elegant, modern and the wavy swirls of the capital "M" in "Magasinet" looked almost like a squirrels tail.

  [Bevan](https://fonts.google.com/specimen/Bevan?query=bevan) was chosen for the headings. It is a bold display font that i think clearly defines a new section of the page with its boldness and thickness.

  [Lato](https://fonts.google.com/specimen/Lato?query=lato) was the given choice for all the body text. It is a very popular and familiar font for people browsing the web. The description says: "The semi-rounded details of the letters give Lato a feeling of warmth, while the strong structure provides stability and seriousness", and i felt that these keywords jived with the website as a whole.

- ## Favicon

  The favicon is the same icon as in the logo, and was the clear candidate for representing Magasinet Ekorren as explained in the [logo](#logo) paragraph.

  ![favicon](main/static/images/acorn.png)

## Features

- ## Header

![The Jet Reds Website Navbar](docs/readme_images/navbar.png)

- The Navbar has a fixed position at the head of the page which sits above all other content. This was chosen over a sticky position mainly for browers compatibility, but it's function does not vary in any significant way to a fixed position.
- To ensure the content sat below the header, a margin was added to the top of the page. More information about this can be found in the [Bugs](#bugs) section.
- Sass was used to override the default colour of the links, with a shadow added to contrast against the background colour of the navbar.

#

- The Navbar was coloured using the Bootstrap 'Danger' colour which was used due to the red colour which is relevant to the bands' name.

![Bootstrap Danger Colour Image](docs/readme_images/colour.png)

#

- The logo was provided by The Jet Reds and, due to the unique font used, was retained in an image format, with CSS added to alter size as required. The logo is also a hyperlink which returns the user to the top of the website. The image can be found [here](assets/img/jr_logo.png).

#

- The Navbar contains links to other section on the website. They are designed to be displayed as clickable links, with an overline attribute applied to the element when the user hovers over a link.

![Navbar Mouseover Image](docs/readme_images/navbar_mouseover.png)

- The displayed links disappear on screens with a resolution width below 768 pixels and are replaced with a hamburger menu.

![Navbar Hamburger Menu Image](docs/readme_images/navbar_hamburger.png)

#

- ## Carousel

  - Rather than using a static hero image, I opted to add a carousel below the header which automatically rotates after a set amount of time has elapsed, but also features controls on either side to allow navigation between images.

  The images used can be found below.

     <details>

    <summary>Carousel Image One</summary>

  ![Desktop Wireframe Image](assets/img/JR_carousel_image1.jpg)
    </details>

     <details>

    <summary>Carousel Image Two</summary>

  ![Desktop Wireframe Image](assets/img/JR_carousel_image2.jpg)
    </details>

     <details>

    <summary>Carousel Image Three</summary>

  ![Desktop Wireframe Image](assets/img/JR_carousel_image3.jpg)
    </details>

  #

  - A div has been placed at the foot of the carousel containing real reviews of the band. The div has been coloured black with an opacity of 0.7. This has been done to contrast against the bright background of the images, but also to also some visibility so the full image can still be seen.

  #

  ![Navbar Hamburger Menu Image](docs/readme_images/carousel_review.png)

  #

  - The div containing the reviews is automatically hidden for screens with a resultion width below 768 pixels to allow full visibility of the images.

#

- ## All Sections

- All sections begin with a shadow applied to the Section tag itself, which is replicated throughout the site. This effect was added to give the appearance of each section of the website being layered on top of the section below it, and to add some seperation between sections, instead of an immediate colour change.

#

![Navbar Hamburger Menu Image](docs/readme_images/section_header.png)

#

- The header of the each section is made up of several elements which make it appear to be protruding from the section above.

  - The About section colour has been set to light gray with an opacity of 0.7. This has been done to contrast the white background, but also allows visibility of the shadow from the section element, making it appear as if a seperate shadow is being cast on the header.
  - The colour of all other sections have been set to white gray with an opacity of 0.9. This has been done to contrast the grey background or the blacka and white image of the event section, but also allows visibility of the shadow from the section element, making it appear as if a seperate shadow is being cast on the header.
  - A border radius of 50% has been applied to the bottom left and right corners of the header, giving it a curved appearance.
  - A further shadow has been applied to the header to accentuate it and make it apparent that this sits below the preceding section, but above the content below.

#

- ## About Section

  - The main feature of the About section is an image of vocalist Craig Redpath. This image has been set as the background of the middle column and centered, with a padding of 50% applied to the top of the image. This has been done to ensure the content remains in the center of the page, with any overlap hidden. The image used is actually larger in size to allow some flexibility, with more or less of the image being shown depending on device type.

  #

  ![Navbar Hamburger Menu Image](docs/readme_images/about_centered.png)

  #

  - To the left of the About section image is information the members of the band. This section has had a border radius of 10% applied, with a border of 2 pixels being applied to the right side, to give an appearance similar to a bracket, but also to highlight the edge of the section at lower resolutions.

  #

  - To the right of the About section image is information about the band, the type of music they play, their inspirations and some additional information about the band members. This section has also had a border radius of 10% applied, with a border of 2 pixels being applied to the left side, to give an appearance similar to a bracket, but also to highlight the edge of the section at lower resolutions.

  #

  - Below a screen resolution width of 992 pixels the image in the center of the About section is hidden, with the remaining sections displayed side by side. An example of this can be seen below.

  <details>
    <summary>About Section Below 992 Pixels</summary>

  ![Mobile Wireframe Image](docs/readme_images/below_992.png)
  </details>

  #

  - Below a screen resolution width of 768 pixels the image in the center of the About section remains hidden, with the remaining sections stacked on top of each other.An example of this can be seen below.

  <details>
    <summary>About Section Below 768 Pixels</summary>

  ![Mobile Wireframe Image](docs/readme_images/below_768.png)
  </details>

#

- ## Media Section

  - The Media section is made up of two subsections detailing the latest single and album releases by the band. Both sections have been given the same white background colour as the header, but with a slightly lower opacity of 0.7. This differentiates them from the header slightly, but still offsets them easily against the grey background.

  #

  ![Mobile Wireframe Image](docs/readme_images/single_section.png)

  #

  - The 'Latest Single Info' section contains the single artwork on the left side, with text information about the single on the right. The image remains centered within the left column until the resolution width is below 768 pixels, at which point the image moves to the top of the section and the text information is displayed below.

  <details>
    <summary>Single Section Below 768 Pixels</summary>

  ![Mobile Wireframe Image](docs/readme_images/single_responsive.png)
  </details>

  #

  - The 'Latest Album Info' section contains the album artwork on the right side, with text information about the album on the left. The image remains centered within the right column until the resolution width is below 768 pixels. At this point the original image is hidden, and a new image appears at the top of the section, with the text information displayed below.

  <details>
  <summary>Album Section Above 768 Pixels</summary>

  ![Mobile Wireframe Image](docs/readme_images/album_desktop.png)
  </details>
    <details>
    <summary>Album Section Below 768 Pixels</summary>

  ![Mobile Wireframe Image](docs/readme_images/album_responsive.png)
  </details>

#

- ## Events Section

  - The Events section has a background of guitarist Dan Richards on the left, with vocalist Craig Redpath on the right wearing a guitar strap showing the bands name. This has been set with a fixed position so different parts of the image are shown as the user scrolls down the page. This also contrasts against the rest of the website which has fixed colours. The image used for this section can be found [here](assets/img/event_image.jpg).

  #

  ![Mobile Wireframe Image](docs/readme_images/events_section.png)

  #

  - The main feature of the Events section are the five divs containing information for venues, locations, dates and times of upcoming events, although they are all fictional. A margin of 2 pixels was applied to each div to space each event slightly apart from eachother and avoid having a large block of colour in the center of the page.

  #

  - The background of the Events section has been set to White with an opacity of 0.9 to make the content stand out from the black and white image behind and to ensure readability of the content.

#

- ## Contact Section

  - The contact section features a form asking for four bits of information - Name, email address, the reason for contact and any further information the user wishes to provide.

  #

  ![Mobile Wireframe Image](docs/readme_images/form.png)

  #

  - The form was set to require all fields to be completed as the 'Reason of Contact' options have been left intentionally vague to prompt the user to submit information.

  #

  ![Mobile Wireframe Image](docs/readme_images/form_validation.png)

  #

  - Both the Submit and Reset buttons were set to bright colours as a call to action to the user, but also to match with the original carousel image displayed when the page is loaded which contains those bright colours prominently.

  #

  ![Mobile Wireframe Image](docs/readme_images/form_buttons.png)

  #

  - A small amount of Javascript was written to remove the default function of the Submit button and replace it with a modal response. The code for this can be found [here](assets/js/main.js).

  #

  - The form has been designed in an appropriate manner with the required information and name tags applied, but does not submit the information, or display another page. Instead, a modal is displayed thanking the user for their contact and advising a response will be received soon, with two seperate buttons available to close the modal.

  #

  ![Mobile Wireframe Image](docs/readme_images/form_modal.png)

#

- ## Footer

  - The Footer is made of three seperate sections.

  #

  ![Mobile Wireframe Image](docs/readme_images/footer.png)

  #

  - On the far left a link is displayed which, when clicked, will return the user to the top of the page.
  - In the center, three Font Awesome icons are displayed linking to the Facebook, Twitter and Instagram profiles for the band. All links open in a new tab.
  - On the far left is a text statement containing the phrase "It goes On & On" which is a slogan used by the band.

  #

  - The footer was coloured using the Bootstrap 'Danger' colour which was used due to the red colour which is relevant to the bands' name and to match the colour of the Navbar.

#

## Deployment

The site was created using Visual Studio Code and GitHub, and deployed to GitHub pages for testing using the below process:

    i. Navigate to the repository on GitHub.com
    ii. Select 'Settings' from the navigation bar near the top of the page.
    iii. Select 'Pages' from the sidebar on the left of the page.
    iv. Under the 'Sources' heading, select the 'Branch' dropdown menu and select the main branch.
    v. Once selected, click the 'Save' button to the right of the dropdown menu.
    vi. Deployment should be confirmed by a message on a green background - The message should have a green tick mark followed by "Your site is published at" followed by the web address.
    vii. Confirm deployment by navigating to the displayed web address.

#

## Testing

- ## Validator Testing

The website was tested using the tools made available by the [World Wide Web Consortium](https://www.w3.org/), also known as "W3C".

The two tools used were the [Markup Validation Service](https://validator.w3.org/#validate_by_uri) and the [CSS Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_uri).

In using the "Validate by URI" function in the HTML validator, I found that the validator was throwing errors related to the jinja templating language mixed with the HTML (for example for and if statements as "{% if x == y %}"). The solution i found was to open the page in a browser, righ click anywhere on the page and press "Check page source", and copying the output HTML directly from there and put it in the "Validate by Direct Input"  function. This way i get the fully rendered HTML without the jinja template tags.

No errors were returned for all HTML or CSS across all tests.

 <details>
  <summary>HTML Validation by URL</summary>

![HTML Validation by URL](docs/readme_images/validation/markup_url.png)

  </details>
 <details>
  <summary>HTML Validation by Direct Input</summary>

![HTML Validation by Direct Input](docs/readme_images/validation/markup_direct.png)

  </details>

  <details>
  <summary>CSS Validation by URL</summary>

![CSS Validation by URL](docs/readme_images/validation/css_url.png)

  </details>
 <details>
  <summary>CSS Validation by Direct Input</summary>

![CSS Validation by Direct Input](docs/readme_images/validation/css_direct.png)

  </details>

#

- ## Manual Testing

  The site was tested manually across a range of devices to ensure all links and styling work correctly and to ensure responsiveness across a range of devices. All features on the page were tested, especially the form validation, to ensure user feedback worked properly and no faulty inputs could be made. Testing was carried out on multiple browsers such as Google Chrome, Microsoft Edge, Mozilla Firefox, Safari and Opera. Testing was carried out on an Apple iPhone 12, Apple iPhone 13, Huawei P20, iPad Mini and Windows 10 Desktops.

  The website was also tested in Internet Explorer 11, where some performance and layout issues are present. I was unable to resolve these as Internet Explorer 11 is not supported by Bootstrap 5.

  #

  - ## Lighthouse Testing

  ![Lighthouse Test Result Image](main/static/readme/lighthouse_summary.png)

  A test was ran using Lighthouse within Google Chrome to verify performance and accessibility standards were met and to ensure best practices were followed.

  The following steps were done to improve the score on the Lighthouse test:

    - Contrasting text and background colors were altered until complying with AAA-standars, with help from Google Dev Tools for maximum readability.
    - Images were compressed by using [TinyPNG](https://tinypng.com/).
    - The 'loading = "lazy"' attribute was added to all images, to get them to load when they are scrolled down to, instead of them all loading when the page initially loads.

  The full report can be viewed [here](main/static/readme/lighthouse_expanded.pdf).

  #

  - ## Wave Testing

  ![Wave Test Result Image](main/static/readme/wave_test.png)

  A further test was ran using the Web Accessibility Evaluation Tool (WAVE) to ensure no errors were returned and to verify that no constrast issues existed on the site. This was an important step to ensure that users with disabilities were not negatively impacted by the design of the site and that the relevant standards have been met.

  The contrast warning seemed to be a bug in the validator, since i could not find the element where the warning occurred. 

  #

- ## Bugs

  - ## Section Header obscured on page scrolling

    A bug was discovered that resulted in the header of a section being obscured if the user clicked a link on the navbar. On clicking the link, the page would scroll, but it did not account for the space taken up by the navbar itself, obscuring the header as seen in the image below.

    ![Header Bug Before Resolution](docs/readme_images/header_bug.png)

    Research was carried out on this bug and a resolution was found in an existing CSS property on the documentation made available on the [Mozilla MDN Web Docs website](https://developer.mozilla.org/en-US/docs/Web/CSS/scroll-margin-top).

    The below code was added to the ID tags of each link and was used to define the scroll snap area on each section of the page. Adding this code resolved this issue as seen in the below image.

    Code used to resolve display issue:

    ```
    scroll-margin-top: 3.7rem;
    ```

    ![Header Bug After Resolution](docs/readme_images/header_bug_resolved.png)

## Credits

- ## Languages

  - [HTML5](https://en.wikipedia.org/wiki/HTML5)
  - [CSS](https://en.wikipedia.org/wiki/CSS)
  - [Javascript](https://en.wikipedia.org/wiki/JavaScript)

- ## Frameworks, Libraries and Tools

  - [Am I Responsive](http://ami.responsivedesign.is/) - Used to verify responsiveness of website on different devices.
  - [Balsamiq](https://balsamiq.com/) - Used to generate Wireframe images.
  - [Bootstrap](https://getbootstrap.com/) - Main framework used for the site, with a focus on responsiveness.
  - [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) - Used for overall development and tweaking, including testing responsiveness and performance.
  - [Colour Contrast Analyser](https://www.tpgi.com/color-contrast-checker/) - Used to check colour contrast to ensure usability for users with visual impairements.
  - [Favicon.io](https://favicon.io) - Used to generate Favicon image.
  - [Font Awesome](https://fontawesome.com/) - Used for Social Media icons in footer.
  - [GitHub](https://github.com/) - Used for version control and hosting.
  - [Google Fonts](https://fonts.google.com/) - Used to import and alter fonts on the page.
  - [JQuery](https://en.wikipedia.org/wiki/JQuery) - Used to override default submit functionality and display modal instead.
  - [LambdaTest](https://www.lambdatest.com/) - Used for Cross Site Browser Testing.
  - [Lite-Server](https://www.npmjs.com/package/lite-server) - Used to host website locally to aid testing before updates were commited to GitHub.
  - [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode) - Used for consistent code formatting.
  - [Sass](https://sass-lang.com/) - Used to override existing Bootstrap variables to enhance readability.
  - [Slack](https://slack.com/) - Used for support and advice from the Code Insitute Community.
  - [TinyPNG](https://tinypng.com/) - Used to compress images to reduce filesize without a reduction in quality.
  - [Visual Studio Code](https://code.visualstudio.com/) - Application used for development of this site.
  - [W3C](https://www.w3.org/) - Used for HTML & CSS Validation.
  - [WAVE](https://wave.webaim.org/) - Used for Accessibility evaluation.

- ## Images

  - [The Jet Reds](https://www.thejetreds.co.uk/)

    - The Jet Reds Logo
    - Album Artwork
    - Single Artwork

  #

  - [Sop Rodchenvko](https://www.soprodchenvko.com/)

    - About Section Image
    - Event Section Background

  #

  - [Dave Thompson Imaging](https://www.facebook.com/DaveThompsonImaging)

    - Carousel Images

  #

- ## Content

  - As this site is based on a real band, some content on this site is based on content from the band, with permission. The content used is as follows:

    - The non-photographic content displayed is taken from the band themselves and is the artwork used on their single and album releases.
    - All photos are real photographs of the band. Details of the photographers is listed in the [Images](#images) section.
    - The text content of the 'What We Do', 'Latest Single' & Latest Album' sections are descriptions written by the band themselves and are featured on [the bands website](https://www.thejetreds.co.uk/).

  - The gig venues listed in the Events section are all real venues, but the dates and times of the events are all fictional.