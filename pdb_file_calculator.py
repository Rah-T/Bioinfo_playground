#Created by- Rahul Ashok Tiwari 
#BIM-2021-28  Msc-2 Bioinformatics 
#MMS Assignment 5

import time

start = time.time()
import pandas as pd 
import re
import math
from numpy import arccos
import numpy as np
import os
os.getcwd()
fil=str(input("Enter your complete pdb file name = "))
sd=str(input("Enter your complete sdf file name = "))
f= open(fil)

co_or=[]
atom1,atom2,len_b,d=[],[],[],[]
for i in f.readlines():
    #print(i)
    result1=re.search(r"^ATOM\s*(\d+)\s*(\w+)\s+\D+\d+\s+(\S+)\s+(\S+)\s+(\S+)", i)
    result2=re.search(r"^HETATM\s*(\d+)\s*(\w+)\s+\D+\d+\s+(\S+)\s+(\S+)\s+(\S+)", i)
    if result1!=None: #regex returns none if no match found
        co_or.append(result1.group(1,2,3,4,5))
        # pass
    elif result2!=None:
        co_or.append(result2.group(1,2,3,4,5))
        # print(result.group(1,2,3,4,5))
        # co_or.append(result.group(1,2,3,4,5))
    # result=re.search(r"^TER\s*(\d+)\s*(\w+)", i)
# print(co_or)
df=pd.DataFrame(co_or,columns=['num','atoms','x','y','z'])
# print(df)
for i in range(len(df['atoms'])):
    # i=str(i)
    df.at[i,'atoms']=str(df.at[i,'atoms'])+"-"+str(df.at[i,'num'])
df=df.set_index('num')
print(df,"\n") 


k=open(sd)#sd file
bonds=pd.DataFrame()
for i in range(4):
    p=k.readline() #just to read and leave the first few lines of sd file

for j in k.readlines():
    bond=re.search(r"^\s+(\d+)\s+(\d+)",j)
    if bond==None:
        pass
    else:
        # print(bond.group(1))
        a=bond.group(1)
        # print(type(a))
        b=bond.group(2)
        x1,y1,z1=float(df.at[a,'x']),float(df.at[a,'y']),float(df.at[a,'z'])
        x2,y2,z2=float(df.at[b,'x']),float(df.at[b,'y']),float(df.at[b,'z'])
        dist=(((x2-x1)**2)+((y2-y1)**2)+((z2-z1)**2))**0.5
        print(f"Bond between two atoms" ,df.at[a,'atoms'],"and",df.at[b,'atoms'],"is",round(dist,3),'Angstorms')
        #bonds.update({df.at[a,'atoms']+' and '+df.at[b,'atoms'] :  round(dist,3)})
        atom1.append(df.at[a,'atoms'])  
        atom2.append(df.at[b,'atoms'])
        len_b.append(round(dist,3))
   
bonds=pd.DataFrame({'atom1':atom1,'atom2':atom2,'len_a_b':len_b,})

#print(at3)  
# print(bonds) 

# at1,at2=bonds.at[0,'atom1'],bonds.at[0,'atom2']

# print(at1,at2)
v_at1,v_at2,v_at3,ang=[],[],[],[]
for i in range(len(bonds.atom1)):
    at1,at2=bonds.at[i,'atom1'],bonds.at[i,'atom2']
    # print(at1,at2,"An")
    # if at1==bonds.atom1[i] and  at2==bonds.atom2[i]:
    a=float(bonds.at[i,"len_a_b"])
    for i in range(len(atom1)):
            if at2==bonds.atom1[i] and  at1!=bonds.atom2[i]:
                at3 = bonds.at[i,'atom2']
                b=float(bonds.at[i,"len_a_b"])
                # print(at1,at2,a,"kok")
                # print(at2,at3,b)
                for i in range(1,len(df.atoms)):
                    if at1==df.atoms[i]:
                        # print(df.atoms[i])
                        i=str(i) #str is imp for calling with dataframe  
                        x1,y1,z1=float(df.at[i,'x']),float(df.at[i,'y']),float(df.at[i,'z'])
                        # print(x1,y1,z1)
                for i in range(1,len(df.atoms)):
                    if at3==df.atoms[i]:
                        # print(df.atoms[i])
                        i=str(i)#+1 because range starting from 1 but df is 0
                        x2,y2,z2=float(df.at[i,'x']),float(df.at[i,'y']),float(df.at[i,'z'])
                        # print(x2,y2,z2)
                c=round((((x2-x1)**2)+((y2-y1)**2)+((z2-z1)**2))**0.5,3)
                # print(at1,at2,a,"a")
                # print(at2,at3,b,"b")
                # print(at1,at3,c,"c")
                # angle =arccos(((a**2)+(b**2)-(c**2))/(2*a*b))
                p=((a**2)+(b**2)-(c**2))/(2*a*b)
                angle =arccos(p*math.pi/180)  #convert output to radians
                print(f"Angles between are",at1,at2,at3,'=', round(math.degrees(angle),3))
                v_at1.append(at1),v_at2.append(at2),v_at3.append(at3),ang.append(round(math.degrees(angle),3))


ang_df=pd.DataFrame({'atom1':v_at1,'atom2':v_at2,'atom3':v_at3,'Angle':ang,})
print(ang_df)

v1,v2,v3,v4,ang_dh=[],[],[],[],[]

for i in range(len(bonds.atom1)):
    v_1,v_2=bonds.at[i,'atom1'],bonds.at[i,'atom2']
    # print(v_1,"vvvv")
    for i in range(len(bonds.atom1)):
            if v_2==bonds.atom1[i] and  v_1!=bonds.atom2[i]:
                v_3 = bonds.at[i,'atom2']
                for i in range(len(bonds.atom1)):
                    if v_3==bonds.atom1[i] and  v_2!=bonds.atom2[i]:
                        v_4 = bonds.at[i,'atom2']
                        # print(v_1,v_2,v_3,v_4)
                        for i in range(1,len(df.atoms)):
                            i=str(i)
                            if v_1==df.at[i,"atoms"]:
                                # i=str(i)
                                # print(v_1,"kkkkk")
                                # # i=str(i+1) #str is imp for calling with dataframe  
                                x1,y1,z1=float(df.at[i,'x']),float(df.at[i,'y']),float(df.at[i,'z'])
                                # print(x1,y1,z1)
                        for i in range(1,len(df.atoms)):
                            i=str(i)
                            if v_2==df.at[i,"atoms"]:
                                # print(df.atoms[i],"llllllll")
                                # i=str(i+1)
                                x2,y2,z2=float(df.at[i,'x']),float(df.at[i,'y']),float(df.at[i,'z'])
                                # print(x2,y2,z2)
                        for i in range(1,len(df.atoms)):
                            i=str(i)
                            if v_3==df.at[i,"atoms"]:
                                # print(df.atoms[i],"mmmmmmmmmmm")
                                # i=str(i+1) #str is imp for calling with dataframe  
                                x3,y3,z3=float(df.at[i,'x']),float(df.at[i,'y']),float(df.at[i,'z'])
                                # print(x3,y3,z3)
                        for i in range(1,len(df.atoms)):
                            i=str(i)
                            if v_4==df.at[i,"atoms"]:
                                # print(df.atoms[i],"nnnnnnnnnn")
                                # i=str(i)#+1 because range starting from 1 but df is 0
                                x4,y4,z4=float(df.at[i,'x']),float(df.at[i,'y']),float(df.at[i,'z'])
                                # print(x4,y4,z4)
                        # print(v_1,x1,y1,z1,v_2,x2,y2,z2,v_3,x3,y3,z3,v_4,x4,y4,z4)
                        vec1=[round(x2-x1,3),round(y2-y1,3),round(z2-z1,3)]
                        vec2=[round(x3-x2,3),round(y3-y2,3),round(z3-z2,3)]
                        vec3=[round(x4-x3,3),round(y4-y3,3),round(z4-z3,3)]
                        angle_v1=np.cross(vec1,vec2)
                        angle_v2=np.cross(vec2,vec3)
                        angle_v3=np.dot(angle_v1,angle_v2)
                        angle_v4 = np.sqrt(angle_v1[0] ** 2 + angle_v1[1] ** 2 + angle_v1[2] ** 2)
                        angle_v5 = np.sqrt(angle_v2[0] ** 2 + angle_v2[1] ** 2 + angle_v2[2] ** 2)
                        p=(angle_v3 / (angle_v4 * angle_v5))
                        dh_Angle = round(np.degrees(np.arccos(p)),3)
                        # print("atoms",v_1,v_2,v_3,v_4)
                        # print("vectors",vec1,vec2,vec3,"\n")
                        # print("angles",angle_v1,angle_v2,"\n",angle_v3,"\n",angle_v4,angle_v5,"\n","Dihedral",dh_Angle)
                        print(f"Dihedral angle between atoms" ,v_1,v_2,v_3,v_4,"is",dh_Angle)
                        v1.append(v_1),v2.append(v_2),v3.append(v_3),v4.append(v_4),ang_dh.append(dh_Angle)
dh_ang_df=pd.DataFrame({"Atom1":v1,"Atom2":v2,"Atom3":v3,"Atom4":v4,"Dihedral_Angles":ang_dh})

dfs = [df,bonds,ang_df,dh_ang_df]
y=str(input("Do you want to export this as an .csv file- Type [Y/N]="))
# y="Y"
if y=="Y":
    name=str(input("Enter name of csv file title to Save as= "))
                        
    with open(name,'a') as f:
        for i in dfs:
            i.to_csv(f,index=False)
            f.write("\n")
else:
    print("OK user")
end = time.time()
print('\n' + '"The time of execution of above program is :',
      (end - start) * 10 ** 3, 'ms"')
               
