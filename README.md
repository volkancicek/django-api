# django-api
django restful api

#Install & Run
Run the following commands at the directory `src/` :

install packages 

`pip install -r requirements.txt`

create DB table

`python manage.py migrate --run-syncdb`

init DB records

`python init_data.py`

run app

`python manage.py runserver 8080`

# Endpoints


**Filters:**
* date filter:
    ```
     /metrics/?date_from=2017-05-01&date_to=2017-05-31
     ```
  
* multiple filters:
    ```
    /metrics/?date_from=2017-05-01&date_to=2017-05-31&channel=facebook
    ```    
**Group By:**
 
* group by single field:
    ```
    /metrics/?group_by=date
    ```
 
* group by multiple field:
    ```
    /metrics/?group_by=channel,country
    ```
      
**Sorting:**
 
* sorting asc:
    ```
    /metrics/?ordering=channel
    ```
 
* sorting desc:
    ```
    /metrics/?ordering=-channel
    ```
            
**Common API use cases:**
* Show the number of impressions and clicks that occurred before the 1st of June 2017, broken down by channel and country, sorted by clicks in descending order

    ```
    /metrics/?date_to=2017-06-01&group_by=channel,country&ordering=-clicks&fields=channel,country,impressions,clicks
    ```
      
     Response:
      
    ```
        [
          {
                "channel": "adcolony",
                "country": "US",
                "impressions": 532608,
                "clicks": 13089
            },
            {
                "channel": "apple_search_ads",
                "country": "US",
                "impressions": 369993,
                "clicks": 11457
            },
            {
                "channel": "vungle",
                "country": "GB",
                "impressions": 266470,
                "clicks": 9430
            },
                  .
                  .
                  .
            ```
      
 * Show the number of installs that occurred in May of 2017 on iOS, broken down by date, sorted by date in ascending order.

     ```
     /metrics/?os=ios&date_from=2017-05-01&date_to=2017-05-31&group_by=date&ordering=date&fields=date,os,installs
     ```
       
      Response:
       
      ```
            [
              {
                  "date": "2017-05-17",
                  "os": "ios",
                  "installs": 755
              },
              {
                  "date": "2017-05-18",
                  "os": "ios",
                  "installs": 765
              },
              {
                  "date": "2017-05-19",
                  "os": "ios",
                  "installs": 745
              },
              .
              .
              .
      ```
        
 * Show revenue, earned on June 1, 2017 in US, broken down by operating system and sorted by revenue in descending order.
 
     ```
     /metrics/?date=2017-06-01&country=US&group_by=os&ordering=-revenue&fields=date,country,revenue,os
     ```
       
      Response:
     ```

       [
           {
               "date": "2017-06-01",
               "country": "US",
               "os": "android",
               "revenue": 662.9599999999999
           },
           {
               "date": "2017-06-01",
               "country": "US",
               "os": "ios",
               "revenue": 630.76
           }
       ]
     ```
       
  * show CPI values for Canada (CA) broken down by channel ordered by CPI in descending order
  
      ```
      /metrics/?country=CA&group_by=channel&ordering=-cpi&fields=country,cpi,channel
      ```
        
       Response:
       
      ```
         [
             {
                 "channel": "facebook",
                 "country": "CA",
                 "cpi": 2.0748663101604277
             },
             {
                 "channel": "chartboost",
                 "country": "CA",
                 "cpi": 2.0
             },
             {
                 "channel": "unityads",
                 "country": "CA",
                 "cpi": 2.0
             },
             {
                 "channel": "google",
                 "country": "CA",
                 "cpi": 1.7419860627177708
             }
         ]
      ```
