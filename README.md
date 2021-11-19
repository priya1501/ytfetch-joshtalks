# YouTube Videos Fetching Task - JoshTalks

## Task  
To make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

## TechStack
* Django
* Django RestFramewok

## Instructions to run the server 
Clone the repo and install Requirements :<br>
```
git clone https://github.com/priya1501/ytfetch-joshtalks
cd path_to_ytfetch-joshtalks
pip install -r requirements.txt (Install the requirements preferrably in Virtual environment)
```
Modify settings.py File - Remove the existing keys and add your own YouTube Data API keys in the form [APIKEY1, APIKEY2, ..]:
```
API_KEYS = ['APIKey1', 'APIKey2', ..] 
```
Run the following command:
```
python manage.py runserver
```
Now open any browser of your choice and follow further steps:
```
To fetch new videos, visit http://127.0.0.1:8000/new 
To view the newly fetched videos, visit http://127.0.0.1:8000
```

## Screenshots 
### When you first visit the website, following page will appear:
![New Page](https://github.com/priya1501/ytfetch-joshtalks/blob/main/new_page.jpeg)
### After visiting the /new endpoint, on successful retrieval of videos, the following page will appear:
![Videos successfullly fetched page](https://github.com/priya1501/ytfetch-joshtalks/blob/main/videos_successfully_fetched.jpeg)
### Now on the home page you can see the list of fetched videos in reverse chronological order:
![Home page](https://github.com/priya1501/ytfetch-joshtalks/blob/main/videos_fetched.jpeg)
