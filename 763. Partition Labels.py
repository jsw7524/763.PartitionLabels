class Solution:
    def partitionLabels(self, S):
     ans=[]
     lenS=len(S)
     dic = {c: i for (i, c) in zip(range(lenS), S)}
     partitionRangeLeft=0
     partitionRangeRight=dic[S[0]]
     for (i,c) in zip(range(lenS), S):
         if i == partitionRangeRight:
             ans.append(partitionRangeRight-partitionRangeLeft +1)
             partitionRangeLeft = partitionRangeRight+1
             partitionRangeRight = dic[S[i+1]] if i+1 < lenS else lenS
         elif partitionRangeRight < dic[S[i]]:
             partitionRangeRight = dic[S[i]]
     return ans
''''''
print("Test1")
sln =Solution()
print(sln.partitionLabels("ababcbacadefegdehijhklij"))
''''''
print("Test2")
sln =Solution()
print(sln.partitionLabels("eaaaabaaec"))
''''''
print("Test3")
sln =Solution()
print(sln.partitionLabels("vhaagbqkaq"))