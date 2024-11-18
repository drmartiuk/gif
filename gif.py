#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image
frames = []
for frame_number in range(1, 16):
    frame = Image.open(f'./{frame_number}.png')
    frames.append(frame)
frames[0].save('VTD.gif',save_all=True,append_images=frames[1:],optimize=False,duration=200,disposal=2,loop=0)

