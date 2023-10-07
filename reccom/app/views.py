from django.shortcuts import render
import pickle as pkl
import os

# Create your views here.
def index(request):
    return render(request,"index.html")

def load(fileName):
    file=open(fileName,'rb')
    data=pkl.load(file)
    file.close()
    return data

def reccomendation(request):
    new_dataset=load("newdata.pkl")
    similarity=load("similar.pkl")
    Name=request.GET['Name']
    Movie=request.GET['Movie']

    def recommend(movie):
        movie_index=new_dataset[new_dataset["title"]==movie].index[0]
        distances=similarity[movie_index]
        movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
        mmovie=[]
        for i in movie_list:
            mmovie.append(new_dataset.iloc[i[0]].title)
        return mmovie
    
    
    mov_var=recommend(Movie)
    msg=''''''
    for i in range(5):
        j=i+1
       
        msg=msg+" ("+str(j)+") " +mov_var[i]
    new_msg=""

    new_msg=Name+" movies realted to "+Movie+" are:"+msg

    
    return render(request,"reccomendation.html",{'recommendation': new_msg})