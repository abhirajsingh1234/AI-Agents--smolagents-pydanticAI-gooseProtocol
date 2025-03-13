
# # first basic code 
# from smolagents import CodeAgent, HfApiModel

# model_id = "HuggingFaceH4/zephyr-7b-beta" 

# model = HfApiModel(model_id=model_id, token="your api key") # You can choose to not pass any model_id to HfApiModel to use a default free model
# # you can also specify a particular provider e.g. provider="together" or provider="sambanova"
# agent = CodeAgent(tools=[], model=model, add_base_tools=True,max_steps=3)

# agent.run(
#     "Could you give me the 18th number in the Fibonacci sequence?",
# )


# # second basic code passing the libraries
# from smolagents import CodeAgent, HfApiModel
# model = HfApiModel()
# agent = CodeAgent(tools=[], model=model, additional_authorized_imports=['requests', 'bs4'])
# agent.run("Could you get me the title of the page at url 'https://github.com/abhirajsingh1234'?")


# # third basic code using toolcallingagent
# from smolagents import ToolCallingAgent,HfApiModel

# model = HfApiModel()
# agent = ToolCallingAgent(tools=[], model=model)
# agent.run("Could you get me the title of the page at url 'https://github.com/abhirajsingh1234'?")



## fourth multiple tools 
# from typing import Optional
# from smolagents import CodeAgent, HfApiModel, tool

# @tool
# def get_travel_duration(start_location: str, destination_location: str, transportation_mode: Optional[str] = None) -> str:
#     """Gets the travel time between two places.

#     Args:
#         start_location: the place from which you start your ride
#         destination_location: the place of arrival
#         transportation_mode: The transportation mode, in 'driving', 'walking', 'bicycling', or 'transit'. Defaults to 'driving'.
#     """
#     import os
#     import googlemaps
#     from datetime import datetime

#     gmaps = googlemaps.Client(os.getenv("GMAPS_API_KEY"))
#     if transportation_mode is None:
#         transportation_mode = "driving"
#     try:
#         directions_result = gmaps.directions(
#             start_location,
#             destination_location,
#             mode=transportation_mode,
#             departure_time=datetime(2025, 6, 6, 11, 0),  # At 11, date far in the future
#         )
#         if len(directions_result) == 0:
#             return "No way found between these places with the required transportation mode."
#         return directions_result[0]["legs"][0]["duration"]["text"]
#     except Exception as e:
#         print(e)
#         return str(e)

# @tool
# def get_weather(location: str, date: Optional[str] = None) -> str:
#     """Fetches current weather information for a given location.
    
#     Args:
#         location: The city or location to get the weather for.
#         date: Optional; a specific date's forecast if supported.
#     """
#     import os
#     import requests
#     api_key = os.getenv("OPENWEATHER_API_KEY")
#     if not api_key:
#         return "OpenWeather API key not set."
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
#     response = requests.get(url)
#     if response.status_code != 200:
#         return f"Error fetching weather: {response.text}"
#     data = response.json()
#     weather_description = data["weather"][0]["description"]
#     temperature = data["main"]["temp"]
#     return f"The weather in {location} is {weather_description} with a temperature of {temperature}°C."

# @tool
# def calculator(expression: str) -> str:
#     """Evaluates a simple mathematical expression.
    
#     Note: For production, consider using a safe parsing library instead of eval.
#     """
#     try:
#         # A simple eval with restricted built-ins; use with caution.
#         result = eval(expression, {"__builtins__": {}}, {})
#         return str(result)
#     except Exception as e:
#         return f"Error evaluating expression: {str(e)}"

# @tool
# def translate_text(text: str, target_language: str = "en") -> str:
#     """Translates text to the target language.
    
#     This is a dummy implementation; in a real scenario, integrate with a translation API.
#     """
#     return f"Translated '{text}' to {target_language} (dummy result)."

# @tool
# def get_wikipedia_summary(query: str, sentences: int = 2) -> str:
#     """Fetches a short summary from Wikipedia for a given query."""
#     import wikipedia
#     try:
#         summary = wikipedia.summary(query, sentences=sentences)
#         return summary
#     except Exception as e:
#         return f"Error fetching summary: {str(e)}"

# # Instantiate the agent with all the tools
# agent = CodeAgent(
#     tools=[get_travel_duration, get_weather, calculator, translate_text, get_wikipedia_summary],
#     model=HfApiModel(),
#     additional_authorized_imports=["datetime"]
# )

# agent.run("Can you give me a nice one-day trip around Paris with a few locations and the times? Could be in the city or outside, but should fit in one day. I'm travelling only with a rented bicycle.")



#fifth code
import code
from smolagents import load_tool, CodeAgent, HfApiModel, DuckDuckGoSearchTool
from dotenv import load_dotenv

load_dotenv()

#Qwen/Qwen2.5-72B-Instruct
model_id = "Qwen/Qwen2.5-72B-Instruct" 

model = HfApiModel(model_id=model_id, token="your api key")

# Import tool from Hub
image_generation_tool = load_tool("m-ric/text-to-image", trust_remote_code=True)

search_tool = DuckDuckGoSearchTool()

agent = CodeAgent(
    tools=[search_tool, image_generation_tool],
    model=model,
    planning_interval=3, # This is where you activate planning!
    max_steps=3
)

# Run it!
result = agent.run(
    "what are the weather conditions in navi mumbai and also tell me which tool used to generate answer answer for this question?",
)



#output of fifth code

# PS C:\Users\ACER\OneDrive\डेस्कटॉप\ai agents> python smallagents.py
# ╭─────────────────────────────────────────────────────────────── New run ───────────────────────────────────────────────────────────────╮
# │                                                                                                                                       │
# │ How long would a cheetah at full speed take to run the length of Pont Alexandre III?                                                  │
# │                                                                                                                                       │
# ╰─ HfApiModel - Qwen/Qwen2.5-72B-Instruct ──────────────────────────────────────────────────────────────────────────────────────────────╯
# ───────────────────────────────────────────────────────────── Initial plan ──────────────────────────────────────────────────────────────
# Here is the plan of action that I will follow to solve the task:
# ```
# 1. Use the web Search tool to find the full speed of a cheetah.
# 2. Perform a Web Search to find the length of Pont Alexandre III.
# 3. Convert the length of the bridge and the cheetah's speed into the same units (meters and meters per second).
# 4. Calculate the time it would take for the cheetah to run the length of the bridge using the Derived Facts.
# 5. Use the Final Answer Tool to Provide the Final Answer.

# <end_plan>
# ```
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Step 1 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  ─ Executing parsed code: ────────────────────────────────────────────────────────────────────────────────────────────────────────────── 
#   cheetah_speed = web_search(query="Cheetah full speed")                                                                                 
#   print(cheetah_speed)                                                                                                                   
#  ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── 
# Execution logs:
# ## Search Results

# [How Fast Can a Cheetah Run? - ThoughtCo](https://www.thoughtco.com/how-fast-can-a-cheetah-run-4587031)
# The top speed of a cheetah is around 69 to 75 mph. However, the cat can only sprint a short distance of around 0.28 miles. A cheetah is  
# about 2.7 times faster than the fastest human runner. A cheetah accelerates very quickly, allowing it to overtake prey at close range.   
# The fastest cheetah on record is Sarah. Sarah lives at the Cinncinati Zoo ...

# [Cheetah - Chase Compilation - YouTube](https://www.youtube.com/watch?v=xaV1_M2j200)
# Cheetah, the fastest land animal, has a recorded speed of 109 - 120 km/h (68 - 75 mph).

# [Cheetah | Smithsonian's National Zoo and Conservation Biology Institute](https://nationalzoo.si.edu/animals/cheetah)
# Built for speed, the cheetah can accelerate from zero to 45 in just 2.5 seconds and reach top speeds of 60 to 70 mph, making it the      
# fastest land mammal! The cheetah's spotted coat helps it camouflage among the dry grasses of the African savanna where it lives. ...     
# (91.4 meters) of an intended victim before the final acceleration. Full sprints ...

# [The Cheetah Is Not The World's Fastest Animal -
# WorldAtlas](https://www.worldatlas.com/animals/the-cheetah-is-not-the-world-s-fastest-animal.html)
# The Cheetah's Claim to Fame A cheetah, an animal capable of running faster than 70 miles per hour, seen sprinting across the grass. The  
# cheetah's swift reputation is definitely well-deserved, as it can accelerate from zero to 60 mph (96 kmh) in a few seconds, reaching top 
# speeds between 60 and 70 mph (96-112 kmh.) This unrivaled burst of ...

# [Cheetah Running at Full Speed! ⚡ #Wildlife # ... - YouTube](https://www.youtube.com/watch?v=TDjhiY5LqI8)
# Watch this incredible cheetah sprint at top speed! ⚡🐆 The fastest land animal, reaching up to 70 mph in just seconds! #Cheetah
# #Wildlife #Shorts

# [What makes a cheetah run so fast? - HowStuffWorks](https://animals.howstuffworks.com/mammals/cheetah-speed.htm)
# The cheetah is the fastest land animal, achieving a top speed of about 70 mph (113 kph) [sources: Blue Lion, Defenders of Wildlife].This 
# incredible speed comes with a price, though -- a cheetah is a rather puny large cat. (It looks a lot like a leopard, but you can tell a  
# cheetah by the bilateral, teardrop-shaped stripes running from either side of its nose to its eyes.)

# [How Fast Can a Cheetah Run? - Our Planet](https://ourplnt.com/cheetah-top-speed/)
# The highest properly measured top speed of a cheetah is 98.1 km/h (61 mph). Sarah, who became a symbol of speed and agility, was featured
# in National Geographic as the world's fastest land mammal. In a remarkable display of her abilities, she completed a 100-meter dash in   
# just 5.95 seconds in 2012, at the age of 11, and was radar-timed ...

# [How Fast Can a Cheetah Run? Top Speed, 6 Unique Features](https://storyteller.travel/how-fast-can-a-cheetah-run/)
# Learn about cheetah cubs: 14 Cute Baby Cheetah Facts How Much Faster is a Cheetah Than a Human? The quick answer is that cheetahs can    
# outrun humans by a lot. Sarah the cheetah, mentioned earlier, did the 100-meter dash in 5.95 seconds, destroying Usain Bolt's 100-meter  
# record time of 9.58 seconds.. The average man can run 5.9 mph (9.5 km/h). At this speed, it would take the average man 38 ...

# [How fast can cheetahs run, and what enables their incredible speed?](https://www.wildlifefaq.com/cheetah-speed/)
# One of the key factors that contribute to a cheetah's speed is its long tail. Acting as a counterbalance, the cheetah's tail helps with  
# high-speed maneuvering, allowing the predator to swiftly change direction while maintaining stability. ... With a flexible spine,        
# cheetahs can stretch their bodies to their full potential, elongating their ...

# [cheetah - Speed of Animals](https://www.speedofanimals.com/animals/cheetah)
# The cheetah is an atypical member of the cat family (Felidae) that is unique in its speed, while lacking climbing abilities. The species 
# is the only living member of the genus Acinonyx. ... cheetah Acinonyx jubatus top speed 74.6 mph feels like 99.4 mph coyote Canis latrans
# top speed 42.9 mph feels like 85.7 mph greyhound Canis familiaris top ...

# Out: None
# [Step 1: Duration 16.69 seconds| Input tokens: 2,513 | Output tokens: 58]
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Step 2 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  ─ Executing parsed code: ────────────────────────────────────────────────────────────────────────────────────────────────────────────── 
#   cheetah_speed_mph = 72                                                                                                                 
#   cheetah_speed_mps = cheetah_speed_mph * (1609.34 / 3600)  # Convert mph to m/s                                                         
#   pont_alexandre_iii_length = web_search(query="Length of Pont Alexandre III")                                                           
#   print(pont_alexandre_iii_length)                                                                                                       
#  ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── 
# Execution logs:
# ## Search Results

# [Pont Alexandre III - Wikipedia](https://en.wikipedia.org/wiki/Pont_Alexandre_III)
# Location on the Seine in Paris.. The Pont Alexandre III (French pronunciation: [pɔ̃ alɛksɑ̃dʁ tʁwa]) is a deck arch bridge that spans the
# Seine in Paris.It connects the Champs-Élysées quarter with those of the Invalides and Eiffel Tower.The bridge is widely regarded as the  
# most ornate, extravagant bridge in the city. [2] [3] It has been classified as a French monument historique since ...

# [Pont Alexandre III Bridge Guide (with Photos) - Delve Into Europe](https://delveintoeurope.com/pont-alexandre-iii-paris/)
# Pont Alexandre III - which translates as Alexander III Bridge - is called Pont Alexandre Trois in French. The Pont Alexandre III Bridge  
# Paris is 160 metres long, and 40 metres wide; the main arch span is 108 metres. It is one of the later examples of the Beaux Arts style  
# prevalent in France in the second half of the 19 th century.

# [Why Pont Alexandre III is Paris' most beautiful bridge](https://frenchmoments.eu/pont-alexandre-iii-paris/)
# Pont Alexandre III was built in the same period as the Grand and Petit Palais, in time for the 1900 World Exhibition. ... The total      
# length is 160 metres, and the width is 40 metres. The bridge has been equipped with electric street lighting since its construction in   
# 1900.

# [The Pont Alexandre III is the most beautiful bridge in Paris.](https://monsieur-de-france.com/en/bridge-pont-alexandre-iii-paris-france)
# The Alexandre III Bridge in figures . The Alexandre III Bridge at sunrise / Photo chosen by Monsieurdefrance.com: Manjik via
# dépositphotos. The bridge is 152 meters long in total, but the arch is 107 meters long and 45 meters wide.It is made of cast steel and   
# rests on two enormous "abutments" that withstand the pressure exerted by the arch.

# [Pont Alexandre III - Wikiwand](https://www.wikiwand.com/en/articles/Alexander_III_Bridge)
# The Pont Alexandre III ... Total length: 160 metres (520 ft) [1] Width: 40 metres (130 ft) [1] Location; Close. Location on the Seine in 
# Paris. History. The Beaux-Arts style bridge, with its exuberant Art Nouveau lamps, cherubs, nymphs and winged horses at both ends, was   
# built between 1896 and 1900.

# [Pont Alexandre III in Paris - Come to Paris](https://www.cometoparis.com/paris-guide/paris-monuments/pont-alexandre-iii-s951)
# The inscription reads 'On April 14th 1900, Emile Loubet, President of the French Republic, opened the Exposition Universelle and
# inaugurated the Pont Alexandre III'. At 154 metres in length and 45 metres in width, this enormous bridge connects the Esplanade des     
# Invalides to the Avenue Wilson Churchill.

# [Pont Alexandre III | Paris.si](https://www.paris.si/pont-alexandre-iii/)
# The Pont Alexandre III lives up to its reputation with its extravagance and architectural design that is subtly modern, and its
# convenient location connecting the Grand Palais with the Invalides. It exudes of royalty, and its sculptural work is highly commendable. 
# ... It rises only 6m above the Seine, and has a length of 107m and a width of 40m ...

# [Pont Alexandre III - The Most Beautiful Bridge in Paris](https://juliasalbum.com/pont-alexandre-iii/)
# Quick Facts about Pont Alexandre III. Pont Alexandre III has a total length of 160 meters and a width of 40 meters. The bridge connects  
# the Champs-Élysées with the Invalides buildings and the Eiffel Tower.; The bridge was named after Tsar Alexander III (the Emperor of     
# Russia from 1881 until 1894).; Gilded Fames sculptures

# [Pont Alexandre III Visiting Guide - Hours, Tickets, and Nearby ...](https://audiala.com/en/france/paris/pont-alexandre-iii)
# Discover essential information about Pont Alexandre III in Paris, France. Learn about its history, architectural significance, and tips  
# for visitors. Optimize your visit with our comprehensive guide. ... measuring 160 meters in length and 40 meters in width, was designed  
# to ensure that it did not obstruct the view of the Champs-Élysées or the ...

# [Pont Alexandre III's lavish decoration - Travel France
# Online](https://www.travelfranceonline.com/pont-alexandre-iiis-lavish-decoration/)
# The Pont Alexandre III is the widest and lowest bridge in Paris; it indeed measures 154 meters in length and 40 meters in width. Pont    
# Alexandre III, a masterpiece of metal architecture. The Pont Alexandre III stands as a masterpiece of steel architecture, characterized  
# by a single arch with three joints, supported by four cast steel girders and ...

# Out: None
# [Step 2: Duration 8.09 seconds| Input tokens: 6,343 | Output tokens: 201]
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Step 3 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  ─ Executing parsed code: ────────────────────────────────────────────────────────────────────────────────────────────────────────────── 
#   pont_alexandre_iii_length_m = 160                                                                                                      
#   time_seconds = pont_alexandre_iii_length_m / cheetah_speed_mps                                                                         
#   final_answer(f"{time_seconds:.2f} seconds")                                                                                            
#  ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── 
# Out - Final answer: 4.97 seconds