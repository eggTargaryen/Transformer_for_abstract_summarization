from tqdm import tqdm

ftrainsrc=open('train.src','w')
ftraintgt=open('train.tgt','w')
ftestsrc=open('test.src','w')
ftesttgt=open('test.tgt','w')
fvocab=open('vocab.txt','w')

vocab=set()
with open('../origin_data','r') as f:
    for i in tqdm(range(2400000)):
        f.readline()
        f.readline()
        summary=f.readline().strip()
        f.readline()
        f.readline()
        context=f.readline().strip()
        f.readline()
        f.readline()
        
        if summary=="" or context=="":
            continue
        vocab=vocab|set(list(context+summary))
        
        if i%2400==0:
            ftestsrc.write(" ".join(list(context))+'\n')
            ftesttgt.write(" ".join(list(summary))+'\n')
        else:
            ftrainsrc.write(" ".join(list(context))+'\n')
            ftraintgt.write(" ".join(list(summary))+'\n')
        #if i==10:
         #   break
       
fvocab.write('<pad>\n')
fvocab.write('<unk>\n')
fvocab.write('<s>\n')
fvocab.write('</s>\n')

for word in vocab:
    fvocab.write(word+'\n')
        
ftrainsrc.close()      
ftraintgt.close()
ftestsrc.close()
ftesttgt.close()
fvocab.close()
