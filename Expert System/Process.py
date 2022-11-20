




class Process():
    def __init__(self):
        
        
        self.response=[-1]*25
        self.get_questions()
        self.get_knowledge()
        self.fix_knowledge()
        
        self.green=[]
        for i in range(len(self.df)):
            self.green.append(i)
        self.yellow=[]
        self.red=[]
        
        self.checkFunction()
        
        # self.temp()        
        
    def get_questions(self):#get questions of txt file
        file=open("questions.txt")
        self.sorular=file.read().splitlines()
        # random.shuffle(self.sorular)
    
    def get_knowledge(self):#get knowledge of csv file
        self.df=pd.read_csv("bilgiler_hazir.csv")
        

    def fix_knowledge(self):#tikli kisimlar 1 boþ kýsýmlar -1 olarak deðiþtirildi.
        self.df=self.df.fillna(0)
        self.df=self.df.replace("x",1)
        self.df.drop(self.df.columns[0],axis=1,inplace=True)
        print(self.df)
     
        
    def checkFunction(self):
        indis=int(0)
        for i in range(len(self.sorular)):
            print(self.sorular[i])
            secim=input("Your answer :")
            self.respons[i]=secim
            
    def Compare(self):
        for i in range(len(self.df)):
            self.ValueCompare(self.respons,self.df.iloc[i][:])
        
        
    def ValueCompare(self,respons,ozellikler):
        print(ozellikler)
        
     
        
     
    def kontrol_fonksiyonu(self):
        self.soru_indis=self.rastgele_soru_sec()
        print(self.sorular[self.soru_indis])
        self.respon=input("Cevabýnýz Nedir:")
        self.renkleri_duzenle()
    def renkleri_duzenle(self):
        temp=[]
        for i in self.green:
            temp.append(i)
        for i in temp:
            # print(self.df.iloc[i][self.soru_indis])
            if self.df.iloc[i][self.soru_indis] == self.respon:
            #     self.yellow.insert(i)
            #     self.green.remove(i)
                pass
            else:
                self.yellow.append(i)
                self.green.remove(i)
        self.renkleri_goster()        
    def renkleri_goster(self):
        print("Renkleri Göster")
        print("Green")
        print(self.green)
        print(self.yellow)
        
    def temp(self):
        for i in range(len(self.sorular)):
            print(i,self.sorular[i])
        
    