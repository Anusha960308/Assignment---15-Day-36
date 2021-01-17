#!/usr/bin/env python
# coding: utf-8

# In[2]:


@approute('/upload')
defupload_file():
    return render_template('upload.html')

@approute('/upload'.methods=['GET','POST'])
defupload_file1():
    if request.method == 'POST':
        f - request.files['file']
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'


# In[3]:


from flask import flask, render_template,request
from werkzeug import secure_filename


# In[5]:


<html>
<body>
<form action = "http://localhost:5000/upload method= 0"
"POST"
enctype = "multipart/form-data">
<input type = "file" name = "file"/>
<input type = "submit"/>
</form>
</body>
</html>


# In[ ]:




