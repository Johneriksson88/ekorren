# The Jet Reds website

![The Jet Reds - Am I Responsive Image](docs/readme_images/am_i_responsive.png)

This website was created as a first portfolio project for Code Institute's Diploma in Web Application Development. The Jet Reds are a real band but, with their permission, I have created this website as I have an interest in and actively follow the band.

The website can be [found here](https://fatheed7.github.io/the-jet-reds/).

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

## UX and UI

- ### Site Owner Goals

  The goal of the site for the owner is to:

  1. Keep fans up to date with the bands latest releases.
  2. Provide some background information about the band, and the type of music they play.
  3. Make fans aware of any upcoming events, including venue, date and time.

#

- ### User Stories

  - #### First Time Visitor Goals

    1. As a first time user, I want to easily understand the type of music played by the band.
    2. As a first time user, I want to be able to easily navigate around the site to find the content I'm looking for.
    3. As a first time user, I'd like to see reviews, to see the opinions of others about the band.

  - #### Returning Visitor Goals

    1. As a returning visitor, I want to find information about any new releases by the band.
    2. As a returning visitor, I want to easily find information about any upcoming shows.
    3. As a returning visitor, I want to find the best way to follow the band on social media.

  - #### Commercial Visitor Goals

    1. As a commercial visitor, I want to easily contact the band with any booking enquiries.

  #

  ## Wireframes

  The wireframes for this site were created using Balasmiq, with each section and subsection noted. I endeavoured to create a single page website and, as such, wireframes are available for desktop view, tablet view and mobile view.

  The sections below show individual wireframes for different devices, with a combined image being available [here](docs/wireframes/collective_wireframe.png).

  The directory containing the wireframe images can be found [here](https://github.com/Fatheed7/the-jet-reds/tree/main/docs/wireframes).

    <details>

    <summary>Desktop Wireframe</summary>

  ![Desktop Wireframe Image](docs/wireframes/desktop_wireframe.png)
    </details>

     <details>
    <summary>Tablet Wireframe</summary>

  ![Tablet Wireframe Image](docs/wireframes/tablet_wireframe.png)
    </details>

     <details>
    <summary>Mobile Wireframe</summary>

  ![Mobile Wireframe Image](docs/wireframes/mobile_wireframe.png)
    </details>

## Design

- ## Imagery

  All of the images used on this website were chosen from the gallery of images currently available on [The Jet Reds Website](https://www.thejetreds.co.uk/gallery/). The main images used were for the Carousel at the top of the page and were used as they clearly show the lineup of the band, but do not detract from the footer within the carousel and contrast well with the opacity of this section.

  The images in the About section was chosen as an "in action" shot, showing vocalist Craig Redpath performing live, but it was also chosen as it fits well between the bracket like borders of the about section, giving the impression of sound waves.

  Both images used in the Media section are the actual artwork used for the album and single described on the site, and are used for this reason.

  The image for the Event section was chosen as it sticks with the theme of basic colours of the website, and matches the black and white images used in the about section. Additionally, whilst the image shows members of the band in action, the image is not too busy and does not distract from the main elements of the Event section.

- ## Colours

  The colours of the website were chosen to constrast with the brightness of the header and carousel images, but to blend in with the images used in other sections. This allowed contrasting colours to be chosen which results in good readability for users. These colours were also tested using the 'Rendering' function within Google Chrome to ensure readability for users with all forms of colour blindness.

  - #9B3545 - This colour was used for the header and footer of the website and was chosen due to the red theme within the bands name, but also due to the colour contrast against the default navbar text colour. A text using the Colour Contrast Analyser can be seen [here](docs/readme_images/header_colours.png).

  - #d1d1d1 - This colour was used as the background for the Media and Contact sections due to it conflicting with the colours of other sections, and against the main body elements.

  - #fff - This plain white colour was chosen for the about section due to its immediate contrast with the carousel images at the top of the page and due to it matching with the black and white nature of the image within the section.

  - rgba(255, 255, 255, 0.7) - This colour was used for the Single and Album containers in the Media section. A white colour was chosen to contrast against the grey background, but some opacity was applied to make this colour more subtle than previous white colours used.

- ## Fonts

  The fonts Roboto & Lato were chosen from the options available from Google Fonts.

  [Roboto](https://fonts.google.com/specimen/Roboto) was chosen as the main font for the website due to it "allowing letters to be settled into their natural width. This makes for a more natural reading rhythm", as described in the About section for the font on the [Google Fonts website](https://fonts.google.com/specimen/Roboto#about).

  [Lato](https://fonts.google.com/specimen/Lato) was chosen due to the rounder nature of the font and was primarily used for the headings of each section, as well as the main content within the Events section.

  These fonts were chosen with user accessibility and readability in mind, with a backup on sans-serif chosen for any instances where these fonts may not be available.

- ## Favicon

  The website [Favicon.io](https://favicon.io/) was used to generate the favicon image for the website. The colour #DC3545 was used for the background of the image. This was originally consistent with the colour used for the header and footer of the website, but this was then changed to #9B3545 for colour contrast reasons. I decided to stick with the originally created Favicon as it still matches the overall theme of the site and is more noticable than the alternative colour. The text was chosen to be white as this contrasts well with the chosen colour, with the font Khmer chosen for readability. Due to the limited space available the initials of the band, TJR, were chosen for the favicon. This is beneficial as it stands out and is easy identifiable when multiple tabs are open.

  ![Mobile Wireframe Image](docs/readme_images/favicon.png)

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

The two tools used were the [Markup Validation Service](https://validator.w3.org/#validate_by_uri) and the [CSS Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_uri). Both tools were used to test the website by URL and also by direct input, with the results shown below.

No errors were returned for all HTML or CSS across all tests. Some warnings were displayed.

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

  The site was tested manually across a range of devices to ensure all links and styling work correctly and to ensure responsiveness across a range of devices. All features on the page were tested, especially the javascript element, to ensure functionality was not impacted in any way. Testing was carried out on multiple browsers such as Google Chrome, Microsoft Edge, Mozilla Firefox, Safari and Opera. Testing was carried out on an Apple iPhone, Apple iPhone 13, Samsung Galaxy S20 FE, Samsung Galaxy A51, Apple iPad Pro & Windows 10 Desktops.

  The website was also tested in Internet Explorer 11, where some performance and layout issues are present. I was unable to resolve these as Internet Explorer 11 is not supported by Bootstrap 5.

  [LambdaTest.com](https://www.lambdatest.com/) was used for cross browser testing.

  #

  - ## Lighthouse Testing

  ![Lighthouse Test Result Image](docs/readme_images/lighthouse.png)

  A test was ran using Lighthouse within Google Chrome to verify performance and accessibility standards were met and to ensure best practices were followed.

  The full report can be viewed [here](docs/lighthouse.pdf).

  #

  - ## Wave Testing

  ![Wave Test Result Image](docs/readme_images/wave.png)

  A further test was ran using the Web Accessibility Evaluation Tool (WAVE) to ensure no errors were returned and to verify that no constrast issues existed on the site. This was an important step to ensure that users with disabilities were not negatively impacted by the design of the site and that the relevant standards have been met.

  A full version of the test can be viewed [here](https://wave.webaim.org/report#/https://fatheed7.github.io/the-jet-reds/).

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