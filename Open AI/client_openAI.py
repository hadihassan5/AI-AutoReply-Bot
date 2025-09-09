from openai import OpenAI

client = OpenAI(
    api_key=""   
)

command = '''
[10:22 AM, 9/9/2025] Hadi Hassan: Arey yaar!   
 Ayein?  Kya matlab ayein?  Kuch toh bolo!  Pizza thanda ho raha hai!    Seriously,  what's the point?
[10:22 AM, 9/9/2025] Hadi Hassan: Kya matlab ayein ayein?    Tell me already!  Pizza bilkul thanda ho gaya hai!
[10:24 AM, 9/9/2025] Name: Pizza ki recipe Dena 
mujy
[10:25 AM, 9/9/2025] Hadi Hassan: Oye!  Pizza recipe?    Seriously?  Saara drama sirf pizza recipe k liye?    Us Farwa wali baat toh?  Bolo na!  Ab toh pizza bhi useless hogaya hai!       
[10:27 AM, 9/9/2025] Name: Chup kr k pizza recipes
[10:29 AM, 9/9/2025] Hadi Hassan: Oye!  Seriously ammi?!    Saara tamasha just for a pizza recipe?!  Bas karo!  Ab pizza bhi nahi chahiye!  Farwa ki baat karo!  Tell me!
[10:30 AM, 9/9/2025] Name: Shut up only pizza recipes in five lines
[11:35 AM, 9/9/2025] Hadi Hassan: hkjh
'''

completions = client.chat.completions.create(
    model="gpt-5",
    messages=[
        {"role": "system", "content": "You are a person named Hadi. You always speak in Roman Urdu and reply like a normal human, not like a robot."},
        {"role": "user", "content": command}
    ]
)

print(completions.choices[0].message.content)
