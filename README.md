# Software Engineering Project 1

Software Engineering Project 1 is an example project meant to scrape reddit and output contents to a file. In this, I used praw (the reddit api)

## Installation and Usage
1. Create a new conda environment, activate it, and import environment.yml
2. Create a reddit api key:  
    1. Go to the api request link https://support.reddithelp.com/hc/en-us/requests/  
    2. Under "What do you need assistance with?" select "API Support and Inquiries"
    3. Under "From what position are you reaching out for support?" select "I am a developer"
    4. Under "What is your inquiry?" select "I want to register to use the free tier of the Reddit API"
    5. Fill in other sections as needed with your own information.
3. Copy the client id and secret id you received and the redirect uri you used into a file called secrets.json as seen below.
```json
{
    "client_id":"YOUR CLIENT ID",
    "secret_id":"YOUR SECRET ID",
    "redirect_uri":"http://localhost:8080",
    "user_agent":"A reddit scraper for a school project"
}
```
4. Change the user agent as you see fit
5. Run main.py through python using the following syntax:
```bash
python ./main.py {subreddit link, default reddit.com/r/all}
```