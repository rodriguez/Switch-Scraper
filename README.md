# Switch-Scraper (**Work in Progress**)
Scrapes the newest submissions to /r/NintendoSwitchDeals and texts the most probable deals for a Nintendo Switch to your phone!
## Backstory
I personally was on the hunt for good deals on a Nintendo Switch console since I wanted a portable gaming system that I could bring abroad during college. Once the project was off the ground and producing results, I was able to use the script to text me recent Nintendo Switch deals so that I could pounce on the deals before the deal expired. I later added support for searching for specific game deals, since the Nintendo system would be of no use to me without any games for the system.
## What Technologies were Used?
### Early Iteration (*Get Everthying Working*)
- Python
- JSON
### Intermediate Iteration (**Streamline Features with new Technologies)**
- Python
- TwilioAPI
- MongoDB
### Current Iteration (Including a Front End)
- Python
- Flask
- MongoDB
- HTML/CSS
# General Project Comments/Complaints/Reflection
Looking back on this project, from a purely efficiency standpoint, this project serves no real purpose for me since I could easily keep refreshing the Switch deals subreddit and pounce on a deal that I liked. I really didn't have to use a DBMS because I could have probably simply scraped the new posts, decide if any were valid deals, and text it to my phone. I initially used a database because since I wanted to take care of the case where the script scrapes the same posts and texts multiple copies to me; this was remedied by storing all posts into the database. However, because the mod team on the subreddit is pretty good, I could have only kept the time stamp of the last post I scrape and check posts after that time stamp such that no post would be scraped more than once. I didn't really need a front end since this was more of a personal project. With all that said, I enjoyed this project because it introduced me to new technologies that I've never used before. I've developed skills that will help me for future projects.
# Credits to Andres Rodriguez and Brandon Chen