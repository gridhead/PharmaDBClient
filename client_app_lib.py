from tkinter import *
from tkinter import ttk
import tkinter.messagebox as msgbox
import mysql.connector

OperationsWindow=Tk()
#OperationsWindow.attributes('-type','splash')
#OperationsWindow.overrideredirect(True)
OperationsWindow.geometry("1280x720")
OperationsWindow.focus_force()
OperationsWindow.resizable(0,0)
OperationsWindow.title("PharmaDB Client")
uriVal,dbsVal,usrVal,pwdVal="","","",""
AttrString=StringVar()
AttrList=[0,0,0,0,0,0,0]
var,ser,avl,class1Var,class2Var,class3Var,class4Var,class5Var,class6Var,class7Var=IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar()

def quitProgram():
    quit()

def wipeTableStats(tabName):
    x = tabName.get_children()
    for item in x:
        tabName.delete(item)

def getAllMedicines():
    try:
        fileObject=open("connCache.txt","r")
        connectStr=fileObject.read()
        fileObject.close()
        connectArr=connectStr.split(" ")
        print(connectArr)
        uriVal,usrVal,pwdVal,dbsVal=str(connectArr[0]),str(connectArr[1]),str(connectArr[2]),str(connectArr[3])
        focus=mysql.connector.connect(host=uriVal,user=usrVal,passwd=pwdVal,database=dbsVal)
        curs=focus.cursor()
        curs.execute("select * from TestMedicines")
        result=curs.fetchall()
        return result
    except Exception as e:
        msgbox.showinfo("Fatal Error","The client was unable to retrieve records from the table. "+str(e))

def getAllManufacts():
    try:
        fileObject=open("connCache.txt","r")
        connectStr=fileObject.read()
        fileObject.close()
        connectArr=connectStr.split(" ")
        print(connectArr)
        uriVal,usrVal,pwdVal,dbsVal=str(connectArr[0]),str(connectArr[1]),str(connectArr[2]),str(connectArr[3])
        focus=mysql.connector.connect(host=uriVal,user=usrVal,passwd=pwdVal,database=dbsVal)
        curs=focus.cursor()
        curs.execute("select * from TestManufacts")
        result=curs.fetchall()
        return result
    except Exception as e:
        msgbox.showinfo("Fatal Error","The client was unable to retrieve records from the table. "+str(e))

def getAllTypeClass():
    try:
        fileObject=open("connCache.txt","r")
        connectStr=fileObject.read()
        fileObject.close()
        connectArr=connectStr.split(" ")
        print(connectArr)
        uriVal,usrVal,pwdVal,dbsVal=str(connectArr[0]),str(connectArr[1]),str(connectArr[2]),str(connectArr[3])
        focus=mysql.connector.connect(host=uriVal,user=usrVal,passwd=pwdVal,database=dbsVal)
        curs=focus.cursor()
        curs.execute("select * from TestTypeClass")
        result=curs.fetchall()
        return result
    except Exception as e:
        msgbox.showinfo("Fatal Error","The client was unable to retrieve records from the table. "+str(e))

def getAllWarehouse():
    try:
        fileObject=open("connCache.txt","r")
        connectStr=fileObject.read()
        fileObject.close()
        connectArr=connectStr.split(" ")
        print(connectArr)
        uriVal,usrVal,pwdVal,dbsVal=str(connectArr[0]),str(connectArr[1]),str(connectArr[2]),str(connectArr[3])
        focus=mysql.connector.connect(host=uriVal,user=usrVal,passwd=pwdVal,database=dbsVal)
        curs=focus.cursor()
        curs.execute("select * from TestWarehouse")
        result=curs.fetchall()
        return result
    except Exception as e:
        msgbox.showinfo("Fatal Error","The client was unable to retrieve records from the table. "+str(e))

def getConnect():
    def mysqllink():
        uriVal=UriBox.get()
        dbsVal=DbsBox.get()
        usrVal=UsrBox.get()
        pwdVal=PwdBox.get()
        print(uriVal,dbsVal,usrVal,pwdVal)
        try:
            focus=mysql.connector.connect(host=uriVal,user=usrVal,passwd=pwdVal,database=dbsVal)
            msgbox.showinfo("Connection Successful!","Welcome "+usrVal+"! You have successfully logged in to "+uriVal)
            connectStr=str(uriVal)+" "+str(usrVal)+" "+str(pwdVal)+" "+str(dbsVal)
            fileObject=open("connCache.txt","w")
            fileObject.write(connectStr)
            fileObject.close()
            getConnectWindow.destroy()
        except Exception as e:
            msgbox.showinfo("Connection Failed!","Unable to estabilish connection to database. "+str(e))    
    getConnectWindow=Toplevel()
    getConnectWindow.geometry("960x540")
    getConnectWindow.resizable(0,0)
    getConnectWindow.title("Connect Now")
    getConnectWindow.grab_set()
    WinTitlePag=Frame(getConnectWindow,width=960,height=200,bd=1,relief="raise",bg="green")
    WinContents=Frame(getConnectWindow,width=960,height=300,bd=1,relief="sunken")
    WinControls=Frame(getConnectWindow,width=960,height=40,bd=1,relief="raise",bg="green")
    WindowTitle=Label(WinTitlePag,font=("Liberation Sans",20,"normal"),text="Connect to your PharmaDB Instance",bg="green",fg="white")
    infStng1=Label(WinContents,text="You are currently accessing the client software using administrator privileges which allows you to potentially create, insert, read, display, update, modify, revoke and delete records seamlessly. Once changes are made and committed, rollback is not possible so you are requested to use some discretion during the operations.",wraplength=450,font=('Liberation Sans',9,'normal'),fg="red",justify=LEFT)
    infStng2=Label(WinContents,text="In order to be able to use the PharmaDB Client, you must connect to your own MySQL Medicine Cluster using the URI, username, password and database provided by your DBA.",wraplength=450,font=('Liberation Sans',9,'normal'),justify=LEFT)
    UriName=Label(WinContents,font=("Liberation Sans",9,"normal"),text="URI String")
    UriBox=Entry(WinContents,font=("Liberation Sans",9,"normal"),bd=1,width=30,bg="white",fg="black")
    UsrName=Label(WinContents,font=("Liberation Sans",9,"normal"),text="Username")
    UsrBox=Entry(WinContents,font=("Liberation Sans",9,"normal"),bd=1,width=30,bg="white",fg="black")
    PwdName=Label(WinContents,font=("Liberation Sans",9,"normal"),text="Password")
    PwdBox=Entry(WinContents,font=("Liberation Sans",9,"normal"),bd=1,width=30,show='*',bg="white",fg="black")
    DbsName=Label(WinContents,font=("Liberation Sans",9,"normal"),text="Database")
    DbsBox=Entry(WinContents,font=("Liberation Sans",9,"normal"),bd=1,width=30,bg="white",fg="black")
    ConnectBtn=Button(WinControls,text="CONNECT NOW",font=("Liberation Sans",9,"bold"),bg="green",fg="white",command=mysqllink,bd=1)
    WinTitlePag.pack(side=TOP)
    WinContents.pack(side=TOP)
    WinControls.pack(side=BOTTOM)
    WindowTitle.place(x=20,y=150)
    infStng1.place(x=20,y=20)
    infStng2.place(x=20,y=100)
    UriName.place(x=20,y=160)
    UriBox.place(x=20,y=180)
    UsrName.place(x=250,y=160)
    UsrBox.place(x=250,y=180)
    PwdName.place(x=250,y=200)
    PwdBox.place(x=250,y=220)
    DbsName.place(x=20,y=200)
    DbsBox.place(x=20,y=220)
    ConnectBtn.place(x=20,y=5)

def creatRecordToMedicine():
    try:
        fileObject=open("connCache.txt","r")
        connectStr=fileObject.read()
        fileObject.close()
        connectArr=connectStr.split(" ")
        print(connectArr)
        uriVal,usrVal,pwdVal,dbsVal=str(connectArr[0]),str(connectArr[1]),str(connectArr[2]),str(connectArr[3])
        focus=mysql.connector.connect(host=uriVal,user=usrVal,passwd=pwdVal,database=dbsVal)
        curs=focus.cursor()
        selectedClass=StringVar()
        def selectType():
            medClass=["0","IsAntiPytc","IsAnalGesc","IsAntiBiot","IsAntiSept","IsMoodStab","IsStimulan","IsTranquil"]
            selectedClass=str(medClass[int(var.get())])
            print(selectedClass)
            fileObject=open("medClassCache.txt","w")
            fileObject.write(selectedClass)
            fileObject.close
        def fetchInputs():
            fileObject=open("medClassCache.txt","r")
            selectedClass=fileObject.read()
            fileObject.close()
            print(selectedClass)
            IsAntiPytc,IsAnalGesc,IsAntiBiot,IsAntiSept,IsMoodStab,IsStimulan,IsTranquil=0,0,0,0,0,0,0
            ReltionNam="TestMedicines"
            MedicineID=MediIDBox.get()
            ManufactID=MfgIDBox.get()
            MediTypeID=TypeIDBox.get()
            MediciName=MedNamBox.get()
            DateOfMfgr=MfgDatBox.get()
            DateOfExpr=ExpDatBox.get()
            if (selectedClass=="IsAntiPytc"):
                IsAntiPytc=1
            elif (selectedClass=="IsAnalGesc"):
                IsAnalGesc=1
            elif (selectedClass=="IsAntiBiot"):
                IsAntiBiot=1
            elif (selectedClass=="IsAntiSept"):
                IsAntiSept=1
            elif (selectedClass=="IsMoodStab"):
                IsMoodStab=1
            elif (selectedClass=="isStimulan"):
                IsStimulan=1
            elif (selectedClass=="IsTranquil"):
                IsTranquil=1
            curs=focus.cursor()
            try:
                taskComp="insert into "+ReltionNam+"(MedicineID,MedName,MedTypeID,MedMfgrID,MfgDate,ExpDate,IsAntiPytc,IsAnalGesc,IsAntiBiot,IsAntiSept,IsMoodStab,IsStimulan,IsTranquil) values ('"+MedicineID+"', '"+MediciName+"', '"+MediTypeID+"', '"+ManufactID+"', '"+DateOfMfgr+"', '"+DateOfExpr+"', "+str(IsAntiPytc)+", "+str(IsAnalGesc)+", "+str(IsAntiBiot)+", "+str(IsAntiSept)+", "+str(IsMoodStab)+", "+str(IsStimulan)+", "+str(IsTranquil)+")"
                print(taskComp)
                curs.execute(taskComp)
                focus.commit()
                msgbox.showinfo("Creation/Insertion Successful","Creation and insertion of 1 record(s) in the Medicine table was peformed successfully!")
                createRecWindow.destroy()
            except Exception as e:
                msgbox.showinfo("Creation/Insertion Failed","The client was unable to perform the creation and insertion functions. "+str(e))

        createRecWindow=Toplevel()
        createRecWindow.geometry("960x540")
        createRecWindow.resizable(0,0)
        createRecWindow.title("Create Records : Medicine Table")
        createRecWindow.grab_set()
        WinTitlePag=Frame(createRecWindow,width=960,height=200,bd=1,relief="raise",bg="green")
        WinContents=Frame(createRecWindow,width=960,height=300,bd=1,relief="sunken")
        WinControls=Frame(createRecWindow,width=960,height=40,bd=1,relief="raise",bg="green")
        WindowTitle=Label(WinTitlePag,font=("Liberation Sans",20,"normal"),text="Create/Insert Records in Medicine Table",bg="green",fg="white")
        infStng1=Label(WinContents,text="You are currently accessing the client software using administrator privileges which allows you to potentially create, insert, read, display, update, modify, revoke and delete records seamlessly. Once changes are made and committed, rollback is not possible so you are requested to use some discretion during the operations.",wraplength=450,font=('Liberation Sans',9,'normal'),fg="red",justify=LEFT)
        infStng2=Label(WinContents,text="You might want to keep in the enterprise relational schema in mind while creating and inserting data in the chosen relation. ASTERISK (*) denotes PRIMARY KEY and CAP (^) denotes REFERENCE KEY.",wraplength=450,font=('Liberation Sans',9,'normal'),justify=LEFT)
        MedNamTex=Label(WinContents,font=("Liberation Sans",9,"normal"),text="Medicine Name")
        MedNamBox=Entry(WinContents,font=("Liberation Sans",9,"normal"),width=30,bd=1,bg="white")
        MediIDTex=Label(WinContents,font=("Liberation Sans",9,"normal"),text="Medi ID*")
        MediIDBox=Entry(WinContents,font=("Liberation Sans",9,"normal"),width=10,bd=1,bg="white")
        TypeIDTex=Label(WinContents,font=("Liberation Sans",9,"normal"),text="Type ID^")
        TypeIDBox=Entry(WinContents,font=("Liberation Sans",9,"normal"),width=10,bd=1,bg="white")
        MfgIDText=Label(WinContents,font=("Liberation Sans",9,"normal"),text="Mfgr ID^")
        MfgIDBox=Entry(WinContents,font=("Liberation Sans",9,"normal"),width=10,bd=1,bg="white")
        MfgDatTex=Label(WinContents,font=("Liberation Sans",9,"normal"),text="Date Of Manufacture")
        MfgDatBox=Entry(WinContents,font=("Liberation Sans",9,"normal"),width=30,bd=1,bg="white")
        ExpDatTex=Label(WinContents,font=("Liberation Sans",9,"normal"),text="Date Of Expiry")
        MfgDatBox=Entry(WinContents,font=("Liberation Sans",9,"normal"),width=30,bd=1,bg="white")
        ExpDatTex=Label(WinContents,font=("Liberation Sans",9,"normal"),text="Date Of Expiry")
        ExpDatBox=Entry(WinContents,font=("Liberation Sans",9,"normal"),width=30,bd=1,bg="white")
        OverCount=Label(WinContents,font=("Liberation Sans",9,"bold"),text="OVER-THE-COUNTER")
        Physician=Label(WinContents,font=("Liberation Sans",9,"bold"),text="PHYSICIAN ADVICE")
        IsAntiPytic=Radiobutton(WinContents,font=("Liberation Sans",9,"normal"),variable=var,value=1,command=selectType,text="Is Anti-Pyretic?")
        IsAnalgesic=Radiobutton(WinContents,font=("Liberation Sans",9,"normal"),variable=var,value=2,command=selectType,text="Is Analgesic?")
        IsAntiBiotc=Radiobutton(WinContents,font=("Liberation Sans",9,"normal"),variable=var,value=3,command=selectType,text="Is Anti-Biotic?")
        IsAntiSeptc=Radiobutton(WinContents,font=("Liberation Sans",9,"normal"),variable=var,value=4,command=selectType,text="Is Anti-Septic?")
        IsMoodStabz=Radiobutton(WinContents,font=("Liberation Sans",9,"normal"),variable=var,value=5,command=selectType,text="Is Mood Stabilizer?")
        IsStimulant=Radiobutton(WinContents,font=("Liberation Sans",9,"normal"),variable=var,value=6,command=selectType,text="Is Stimulant?")
        IsTranquilz=Radiobutton(WinContents,font=("Liberation Sans",9,"normal"),variable=var,value=7,command=selectType,text="Is Tranquilizer?")
        CommitBtn=Button(WinControls,text="COMMIT INSERTION",font=("Liberation Sans",9,"bold"),bg="green",fg="white",command=fetchInputs,bd=1)
        WinTitlePag.pack(side=TOP)
        WinContents.pack(side=TOP)
        WinControls.pack(side=BOTTOM)
        WindowTitle.place(x=20,y=150)
        infStng1.place(x=20,y=20)
        infStng2.place(x=20,y=100)
        MediIDTex.place(x=20,y=160)
        MediIDBox.place(x=20,y=180)
        MedNamTex.place(x=110,y=160)
        MedNamBox.place(x=110,y=180)
        TypeIDTex.place(x=20,y=200)
        TypeIDBox.place(x=20,y=220)
        MfgDatTex.place(x=110,y=200)
        MfgDatBox.place(x=110,y=220)
        MfgIDText.place(x=20,y=240)
        MfgIDBox.place(x=20,y=260)
        ExpDatTex.place(x=110,y=240)
        ExpDatBox.place(x=110,y=260)
        OverCount.place(x=340,y=160)
        IsAntiPytic.place(x=340,y=180)
        IsAnalgesic.place(x=340,y=200)
        IsAntiSeptc.place(x=340,y=220)
        Physician.place(x=490,y=160)
        IsAntiBiotc.place(x=490,y=180)
        IsTranquilz.place(x=490,y=200)
        IsMoodStabz.place(x=490,y=220)
        IsStimulant.place(x=490,y=240)
        CommitBtn.place(x=20,y=5)
    except Exception as e:
        msgbox.showinfo("Connection Failed!","Creation/Insertion failed due to not being able to connect. "+str(e))

def creatRecordToTypes():
    try:
        fileObject=open("connCache.txt","r")
        connectStr=fileObject.read()
        fileObject.close()
        connectArr=connectStr.split(" ")
        print(connectArr)
        uriVal,usrVal,pwdVal,dbsVal=str(connectArr[0]),str(connectArr[1]),str(connectArr[2]),str(connectArr[3])
        focus=mysql.connector.connect(host=uriVal,user=usrVal,passwd=pwdVal,database=dbsVal)
        curs=focus.cursor()
        def fetchInputs():
            ReltionNam="TestTypeClass"
            TypeID=TypeIDBox.get()
            TypNam=TypNamBox.get()
            DemAmt=DemAmtBox.get()
            Avblty=AvbltyBox.get()
            InvLim=InvLimBox.get()
            curs=focus.cursor()
            try:
                taskComp="insert into "+ReltionNam+"(TypeID,TypeName,DemandAmt,AvbltyAmt,StockLimt) values('"+TypeID+"', '"+TypNam+"', "+str(DemAmt)+", "+str(Avblty)+", "+str(InvLim)+")"
                print(taskComp)
                curs.execute(taskComp)
                focus.commit()
                msgbox.showinfo("Creation/Insertion Successful","Creation and insertion of 1 record(s) in the Type table was peformed successfully!")
                createRecWindow.destroy()
            except Exception as e:
                msgbox.showinfo("Creation/Insertion Failed","The client was unable to perform the creation and insertion functions. "+str(e))
        createRecWindow=Toplevel()
        createRecWindow.geometry("960x540")
        createRecWindow.resizable(0,0)
        createRecWindow.title("Create Records : Type Table")
        createRecWindow.grab_set()
        WinTitlePag=Frame(createRecWindow,width=960,height=200,bd=1,relief="raise",bg="green")
        WinContents=Frame(createRecWindow,width=960,height=300,bd=1,relief="sunken")
        WinControls=Frame(createRecWindow,width=960,height=40,bd=1,relief="raise",bg="green")
        WindowTitle=Label(WinTitlePag,font=("Liberation Sans",20,"normal"),text="Create/Insert Records in Type Table",bg="green",fg="white")
        infStng1=Label(WinContents,text="You are currently accessing the client software using administrator privileges which allows you to potentially create, insert, read, display, update, modify, revoke and delete records seamlessly. Once changes are made and committed, rollback is not possible so you are requested to use some discretion during the operations.",wraplength=450,font=('Liberation Sans',9,'normal'),fg="red",justify=LEFT)
        infStng2=Label(WinContents,text="You might want to keep in the enterprise relational schema in mind while creating and inserting data in the chosen relation. ASTERISK (*) denotes PRIMARY KEY and CAP (^) denotes REFERENCE KEY.",wraplength=450,font=('Liberation Sans',9,'normal'),justify=LEFT)
        TypeIDTex=Label(WinContents,font=("Liberation Sans",9,"normal"),text="Type ID*")
        TypeIDBox=Entry(WinContents,font=("Liberation Sans",9,"normal"),width=10,bd=1,bg="white")
        DemAmtTex=Label(WinContents,font=("Liberation Sans",9,"normal"),text="Demand %")
        DemAmtBox=Entry(WinContents,font=("Liberation Sans",9,"normal"),width=10,bd=1,bg="white")
        AvbltyTex=Label(WinContents,font=("Liberation Sans",9,"normal"),text="Avblty %")
        AvbltyBox=Entry(WinContents,font=("Liberation Sans",9,"normal"),width=10,bd=1,bg="white")
        TypNamTex=Label(WinContents,font=("Liberation Sans",9,"normal"),text="Type Name")
        TypNamBox=Entry(WinContents,font=("Liberation Sans",9,"normal"),width=36,bd=1,bg="white")
        InvLimTex=Label(WinContents,font=("Liberation Sans",9,"normal"),text="Capacity")
        InvLimBox=Entry(WinContents,font=("Liberation Sans",9,"normal"),width=36,bd=1,bg="white")
        CommitBtn=Button(WinControls,text="COMMIT INSERTION",font=("Liberation Sans",9,"bold"),bg="green",fg="white",command=fetchInputs,bd=1)
        WinTitlePag.pack(side=TOP)
        WinContents.pack(side=TOP)
        WinControls.pack(side=BOTTOM)
        WindowTitle.place(x=20,y=150)
        infStng1.place(x=20,y=20)
        infStng2.place(x=20,y=100)
        TypeIDTex.place(x=20,y=160)
        TypeIDBox.place(x=20,y=180)
        DemAmtTex.place(x=110,y=160)
        DemAmtBox.place(x=110,y=180)
        AvbltyTex.place(x=200,y=160)
        AvbltyBox.place(x=200,y=180)
        TypNamTex.place(x=20,y=200)
        TypNamBox.place(x=20,y=220)
        InvLimTex.place(x=20,y=240)
        InvLimBox.place(x=20,y=260)
        CommitBtn.place(x=20,y=5)
    except Exception as e:
        msgbox.showinfo("Connection Failed!","Creation/Insertion failed due to not being able to connect. "+str(e))

def creatRecordToManufacts():
    try:
        fileObject=open("connCache.txt","r")
        connectStr=fileObject.read()
        fileObject.close()
        connectArr=connectStr.split(" ")
        print(connectArr)
        uriVal,usrVal,pwdVal,dbsVal=str(connectArr[0]),str(connectArr[1]),str(connectArr[2]),str(connectArr[3])
        focus=mysql.connector.connect(host=uriVal,user=usrVal,passwd=pwdVal,database=dbsVal)
        curs=focus.cursor()
        selectedClass=StringVar()
        selectServRat=StringVar()
        selectAvblRat=StringVar()
        def selectClassOne():
            AttrList[0]=1
        def selectClassTwo():
            AttrList[1]=1
        def selectClassThr():
            AttrList[2]=1
        def selectClassFou():
            AttrList[3]=1
        def selectClassFiv():
            AttrList[4]=1
        def selectClassSix():
            AttrList[5]=1
        def selectClassSev():
            AttrList[6]=1
        def selectServRate():
            servRateList=["0","BAD","POOR","MEDIOCRE","GOOD","EXCELLENT"]
            selectServRat=str(servRateList[int(ser.get())])
            print(selectServRat)
            fileObject=open("medServCache.txt","w")
            fileObject.write(selectServRat)
            fileObject.close
        def selectAvailable():
            avblRateList=["0","VERY LOW","LOW","MODERATE","HIGH","VERY HIGH"]
            selectAvblRat=str(avblRateList[int(avl.get())])
            print(selectAvblRat)
            fileObject=open("medAvblCache.txt","w")
            fileObject.write(selectAvblRat)
            fileObject.close
        def fetchInputs():
            fileObject=open("medClassCache.txt","r")
            selectedClass=fileObject.read()
            fileObject.close()
            fileObject=open("medServCache.txt","r")
            selectServRat=fileObject.read()
            fileObject.close()
            fileObject=open("medAvblCache.txt","r")
            selectAvblRat=fileObject.read()
            fileObject.close()
            print(selectedClass)
            print(selectServRat)
            print(selectAvblRat)
            IsAntiPytc,IsAnalGesc,IsAntiBiot,IsAntiSept,IsMoodStab,IsStimulan,IsTranquil=AttrList[0],AttrList[1],AttrList[2],AttrList[3],AttrList[4],AttrList[5],AttrList[6]
            ReltionNam="TestManufacts"
            MfgrID=MfgrIDBox.get()
            CosInd=CosIndBox.get()
            MfgNam=MfgNamBox.get()
            Cuntry=CuntryBox.get()
            curs=focus.cursor()
            try:
                taskComp="insert into "+ReltionNam+"(MfgrID,MfgName,Country,IfAvail,IfPrice,UserRev,MakesAnPy,MakesAnGe,MakesAnBi,MakesAnSe,MakesMoSt,MakesStim,MakesTran) values ('"+MfgrID+"', '"+MfgNam+"', '"+Cuntry+"', '"+selectAvblRat+"', '"+CosInd+"', '"+selectServRat+"', "+str(IsAntiPytc)+", "+str(IsAnalGesc)+", "+str(IsAntiBiot)+", "+str(IsAntiSept)+", "+str(IsMoodStab)+", "+str(IsStimulan)+", "+str(IsTranquil)+")"
                print(taskComp)
                curs.execute(taskComp)
                focus.commit()
                msgbox.showinfo("Creation/Insertion Successful","Creation and insertion of 1 record(s) in the Medicine table was peformed successfully!")
                createRecWindow.destroy()
            except Exception as e:
                msgbox.showinfo("Creation/Insertion Failed","The client was unable to perform the creation and insertion functions. "+str(e))
        createRecWindow=Toplevel()
        createRecWindow.geometry("960x540")
        createRecWindow.resizable(0,0)
        createRecWindow.title("Create Records : Manufacturer Table")
        createRecWindow.grab_set()
        WinTitlePag=Frame(createRecWindow,width=960,height=200,bd=1,relief="raise",bg="green")
        WinContents=Frame(createRecWindow,width=960,height=300,bd=1,relief="sunken")
        WinControls=Frame(createRecWindow,width=960,height=40,bd=1,relief="raise",bg="green")
        WindowTitle=Label(WinTitlePag,font=("Liberation Sans",20,"normal"),text="Create/Insert Records in Manufacturer Table",bg="green",fg="white")
        infStng1=Label(WinContents,text="You are currently accessing the client software using administrator privileges which allows you to potentially create, insert, read, display, update, modify, revoke and delete records seamlessly. Once changes are made and committed, rollback is not possible so you are requested to use some discretion during the operations.",wraplength=450,font=('Liberation Sans',9,'normal'),fg="red",justify=LEFT)
        infStng2=Label(WinContents,text="You might want to keep in the enterprise relational schema in mind while creating and inserting data in the chosen relation. ASTERISK (*) denotes PRIMARY KEY and CAP (^) denotes REFERENCE KEY.",wraplength=450,font=('Liberation Sans',9,'normal'),justify=LEFT)
        MfgrIDTex=Label(WinContents,font=("Liberation Sans",9,"normal"),text="Mfgr ID*")
        MfgrIDBox=Entry(WinContents,font=("Liberation Sans",9,"normal"),width=15,bd=1,bg="white")
        CosIndTex=Label(WinContents,font=("Liberation Sans",9,"normal"),text="Cost %")
        CosIndBox=Entry(WinContents,font=("Liberation Sans",9,"normal"),width=15,bd=1,bg="white")
        MfgNamTex=Label(WinContents,font=("Liberation Sans",9,"normal"),text="Manufacturer Name")
        MfgNamBox=Entry(WinContents,font=("Liberation Sans",9,"normal"),width=32,bd=1,bg="white")
        CuntryTex=Label(WinContents,font=("Liberation Sans",9,"normal"),text="Country")
        CuntryBox=Entry(WinContents,font=("Liberation Sans",9,"normal"),width=32,bd=1,bg="white")
        UseRevTex=Label(WinContents,font=("Liberation Sans",9,"bold"),text="SERVICE QUALITY")
        Rate5Star=Radiobutton(WinContents,font=("Liberation Sans",9,"normal"),variable=ser,value=5,command=selectServRate,text="Excellent")
        Rate4Star=Radiobutton(WinContents,font=("Liberation Sans",9,"normal"),variable=ser,value=4,command=selectServRate,text="Good")
        Rate3Star=Radiobutton(WinContents,font=("Liberation Sans",9,"normal"),variable=ser,value=3,command=selectServRate,text="Mediocre")
        Rate2Star=Radiobutton(WinContents,font=("Liberation Sans",9,"normal"),variable=ser,value=2,command=selectServRate,text="Poor")
        Rate1Star=Radiobutton(WinContents,font=("Liberation Sans",9,"normal"),variable=ser,value=1,command=selectServRate,text="Bad")
        AvbRevTex=Label(WinContents,font=("Liberation Sans",9,"bold"),text="AVAILABILITY")
        Avbl5Star=Radiobutton(WinContents,font=("Liberation Sans",9,"normal"),variable=avl,value=5,command=selectAvailable,text="Very High")
        Avbl4Star=Radiobutton(WinContents,font=("Liberation Sans",9,"normal"),variable=avl,value=4,command=selectAvailable,text="High")
        Avbl3Star=Radiobutton(WinContents,font=("Liberation Sans",9,"normal"),variable=avl,value=3,command=selectAvailable,text="Moderate")
        Avbl2Star=Radiobutton(WinContents,font=("Liberation Sans",9,"normal"),variable=avl,value=2,command=selectAvailable,text="Low")
        Avbl1Star=Radiobutton(WinContents,font=("Liberation Sans",9,"normal"),variable=avl,value=1,command=selectAvailable,text="Very Low")
        OverCount=Label(WinContents,font=("Liberation Sans",9,"bold"),text="OVER-THE-COUNTER")
        Physician=Label(WinContents,font=("Liberation Sans",9,"bold"),text="PHYSICIAN ADVICE")
        IsAntiPytic=Checkbutton(WinContents,font=("Liberation Sans",9,"normal"),variable=class1Var,onvalue=1,offvalue=0,command=selectClassOne,text="Is Anti-Pyretic?")
        IsAnalgesic=Checkbutton(WinContents,font=("Liberation Sans",9,"normal"),variable=class2Var,onvalue=1,offvalue=0,command=selectClassTwo,text="Is Analgesic?")
        IsAntiBiotc=Checkbutton(WinContents,font=("Liberation Sans",9,"normal"),variable=class3Var,onvalue=1,offvalue=0,command=selectClassThr,text="Is Anti-Biotic?")
        IsAntiSeptc=Checkbutton(WinContents,font=("Liberation Sans",9,"normal"),variable=class4Var,onvalue=1,offvalue=0,command=selectClassFou,text="Is Anti-Septic?")
        IsMoodStabz=Checkbutton(WinContents,font=("Liberation Sans",9,"normal"),variable=class5Var,onvalue=1,offvalue=0,command=selectClassFiv,text="Is Mood Stabilizer?")
        IsStimulant=Checkbutton(WinContents,font=("Liberation Sans",9,"normal"),variable=class6Var,onvalue=1,offvalue=0,command=selectClassSix,text="Is Stimulant?")
        IsTranquilz=Checkbutton(WinContents,font=("Liberation Sans",9,"normal"),variable=class7Var,onvalue=1,offvalue=0,command=selectClassSev,text="Is Tranquilizer?")
        CommitBtn=Button(WinControls,text="COMMIT INSERTION",font=("Liberation Sans",9,"bold"),bg="green",fg="white",command=fetchInputs,bd=1)
        WinTitlePag.pack(side=TOP)
        WinContents.pack(side=TOP)
        WinControls.pack(side=BOTTOM)
        WindowTitle.place(x=20,y=150)
        infStng1.place(x=20,y=20)
        infStng2.place(x=20,y=100)
        MfgrIDTex.place(x=20,y=160)
        MfgrIDBox.place(x=20,y=180)
        CosIndTex.place(x=140,y=160)
        CosIndBox.place(x=140,y=180)
        MfgNamTex.place(x=20,y=200)
        MfgNamBox.place(x=20,y=220)
        CuntryTex.place(x=20,y=240)
        CuntryBox.place(x=20,y=260)
        UseRevTex.place(x=270,y=160)
        Rate5Star.place(x=270,y=180)
        Rate4Star.place(x=270,y=200)
        Rate3Star.place(x=270,y=220)
        Rate2Star.place(x=270,y=240)
        Rate1Star.place(x=270,y=260)
        AvbRevTex.place(x=400,y=160)
        Avbl5Star.place(x=400,y=180)
        Avbl4Star.place(x=400,y=200)
        Avbl3Star.place(x=400,y=220)
        Avbl2Star.place(x=400,y=240)
        Avbl1Star.place(x=400,y=260)
        OverCount.place(x=510,y=160)
        IsAntiPytic.place(x=510,y=180)
        IsAnalgesic.place(x=510,y=200)
        IsAntiSeptc.place(x=510,y=220)
        Physician.place(x=660,y=160)
        IsAntiBiotc.place(x=660,y=180)
        IsTranquilz.place(x=660,y=200)
        IsMoodStabz.place(x=660,y=220)
        IsStimulant.place(x=660,y=240)
        CommitBtn.place(x=20,y=5)
    except Exception as e:
        msgbox.showinfo("Connection Failed!","Creation/Insertion failed due to not being able to connect. "+str(e))

def creatRecordToWarehouse():
    try:
        fileObject=open("connCache.txt","r")
        connectStr=fileObject.read()
        fileObject.close()
        connectArr=connectStr.split(" ")
        print(connectArr)
        uriVal,usrVal,pwdVal,dbsVal=str(connectArr[0]),str(connectArr[1]),str(connectArr[2]),str(connectArr[3])
        focus=mysql.connector.connect(host=uriVal,user=usrVal,passwd=pwdVal,database=dbsVal)
        curs=focus.cursor()
        def fetchInputs():
            ReltionNam="TestWarehouse"
            InveID=InveIDBox.get()
            MediID=MediIDBox.get()
            Avblty=AvbltyBox.get()
            DatMfg=DatMfgBox.get()
            DatExp=DatExpBox.get()
            curs=focus.cursor()
            try:
                taskComp="insert into "+ReltionNam+"(InvID,WareMedID,StckLimit,MfgWareDt,ExpWareDt) values('"+InveID+"', '"+MediID+"', "+str(Avblty)+", '"+str(DatMfg)+"', '"+str(DatExp)+"')"
                print(taskComp)
                curs.execute(taskComp)
                focus.commit()
                msgbox.showinfo("Creation/Insertion Successful","Creation and insertion of 1 record(s) in the Type table was peformed successfully!")
                createRecWindow.destroy()
            except Exception as e:
                msgbox.showinfo("Creation/Insertion Failed","The client was unable to perform the creation and insertion functions. "+str(e))
        createRecWindow=Toplevel()
        createRecWindow.geometry("960x540")
        createRecWindow.resizable(0,0)
        createRecWindow.title("Create Records : Warehouse Table")
        createRecWindow.grab_set()
        WinTitlePag=Frame(createRecWindow,width=960,height=200,bd=1,relief="raise",bg="green")
        WinContents=Frame(createRecWindow,width=960,height=300,bd=1,relief="sunken")
        WinControls=Frame(createRecWindow,width=960,height=40,bd=1,relief="raise",bg="green")
        WindowTitle=Label(WinTitlePag,font=("Liberation Sans",20,"normal"),text="Create/Insert Records in Warehouse Table",bg="green",fg="white")
        infStng1=Label(WinContents,text="You are currently accessing the client software using administrator privileges which allows you to potentially create, insert, read, display, update, modify, revoke and delete records seamlessly. Once changes are made and committed, rollback is not possible so you are requested to use some discretion during the operations.",wraplength=450,font=('Liberation Sans',9,'normal'),fg="red",justify=LEFT)
        infStng2=Label(WinContents,text="You might want to keep in the enterprise relational schema in mind while creating and inserting data in the chosen relation. ASTERISK (*) denotes PRIMARY KEY and CAP (^) denotes REFERENCE KEY.",wraplength=450,font=('Liberation Sans',9,'normal'),justify=LEFT)
        InveIDTex=Label(WinContents,font=("Liberation Sans",9,"normal"),text="InvID*")
        InveIDBox=Entry(WinContents,font=("Liberation Sans",9,"normal"),width=10,bd=1,bg="white")
        MediIDTex=Label(WinContents,font=("Liberation Sans",9,"normal"),text="MedID^")
        MediIDBox=Entry(WinContents,font=("Liberation Sans",9,"normal"),width=10,bd=1,bg="white")
        AvbltyTex=Label(WinContents,font=("Liberation Sans",9,"normal"),text="Available")
        AvbltyBox=Entry(WinContents,font=("Liberation Sans",9,"normal"),width=10,bd=1,bg="white")
        DatMfgTex=Label(WinContents,font=("Liberation Sans",9,"normal"),text="Date Of Manufacture")
        DatMfgBox=Entry(WinContents,font=("Liberation Sans",9,"normal"),width=36,bd=1,bg="white")
        DatExpTex=Label(WinContents,font=("Liberation Sans",9,"normal"),text="Date Of Expiry")
        DatExpBox=Entry(WinContents,font=("Liberation Sans",9,"normal"),width=36,bd=1,bg="white")
        CommitBtn=Button(WinControls,text="COMMIT INSERTION",font=("Liberation Sans",9,"bold"),bg="green",fg="white",command=fetchInputs,bd=1)
        WinTitlePag.pack(side=TOP)
        WinContents.pack(side=TOP)
        WinControls.pack(side=BOTTOM)
        WindowTitle.place(x=20,y=150)
        infStng1.place(x=20,y=20)
        infStng2.place(x=20,y=100)
        InveIDTex.place(x=20,y=160)
        InveIDBox.place(x=20,y=180)
        MediIDTex.place(x=110,y=160)
        MediIDBox.place(x=110,y=180)
        AvbltyTex.place(x=200,y=160)
        AvbltyBox.place(x=200,y=180)
        DatMfgTex.place(x=20,y=200)
        DatMfgBox.place(x=20,y=220)
        DatExpTex.place(x=20,y=240)
        DatExpBox.place(x=20,y=260)
        CommitBtn.place(x=20,y=5)
    except Exception as e:
        msgbox.showinfo("Connection Failed!","Creation/Insertion failed due to not being able to connect. "+str(e))

def creatRecord():
    createRecWindow=Toplevel()
    createRecWindow.geometry("960x540")
    createRecWindow.resizable(0,0)
    createRecWindow.title("Create Records")
    createRecWindow.grab_set()
    WinTitlePag=Frame(createRecWindow,width=960,height=200,bd=1,relief="raise",bg="green")
    WinContents=Frame(createRecWindow,width=960,height=300,bd=1,relief="sunken")
    WinControls=Frame(createRecWindow,width=960,height=40,bd=1,relief="raise",bg="green")
    WindowTitle=Label(WinTitlePag,font=("Liberation Sans",20,"normal"),text="Create & Insert New Records",bg="green",fg="white")
    infStng1=Label(WinContents,text="You are currently accessing the client software using administrator privileges which allows you to potentially create, insert, read, display, update, modify, revoke and delete records seamlessly. Once changes are made and committed, rollback is not possible so you are requested to use some discretion during the operations.",wraplength=450,font=('Liberation Sans',9,'normal'),fg="red",justify=LEFT)
    infStng2=Label(WinContents,text="In order to be able to view or make any changes on the table, it is essential to let know which relation you are interested in. Select from the given list of tables to continue.",wraplength=450,font=('Liberation Sans',9,'normal'),justify=LEFT)
    MedRelTex=Label(WinContents,font=("Liberation Sans",9,"italic"),text="For Medicines")
    MedRelBox=Button(WinContents,font=("Liberation Sans",9,"bold"),text="MEDICINE",width=15,height=1,fg="white",bg="green",command=creatRecordToMedicine,bd=1)
    WarRelTex=Label(WinContents,font=("Liberation Sans",9,"italic"),text="For Warehouses")
    WarRelBox=Button(WinContents,font=("Liberation Sans",9,"bold"),text="WAREHOUSE",width=15,height=1,fg="white",bg="green",command=creatRecordToWarehouse,bd=1)
    MfgRelTex=Label(WinContents,font=("Liberation Sans",9,"italic"),text="For Manufacturers")
    MfgRelBox=Button(WinContents,font=("Liberation Sans",9,"bold"),text="MANUFACTURER",width=15,height=1,fg="white",bg="green",command=creatRecordToManufacts,bd=1)
    MtyRelTex=Label(WinContents,font=("Liberation Sans",9,"italic"),text="For MedicineTypes")
    MtyRelBox=Button(WinContents,font=("Liberation Sans",9,"bold"),text="MEDICINETYPE",width=15,height=1,fg="white",bg="green",command=creatRecordToTypes,bd=1)
    WinTitlePag.pack(side=TOP)
    WinContents.pack(side=TOP)
    WinControls.pack(side=BOTTOM)
    WindowTitle.place(x=20,y=150)
    infStng1.place(x=20,y=20)
    infStng2.place(x=20,y=100)
    MedRelTex.place(x=20,y=160)
    MedRelBox.place(x=20,y=180)
    MtyRelTex.place(x=20,y=220)
    MtyRelBox.place(x=20,y=240)
    WarRelTex.place(x=160,y=160)
    WarRelBox.place(x=160,y=180)
    MfgRelTex.place(x=160,y=220)
    MfgRelBox.place(x=160,y=240)

def updatRecordToMedicine():
    try:
        fileObject=open("connCache.txt","r")
        connectStr=fileObject.read()
        fileObject.close()
        connectArr=connectStr.split(" ")
        print(connectArr)
        uriVal,usrVal,pwdVal,dbsVal=str(connectArr[0]),str(connectArr[1]),str(connectArr[2]),str(connectArr[3])
        focus=mysql.connector.connect(host=uriVal,user=usrVal,passwd=pwdVal,database=dbsVal)
        curs=focus.cursor()
        selectedClass=StringVar()
        def selectType():
            medClass=["0","IsAntiPytc","IsAnalGesc","IsAntiBiot","IsAntiSept","IsMoodStab","IsStimulan","IsTranquil"]
            selectedClass=str(medClass[int(var.get())])
            print(selectedClass)
            fileObject=open("medClassCache.txt","w")
            fileObject.write(selectedClass)
            fileObject.close
        def fetchInputs():
            fileObject=open("medClassCache.txt","r")
            selectedClass=fileObject.read()
            fileObject.close()
            print(selectedClass)
            IsAntiPytc,IsAnalGesc,IsAntiBiot,IsAntiSept,IsMoodStab,IsStimulan,IsTranquil=0,0,0,0,0,0,0
            ReltionNam="TestMedicines"
            MIDPre=MIDPreBox.get()
            MedicineID=MediIDBox.get()
            ManufactID=MfgIDBox.get()
            MediTypeID=TypeIDBox.get()
            MediciName=MedNamBox.get()
            DateOfMfgr=MfgDatBox.get()
            DateOfExpr=ExpDatBox.get()
            if (selectedClass=="IsAntiPytc"):
                IsAntiPytc=1
            elif (selectedClass=="IsAnalGesc"):
                IsAnalGesc=1
            elif (selectedClass=="IsAntiBiot"):
                IsAntiBiot=1
            elif (selectedClass=="IsAntiSept"):
                IsAntiSept=1
            elif (selectedClass=="IsMoodStab"):
                IsMoodStab=1
            elif (selectedClass=="IsStimulan"):
                IsStimulan=1
            elif (selectedClass=="IsTranquil"):
                IsTranquil=1
            curs=focus.cursor()
            try:
                updateMediID,updateMedNam,updateMedTypID,updateMedMfgID,updateDatMfg,updateDatExp="","","","","",""
                updateAntiPytc,updateAnalGesc,updateAntiBiot,updateAntiSept,updateMoodStab,updateStimulan,updateTranquil="","","","","","",""
                if (MedicineID!=''):
                    updateMediID="MedicineID='"+MedicineID+"'"
                    taskComp="update "+ReltionNam+" set "+updateMediID+" where MedicineID='"+MIDPre+"'"
                    print(taskComp)
                    curs.execute(taskComp)
                    focus.commit()
                if (MediciName!=''):
                    updateMedNam="MedName='"+MediciName+"'"
                    taskComp="update "+ReltionNam+" set "+updateMedNam+" where MedicineID='"+MIDPre+"'"
                    print(taskComp)
                    curs.execute(taskComp)
                    focus.commit()
                if (MediTypeID!=''):
                    updateMedTypID="MedTypeID='"+MediTypeID+"'"
                    taskComp="update "+ReltionNam+" set "+updateMedTypID+" where MedicineID='"+MIDPre+"'"
                    print(taskComp)
                    curs.execute(taskComp)
                    focus.commit()
                if (ManufactID!=''):
                    updateMedMfgID="MedMfgrID='"+ManufactID+"'"
                    taskComp="update "+ReltionNam+" set "+updateMedMfgID+" where MedicineID='"+MIDPre+"'"
                    print(taskComp)
                    curs.execute(taskComp)
                    focus.commit()
                if (DateOfMfgr!=''):
                    updateDatMfg="MfgDate='"+DateOfMfgr+"'"
                    taskComp="update "+ReltionNam+" set "+updateDatMfg+" where MedicineID='"+MIDPre+"'"
                    print(taskComp)
                    curs.execute(taskComp)
                    focus.commit()
                if (DateOfExpr!=''):
                    updateDatExp="ExpDate='"+DateOfExpr+"'"
                    taskComp="update "+ReltionNam+" set "+updateDatExp+" where MedicineID='"+MIDPre+"'"
                    print(taskComp)
                    curs.execute(taskComp)
                    focus.commit()
                if (IsAntiPytc!=''):
                    updateAntiPytc="IsAntiPytc='"+str(IsAntiPytc)+"'"
                    taskComp="update "+ReltionNam+" set "+updateAntiPytc+" where MedicineID='"+MIDPre+"'"
                    print(taskComp)
                    curs.execute(taskComp)
                    focus.commit()
                if (IsAnalGesc!=''):
                    updateAnalGesc="IsAnalGesc='"+str(IsAnalGesc)+"'"
                    taskComp="update "+ReltionNam+" set "+updateAnalGesc+" where MedicineID='"+MIDPre+"'"
                    print(taskComp)
                    curs.execute(taskComp)
                    focus.commit()
                if (IsAntiBiot!=''):
                    updateAntiBiot="IsAntiBiot='"+str(IsAntiBiot)+"'"
                    taskComp="update "+ReltionNam+" set "+updateAntiBiot+" where MedicineID='"+MIDPre+"'"
                    print(taskComp)
                    curs.execute(taskComp)
                    focus.commit()
                if (IsAntiSept!=''):
                    updateAntiSept="IsAntiSept='"+str(IsAntiSept)+"'"
                    taskComp="update "+ReltionNam+" set "+updateAntiSept+" where MedicineID='"+MIDPre+"'"
                    print(taskComp)
                    curs.execute(taskComp)
                    focus.commit()
                if (IsMoodStab!=''):
                    updateMoodStab="IsMoodStab='"+str(IsMoodStab)+"'"
                    taskComp="update "+ReltionNam+" set "+updateMoodStab+" where MedicineID='"+MIDPre+"'"
                    print(taskComp)
                    curs.execute(taskComp)
                    focus.commit()
                if (IsStimulan!=''):
                    updateStimulan="IsStimulan='"+str(IsStimulan)+"'"
                    taskComp="update "+ReltionNam+" set "+updateStimulan+" where MedicineID='"+MIDPre+"'"
                    print(taskComp)
                    curs.execute(taskComp)
                    focus.commit()
                if (IsTranquil!=''):
                    updateTranquil="IsTranquil='"+str(IsTranquil)+"'"
                    taskComp="update "+ReltionNam+" set "+updateTranquil+" where MedicineID='"+MIDPre+"'"
                    print(taskComp)
                    curs.execute(taskComp)
                    focus.commit()
                msgbox.showinfo("Updation Successful","Creation and insertion of 1 record(s) in the Medicine table was peformed successfully!")
                createRecWindow.destroy()
            except Exception as e:
                msgbox.showinfo("Creation/Insertion Failed","The client was unable to perform the creation and insertion functions. "+str(e))

        createRecWindow=Toplevel()
        createRecWindow.geometry("960x540")
        createRecWindow.resizable(0,0)
        createRecWindow.title("Update Records : Medicine Table")
        createRecWindow.grab_set()
        WinTitlePag=Frame(createRecWindow,width=960,height=200,bd=1,relief="raise",bg="green")
        WinContents=Frame(createRecWindow,width=960,height=300,bd=1,relief="sunken")
        WinControls=Frame(createRecWindow,width=960,height=40,bd=1,relief="raise",bg="green")
        WindowTitle=Label(WinTitlePag,font=("Liberation Sans",20,"normal"),text="Update Records in Medicine Table",bg="green",fg="white")
        infStng1=Label(WinContents,text="You are currently accessing the client software using administrator privileges which allows you to potentially create, insert, read, display, update, modify, revoke and delete records seamlessly. Once changes are made and committed, rollback is not possible so you are requested to use some discretion during the operations.",wraplength=450,font=('Liberation Sans',9,'normal'),fg="red",justify=LEFT)
        olderInt=Label(WinContents,text="PREDICATE",wraplength=450,font=('Liberation Sans',9,'bold'),fg="black",justify=LEFT)
        oldrDesc=Label(WinContents,text="Primary Key",wraplength=450,font=('Liberation Sans',9,'italic'),fg="black",justify=LEFT)
        newerInt=Label(WinContents,text="UPDATE NOW",wraplength=450,font=('Liberation Sans',9,'bold'),fg="black",justify=LEFT)
        newrDesc=Label(WinContents,text="Leave EMPTY for NO CHANGE to occur",wraplength=450,font=('Liberation Sans',9,'italic'),fg="black",justify=LEFT)
        MIDPreTex=Label(WinContents,font=("Liberation Sans",9,"normal"),text="Medi ID*")
        MIDPreBox=Entry(WinContents,font=("Liberation Sans",9,"normal"),width=10,bd=1,bg="white")
        MedNamTex=Label(WinContents,font=("Liberation Sans",9,"normal"),text="Medicine Name")
        MedNamBox=Entry(WinContents,font=("Liberation Sans",9,"normal"),width=30,bd=1,bg="white")
        MediIDTex=Label(WinContents,font=("Liberation Sans",9,"normal"),text="Medi ID*")
        MediIDBox=Entry(WinContents,font=("Liberation Sans",9,"normal"),width=10,bd=1,bg="white")
        TypeIDTex=Label(WinContents,font=("Liberation Sans",9,"normal"),text="Type ID^")
        TypeIDBox=Entry(WinContents,font=("Liberation Sans",9,"normal"),width=10,bd=1,bg="white")
        MfgIDText=Label(WinContents,font=("Liberation Sans",9,"normal"),text="Mfgr ID^")
        MfgIDBox=Entry(WinContents,font=("Liberation Sans",9,"normal"),width=10,bd=1,bg="white")
        MfgDatTex=Label(WinContents,font=("Liberation Sans",9,"normal"),text="Date Of Manufacture")
        MfgDatBox=Entry(WinContents,font=("Liberation Sans",9,"normal"),width=30,bd=1,bg="white")
        ExpDatTex=Label(WinContents,font=("Liberation Sans",9,"normal"),text="Date Of Expiry")
        MfgDatBox=Entry(WinContents,font=("Liberation Sans",9,"normal"),width=30,bd=1,bg="white")
        ExpDatTex=Label(WinContents,font=("Liberation Sans",9,"normal"),text="Date Of Expiry")
        ExpDatBox=Entry(WinContents,font=("Liberation Sans",9,"normal"),width=30,bd=1,bg="white")
        OverCount=Label(WinContents,font=("Liberation Sans",9,"bold"),text="OVER-THE-COUNTER")
        Physician=Label(WinContents,font=("Liberation Sans",9,"bold"),text="PHYSICIAN ADVICE")
        IsAntiPytic=Radiobutton(WinContents,font=("Liberation Sans",9,"normal"),variable=var,value=1,command=selectType,text="Is Anti-Pyretic?")
        IsAnalgesic=Radiobutton(WinContents,font=("Liberation Sans",9,"normal"),variable=var,value=2,command=selectType,text="Is Analgesic?")
        IsAntiBiotc=Radiobutton(WinContents,font=("Liberation Sans",9,"normal"),variable=var,value=3,command=selectType,text="Is Anti-Biotic?")
        IsAntiSeptc=Radiobutton(WinContents,font=("Liberation Sans",9,"normal"),variable=var,value=4,command=selectType,text="Is Anti-Septic?")
        IsMoodStabz=Radiobutton(WinContents,font=("Liberation Sans",9,"normal"),variable=var,value=5,command=selectType,text="Is Mood Stabilizer?")
        IsStimulant=Radiobutton(WinContents,font=("Liberation Sans",9,"normal"),variable=var,value=6,command=selectType,text="Is Stimulant?")
        IsTranquilz=Radiobutton(WinContents,font=("Liberation Sans",9,"normal"),variable=var,value=7,command=selectType,text="Is Tranquilizer?")
        CommitBtn=Button(WinControls,text="COMMIT INSERTION",font=("Liberation Sans",9,"bold"),bg="green",fg="white",command=fetchInputs,bd=1)
        WinTitlePag.pack(side=TOP)
        WinContents.pack(side=TOP)
        WinControls.pack(side=BOTTOM)
        WindowTitle.place(x=20,y=150)
        infStng1.place(x=20,y=20)
        olderInt.place(x=20,y=120)
        oldrDesc.place(x=20,y=140)
        newerInt.place(x=120,y=120)
        newrDesc.place(x=120,y=140)
        MIDPreTex.place(x=20,y=160)
        MIDPreBox.place(x=20,y=180)
        MediIDTex.place(x=120,y=160)
        MediIDBox.place(x=120,y=180)
        MedNamTex.place(x=210,y=160)
        MedNamBox.place(x=210,y=180)
        TypeIDTex.place(x=120,y=200)
        TypeIDBox.place(x=120,y=220)
        MfgDatTex.place(x=210,y=200)
        MfgDatBox.place(x=210,y=220)
        MfgIDText.place(x=120,y=240)
        MfgIDBox.place(x=120,y=260)
        ExpDatTex.place(x=210,y=240)
        ExpDatBox.place(x=210,y=260)
        OverCount.place(x=440,y=160)
        IsAntiPytic.place(x=440,y=180)
        IsAnalgesic.place(x=440,y=200)
        IsAntiSeptc.place(x=440,y=220)
        Physician.place(x=590,y=160)
        IsAntiBiotc.place(x=590,y=180)
        IsTranquilz.place(x=590,y=200)
        IsMoodStabz.place(x=590,y=220)
        IsStimulant.place(x=590,y=240)
        CommitBtn.place(x=20,y=5)
    except Exception as e:
        msgbox.showinfo("Connection Failed!","Creation/Insertion failed due to not being able to connect. "+str(e))

def updatRecordToWarehouse():
    try:
        fileObject=open("connCache.txt","r")
        connectStr=fileObject.read()
        fileObject.close()
        connectArr=connectStr.split(" ")
        print(connectArr)
        uriVal,usrVal,pwdVal,dbsVal=str(connectArr[0]),str(connectArr[1]),str(connectArr[2]),str(connectArr[3])
        focus=mysql.connector.connect(host=uriVal,user=usrVal,passwd=pwdVal,database=dbsVal)
        curs=focus.cursor()
        def fetchInputs():
            ReltionNam="TestWarehouse"
            InvPre=InvPreBox.get()
            InveID=InveIDBox.get()
            MediID=MediIDBox.get()
            Avblty=AvbltyBox.get()
            DatMfg=DatMfgBox.get()
            DatExp=DatExpBox.get()
            curs=focus.cursor()
            try:
                updateInveID,updateMediID,updateAvblty,updateDatMfg,updateDatExp="","","","",""
                if (InveID!=''):
                    updateInveID="InvID='"+InveID+"' "
                    taskComp="update "+ReltionNam+" set "+updateInveID+" where InvID='"+InvPre+"'"
                    print(taskComp)
                    curs.execute(taskComp)
                    focus.commit()
                if (MediID!=''):
                    updateMediID="WareMedID='"+MediID+"' "
                    taskComp="update "+ReltionNam+" set "+updateMediID+" where InvID='"+InvPre+"'"
                    print(taskComp)
                    curs.execute(taskComp)
                    focus.commit()
                if (Avblty!=''):
                    updateAvblty="StckLimit="+str(Avblty)+" "
                    taskComp="update "+ReltionNam+" set "+updateAvblty+" where InvID='"+InvPre+"'"
                    print(taskComp)
                    curs.execute(taskComp)
                    focus.commit()
                if (DatMfg!=''):
                    updateDatMfg="MfgWareDt='"+DatMfg+"' "
                    taskComp="update "+ReltionNam+" set "+updateDatMfg+" where InvID='"+InvPre+"'"
                    print(taskComp)
                    curs.execute(taskComp)
                    focus.commit()
                if (DatExp!=''):
                    updateDatExp="ExpWareDt='"+DatExp+"' "
                    taskComp="update "+ReltionNam+" set "+updateDatExp+" where InvID='"+InvPre+"'"
                    print(taskComp)
                    curs.execute(taskComp)
                    focus.commit()
                taskComp="update "+ReltionNam+" set "+updateInveID+updateMediID+updateAvblty+updateDatMfg+updateDatExp+" where InvID='"+InvPre+"'"
                msgbox.showinfo("Updation Successful","Updation of 1 record(s) in the Warehouse table was peformed successfully!")
                createRecWindow.destroy()
            except Exception as e:
                msgbox.showinfo("Updation Failed","The client was unable to perform the creation and insertion functions. "+str(e))

        createRecWindow=Toplevel()
        createRecWindow.geometry("960x540")
        createRecWindow.resizable(0,0)
        createRecWindow.title("Update Records : Warehouse Table")
        createRecWindow.grab_set()
        WinTitlePag=Frame(createRecWindow,width=960,height=200,bd=1,relief="raise",bg="green")
        WinContents=Frame(createRecWindow,width=960,height=300,bd=1,relief="sunken")
        WinControls=Frame(createRecWindow,width=960,height=40,bd=1,relief="raise",bg="green")
        WindowTitle=Label(WinTitlePag,font=("Liberation Sans",20,"normal"),text="Update Records in Warehouse Table",bg="green",fg="white")
        infStng1=Label(WinContents,text="You are currently accessing the client software using administrator privileges which allows you to potentially create, insert, read, display, update, modify, revoke and delete records seamlessly. Once changes are made and committed, rollback is not possible so you are requested to use some discretion during the operations.",wraplength=450,font=('Liberation Sans',9,'normal'),fg="red",justify=LEFT)
        olderInt=Label(WinContents,text="PREDICATE",wraplength=450,font=('Liberation Sans',9,'bold'),fg="black",justify=LEFT)
        oldrDesc=Label(WinContents,text="Primary Key",wraplength=450,font=('Liberation Sans',9,'italic'),fg="black",justify=LEFT)
        newerInt=Label(WinContents,text="UPDATE NOW",wraplength=450,font=('Liberation Sans',9,'bold'),fg="black",justify=LEFT)
        newrDesc=Label(WinContents,text="Leave EMPTY for NO CHANGE to occur",wraplength=450,font=('Liberation Sans',9,'italic'),fg="black",justify=LEFT)
        InvPreTex=Label(WinContents,font=("Liberation Sans",9,"normal"),text="InvID*")
        InvPreBox=Entry(WinContents,font=("Liberation Sans",9,"normal"),width=10,bd=1,bg="white")
        InveIDTex=Label(WinContents,font=("Liberation Sans",9,"normal"),text="InvID*")
        InveIDBox=Entry(WinContents,font=("Liberation Sans",9,"normal"),width=10,bd=1,bg="white")
        MediIDTex=Label(WinContents,font=("Liberation Sans",9,"normal"),text="MedID^")
        MediIDBox=Entry(WinContents,font=("Liberation Sans",9,"normal"),width=10,bd=1,bg="white")
        AvbltyTex=Label(WinContents,font=("Liberation Sans",9,"normal"),text="Available")
        AvbltyBox=Entry(WinContents,font=("Liberation Sans",9,"normal"),width=10,bd=1,bg="white")
        DatMfgTex=Label(WinContents,font=("Liberation Sans",9,"normal"),text="Date Of Manufacture")
        DatMfgBox=Entry(WinContents,font=("Liberation Sans",9,"normal"),width=36,bd=1,bg="white")
        DatExpTex=Label(WinContents,font=("Liberation Sans",9,"normal"),text="Date Of Expiry")
        DatExpBox=Entry(WinContents,font=("Liberation Sans",9,"normal"),width=36,bd=1,bg="white")
        CommitBtn=Button(WinControls,text="COMMIT INSERTION",font=("Liberation Sans",9,"bold"),bg="green",fg="white",command=fetchInputs,bd=1)
        WinTitlePag.pack(side=TOP)
        WinContents.pack(side=TOP)
        WinControls.pack(side=BOTTOM)
        WindowTitle.place(x=20,y=150)
        infStng1.place(x=20,y=20)
        olderInt.place(x=20,y=120)
        oldrDesc.place(x=20,y=140)
        newerInt.place(x=120,y=120)
        newrDesc.place(x=120,y=140)
        InvPreTex.place(x=20,y=160)
        InvPreBox.place(x=20,y=180)
        InveIDTex.place(x=120,y=160)
        InveIDBox.place(x=120,y=180)
        MediIDTex.place(x=210,y=160)
        MediIDBox.place(x=210,y=180)
        AvbltyTex.place(x=300,y=160)
        AvbltyBox.place(x=300,y=180)
        DatMfgTex.place(x=120,y=200)
        DatMfgBox.place(x=120,y=220)
        DatExpTex.place(x=120,y=240)
        DatExpBox.place(x=120,y=260)
        CommitBtn.place(x=20,y=5)
    except Exception as e:
        msgbox.showinfo("Connection Failed!","Creation/Insertion failed due to not being able to connect. "+str(e))

def updatRecord():
    createRecWindow=Toplevel()
    createRecWindow.geometry("960x540")
    createRecWindow.resizable(0,0)
    createRecWindow.title("Create Records")
    createRecWindow.grab_set()
    WinTitlePag=Frame(createRecWindow,width=960,height=200,bd=1,relief="raise",bg="green")
    WinContents=Frame(createRecWindow,width=960,height=300,bd=1,relief="sunken")
    WinControls=Frame(createRecWindow,width=960,height=40,bd=1,relief="raise",bg="green")
    WindowTitle=Label(WinTitlePag,font=("Liberation Sans",20,"normal"),text="Update Records",bg="green",fg="white")
    infStng1=Label(WinContents,text="You are currently accessing the client software using administrator privileges which allows you to potentially create, insert, read, display, update, modify, revoke and delete records seamlessly. Once changes are made and committed, rollback is not possible so you are requested to use some discretion during the operations.",wraplength=450,font=('Liberation Sans',9,'normal'),fg="red",justify=LEFT)
    infStng2=Label(WinContents,text="In order to be able to view or make any changes on the table, it is essential to let know which relation you are interested in. Select from the given list of tables to continue.",wraplength=450,font=('Liberation Sans',9,'normal'),justify=LEFT)
    MedRelTex=Label(WinContents,font=("Liberation Sans",9,"italic"),text="For Medicines")
    MedRelBox=Button(WinContents,font=("Liberation Sans",9,"bold"),text="MEDICINE",width=15,height=1,fg="white",bg="green",command=updatRecordToMedicine,bd=1)
    WarRelTex=Label(WinContents,font=("Liberation Sans",9,"italic"),text="For Warehouses")
    WarRelBox=Button(WinContents,font=("Liberation Sans",9,"bold"),text="WAREHOUSE",width=15,height=1,fg="white",bg="green",command=updatRecordToWarehouse,bd=1)
    #MfgRelTex=Label(WinContents,font=("Liberation Sans",9,"italic"),text="For Manufacturers")
    #MfgRelBox=Button(WinContents,font=("Liberation Sans",9,"bold"),text="MANUFACTURER",width=15,height=1,fg="white",bg="green",command=creatRecordToManufacts,bd=1)
    #MtyRelTex=Label(WinContents,font=("Liberation Sans",9,"italic"),text="For MedicineTypes")
    #MtyRelBox=Button(WinContents,font=("Liberation Sans",9,"bold"),text="MEDICINETYPE",width=15,height=1,fg="white",bg="green",command=creatRecordToTypes,bd=1)
    WinTitlePag.pack(side=TOP)
    WinContents.pack(side=TOP)
    WinControls.pack(side=BOTTOM)
    WindowTitle.place(x=20,y=150)
    infStng1.place(x=20,y=20)
    infStng2.place(x=20,y=100)
    MedRelTex.place(x=20,y=160)
    MedRelBox.place(x=20,y=180)
    #MtyRelTex.place(x=20,y=220)
    #MtyRelBox.place(x=20,y=240)
    WarRelTex.place(x=160,y=160)
    WarRelBox.place(x=160,y=180)
    #MfgRelTex.place(x=160,y=220)
    #MfgRelBox.place(x=160,y=240)

def checkBalanc():
    summation=0
    try:
        fileObject=open("connCache.txt","r")
        connectStr=fileObject.read()
        fileObject.close()
        connectArr=connectStr.split(" ")
        print(connectArr)
        uriVal,usrVal,pwdVal,dbsVal=str(connectArr[0]),str(connectArr[1]),str(connectArr[2]),str(connectArr[3])
        focus=mysql.connector.connect(host=uriVal,user=usrVal,passwd=pwdVal,database=dbsVal)
        curs=focus.cursor()
        trytoask="select sum(EarnedCash) from TestProfitTab"
        curs.execute(trytoask)
        summation=curs.fetchall()[0][0]
    except Exception as e:
        msgbox.showinfo("Creation/Insertion Failed","The client was unable to perform the creation and insertion functions. "+str(e))

    createRecWindow=Toplevel()
    createRecWindow.geometry("960x540")
    createRecWindow.resizable(0,0)
    createRecWindow.title("Check Balance")
    createRecWindow.grab_set()
    WinTitlePag=Frame(createRecWindow,width=960,height=200,bd=1,relief="raise",bg="green")
    WinContents=Frame(createRecWindow,width=960,height=300,bd=1,relief="sunken")
    WinControls=Frame(createRecWindow,width=960,height=40,bd=1,relief="raise",bg="green")
    WindowTitle=Label(WinTitlePag,font=("Liberation Sans",20,"normal"),text="Check Balance",bg="green",fg="white")
    infStng1=Label(WinContents,text="You are currently accessing the client software using administrator privileges which allows you to potentially create, insert, read, display, update, modify, revoke and delete records seamlessly. Once changes are made and committed, rollback is not possible so you are requested to use some discretion during the operations.",wraplength=450,font=('Liberation Sans',9,'normal'),fg="red",justify=LEFT)
    infStng2=Label(WinContents,text="Here is the combined earning of all the pharmaceutical corporations which work under the PharmaDB service and sell products here. Contact your adminstrator for further details.",wraplength=450,font=('Liberation Sans',9,'normal'),justify=LEFT)    
    PriceHead=Label(WinContents,font=("Liberation Sans",9,"bold"),text="Total Earnings")
    PriceSign=Label(WinContents,font=("Liberation Sans",20,"normal"),text="Rs.")
    PriceData=Label(WinContents,font=("Liberation Sans",20,"normal"),text=summation)
    WinTitlePag.pack(side=TOP)
    WinContents.pack(side=TOP)
    WinControls.pack(side=BOTTOM)
    WindowTitle.place(x=20,y=150)
    infStng1.place(x=20,y=20)
    infStng2.place(x=20,y=100)
    PriceHead.place(x=20,y=170)
    PriceSign.place(x=20,y=190)
    PriceData.place(x=65,y=190)

def deletRecord():
    try:
        fileObject=open("connCache.txt","r")
        connectStr=fileObject.read()
        fileObject.close()
        connectArr=connectStr.split(" ")
        print(connectArr)
        uriVal,usrVal,pwdVal,dbsVal=str(connectArr[0]),str(connectArr[1]),str(connectArr[2]),str(connectArr[3])
        focus=mysql.connector.connect(host=uriVal,user=usrVal,passwd=pwdVal,database=dbsVal)
        curs=focus.cursor()

        def delMeds():
            ReltionNam="TestMedicines"
            MediID=DelMedBox.get()
            curs=focus.cursor()
            curs.execute("select * from TestMedicines")
            result=curs.fetchall()
            num,arr=len(result),[]
            for i in result:
                arr.append(i[0])
            print(arr)
            if MediID not in arr:
                msgbox.showinfo("Deletion Failed","The specified ID was not found in the table.")
                createRecWindow.destroy()
            else:
                try:
                    taskComp="delete from "+ReltionNam+" where MedicineID='"+MediID+"'"
                    print(taskComp)
                    curs.execute(taskComp)
                    focus.commit()
                    msgbox.showinfo("Deletion Successful","Deletion of 1 record(s) from the Medicine table was peformed successfully!")
                    createRecWindow.destroy()
                except Exception as e:
                    msgbox.showinfo("Deletion Failed","The client was unable to perform the deletion functions. "+str(e))

        def delMfgs():
            ReltionNam="TestManufacts"
            MfgrID=DelMfgBox.get()
            curs=focus.cursor()
            curs.execute("select * from TestManufacts")
            result=curs.fetchall()
            num,arr=len(result),[]
            for i in result:
                arr.append(i[0])
            print(arr)
            if MfgrID not in arr:
                msgbox.showinfo("Deletion Failed","The specified ID was not found in the table.")
                createRecWindow.destroy()
            else:
                try:
                    taskComp="delete from "+ReltionNam+" where MfgrID='"+MfgrID+"'"
                    print(taskComp)
                    curs.execute(taskComp)
                    focus.commit()
                    msgbox.showinfo("Deletion Successful","Deletion of 1 record(s) from the Manufacturer table was peformed successfully!")
                    createRecWindow.destroy()
                except Exception as e:
                    msgbox.showinfo("Deletion Failed","The client was unable to perform the deletion functions. "+str(e))

        def delWars():
            ReltionNam="TestWarehouse"
            InveID=DelWarBox.get()
            curs=focus.cursor()
            curs.execute("select * from TestWarehouse")
            result=curs.fetchall()
            num,arr=len(result),[]
            for i in result:
                arr.append(i[0])
            print(arr)
            if InveID not in arr:
                msgbox.showinfo("Deletion Failed","The specified ID was not found in the table.")
                createRecWindow.destroy()
            else:
                try:
                    taskComp="delete from "+ReltionNam+" where InvID='"+InveID+"'"
                    print(taskComp)
                    curs.execute(taskComp)
                    focus.commit()
                    msgbox.showinfo("Deletion Successful","Deletion of 1 record(s) from the Warehouse table was peformed successfully!")
                    createRecWindow.destroy()
                except Exception as e:
                    msgbox.showinfo("Deletion Failed","The client was unable to perform the deletion functions. "+str(e))

        def delTyps():
            ReltionNam="TestTypeClass"
            TypeID=DelTypBox.get()
            curs=focus.cursor()
            curs.execute("select * from TestManufacts")
            result=curs.fetchall()
            num,arr=len(result),[]
            for i in result:
                arr.append(i[0])
            print(arr)
            if TypeID not in arr:
                msgbox.showinfo("Deletion Failed","The specified ID was not found in the table.")
                createRecWindow.destroy()
            else:
                try:
                    taskComp="delete from "+ReltionNam+" where TypeID='"+TypeID+"'"
                    print(taskComp)
                    curs.execute(taskComp)
                    focus.commit()
                    msgbox.showinfo("Deletion Successful","Deletion of 1 record(s) from the Type table was peformed successfully!")
                    createRecWindow.destroy()
                except Exception as e:
                    msgbox.showinfo("Deletion Failed","The client was unable to perform the deletion functions. "+str(e))

        createRecWindow=Toplevel()
        createRecWindow.geometry("960x540")
        createRecWindow.resizable(0,0)
        createRecWindow.title("Create Records")
        createRecWindow.grab_set()
        WinTitlePag=Frame(createRecWindow,width=960,height=200,bd=1,relief="raise",bg="green")
        WinContents=Frame(createRecWindow,width=960,height=300,bd=1,relief="sunken")
        WinControls=Frame(createRecWindow,width=960,height=40,bd=1,relief="raise",bg="green")
        WindowTitle=Label(WinTitlePag,font=("Liberation Sans",20,"normal"),text="Delete Records",bg="green",fg="white")
        infStng1=Label(WinContents,text="You are currently accessing the client software using administrator privileges which allows you to potentially create, insert, read, display, update, modify, revoke and delete records seamlessly. Once changes are made and committed, rollback is not possible so you are requested to use some discretion during the operations.",wraplength=450,font=('Liberation Sans',9,'normal'),fg="red",justify=LEFT)
        infStng2=Label(WinContents,text="In order to be able to view or make any changes on the table, it is essential to let know which relation you are interested in. Select from the given list of tables to continue.",wraplength=450,font=('Liberation Sans',9,'normal'),justify=LEFT)
        FromWhere=Label(WinContents,font=("Liberation Sans",9,"bold"),text="From where do you wish to delete records?")
        DelMedTex=Label(WinContents,font=("Liberation Sans",9,"italic"),text="From Medicines")
        DelMedIDS=Label(WinContents,font=("Liberation Sans",9,"bold"),text="MediID*")
        DelMedBox=Entry(WinContents,font=("Liberation Sans",9,"normal"),width=10,bd=1,bg="white")
        DelMedBtn=Button(WinContents,text="DELETE",font=("Liberation Sans",9,"bold"),bg="red",fg="white",command=delMeds,bd=1)
        DelWarTex=Label(WinContents,font=("Liberation Sans",9,"italic"),text="From Warehouses")
        DelWarIDS=Label(WinContents,font=("Liberation Sans",9,"bold"),text="InveID*")
        DelWarBox=Entry(WinContents,font=("Liberation Sans",9,"normal"),width=10,bd=1,bg="white")
        DelWarBtn=Button(WinContents,text="DELETE",font=("Liberation Sans",9,"bold"),bg="red",fg="white",command=delWars,bd=1)
        DelMfgTex=Label(WinContents,font=("Liberation Sans",9,"italic"),text="From Manufacturers")
        DelMfgIDS=Label(WinContents,font=("Liberation Sans",9,"bold"),text="MfgrID*")
        DelMfgBox=Entry(WinContents,font=("Liberation Sans",9,"normal"),width=10,bd=1,bg="white")
        DelMfgBtn=Button(WinContents,text="DELETE",font=("Liberation Sans",9,"bold"),bg="red",fg="white",command=delMfgs,bd=1)
        DelTypTex=Label(WinContents,font=("Liberation Sans",9,"italic"),text="From Medicine Types")
        DelTypIDS=Label(WinContents,font=("Liberation Sans",9,"bold"),text="TypeID*")
        DelTypBox=Entry(WinContents,font=("Liberation Sans",9,"normal"),width=10,bd=1,bg="white")
        DelTypBtn=Button(WinContents,text="DELETE",font=("Liberation Sans",9,"bold"),bg="red",fg="white",command=delTyps,bd=1)
        WinTitlePag.pack(side=TOP)
        WinContents.pack(side=TOP)
        WinControls.pack(side=BOTTOM)
        WindowTitle.place(x=20,y=150)
        infStng1.place(x=20,y=20)
        infStng2.place(x=20,y=100)
        FromWhere.place(x=20,y=160)
        DelMedTex.place(x=20,y=190)
        DelMedIDS.place(x=20,y=210)
        DelMedBox.place(x=20,y=230)
        DelMedBtn.place(x=20,y=255)
        DelWarTex.place(x=140,y=190)
        DelWarIDS.place(x=140,y=210)
        DelWarBox.place(x=140,y=230)
        DelWarBtn.place(x=140,y=255)
        DelMfgTex.place(x=260,y=190)
        DelMfgIDS.place(x=260,y=210)
        DelMfgBox.place(x=260,y=230)
        DelMfgBtn.place(x=260,y=255)
        DelTypTex.place(x=380,y=190)
        DelTypIDS.place(x=380,y=210)
        DelTypBox.place(x=380,y=230)
        DelTypBtn.place(x=380,y=255)
    except Exception as e:
        msgbox.showinfo("Connection Failed!","Creation/Insertion failed due to not being able to connect. "+str(e))

def RefreshMedi(searched):
    try:
        fileObject=open("connCache.txt","r")
        connectStr=fileObject.read()
        fileObject.close()
        connectArr=connectStr.split(" ")
        print(connectArr)
        uriVal,usrVal,pwdVal,dbsVal=str(connectArr[0]),str(connectArr[1]),str(connectArr[2]),str(connectArr[3])
        focus=mysql.connector.connect(host=uriVal,user=usrVal,passwd=pwdVal,database=dbsVal)
        curs=focus.cursor()
        result=[]
        if searched=='':
            curs.execute("select * from TestMedicines")
            result=curs.fetchall()
        else:
            MediIDLike="MedicineID like '"+searched+"%' or MedicineID like '%"+searched+"%' or MedicineID like '%"+searched+"'"
            MedNamLike="MedName like '"+searched+"%' or MedName like '%"+searched+"%' or MedName like '%"+searched+"'"
            MedTypLike="MedTypeID like '"+searched+"%' or MedTypeID like '%"+searched+"%' or MedTypeID like '%"+searched+"'"
            MfgDatLike="MfgDate like '"+searched+"%' or MfgDate like '%"+searched+"%' or MfgDate like '%"+searched+"'"
            ExpDatLike="ExpDate like '"+searched+"%' or ExpDate like '%"+searched+"%' or ExpDate like '%"+searched+"'"
            trytoask="select * from TestMedicines where "+MediIDLike+" or "+MedNamLike+" or "+MedTypLike+" or "+MfgDatLike+" or "+ExpDatLike
            print(trytoask)
            curs.execute(trytoask)
            result=curs.fetchall()
        return result
    except Exception as e:
        msgbox.showinfo("Fatal Error","The client was unable to retrieve records from the table. "+str(e))

def RefreshWare(searched):
    try:
        fileObject=open("connCache.txt","r")
        connectStr=fileObject.read()
        fileObject.close()
        connectArr=connectStr.split(" ")
        print(connectArr)
        uriVal,usrVal,pwdVal,dbsVal=str(connectArr[0]),str(connectArr[1]),str(connectArr[2]),str(connectArr[3])
        focus=mysql.connector.connect(host=uriVal,user=usrVal,passwd=pwdVal,database=dbsVal)
        curs=focus.cursor()
        result=[]
        if searched=='':
            curs.execute("select * from TestWarehouse")
            result=curs.fetchall()
        else:
            MediIDLike="WareMedID like '"+searched+"%' or WareMedID like '%"+searched+"%' or WareMedID like '%"+searched+"'"
            InveIDLike="InvID like '"+searched+"%' or InvID like '%"+searched+"%' or InvID like '%"+searched+"'"
            StkLimLike="StckLimit like '"+searched+"%' or StckLimit like '%"+searched+"%' or StckLimit like '%"+searched+"'"
            MfgDatLike="MfgWareDt like '"+searched+"%' or MfgWareDt like '%"+searched+"%' or MfgWareDt like '%"+searched+"'"
            ExpDatLike="ExpWareDt like '"+searched+"%' or ExpWareDt like '%"+searched+"%' or ExpWareDt like '%"+searched+"'"
            trytoask="select * from TestWarehouse where "+MediIDLike+" or "+InveIDLike+" or "+StkLimLike+" or "+MfgDatLike+" or "+ExpDatLike
            print(trytoask)
            curs.execute(trytoask)
            result=curs.fetchall()
        return result
    except Exception as e:
        msgbox.showinfo("Fatal Error","The client was unable to retrieve records from the table. "+str(e))

def RefreshType(searched):
    try:
        fileObject=open("connCache.txt","r")
        connectStr=fileObject.read()
        fileObject.close()
        connectArr=connectStr.split(" ")
        print(connectArr)
        uriVal,usrVal,pwdVal,dbsVal=str(connectArr[0]),str(connectArr[1]),str(connectArr[2]),str(connectArr[3])
        focus=mysql.connector.connect(host=uriVal,user=usrVal,passwd=pwdVal,database=dbsVal)
        curs=focus.cursor()
        result=[]
        if searched=='':
            curs.execute("select * from TestTypeClass")
            result=curs.fetchall()
        else:
            TypeIDLike="TypeID like '"+searched+"%' or TypeID like '%"+searched+"%' or TypeID like '%"+searched+"'"
            TypNamLike="TypeName like '"+searched+"%' or TypeName like '%"+searched+"%' or TypeName like '%"+searched+"'"
            DemAmtLike="DemandAmt like '"+searched+"%' or DemandAmt like '%"+searched+"%' or DemandAmt like '%"+searched+"'"
            AvbltyLike="AvbltyAmt like '"+searched+"%' or AvbltyAmt like '%"+searched+"%' or AvbltyAmt like '%"+searched+"'"
            StkLimLike="StockLimt like '"+searched+"%' or StockLimt like '%"+searched+"%' or StockLimt like '%"+searched+"'"
            trytoask="select * from TestTypeClass where "+TypeIDLike+" or "+TypNamLike+" or "+DemAmtLike+" or "+AvbltyLike+" or "+StkLimLike
            print(trytoask)
            curs.execute(trytoask)
            result=curs.fetchall()
        return result
    except Exception as e:
        msgbox.showinfo("Fatal Error","The client was unable to retrieve records from the table. "+str(e))

def RefreshMfgr(searched):
    try:
        fileObject=open("connCache.txt","r")
        connectStr=fileObject.read()
        fileObject.close()
        connectArr=connectStr.split(" ")
        print(connectArr)
        uriVal,usrVal,pwdVal,dbsVal=str(connectArr[0]),str(connectArr[1]),str(connectArr[2]),str(connectArr[3])
        focus=mysql.connector.connect(host=uriVal,user=usrVal,passwd=pwdVal,database=dbsVal)
        curs=focus.cursor()
        result=[]
        if searched=='':
            curs.execute("select * from TestManufacts")
            result=curs.fetchall()
        else:
            MfgrIDLike="MfgrID like '"+searched+"%' or MfgrID like '%"+searched+"%' or MfgrID like '%"+searched+"'"
            MfgNamLike="MfgName like '"+searched+"%' or MfgName like '%"+searched+"%' or MfgName like '%"+searched+"'"
            CuntryLike="Country like '"+searched+"%' or Country like '%"+searched+"%' or Country like '%"+searched+"'"
            AvbltyLike="IfAvail like '"+searched+"%' or IfAvail like '%"+searched+"%' or IfAvail like '%"+searched+"'"
            PricinLike="IfPrice like '"+searched+"%' or IfPrice like '%"+searched+"%' or IfPrice like '%"+searched+"'"
            UseRevLike="UserRev like '"+searched+"%' or UserRev like '%"+searched+"%' or UserRev like '%"+searched+"'"
            trytoask="select * from TestManufacts where "+MfgrIDLike+" or "+MfgNamLike+" or "+CuntryLike+" or "+AvbltyLike+" or "+PricinLike+" or "+UseRevLike
            print(trytoask)
            curs.execute(trytoask)
            result=curs.fetchall()
        return result
    except Exception as e:
        msgbox.showinfo("Fatal Error","The client was unable to retrieve records from the table. "+str(e))

def drawMedTable(where):
    def fetchInputs():
        searched=MedSearchBar.get()
        wipeTableStats(MedTable)
        for recs in RefreshMedi(searched):
            MedTable.insert('',0, text='', value = recs)

    MedSearchBar=Entry(where,font=("Liberation Sans",15,"normal"),width=15,bd=1,bg="white")
    MedSearchBar.place(x=620,y=40)
    SearchMedBtn=Button(where,text="FIND",font=("Liberation Sans",10,"bold"),bg="green",fg="white",command=fetchInputs,bd=1)
    SearchMedBtn.place(x=792,y=40)
    MediText=Label(where,font=("Liberation Sans",20,"normal"),fg="green",text="Medicines").place(x=10,y=25)
    MediDesc=Label(where,font=( "Liberation Sans",10,"normal"),fg="green",text="Relation about medicines").place(x=10,y=55)
    MedTable=ttk.Treeview(where)
    MedTable['show'] = 'headings'
    MedTable["column"]=("MedID","Titles","TypeID","MfgrID","MfgDate","ExpDate","AntiPytc","AnalGesc","AntiBiot","AntiSept","MoodStab","Stimulan","Tranquil")
    MedTable.column("MedID",width=50)
    MedTable.column("Titles",width=280)
    MedTable.column("TypeID",width=50)
    MedTable.column("MfgrID",width=50)
    MedTable.column("MfgDate",width=100)
    MedTable.column("ExpDate",width=100)
    MedTable.column("AntiPytc",width=30)
    MedTable.column("AnalGesc",width=30)
    MedTable.column("AntiBiot",width=30)
    MedTable.column("AntiSept",width=30)
    MedTable.column("MoodStab",width=30)
    MedTable.column("Stimulan",width=30)
    MedTable.column("Tranquil",width=30)
    MedTable.heading("MedID",text="MedID")
    MedTable.heading("Titles",text="Medicine Name")
    MedTable.heading("TypeID",text="TypID")
    MedTable.heading("MfgrID",text="MfgID")
    MedTable.heading("MfgDate",text="MfgDate")
    MedTable.heading("ExpDate",text="ExpDate")
    MedTable.heading("AntiPytc",text="AP")
    MedTable.heading("AnalGesc",text="AG")
    MedTable.heading("AntiBiot",text="AB")
    MedTable.heading("AntiSept",text="AS")
    MedTable.heading("MoodStab",text="MS")
    MedTable.heading("Stimulan",text="ST")
    MedTable.heading("Tranquil",text="TQ")
    MedTable.place(x=10,y=80)
    return MedTable

def drawMfgTable(where):
    def fetchInputs():
        searched=MfgSearchBar.get()
        wipeTableStats(MfgTable)
        for recs in RefreshMfgr(searched):
            MfgTable.insert('',0, text='', value = recs)

    MfgSearchBar=Entry(where,font=("Liberation Sans",15,"normal"),width=15,bd=1,bg="white")
    MfgSearchBar.place(x=620,y=325)
    SearchMfgBtn=Button(where,text="FIND",font=("Liberation Sans",10,"bold"),bg="green",fg="white",command=fetchInputs,bd=1)
    SearchMfgBtn.place(x=792,y=325)
    MfgrText=Label(where,font=("Liberation Sans",20,"normal"),fg="green",text="Manufacturers").place(x=10,y=310)
    MfgrDesc=Label(where,font=("Liberation Sans",10,"normal"),fg="green",text="Relation about manufacturers").place(x=10,y=340)
    MfgTable=ttk.Treeview(where)
    MfgTable['show'] = 'headings'
    MfgTable["column"]=("MfgrID","MfgName","Country","IfAvail","IfPrice","UserRev","MakesAnPy","MakesAnGe","MakesAnBi","MakesAnSe","MakesMoSt","MakesStim","MakesTran")
    MfgTable.column("MfgrID",width=50)
    MfgTable.column("MfgName",width=200)
    MfgTable.column("Country",width=90)
    MfgTable.column("IfAvail",width=90)
    MfgTable.column("IfPrice",width=100)
    MfgTable.column("UserRev",width=100)
    MfgTable.column("MakesAnPy",width=30)
    MfgTable.column("MakesAnGe",width=30)
    MfgTable.column("MakesAnBi",width=30)
    MfgTable.column("MakesAnSe",width=30)
    MfgTable.column("MakesMoSt",width=30)
    MfgTable.column("MakesStim",width=30)
    MfgTable.column("MakesTran",width=30)
    MfgTable.heading("MfgrID",text="MfgID")
    MfgTable.heading("MfgName",text="Manufacturer Name")
    MfgTable.heading("Country",text="Country")
    MfgTable.heading("IfAvail",text="Available")
    MfgTable.heading("IfPrice",text="Pricing")
    MfgTable.heading("UserRev",text="Review")
    MfgTable.heading("MakesAnPy",text="AP")
    MfgTable.heading("MakesAnGe",text="AG")
    MfgTable.heading("MakesAnBi",text="AB")
    MfgTable.heading("MakesAnSe",text="AS")
    MfgTable.heading("MakesMoSt",text="MS")
    MfgTable.heading("MakesStim",text="ST")
    MfgTable.heading("MakesTran",text="TQ")
    MfgTable.place(x=10,y=365)

def drawTypTable(where):
    def fetchInputs():
        searched=TypSearchBar.get()
        wipeTableStats(TypTable)
        for recs in RefreshType(searched):
            TypTable.insert('',0, text='', value = recs)

    TypSearchBar=Entry(where,font=("Liberation Sans",15,"normal"),width=10,bd=1,bg="white")
    TypSearchBar.place(x=1090,y=325)
    SearchTypBtn=Button(where,text="FIND",font=("Liberation Sans",10,"bold"),bg="green",fg="white",command=fetchInputs,bd=1)
    SearchTypBtn.place(x=1208,y=325)
    TypeTable=Label(where,font=("Liberation Sans",20,"normal"),fg="green",text="Types").place(x=865,y=310)
    TypeDesc=Label(where,font=("Liberation Sans",10,"normal"),fg="green",text="Relation about medicine types").place(x=865,y=340)
    TypTable=ttk.Treeview(where)
    TypTable['show'] = 'headings'
    TypTable["column"]=("TypeID","TypeName","DemandAmt","AvbltyAmt","StockLimt")
    TypTable.column("TypeID",width=50)
    TypTable.column("TypeName",width=150)
    TypTable.column("DemandAmt",width=50)
    TypTable.column("AvbltyAmt",width=50)
    TypTable.column("StockLimt",width=100)
    TypTable.heading("TypeID",text="TypID")
    TypTable.heading("TypeName",text="TypeName")
    TypTable.heading("DemandAmt",text="Dem.")
    TypTable.heading("AvbltyAmt",text="Avb.")
    TypTable.heading("StockLimt",text="Stock")
    TypTable.place(x=865,y=365)

def drawWarTable(where):
    def fetchInputs():
        searched=WarSearchBar.get()
        wipeTableStats(WarTable)
        for recs in RefreshWare(searched):
            WarTable.insert('',0, text='', value = recs)

    WarSearchBar=Entry(where,font=("Liberation Sans",15,"normal"),width=10,bd=1,bg="white")
    WarSearchBar.place(x=1090,y=40)
    SearchWarBtn=Button(where,text="FIND",font=("Liberation Sans",10,"bold"),bg="green",fg="white",command=fetchInputs,bd=1)
    SearchWarBtn.place(x=1208,y=40)
    WareText=Label(where,font=("Liberation Sans",20,"normal"),fg="green",text="Warehouse").place(x=865,y=25)
    WareDesc=Label(where,font=("Liberation Sans",10,"normal"),fg="green",text="Relation about availability").place(x=865,y=55)
    WarTable=ttk.Treeview(where)
    WarTable['show']='headings'
    WarTable["column"]=("InvID","MedID","StkLim","MfgDat","ExpDat")
    WarTable.column("InvID",width=50)
    WarTable.column("MedID",width=50)
    WarTable.column("StkLim",width=100)
    WarTable.column("MfgDat",width=100)
    WarTable.column("ExpDat",width=100)
    WarTable.heading("InvID",text="InvID")
    WarTable.heading("MedID",text="MedID")
    WarTable.heading("StkLim",text="StkLim")
    WarTable.heading("MfgDat",text="MfgDat")
    WarTable.heading("ExpDat",text="ExpDat")
    WarTable.place(x=865,y=80)

def mainWindow(where):
    #Layout
    OperationPage=Frame(where,width=1280,height=100,bd=1,relief="raise",bg="green")
    ViewTablePage=Frame(where,width=1280,height=600,bd=1,relief="sunken")
    StatusBarSect=Frame(where,width=1280,height=20,bd=1,relief="raise",bg="green")
    #Positioning
    OperationPage.pack(side=TOP)
    StatusBarSect.pack(side=BOTTOM)
    ViewTablePage.pack(side=LEFT)
    titleText=Label(OperationPage,font=("Liberation Sans",20,"normal"),text="PharmaDB Client",bg="green",fg="white").place(x=10,y=20)
    SubTextOP=Label(OperationPage,font=("Liberation Sans",10,"normal"),text="Don't do drugs, kid!",bg="green",fg="white").place(x=10,y=50)
    OperaText=Label(OperationPage,font=("Liberation Sans",10,"bold"),text="ADMINISTRATION CONTROL",bg="green",fg="white").place(x=500,y=20)
    URIConBtn=Button(OperationPage,font=("Liberation Sans",9,"bold"),text="CONNECT NOW",bg="green",bd=1,fg="white",width=15,height=1,command=getConnect).place(x=500,y=40)
    CreatBtn=Button(OperationPage,font=("Liberation Sans",9,"bold"),text="CREATE RECORDS",bg="green",bd=1,fg="white",width=15,height=1,command=creatRecord).place(x=640,y=40)
    UpdtBtn=Button(OperationPage,font=("Liberation Sans",9,"bold"),text="UPDATE RECORDS",bg="green",bd=1,fg="white",width=15,height=1,command=updatRecord).place(x=780,y=40)
    DlteBtn=Button(OperationPage,font=("Liberation Sans",9,"bold"),text="DELETE RECORDS",bg="green",bd=1,fg="white",width=15,height=1,command=deletRecord).place(x=920,y=40)
    StatBtn=Button(OperationPage,font=("Liberation Sans",9,"bold"),text="CHECK STATISTICS",bg="green",bd=1,fg="white",width=15,height=1,command=checkBalanc).place(x=1060,y=40)
    ExitBtn=Button(OperationPage,font=("Liberation Sans",9,"bold"),text="EXIT",bg="green",bd=1,fg="white",width=5,command=quitProgram,height=1).place(x=1200,y=40)
    predfre=Label(ViewTablePage,font=("Liberation Sans",9,"bold"),text="Run the search without any predicate to display all records. Find again to refresh cache.").place(x=10,y=0)
    StatTexOne=Label(StatusBarSect,font=("Liberation Sans",9,"normal"),text="Welcome to PharmaDB Client!",bg="green",fg="white").place(x=10,y=0)
    StatTexTwo=Label(StatusBarSect,font=("Liberation Sans",9,"bold"),text="READY",bg="green",fg="white").place(x=1220,y=0)
    drawMedTable(ViewTablePage)
    drawMfgTable(ViewTablePage)
    drawTypTable(ViewTablePage)
    drawWarTable(ViewTablePage)

mainWindow(OperationsWindow)

OperationsWindow.mainloop()