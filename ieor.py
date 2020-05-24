#!/usr/bin/env python
# coding: utf-8

# In[49]:


# importing networkx 
import networkx as nx 
# importing matplotlib.pyplot 
import matplotlib.pyplot as plt 
  
g = nx.Graph() 


# In[50]:



# Agra
g.add_edge('Agra', 'Hathras', weight= 51.6)
g.add_edge('Agra', 'Mathura', weight= 73.4)
g.add_edge('Agra', 'Firozabad', weight= 44.6)

# Aligarh
g.add_edge('Aligarh', 'Agra', weight= 89.4)
g.add_edge('Aligarh', 'Moradabad', weight= 136.0)
g.add_edge('Aligarh', 'Bulandshahar', weight= 79.6)
g.add_edge('Aligarh', 'Etah', weight= 72.9)

# Prayagraj
g.add_edge('Prayagraj', 'Fatehpur', weight= 133.0)
g.add_edge('Prayagraj', 'Pratapgarh', weight= 61.4)
g.add_edge('Prayagraj', 'Jaunpur', weight= 112.0)
g.add_edge('Prayagraj', 'Raebareli', weight= 121.0)
g.add_edge('Prayagraj', 'Varanasi', weight= 121.0)

# Ambedkar Nagar
g.add_edge('Ambedkar Nagar', 'Auraiya', weight= 372.0)

# Amethi
g.add_edge('Amethi', 'Prayagraj', weight= 101.0)
g.add_edge('Amethi', 'Raebareli', weight= 61.1)
g.add_edge('Amethi', 'Sultanpur', weight= 34.8)
g.add_edge('Amethi', 'Pratapgarh', weight= 38.3)

# Amroha
g.add_edge('Amroha', 'Moradabad', weight= 39.7)
g.add_edge('Amroha', 'Hapur', weight= 76.2)

# # Auraiya
g.add_edge('Auraiya', 'Etawah', weight= 64.1)
g.add_edge('Auraiya', 'Kannauj', weight= 137.0)

# # Ayodhya
g.add_edge('Ayodhya', 'Barabanki', weight= 108.0)
g.add_edge('Ayodhya', 'Raebareli', weight= 148.0)
g.add_edge('Ayodhya', 'Sultanpur', weight= 67.1)
g.add_edge('Ayodhya', 'Basti', weight= 56.7)
g.add_edge('Ayodhya', 'Gonda', weight= 50.0)

# # Azamgarh
g.add_edge('Azamgarh', 'Varanasi', weight= 102.0)
g.add_edge('Azamgarh', 'Ambedkar Nagar', weight= 87.7)
g.add_edge('Azamgarh', 'Basti', weight= 128.0)

# # Baghpat
g.add_edge('Baghpat', 'Meerut', weight= 48.0)
g.add_edge('Baghpat', 'Ghaziabad', weight= 48.3)
g.add_edge('Baghpat', 'Shamli', weight= 61.6)

# # Bahraich
g.add_edge('Bahraich', 'Lakhimpur Kheri', weight= 131.0)
g.add_edge('Bahraich', 'Lucknow', weight= 128.0)
g.add_edge('Bahraich', 'Basti', weight= 171.0)
g.add_edge('Bahraich', 'Gonda', weight= 101.0)

# # Ballia
g.add_edge('Ballia', 'Ghazipur', weight= 604.0)

# # Balrampur
g.add_edge('Balrampur', 'Bahraich', weight= 62.7)
g.add_edge('Balrampur', 'Gonda', weight= 41.8)
g.add_edge('Balrampur', 'Basti', weight= 136.0)

# # Banda
g.add_edge('Banda', 'Fatehpur', weight= 76.8)
g.add_edge('Banda', 'Chitrakoot', weight= 70.0)

# # Barabanki
g.add_edge('Barabanki', 'Lucknow', weight= 36.0)
g.add_edge('Barabanki', 'Bahraich', weight= 98.7)
g.add_edge('Barabanki', 'Unnao', weight= 96.1)

# # Bereilly
g.add_edge('Bereilly', 'Shahjahanpur', weight= 81.4)
g.add_edge('Bereilly', 'Rampur', weight= 70.1)
g.add_edge('Bereilly', 'Pilibhit', weight= 50.9)

# # Basti
g.add_edge('Basti', 'Gorakhpur', weight= 67.0)
g.add_edge('Basti', 'Ambedkar Nagar', weight= 60.6)

# # Bhadohi	

# # Bijnor
g.add_edge('Bijnor', 'Meerut', weight= 74.0)

# # Budaun

# # Bulandshahar
g.add_edge('Bulandshahar', 'Ghaziabad', weight= 54.2)
g.add_edge('Bulandshahar', 'Meerut', weight= 68.8)
g.add_edge('Bulandshahar', 'Moradabad', weight= 121.0)

# # Chandauli
g.add_edge('Chandauli', 'Varanasi', weight= 33.2)
g.add_edge('Chandauli', 'Ghazipur', weight= 66.9)

# # Chitrakoot
g.add_edge('Chitrakoot', 'Prayagraj', weight= 116.0)

# # Deoria

# # Etah
g.add_edge('Etah', 'Mainpuri', weight= 60.1)

# # Etawah
g.add_edge('Etawah', 'Farukkhabad', weight= 94.0)
g.add_edge('Etawah', 'Firozabad', weight= 81.6)
g.add_edge('Etawah', 'Kannauj', weight= 105.0)

# # Farukkhabad
g.add_edge('Farukkhabad', 'Mainpuri', weight= 63.7)
g.add_edge('Farukkhabad', 'Kannauj', weight= 103.0)

# # Fatehpur
g.add_edge('Fatehpur', 'Kanpur', weight= 82.6)
g.add_edge('Fatehpur', 'Raebareli', weight= 63.7)

# # Firozabad

# # Gautam Buddha Nagar
g.add_edge('Gautam Buddha Nagar', 'Ghaziabad', weight= 50.5)

# # Ghaziabad
g.add_edge('Ghaziabad', 'Meerut', weight= 47.8)

# # Ghazipur
g.add_edge('Ghazipur', 'Varanasi', weight= 82.6)
g.add_edge('Ghazipur', 'Mau', weight= 41.4)

# # Gonda
g.add_edge('Gonda', 'Barabanki', weight= 87.8)
g.add_edge('Gonda', 'Basti', weight= 95.1)

# # Gorakhpur
g.add_edge('Gorakhpur', 'Mau', weight= 101.0)

# # Hamirpur
g.add_edge('Hamirpur', 'Kanpur', weight= 61.7)
g.add_edge('Hamirpur', 'Banda', weight= 88.5)

# # Hapur
g.add_edge('Hapur', 'Meerut', weight= 30.8)
g.add_edge('Hapur', 'Bulandshahar', weight= 38.0)
g.add_edge('Hapur', 'Ghaziabad', weight= 34.7)

# # Hardoi

# # Hathras
g.add_edge('Hathras', 'Aligarh', weight= 35.6)

# # Jalaun
g.add_edge('Jalaun', 'Kanpur', weight= 133.0)

# # Jaunpur
g.add_edge('Jaunpur', 'Varanasi', weight= 62.0)
g.add_edge('Jaunpur', 'Pratapgarh', weight= 92.2)
g.add_edge('Jaunpur', 'Sultanpur', weight= 88.9)

# # Jhansi
g.add_edge('Jhansi', 'Lalitpur', weight= 96.3)
g.add_edge('Jhansi', 'Jalaun', weight= 125.0)

# # Kannauj
g.add_edge('Kannauj', 'Kanpur', weight= 89.0)

# # Kanpur
g.add_edge('Kanpur', 'Auraiya', weight= 92.9)
g.add_edge('Kanpur', 'Lucknow', weight= 99.3)
g.add_edge('Kanpur', 'Raebareli', weight= 130.0)

# # Kasganj

# # Kaushambi
g.add_edge('Kaushambi', 'Fatehpur', weight= 107.0)

# # Kushi Nagar
g.add_edge('Kushi Nagar', 'Gorakhpur', weight= 67.7)

# # Lakhimpur Kheri
g.add_edge('Lakhimpur Kheri', 'Pilibhit', weight= 144.0)

# # Lalitpur

# # Lucknow
g.add_edge('Lucknow', 'Sitapur', weight= 89.1)
g.add_edge('Lucknow', 'Raebareli', weight= 79.9)

# # Maharajganj
g.add_edge('Maharajganj', 'Gorakhpur', weight= 71.0)
g.add_edge('Maharajganj', 'Deoria', weight= 86.6)

# # Mahoba
g.add_edge('Mahoba', 'Jhansi', weight= 167.0)

# # Mainpuri
g.add_edge('Mainpuri', 'Kannauj', weight= 139.0)
g.add_edge('Mainpuri', 'Firozabad', weight= 93.8)

# # Mathura

# # Mau

# # Meerut
g.add_edge('Meerut', 'Shamli', weight= 67.6)
g.add_edge('Meerut', 'Muzaffar Nagar', weight= 57.3)

# # Mirzapur
g.add_edge('Mirzapur', 'Prayagraj', weight= 91.1)
g.add_edge('Mirzapur', 'Varanasi', weight= 66.3)
g.add_edge('Mirzapur', 'Chandauli', weight= 91.1)

# # Moradabad

# # Muzaffar Nagar

# # Pilibhit

# # Pratapgarh
g.add_edge('Pratapgarh', 'Sultanpur', weight= 46.1)
g.add_edge('Pratapgarh', 'Raebareli', weight= 98.7)

# # Raebareli
g.add_edge('Raebareli', 'Sultanpur', weight= 86.4)

# # Rampur
g.add_edge('Rampur', 'Moradabad', weight= 26.9)

# # Saharanpur
g.add_edge('Saharanpur', 'Shamli', weight= 73.8)

# # Sambhal


# # Sant Kabir Nagar
g.add_edge('Sant Kabir Nagar', 'Basti', weight= 34.5)
g.add_edge('Sant Kabir Nagar', 'Gorakhpur', weight= 44.8)

# # Shahjahanpur
g.add_edge('Shahjahanpur', 'Sitapur', weight= 85.8)

# # Shamli

# # Shravasti
g.add_edge('Shravasti', 'Balrampur', weight= 16.8)
g.add_edge('Shravasti', 'Bahraich', weight= 46.4)
g.add_edge('Shravasti', 'Gonda', weight= 56.6)

# # Siddharth Nagar
g.add_edge('Siddharth Nagar', 'Balrampur', weight= 101.0)
g.add_edge('Siddharth Nagar', 'Basti', weight= 69.0)
g.add_edge('Siddharth Nagar', 'Gorakhpur', weight= 107.0)

# # Sitapur


# # Sonbhadra

# # Sultanpur
g.add_edge('Sultanpur', 'Ambedkar Nagar', weight= 83.9)
g.add_edge('Sultanpur', 'Lucknow', weight= 139.0)

# # Unnao
g.add_edge('Unnao', 'Kanpur', weight= 31.2)
g.add_edge('Unnao', 'Lucknow', weight= 74.7)

# Varanasi


# In[56]:


nx.draw_random(g, with_labels = True) 


# In[36]:


length = nx.floyd_warshall(g)


# In[40]:


dis = []
for key in length:
    dis.append(key)


# In[42]:


res = {}
for item in dis:
    sum = 0.0
    for d in length:
        sum = sum + length[item][d]
    res[item] = sum


# In[45]:


{k: v for k, v in sorted(res.items(), key=lambda item: item[1])}


# In[ ]:




