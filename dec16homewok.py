superLst=[]


mi=['Rohit Sharma','Hardik Pandya','Jasprit Bumrah','Suryakumar Yadav','Tilak Varma','Will Jacks','Bevon Jacobs','Naman Dhir','Mitchell Santner','Ashwani Kumar','Deepak Chahar']


rcb=['Virat Kohli','Rajat Patidar','Phil Salt','Jitesh Sharma','Liam Livingstone','Tim David','Suyash Sharma','Nuwan Thushara','Lungi Ngidi','Bhuvneshwar Kumar','Yash Dayal']


pbks=['Shreyas Iyer','Arshdeep Singh','Yuzvendra Chahal','Josh Inglis','Lockie Ferguson','Marco Jansen','Marcus Stoinis','Prabhsimran Singh','Pyla Avinash','Suryansh Shedge','Harpreet Brar']

gt=['Shubman Gill','Jos Buttler','Sai Sudharsan','Shahrukh Khan','Rashid Khan','Prasidh Krishna','Mohammed Siraj','Gerald Coetzee','Anuj Rawat','Nishant Sindhu','Mahipal Lomror']


superLst.append(mi)

superLst.append(rcb)

superLst.append(pbks)

superLst.append(gt)



for team in range(0,1):
    for players in superLst[team]:
        print(players)
        for char in players:
            print(char)
            
print("Gt Team Players\n")
            
for team in range(1,2):
    for players in superLst[team]:
        print(players)
        for char in players:
            print(f"{char}")
            
            
print("Rcb Team Players\n")


for team in range(2,3):
    for players in superLst[team]:
        print(players)
        for char in players:
            print(f"{char}")
            
print("Pbks Team Players\n")
            
for team in range(3,4):
    print("Pbks Team Players\n")
    for players in superLst[team]:
        # print("Pbks Team Players\n")
        print(players)
        for char in players:
            print(f"{char}")
            
            
            
    