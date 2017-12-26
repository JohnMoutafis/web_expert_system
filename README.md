# Web Expert System

## This is a proof of concept project.

Using PyKnown (https://github.com/buguroo/pyknow) module, 
create a Web Expert System to implement rules and return responses
based on the outcome of those rules. 

## Usage

1. Install the requirements:
    
    `pip install -r requirements.txt`

2. Start the server:

    `python app.py`
    
3. Use the endpoints:

    - Robot endpoint:
    
        To use this endpoint you need to make a POST request as follows:
    
          http POST http://localhost:5000/example/robot/
          light='green'
          
        Response:
        
          { 
            "response": 'Cross the road' 
          }
    
    - Maximum endpoint:
    
        To use this endpoint you need to make a POST request as follows:
        
          http POST http://localhost:5000/example/maximum/
          find_max_of=[20, 31, 4, 141, 1, 12]
         
        Response:
        
          { 
            "response": 141 
          }
