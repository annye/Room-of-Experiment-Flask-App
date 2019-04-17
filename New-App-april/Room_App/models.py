'''
Created on 10 Feb 2019

@author: A.Braca
'''


from py2neo import Graph, Node, Relationship, authenticate
from passlib.hash import bcrypt
from datetime import datetime
import uuid
import pdb
import sys  
import json 
import pandas as pd 
from pandas import DataFrame



graph = Graph()  

authenticate("localhost:7474", "neo4j", "python")

class User:
    def __init__(self, username):
        self.username = username

    def find(self):
        user = graph.find_one("User", "username", self.username)
        return user

    def register(self, password):
        if not self.find():
            user = Node("User", username=self.username, password=password)
            graph.create(user)
            return True
        return False

    def verify_password(self, password):
        user = self.find()

        if not user:
            return False

        return password ==user["password"]



    def add_survey(self,gender,
                        sexuality,
                        ethnicity,
                        occupation,
                        marital_status,
                        education,
                        vehicle,
                        age,
                        religion,
                        recreation):
        user = self.find()

        demographic = Node(
            "Demographic",
            id=str(uuid.uuid4()),
            gender=gender,
            sexuality=sexuality,
            ethnicity=ethnicity,
            occupation=occupation,
            marital_status=marital_status,
            education=education,
            vehicle=vehicle,
            religion=religion,
            age=age,
            recreation=recreation,
            timestamp=int(datetime.now().strftime("%s")),
            date=datetime.now().strftime("%F")
        )

        rel = Relationship(user, "DEMOGRAPHIC_FACTORS", demographic)
        graph.create(rel)
    

    def add_personality(self, likert):
        user=self.find()
        personality = Node(
        "Personality",
        id=str(uuid.uuid4()),
        p1=likert[0],
        p2=likert[1],
        p5=likert[2],
        p8=likert[3],
        p10=likert[4],
        p12=likert[5],
        p18=likert[6],
        p19=likert[7],
        p20=likert[8],
        p24=likert[9],
        p27=likert[10],
        p28=likert[11],
        p29=likert[12],
        p30=likert[13], 
        p31=likert[14],
        p32=likert[15],
        p33=likert[16],
        p34=likert[17],
        p36=likert[18],
        p37=likert[19],
        p39=likert[20],
        p40=likert[21], 
        p42=likert[22], 
        p44=likert[23],
        p46=likert[24],
        p47=likert[25],
        p48=likert[26],
        p49=likert[27],
        p50=likert[28],
        p51=likert[29],
        timestamp=int(datetime.now().strftime("%s")),
        date=datetime.now().strftime("%F")
        )
        rel2 = Relationship(user, "PERSONALITY_TRAITS", personality)
        graph.create(rel2)

    def add_values(self, likert):
        user=self.find()
        values = Node(
        "Values",
        id=str(uuid.uuid4()),
        v1=likert[0],
        v2=likert[1],
        v3=likert[2],
        v4=likert[3],
        v5=likert[4],
        v6=likert[5],
        v7=likert[6],
        v8=likert[7],
        v9=likert[8],
        v10=likert[9],
        v11=likert[10],
        v12=likert[11],
        v13=likert[12],
        v14=likert[13], 
        v15=likert[14],
        v16=likert[15],
        v17=likert[16],
        v18=likert[17],
        v19=likert[18],
        v20=likert[19],
        v21=likert[20],
        v22=likert[21],
        v23=likert[22], 
        v24=likert[23],
        v25=likert[24],
        v26=likert[25],
        v27=likert[26],
        v28=likert[27],
        v29=likert[28],
        v30=likert[29],
        v31=likert[30],
        v32=likert[31],
        v33=likert[32],
        timestamp=int(datetime.now().strftime("%s")),
        date=datetime.now().strftime("%F")
        )
        rel_values = Relationship(user, "Belief_system", values)
        graph.create(rel_values)




    def add_sensory(self,
                        s1,s2,s3,s4,s5,s6):
        user = self.find()
        sensory = Node(
        "Sensory",
        id=str(uuid.uuid4()),
        s1=s1,
        s2=s2,
        s3=s3,
        s4=s4,
        s5=s5,
        s6=s6
           )
        rel_perception = Relationship(user, "Communication_channel", sensory)
        graph.create(rel_perception)

    def add_table_1(self, rates1,rates2,rates3,rates4,rates5):
        user = self.find()
        table1 = Node(
        "Check-ups_ever",
        rates1=rates1,
        rates2=rates2,
        rates3=rates3,
        rates4=rates4,
        rates5=rates5
                    )
        rel_table1 = Relationship(user,"Check-ups_Hardly-ever",table1)
        graph.create(rel_table1)

    def add_table_2(self, r_1,r_2,r_3,r_4,r_5):
        user = self.find()
        table2 = Node(
        "Check-ups_occacionally",
        r_1=r_1,
        r_2=r_2,
        r_3=r_3,
        r_4=r_4,
        r_5=r_5
                    )
        rel_table2 = Relationship(user,"Check-ups_Occacionally",table2)
        graph.create(rel_table2)

    def add_table_3(self, tq_1,tq_2,tq_3,tq_4,tq_5):
        user = self.find()
        table3 = Node(
        "Toothbrushes_1",
        tq_1=tq_1,
        tq_2=tq_2,
        tq_3=tq_3,
        tq_4=tq_4,
        tq_5=tq_5
                    )
        rel_table3 = Relationship(user,"Changing_toothbrushes_Very_Rare",table3)
        graph.create(rel_table3)

    
    def add_table_4(self, sq_1,sq_2,sq_3,sq_4,sq_5):
        user = self.find()
        table4 = Node(
        "Toothbrushes_2",
        sq_1=sq_1,
        sq_2=sq_2,
        sq_3=sq_3,
        sq_4=sq_4,
        sq_5=sq_5
                    )
        rel_table4 = Relationship(user,"Changing_toothbrushes_Sometimes", table4)
        graph.create(rel_table4)


    def add_table_5(self, ssq_1,ssq_2,ssq_3,ssq_4,ssq_5, ssq_6, ssq_7):
        user = self.find()
        table5 = Node(
        "Smoke_yes",
        ssq_1=ssq_1,
        ssq_2=ssq_2,
        ssq_3=ssq_3,
        ssq_4=ssq_4,
        ssq_5=ssq_5,
        ssq_6=ssq_6,
        ssq_7=ssq_7
                    )
        rel_table5 = Relationship(user,"Smoke_Yes",table5)
        graph.create(rel_table5)
        
    
    def add_table_7(self, m_1,m_2,m_3,m_4,m_5):
        user = self.find()
        table7 = Node(
        "Mouthwash",
        m_1=m_1,
        m_2=m_2,
        m_3=m_3,
        m_4=m_4,
        m_5=m_5
        
                    )
        rel_table7 = Relationship(user,"Mouthwash_Floss",table7)
        graph.create(rel_table7)


 
    def add_odontophobia(self, likert):
        user=self.find()
        odontophobia = Node(
            "Odontophobia",
            id=str(uuid.uuid4()),
            f1=likert[0],
            f2=likert[1],
            f3=likert[2],
            f4=likert[3],
            f5=likert[4],
            f6=likert[5],
            f7=likert[6],
            f8=likert[7],
            f9=likert[8],
            f10=likert[9],
            
            timestamp=int(datetime.now().strftime("%s")),
            date=datetime.now().strftime("%F")
        )
        rel_odonto = Relationship(user, "Odontophobia",odontophobia )
        graph.create(rel_odonto)
    



    def add_arguments(self,
                            issue, side,type_schema, premise_type, 
                            argu, major_premise,evidence,minor_premise,
                            conclusion,type_dialog,influence_social,
                            support, source):
        
        user=self.find()
        print("Adding arguments")
        print (issue, side, type_schema,premise_type, 
                            argu, major_premise,minor_premise,
                            conclusion,type_dialog,influence_social,
                            support, source)

        argument = Node(
            "Argument",
            id=str(uuid.uuid4()),
            issue=issue, 
            side=side,
            type_schema=type_schema,
            premise_type=premise_type, 
            argu=argu, 
            major_premise=major_premise,
            minor_premise=minor_premise,
            conclusion=conclusion,
            type_dialog=type_dialog,
            influence_social=influence_social,
            support=support, 
            source=source, 
            
        )
        graph.create(argument)
        rel_admin_argu = Relationship(user, "Admin_Present_Arguments", argument)
        print(rel_admin_argu)
        graph.create(rel_admin_argu)

    
    def like_argument(self, argument_id, rating):
        value_dict = {6: 'DISAGREE',
                      1: 'HAS_RATED_1',
                      2: 'HAS_RATED_2',
                      3: 'HAS_RATED_3',
                      4: 'HAS_RATED_4',
                      5: 'HAS_RATED_5'
                      }
        user = self.find()
        post = graph.find_one("Argument", "id",argument_id)
        if rating == 6:
            rel = Relationship(user,
                               value_dict[rating],
                               post)
            graph.merge(rel)
            graph.create_unique(rel)
        else:
            rel = Relationship(user,
                               value_dict[rating],
                               post,
                               stars=rating)
            graph.merge(rel)
            graph.create_unique(rel)   
    
    
    def add_ratings(self,stars):
        user = self.find()
       
      
        rates= Node(
        "Ratings",
        id=str(uuid.uuid4()),
        rating=stars,
        )
        rel_stars = Relationship(user, "RATING", rates)
        graph.merge(rel_stars)
        graph.create_unique(rel_stars)
   
        print(rel_stars)


def five_stars(self, argument_id,stars):
        user = self.find()
        post = graph.find_one("Argument", "id",argument_id)
        
        mrel5=Relationship(user,"HAS_RATED",post,stars=5)
        mrel4=Relationship(user,"HAS_RATED",post,stars=4)
        mrel3=Relationship(user,"HAS_RATED",post,stars=3)
        mrel2=Relationship(user,"HAS_RATED",post,stars=2)
        mrel1=Relationship(user,"HAS_RATED",post,stars=1)
        graph.create(mrel5,mrel4,mrel3,mrel2,mrel1)

      
def display(index_col=None,columns= None):
    """Retrieve arguments from graoh database."""
    postsA = graph.cypher.execute("match(n:Argument)WHERE n.side='SideA'return n")
    postsB = graph.cypher.execute("match(n:Argument)WHERE n.side='SideB'return n")
    posts = graph.cypher.execute("match(n:Argument)return n")
    return  postsA, postsB, posts