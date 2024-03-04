**Wonders Of India**
<br>
Video Demo:  https://youtu.be/oVSRQW1FmbA?si=Eq6PLmpwf-mNb1-w
<br>
Description:


    In this final project, there are "static" and "templates" folders.

    In the "static" folder, there's a "styles.css" file and several .jpg files.

    Within the "templates" folder, you'll find HTML files used for structuring the webpage.

    Let's delve into the "templates" folder:

        'layout.html': This file creates the basic layout of the webpage. It serves as the foundation for all other HTML files. Within the <head> section, I've utilized <meta> tags to describe the webpage. Additionally, I've included Bootstrap and my custom stylesheet, 'styles.css'. At the end of the <head>, jinja syntax is used to incorporate headers from the templates. Within the body, a Bootstrap-based navigation bar is created, followed by Jinja syntax to include the header and the rest of the body content.

        'index.html': This file constructs the homepage. It features a table displaying the names of the wonders, the respective states they're in, and their notable features.

        'gommateshwara.html', 'hampi.html', 'harmandir.html', 'khajuraho.html', 'konark.html', 'nalanda.html', and 'taj.html': These files individually describe India's seven wonders. Each page includes an image and brief details of the respective wonder.

    In the "static" folder:

        'styles.css': This CSS file contains all the styling properties utilized on the webpage. Additionally, it incorporates a background image ('background.jpg').

        There are also seven more .jpg files, each depicting one of the seven wonders of India.

    Lastly, in 'app.py':

        I've imported Flask to run the webpage. There are a total of eight routes, each leading to a specific page previously defined:

        '/': The homepage created using 'index.html'.
        Seven other routes leading to pages describing India's seven wonders.



    How my website works?
        After running, you will first see a navigation bar at the top of the page. You can use it to go to other pages of my website. And in the center of the navigation bar you will see 'Wonders Of India' writen. You can click that and return back to the homepage of my website anytime.

        Below navigation bar, there is a table which will show you name of the wonders, which state they are in and what they are known for.

        You can click the name of any wonder and it will take you to another page where you can see little more details about that wonder.

        After clicking, you will see name of the wonder, little description about it, below that a image of that wonder and lastly, below that image you will see more details about that wonder.

        All the pages describing the wonders are design same.



    That's a wrap! I hope you enjoy exploring this site and learning about India's fascinating seven wonders.
