# Quick guide to using Elasticsearch (via Kibana)



The data is uploaded to an Elasticsearch search engine. The data can be accessed via the Kibana dashboard.



Access the search engine on: http://130.226.98.25:5601/

You will then reach the logon screen. Used the login information provided in the e-mail:

![image-20210709151503890](C:\Users\kgk\AppData\Roaming\Typora\typora-user-images\image-20210709151503890.png)



When logging in, you will reach the Kibana dashboard. Kibana is a pretty massive application with a ton of features. Here we are only using it as a search engine. 

You can access the data by clicking the menu icon in the top left corner (the 3 horizontal stripes) and selecting "Discover" under the "Kibana" heading:

![image-20210709151637463](C:\Users\kgk\AppData\Roaming\Typora\typora-user-images\image-20210709151637463.png)



The "Discover" dashboard is the main interface for searching data. The search engine contains several dataset and it may default to another dataset than the one relevant for your project.

You can change the dataset to the DRR set by selecting it from the drop-down to the left just below the "Search" field and "Add filter" option. Select "drr*" to select the DRR data:

![image-20210709151938165](C:\Users\kgk\AppData\Roaming\Typora\typora-user-images\image-20210709151938165.png)



Kibana will show all results by default. The texts can be searched by using the search field. The search field works by first writing the field in the data to search in and the type what to search for. The actual text in the data is located in the field "text", so to search the textual content, a query would look like this:

![image-20210709152149233](C:\Users\kgk\AppData\Roaming\Typora\typora-user-images\image-20210709152149233.png)



After pressing Enter or clicking "Update", Kibana will search the texts. When finished it will display the number of hits and the results: 

![image-20210709152244665](C:\Users\kgk\AppData\Roaming\Typora\typora-user-images\image-20210709152244665.png)



Each result can be expanded. Note that each hit contains the URL to the page or pdf in the field "url": 

![image-20210709152336156](C:\Users\kgk\AppData\Roaming\Typora\typora-user-images\image-20210709152336156.png)



The result view can be customized by picking what fields to display from the "Available fields" to the left. By clicking "Add" for the field, it will be added as a column to the result window.

![image-20210709152413349](C:\Users\kgk\AppData\Roaming\Typora\typora-user-images\image-20210709152413349.png)





It is also possible to add filters by clicking "Add filter". The data contains limited information to filter but these could be relevant options:

- "org": What organization the text is from ("unddr" or "drmkc")
- "type": What type of data it is ("webpage" or "pdf")



To only search the pdfs, a filter can be added as below:

![image-20210709152704270](C:\Users\kgk\AppData\Roaming\Typora\typora-user-images\image-20210709152704270.png)



The results will then be updated according to the filter.



Read more about searching in Kibana here: https://www.elastic.co/guide/en/kibana/current/discover.html#search-in-discover