# FreePL

**FREEPL is a online fantasy cricket game where the player gets to create a team according to the live matches going on around th world.


The player at the end with highest total stocks and cash wins the game.


## Building from Source

1. Create a **virtual environment** with virtualenv (install virtualenv, if its not installed).

    ```
    virtualenv freepl

    ```

2. Clone the project in the virtual environment directory.

    ```
    cd freepl
    git clone https://github.com/lugnitdgp/freepl_main.git

    ```

3. Activate the virtual environemnt.

    #### For Linux/Mac OSX   
    ```
    source bin/activate

    ```

    #### For Windows
    ```
    .\Scripts\activate

    ```

4. Install the requirements.

    ```
    cd freepl_main
    pip install -r requirements.txt

    ```

5. Copy the settings.py.example file in the freepl_main directory to settings.py

    ```
    cd freepl_main
    cp settings.py.example settings.py
    cd ..

    ```

6. Open the settings.py file and add an arbitary secret key.

7. Generate Google+ OAuth credentials with the following steps:

    + Go to [Google developer console](https://console.developers.google.com/)    

    + Create a new project if you do not have any (see the drop-down at the top left of your screen).

    + After the project is created you will be redirected to a dashboard. Click on **ENABLE API** button.

    + Select **Google+** API from the Social APIs section.
    + On the next page, click the **Enable** button to enable Google+ API for your project.

    + To generate credentials, select the Credentials tab from the left navigation menu and hit the ‘Create Credentials’ button.

    + From the drop-down, select OAuth client ID.

    + On the next screen, select the application type (web application in this case) and enter your authorized javascript origins and redirect uri. For now, just set the origin as http://localhost:8000 and the redirect URI as http://localhost:8000/complete/google-oauth2/

    + Now, go to `settings.py` and add your OAuth credentials like this:

    ```python
    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = <client ID>
    SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = <client secret>

    ```

8. Generate Facebook login credentials with the following steps:

    + Go to [Facebook Developers Console](https://developers.facebook.com/)

    + Click on **My Apps** and then **Add a New App**.

    + Enter _Display Name_ and _Contact Email_ and click on **Create App Id**.

    + Select **Facebook login** and choose **set up**. Pick **Web** on the next page.

    + Enter `http://localhost:8000` as the _Site Url_ and hit **Save**.

    + Now go to **Settings/Basic** and then in the _App Domains_ just put `localhost` and hit **Save Changes**.

    + Grab the App ID and App Secret and add them to `settings.py` likethis:

    ```python
    SOCIAL_AUTH_FACEBOOK_KEY = <app ID>
    SOCIAL_AUTH_FACEBOOK_SECRET = <app secret>

    ```

9.  Migrate your database and run the Django Development Server.

    ```
    ./manage.py makemigrations
    ./manage.py migrate
    ./manage.py runserver

    ```

10. Open `http://localhost:8000` in your browser. (Opening `http://127.0.0.1:8000` will cause problems with Social Login)

## For contributors

FreePL uses the following technologies:

+ HTML/CSS/JavaScript
+ Pyhton(Django)

## If you wish to contribute, please open a **new issue** before making any pull request. **Every pull request should
have a reference to an issue.**


### Making your your first pull request

- First, fork this repository
- Clone it using ``` git clone https://github.com/[username]/freepl_main.git ```
- It is always recommended to make your changes in a new branch rather than master.
  So create a new branch using ``` git branch mybug ```
- Checkout into your new branch using ``` git checkout mybug ```
- Hack the code, and do all kinds of awesome stuff.
- After you are done add your changes using ``` git add --all```
- Commit your changes using ``` git commit ``` and provide a commit message.
- After you have committed your changes push your changes to your forked repository
  using ``` git push origin mybug ```
- Finally create a pull request from github.
- If everything is alright then soon your changes will get merged or else you will
  be asked to make changes.

There should be **only one commit per pull request**.

Please try to make sure that your commit message and body follows the
guidelines below.

- Commit message should be of the form : ``` Fixes issue #[issue_number] - what you solved in one line ```
- After commit message, there should be a commit body where you can mention what you did in short or in detail

Please try to follow this format as it will be helpul for maintainers as well as co-developers/contributors
to stay aligned.
