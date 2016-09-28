def load_data(filepath):
    a=[]
    with open(filepath) as iner:
        for line in iner:
            a+=line.split()
    return a

def get_most_frequent_words(text):
    d={}
    for i in text:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return sorted(d, key=d.__getitem__)

if __name__ == '__main__':
    filepath1=input()
    text=load_data(filepath1)
    d=get_most_frequent_words(text)
    for i in range(len(d)):
        print(d[-i-1])
        if i==9:
            break
