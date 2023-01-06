import argparse


parser = argparse.ArgumentParser(description='Input files')
parser.add_argument('indir', type=str, help='Input dir for videos')
parser.add_argument('outdir', type=str, help='Output dir for image')
args = parser.parse_args()

text_pairs = open(args.indir).read()[:-1]
out_file  = args.outdir


def levenstein(A:str,B:str):
    A = list(A)
    B = list(B)
    arr = [[(i+j) if i*j==0 else 0  for i in range(len(A)+1)]
            for j in range(len(B)+1)]
    for i in range(1,len(A)+1):
        for j in range(1,len(B)+1):
            if A[i-1] == B[j-1]:
                arr[i][j] = arr[i-1][j-1]
            else : 
                arr[i][j] = 1 + min(arr[i-1][j],arr[j-1][i],arr[i-1][j-1])
    
    return arr[len(A)][len(B)]


text_pairs = text_pairs.split(" ")
scores_list = []
final_list = []


for i in range(len(text_pairs)//2):
    text_1 = open(text_pairs[i]).read().split(" ")
    text_2 = open(text_pairs[i+1]).read().split(" ")
    for i,j in zip(text_1,text_2):
        print(i,j)
        i = i.ljust(len(j)," ")
        j = j.ljust(len(i)," ")
            
        scores_list.append(levenstein(i,j))
        print(i,j,levenstein(i,j))
    final_list.append(sum(scores_list))
  

print(final_list)
out_file = open(out_file,"w+")
out_file.write(str(final_list))


                      