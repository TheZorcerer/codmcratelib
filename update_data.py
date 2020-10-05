# Run this to update local crate data from patchy's website
import requests 
data_url = "http://patchythedog.netlify.com/data/crates.json"
  

r = requests.get(data_url)
  
with open("crates.json",'wb') as f: 
    f.write(r.content) 