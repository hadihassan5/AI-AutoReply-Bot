import google.generativeai as genai

# 👇 Apni Gemini API key daal do
genai.configure(api_key="")

# Gemini model select karo
model = genai.GenerativeModel("gemini-1.5-flash")

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

# Prompt ko Roman Urdu Hadi style me answer karwana
system_message = "Tum ek insaan ho jiska naam Hadi hai. Tum hamesha Roman Urdu me baat karte ho aur normal insaan ki tarah jawab dete ho, robot ki tarah nahi."

# Model se response lena
response = model.generate_content(
    system_message + "\nUser:\n" + command
)

print(response.text)
