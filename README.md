### Monkey Search - Retrieval (Web Scraping)
- - -
#### Introduction:
#### Monkey search engine search the movies / tv series / franchise as per the keyword enter by the user, recommend the movies as per the user preferred Genre,Trending news and coming soon movies with top 250 pickups, search results can be redirected to their trailer links, Admin can also view the statistics on the data captured


## Tech stack used
- - - 
1. ReactJs - Building frontend.
2. NodeJs - Process api before hitting the backend
3. Python Flask - API development.
## Frontend
- - -
## Steps to Run
- - -
1. Clone the repository 
```
https://github.com/samyakjain20/retreival-mern/
```
2. Install the node modules. Open two terminals.
### Terminal1
- - -
```
cd frontend
npm install
```
### Terminal2
- - -
```
cd middleware
npm install
```
3. Run both the servers - reactjs, nodejs.
### Terminal1
- - -
```
cd frontend
npm run start
```
### Terminal2
- - -
```
cd middleware
npm run start
```
## Backend Services
- - -
## Steps to run
- - -
1. Clone the project 
```
https://github.com/yash-pathak-1997/SSD-Project-Python.git
```
2. Run main.py
```
python3 main.py
```
## APIs
- - -
1. Admin data API : To populate the dashboard for Admin displaying no of movies per language, Genre, Day wise hits
```
http://localhost:7200/api/admin
```
2.  Coming Soon: API to Display Coming soon movies
```
http://localhost:7200/api/comingSoon
```
3. Recently Viewed: API to display the movies recently viewed by user
```
http://localhost:7200/api/recentlyViewed
```
4. Search : To display list of info on query data
```
http://localhost:7200/api/search?keyword=pirates
```
5. Search on Enter : To display data in cards when enter click on keyword searched
```
 http://localhost:7200/api/search/display?keyword=pirates
```
6. Search Click : To display information(Description,Director,cast etc....) of specific movie clicked by user
```
http://localhost:7200//api/search_click
```
7. News : To display current trending news related to tv, movies, shows etc..
```
http://localhost:7200/api/showNews
```
8. Top 250 : To display top 250 movies , having different filters and sorting options 
```
http://localhost:7200/api/top/250
```
9. User Fav : Displaying movies as per the user fav choice on the basis of clicks and serach
```
 http://localhost:7200/api/userFav
```

