## complete path 1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"check_loc": true}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_range
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_send_email
* affirm
    - utter_ask_email
* send_email{"email": "agarwal.nageshwari@gmail.com"}
    - slot{"email": "agarwal.nageshwari@gmail.com"}
    - action_send_mail
    - utter_email_sent
    - export

## complete path 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "goa"}
    - slot{"location": "goa"}
    - action_check_location
    - slot{"check_loc": false}
    - utter_loc_invalid
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"check_loc": true}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_range
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_send_email
* affirm
    - utter_ask_email
* send_email{"email": "agarwal.nageshwari@gmail.com"}
    - slot{"email": "agarwal.nageshwari@gmail.com"}
    - action_send_mail
    - utter_email_sent
    - export

## complete path 3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"check_loc": true}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_range
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_send_email
* deny
    - utter_goodbye
    - export

## interactive_story_1
* greet
    - utter_greet 
* restaurant_search{"cuisine": "italian"} 
    - slot{"cuisine": "italian"}
    - utter_ask_range
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"check_loc": true}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_send_email
* deny
    - utter_goodbye
    - export

## interactive_story_2    
* greet
    - utter_greet
* restaurant_search{"location": "delhi ncr"}
    - slot{"location": "delhi ncr"}
    - action_check_location
    - slot{"check_loc": true}
    - slot{"location": "Delhi NCR"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_range
* budget{"price": "300-700"}
    - slot{"price": "300-700"}
    - action_search_restaurants
    - slot{"location": "Delhi NCR"}
    - utter_send_email
* affirm
    - utter_ask_email
* send_email{"email": "agarwal.nageshwari@gmail.com"}
    - slot{"email": "agarwal.nageshwari@gmail.com"}
    - action_send_mail
    - utter_email_sent
    - export

## interactive_story_3
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "pune"}
    - slot{"cuisine": "italian"}
    - slot{"location": "pune"}
    - action_check_location
    - slot{"check_loc": true}
    - slot{"location": "Pune"}
    - utter_ask_range
* budget{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - action_search_restaurants
    - slot{"location": "Pune"}
    - utter_send_email
* affirm
    - utter_ask_email
* send_email{"email": "agarwal.nageshwari@gmail.com"}
    - slot{"email": "agarwal.nageshwari@gmail.com"}
    - action_send_mail
    - slot{"email": "agarwal.nageshwari@gmail.com"}
    - utter_email_sent

## interactive_story_4
* greet
    - utter_greet
* restaurant_search{"price": "More than Rs.700", "cuisine": "south indian", "location": "chandigarh"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "chandigarh"}
    - slot{"price": "More than Rs.700"}
    - action_check_location
    - slot{"check_loc": true}
    - slot{"location": "Chandigarh"}
    - action_search_restaurants
    - slot{"location": "Chandigarh"}
    - utter_send_email
* affirm
    - utter_ask_email
* send_email{"email": "agarwal.nageshwari@gmail.com"}
    - slot{"email": "agarwal.nageshwari@gmail.com"}
    - action_send_mail
    - slot{"email": "agarwal.nageshwari@gmail.com"}
    - utter_email_sent
    - export

## interactive_story_5
* greet
    - utter_greet
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - utter_ask_location
* location_dataset{"location": "purulia"}
    - slot{"location": "purulia"}
    - action_check_location
    - slot{"check_loc": false}
    - slot{"location": null}
    - utter_loc_invalid
    - utter_ask_location
* location_dataset{"location": "pune"}
    - slot{"location": "pune"}
    - action_check_location
    - slot{"check_loc": true}
    - slot{"location": "Pune"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_search_restaurants
    - slot{"location": "Pune"}
    - utter_send_email
* affirm
    - utter_ask_email
* send_email{"email": "agarwal.nageshwari@gmail.com"}
    - slot{"email": "agarwal.nageshwari@gmail.com"}
    - action_send_mail
    - slot{"email": "agarwal.nageshwari@gmail.com"}
    - utter_email_sent
    - export

## interactive_story_6
* greet
    - utter_greet
* restaurant_search{"price": "More than Rs.700", "location": "dhanbad"}
    - slot{"location": "dhanbad"}
    - slot{"price": "More than Rs.700"}
    - action_check_location
    - slot{"check_loc": true}
    - slot{"location": "Dhanbad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "Dhanbad"}
    - utter_send_email
* deny
    - utter_goodbye
    - export

## interactive_story_7
* greet
    - utter_greet
* restaurant_search{"price": "More than Rs.700", "location": "dhanbad"}
    - slot{"location": "dhanbad"}
    - slot{"price": "More than Rs.700"}
    - action_check_location
    - slot{"check_loc": true}
    - slot{"location": "Dhanbad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "Dhanbad"}
    - utter_send_email
* affirm
    - utter_ask_email
* send_email{"email": "agarwal.nageshwari@gmail.com"}
    - slot{"email": "agarwal.nageshwari@gmail.com"}
    - action_send_mail
    - slot{"email": "agarwal.nageshwari@gmail.com"}
    - utter_email_sent
    - export

## interactive_story_8
* greet
    - utter_greet
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - utter_ask_location
* location_dataset{"location": "purulia"}
    - slot{"location": "purulia"}
    - action_check_location
    - slot{"check_loc": false}
    - slot{"location": null}
    - utter_loc_invalid
    - utter_ask_location
* location_dataset{"location": "pune"}
    - slot{"location": "pune"}
    - action_check_location
    - slot{"check_loc": true}
    - slot{"location": "Pune"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_search_restaurants
    - slot{"location": "Pune"}
    - utter_send_email
* deny
    - utter_goodbye
    - export

## interactive_story_9
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"check_loc": true}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_range
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - action_search_restaurants
    - utter_send_email
* deny
    - utter_goodbye
    - export

## interactive_story_10
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "goa"}
    - slot{"location": "goa"}
    - action_check_location
    - slot{"check_loc": false}
    - utter_loc_invalid
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - action_check_location
    - slot{"check_loc": true}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_range
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - action_search_restaurants
    - utter_send_email
* deny
    - utter_goodbye
    - export

## interactive_story_11
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"check_loc": true}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_range
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - action_search_restaurants
    - utter_send_email
* affirm
    - utter_ask_email
* send_email{"email": "agarwal.nageshwari@gmail.com"}
    - slot{"email": "agarwal.nageshwari@gmail.com"}
    - action_send_mail
    - slot{"email": "agarwal.nageshwari@gmail.com"}
    - utter_email_sent
    - export

## interactive_story_12
* greet
    - utter_greet 
* restaurant_search{"cuisine": "italian"} 
    - slot{"cuisine": "italian"}
    - utter_ask_range
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"check_loc": true}
    - slot{"location": "delhi"}
    - utter_send_email
* affirm
    - utter_ask_email
* send_email{"email": "agarwal.nageshwari@gmail.com"}
    - slot{"email": "agarwal.nageshwari@gmail.com"}
    - action_send_mail
    - slot{"email": "agarwal.nageshwari@gmail.com"}
    - utter_email_sent
    - export

## interactive_story_13    
* greet
    - utter_greet
* restaurant_search{"location": "delhi ncr"}
    - slot{"location": "delhi ncr"}
    - action_check_location
    - slot{"check_loc": true}
    - slot{"location": "Delhi NCR"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_range
* budget{"price": "300-700"}
    - slot{"price": "300-700"}
    - action_search_restaurants
    - slot{"location": "Delhi NCR"}
    - utter_send_email
* deny
    - utter_goodbye
    - export

## interactive_story_14
* greet
    - utter_greet
* restaurant_search{"price": "More than Rs.700", "cuisine": "south indian", "location": "chandigarh"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "chandigarh"}
    - slot{"price": "More than Rs.700"}
    - action_check_location
    - slot{"check_loc": true}
    - slot{"location": "Chandigarh"}
    - action_search_restaurants
    - slot{"location": "Chandigarh"}
    - utter_send_email
* deny
    - utter_goodbye
    - export

## interactive_story_15
* greet
    - utter_greet
* restaurant_search{"price": "Less than Rs.300","cuisine": "american"}
    - slot{"price": "Less than Rs.300"}
    - slot{"cuisine": "american"}
    - utter_ask_location
* location_dataset{"location": "Pune"}
    - slot{"location": "Pune"}
    - action_check_location
    - slot{"check_loc": true}
    - slot{"location": "Pune"}
    - action_search_restaurants
    - slot{"location": "Pune"}
    - utter_send_email
* affirm
    - utter_ask_email
* send_email{"email": "agarwal.nageshwari@gmail.com"}
    - slot{"email": "agarwal.nageshwari@gmail.com"}
    - action_send_mail
    - slot{"email": "agarwal.nageshwari@gmail.com"}
    - utter_email_sent
    - export

## interactive_story_16
* greet
    - utter_greet
* restaurant_search{"price": "Less than Rs.300","cuisine": "american"}
    - slot{"price": "Less than Rs.300"}
    - slot{"cuisine": "american"}
    - utter_ask_location
* location_dataset{"location": "Pune"}
    - slot{"location": "Pune"}
    - action_check_location
    - slot{"check_loc": true}
    - slot{"location": "Pune"}
    - action_search_restaurants
    - slot{"location": "Pune"}
    - utter_send_email
* deny
    - utter_goodbye
    - export

## interactive_story_17
* greet
    - utter_greet 
* restaurant_search{"cuisine": "italian"} 
    - slot{"cuisine": "italian"}
    - utter_ask_range
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - utter_ask_location
* restaurant_search{"location": "puri"}
    - action_check_location
    - slot{"check_loc": false}
    - utter_loc_invalid
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - action_check_location
    - slot{"check_loc": true}
    - slot{"location": "delhi"}
    - utter_send_email
* deny
    - utter_goodbye
    - export

## interactive_story_18
* greet
    - utter_greet 
* restaurant_search{"cuisine": "italian"} 
    - slot{"cuisine": "italian"}
    - utter_ask_range
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - utter_ask_location
* restaurant_search{"location": "puri"}
    - action_check_location
    - slot{"check_loc": false}
    - utter_loc_invalid
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - action_check_location
    - slot{"check_loc": true}
    - slot{"location": "delhi"}
    - utter_send_email
* affirm
    - utter_ask_email
* send_email{"email": "agarwal.nageshwari@gmail.com"}
    - slot{"email": "agarwal.nageshwari@gmail.com"}
    - action_send_mail
    - slot{"email": "agarwal.nageshwari@gmail.com"}
    - utter_email_sent
    - export

## interactive_story_19
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "pune"}
    - slot{"cuisine": "italian"}
    - slot{"location": "pune"}
    - action_check_location
    - slot{"check_loc": true}
    - slot{"location": "Pune"}
    - utter_ask_range
* budget{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - action_search_restaurants
    - slot{"location": "Pune"}
    - utter_send_email
* deny
    - utter_goodbye
    - export

## interactive_story_20
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "puri"}
    - slot{"cuisine": "italian"}
    - slot{"location": "puri"}
    - action_check_location
    - slot{"check_loc": false}
    - utter_loc_invalid
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - action_check_location
    - slot{"check_loc": true}
    - slot{"location": "delhi"}
    - utter_ask_range
* budget{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - action_search_restaurants
    - slot{"location": "Pune"}
    - utter_send_email
* deny
    - utter_goodbye
    - export

## interactive_story_21
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "puri"}
    - slot{"cuisine": "italian"}
    - slot{"location": "puri"}
    - action_check_location
    - slot{"check_loc": false}
    - utter_loc_invalid
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - action_check_location
    - slot{"check_loc": true}
    - slot{"location": "delhi"}
    - utter_ask_range
* budget{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - action_search_restaurants
    - slot{"location": "Pune"}
    - utter_send_email
* deny
    - utter_goodbye
    - export

## interactive_story_22
* greet
    - utter_greet
* restaurant_search{"price": "More than Rs.700", "cuisine": "south indian", "location": "puri"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "puri"}
    - slot{"price": "More than Rs.700"}
    - action_check_location
    - slot{"check_loc": false}
    - utter_loc_invalid
    - utter_ask_location
* restaurant_search{"location": "Chandigarh"}
    - action_check_location
    - slot{"check_loc": true}
    - slot{"location": "Chandigarh"}
    - action_search_restaurants
    - slot{"location": "Chandigarh"}
    - utter_send_email
* affirm
    - utter_ask_email
* send_email{"email": "agarwal.nageshwari@gmail.com"}
    - slot{"email": "agarwal.nageshwari@gmail.com"}
    - action_send_mail
    - slot{"email": "agarwal.nageshwari@gmail.com"}
    - utter_email_sent
    - export

## interactive_story_23
* greet
    - utter_greet
* restaurant_search{"price": "More than Rs.700", "cuisine": "south indian", "location": "puri"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "puri"}
    - slot{"price": "More than Rs.700"}
    - action_check_location
    - slot{"check_loc": false}
    - utter_loc_invalid
    - utter_ask_location
* restaurant_search{"location": "Chandigarh"}
    - action_check_location
    - slot{"check_loc": true}
    - slot{"location": "Chandigarh"}
    - action_search_restaurants
    - slot{"location": "Chandigarh"}
    - utter_send_email
* deny
    - utter_goodbye
    - export

## interactive_story_24   
* greet
    - utter_greet
* restaurant_search{"location": "puri"}
    - slot{"location": "puri"}
    - action_check_location
    - slot{"check_loc": false}
    - utter_loc_invalid
    - utter_ask_location
* restaurant_search{"location": "delhi ncr"}
    - action_check_location
    - slot{"check_loc": true}
    - slot{"location": "delhi ncr"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_range
* budget{"price": "300-700"}
    - slot{"price": "300-700"}
    - action_search_restaurants
    - slot{"location": "Delhi NCR"}
    - utter_send_email
* affirm
    - utter_ask_email
* send_email{"email": "agarwal.nageshwari@gmail.com"}
    - slot{"email": "agarwal.nageshwari@gmail.com"}
    - action_send_mail
    - utter_email_sent
    - export

## interactive_story_25 
* greet
    - utter_greet
* restaurant_search{"location": "puri"}
    - slot{"location": "puri"}
    - action_check_location
    - slot{"check_loc": false}
    - utter_loc_invalid
    - utter_ask_location
* restaurant_search{"location": "delhi ncr"}
    - action_check_location
    - slot{"check_loc": true}
    - slot{"location": "delhi ncr"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_range
* budget{"price": "300-700"}
    - slot{"price": "300-700"}
    - action_search_restaurants
    - slot{"location": "Delhi NCR"}
    - utter_send_email
* deny
    - utter_goodbye
    - export

## interactive_story_26
* greet
    - utter_greet
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - utter_ask_location
* location_dataset{"location": "pune"}
    - slot{"location": "pune"}
    - action_check_location
    - slot{"check_loc": true}
    - slot{"location": "Pune"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_search_restaurants
    - slot{"location": "Pune"}
    - utter_send_email
* affirm
    - utter_ask_email
* send_email{"email": "agarwal.nageshwari@gmail.com"}
    - slot{"email": "agarwal.nageshwari@gmail.com"}
    - action_send_mail
    - slot{"email": "agarwal.nageshwari@gmail.com"}
    - utter_email_sent
    - export

## interactive_story_27
* greet
    - utter_greet
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - utter_ask_location
* location_dataset{"location": "pune"}
    - slot{"location": "pune"}
    - action_check_location
    - slot{"check_loc": true}
    - slot{"location": "Pune"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_search_restaurants
    - slot{"location": "Pune"}
    - utter_send_email
* deny
    - utter_goodbye
    - export

## interactive_story_28
* greet
    - utter_greet
* restaurant_search{"price": "More than Rs.700", "location": "puri"}
    - slot{"location": "puri"}
    - slot{"price": "More than Rs.700"}
    - action_check_location
    - slot{"check_loc": false}
    - utter_loc_invalid
    - utter_ask_location
* restaurant_search{"location": "dhanbad"}
    - action_check_location
    - slot{"check_loc": true}
    - slot{"location": "dhanbad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "Dhanbad"}
    - utter_send_email
* affirm
    - utter_ask_email
* send_email{"email": "agarwal.nageshwari@gmail.com"}
    - slot{"email": "agarwal.nageshwari@gmail.com"}
    - action_send_mail
    - slot{"email": "agarwal.nageshwari@gmail.com"}
    - utter_email_sent
    - export

## interactive_story_29
* greet
    - utter_greet
* restaurant_search{"price": "More than Rs.700", "location": "puri"}
    - slot{"location": "puri"}
    - slot{"price": "More than Rs.700"}
    - action_check_location
    - slot{"check_loc": false}
    - utter_loc_invalid
    - utter_ask_location
* restaurant_search{"location": "dhanbad"}
    - action_check_location
    - slot{"check_loc": true}
    - slot{"location": "dhanbad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "Dhanbad"}
    - utter_send_email
* deny
    - utter_goodbye
    - export

## interactive_story_30
* greet
    - utter_greet
* restaurant_search{"price": "Less than Rs.300", "cuisine": "american"}
    - slot{"price": "Less than Rs.300"}
    - slot{"cuisine": "american"}
    - utter_ask_location
* restaurant_search{"location": "puri"}
    - slot{"location": "puri"}
    - action_check_location
    - slot{"check_loc": false}
    - utter_loc_invalid
    - utter_ask_location
* location_dataset{"location": "Pune"}
    - slot{"location": "Pune"}
    - action_check_location
    - slot{"check_loc": true}
    - slot{"location": "Pune"}
    - action_search_restaurants
    - slot{"location": "Pune"}
    - utter_send_email
* affirm
    - utter_ask_email
* send_email{"email": "agarwal.nageshwari@gmail.com"}
    - slot{"email": "agarwal.nageshwari@gmail.com"}
    - action_send_mail
    - slot{"email": "agarwal.nageshwari@gmail.com"}
    - utter_email_sent
    - export

## interactive_story_31
* greet
    - utter_greet
* restaurant_search{"price": "Less than Rs.300", "cuisine": "american"}
    - slot{"price": "Less than Rs.300"}
    - slot{"cuisine": "american"}
    - utter_ask_location
* restaurant_search{"location": "puri"}
    - slot{"location": "puri"}
    - action_check_location
    - slot{"check_loc": false}
    - utter_loc_invalid
    - utter_ask_location
* location_dataset{"location": "Pune"}
    - slot{"location": "Pune"}
    - action_check_location
    - slot{"check_loc": true}
    - slot{"location": "Pune"}
    - action_search_restaurants
    - slot{"location": "Pune"}
    - utter_send_email
* deny
    - utter_goodbye
    - export