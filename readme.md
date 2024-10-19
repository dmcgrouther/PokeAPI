## Gotta get request them all!!

This SDK will help you get up and running to pull data from the PokeAPI. 

### How do I install and get this running? 

In order to run the code from this repo, go through the following steps:

1. Download this repository to your local machine.

2. Change into the respective folder.

3. Install requests using this command in the terminal.\
`pip install requests`

4. You will now be ready to run the Python files which interact with the PokeAPI. In your terminal, you can run one of these commands:\
`python get_pokemon.py`\
`python get_pokemon_all_data.py`\
`python get_original_151.py`\
`python get_generation_all_data.py`

5. In order to test if this works, view the data that is returned when you run the command in the terminal. For example, when running get_pokemon.py or get_pokemon_all_data.py you should be able to see the respective Pokemon you entered in the data returned.\ 
get_original_151.py is the only file with a built in test. 

### What is the purpose of this SDK? What were the design decisions?

When creating this SDK I wanted to make it so the developer can get working as soon as possible and make API calls seamlessly. 

While working on this project I wanted to make sure to keep it simple and readable for other developers to use. 

#### Notes:

Regarding my familiarity with Pokemon, I am familiar with generation 1 & kanto region; other than that I am not very familiar with the others. I did not have a great idea of what to look for with generation data so I focused on pokemon data. 

This medium article helped me get up and running with the API:\
https://medium.com/@mohamed.mywork/learn-apis-with-pok%C3%A9mon-and-python-7003b35b5ba\
https://github.com/Mouhamed-dridi/Pokemon__API/blob/master/api.py

If I had more time I would have added more robust testing.