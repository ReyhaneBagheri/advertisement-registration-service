# advertisement-registration-service
Advertisements include all types of vehicles. Each user can send an advertisement of his vehicle in the form of a combination of text and image description and his email address.
### Our service checks the registered ad in the first step.
 - Each ad is placed in its corresponding category according to the type of vehicle in its image (car, motorcycle, bicycle, etc).
 - If the ad image does not contain any vehicle, the ad will be rejected.
- Finally, after processing the ad, the user will be notified of the result of his ad registration by sending an email. 
- In this email, if the ad is approved, a link to the ad along with its category will be placed. 
- If the ad is rejected, this will be mentioned in the email.

### Project Description
- Our software consists of two backend services. 
- The first service is responsible for receiving user requests and responding to them.
-  The second service has the task of processing (determining the category or rejecting the ad).
#### First service
##### This service consists of two APIs.
- Ad registration API:
1-This API receives the information of an ad including text, image and email of its sender.
2-The information of this ad, including the text and email address of the sender, is stored in the database and a unique identifier(ID) is considered for it.
3-Stores the image in an object storage.
4-Writes the ad ID for processing into the RabbitMQ queue.
5-As a response to the request, a message like (Your ad was registered with this ID) will be sent to the user.
- Ad receiving API:
1-This API receives the ID of an ad.
2-If the ID related to an ad has not been checked, in response, a message like (Your ad is in the review queue) will be sent to the user.
3-If the ID related to an ad is rejected, a message like (your ad was not approved) will be given in response.
4-If this ID corresponds to a verified ad, the information of this ad including text, image and category and status will be returned in the response.

#### Second service
- The task of this service is to read advertisements from the RabbitMQ queue, process them and save the result on the database.
1-This service is connected to the RabbitMQ queue and listens for new messages. Each message corresponds to a registered advertisement.
2-In each message read from the queue, there is an advertisement ID. With this ID, the ad photo is received from the object storage.
3-The ad photo is sent to the photo tagging service for processing. From the response of the tagging service, the first tag is selected as the ad category. We put this category in the category column of the database.
4-By using the email sending service, an email is sent to the user to inform the user of the status (approval or rejection) of her ad.
### Images of project
- POST request 










![1](https://user-images.githubusercontent.com/78312765/204086307-b65cf5d3-9b5a-4661-b8a3-42c44c5d42fb.png)












- GET request 













![2](https://user-images.githubusercontent.com/78312765/204086311-f676120e-ce9b-423c-b9ea-6189007c113f.png)











- Response of POST request 









![3](https://user-images.githubusercontent.com/78312765/204086312-6c59b03e-8c0e-430d-9fb5-4cc4ea1633df.png)











- Request response after confirmation












![4](https://user-images.githubusercontent.com/78312765/204086313-d1a4ada8-d3b2-4cf3-a794-90cafa0b7dd2.png)











- Request response to the ad that is being reviewed












![5](https://user-images.githubusercontent.com/78312765/204086314-7bd45c2a-c8b3-4ae3-b5c7-1bdfef9c3759.png)












- The second service is checking the information











![6](https://user-images.githubusercontent.com/78312765/204086315-75338bec-989c-4b23-9d9e-c200bc5af940.png)











- Second service response












![7](https://user-images.githubusercontent.com/78312765/204086316-dbb7426b-439d-40b3-8114-4b3eeaf929a0.png)










- The email sent by the second service to the user






![8](https://user-images.githubusercontent.com/78312765/204086317-2496ef10-26ef-4b82-a778-f59c3f2c8089.png)
