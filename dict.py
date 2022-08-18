import importlib
from itertools import count
importlib


def most_freq(sentence):
    output=sorted(sentence)
    i=0
    while i<len(output):
        rep=0
        for number in output:
            
            if number==output[i]:
                rep=rep+1
                myDict.update({number:rep})

        i+=1

    
    return output


myDict={
    
}


sentence=input("enter a string:\n ")
output=most_freq(sentence)
sort_output=sorted(myDict.items(),key=lambda x:x[1], reverse=True)
sort_output_dict=dict(sort_output)
print("this is output returned by function most_freq func: ",output)
print("this is output of sorted key values from myDict its in tupple: ",sort_output)
print("this is output of sorted myDict according to the count: ",sort_output_dict)









"""
myDict.pop("c++")
print(myDict)
print(len(myDict))

myDict["python"]="friendly"
print(myDict)
print(len(myDict))
value=myDict.get("c")
print(value)

myDict.popitem()
print(myDict)
print(len(myDict))
"""