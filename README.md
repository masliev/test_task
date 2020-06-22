# test_task
## Overview
I chose to use service-based approach that give us flexibility, modifiability and following SOLID and DRY principle.
For the template things I used python dict because it's easy to control, memory-optimized and fully integrated with python ecosystem unlike other solutions like yaml, json files etc.


## How to set up this project?
- create virtualenv
- install requirements (req.txt)
- run python main.py 

## Important notes
Firstly I prepared questionnarie with 2 questions
![alt text](https://i.imgur.com/BS11f69.png)

this template generated from answers based on this two questions
![alt text](https://i.imgur.com/vh5zqeK.png)


then I extended it with one more question
![alt text](https://i.imgur.com/6Q3CzCd.png)

This template generated from answers based on three questions. Instead of getting an error I prepared services to handle unexpected field by adding it to the template but with just an internal typeform id of the answer.
![alt text](https://i.imgur.com/2DymRMf.png)

You can play with it by changing questionnaire_id in api_service and running python main.py
![alt text](https://i.imgur.com/KXbq7YQ.png)

## Link to video
https://mega.nz/file/b5hikSaC#xpvJy814D96ZQTcHFTR4AE50TlH3QEAkAvskut2Zs8k
