from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.slider import Slider
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty,StringProperty
from kivy.app import runTouchApp
import time
from time import strftime
import datetime
import sqlite3
from kivy.clock import Clock
global gscore
global gname
global gdescpt
global glastpausedtime
global gcooltime
global gtotaltimetaken
global gstate
global greqmnts
global ginternet
global gwriteable
global greadable
global gotherreq
global instruction
global edit
global end
global start
global complete
gstate = False
ginternet = False
gwriteable = False
greadable = False
gotherreq = False
gscore = 0.0
global refresh 
refresh = 0
global tupcount
Window.softinput_mode="below_target"
class MainScreenManager(ScreenManager):
	pass
class CustomBoxLayout(BoxLayout):
	def editclick(self,instance):
		id=str(instance.parent.parent.ids.tid.text)
		print("edited")
	def endclick(self,instance):
		id=str(instance.parent.parent.ids.tid.text)
		dbupdate(id,"en")
		print("Ended")
	def completedclick(self,instance):
		id=str(instance.parent.parent.ids.tid.text)
		dbupdate(id,"c")
		print("completed")
		#name contains the task name
		#print(instance.parent.ids.name.text)
		
		#App.get_running_app().restart()
		#see below build method to see restart()

#Update the Data Base
def dbupdate(id,var):
	if (var=="c"):
		pass
	elif (var=="en"):
		print("ended")
		pass
		#MainScreen().on_stop()
	elif (var=="s"):
		MainScreen().start()
		print(id)
		pass
#def update_time(self,*args):
#		minutes, seconds = divmod(self.sw_seconds, 60)
#		self.ids.stopwatch.text = f'{int(minutes):02}:{int(seconds):02}'
#def on_start(self,*args):
#		self.sw_started=True
#		Clock.schedule_interval(self.update_time,1)		
#	def on_stop(self,*args):
#		sw_seconds=0
#		sw_started=False		

	
class CShowTask(BoxLayout):
	def pressed(self,*args):
		print("pressed")

class MainScreen(Screen):
	#number = NumericProperty()
	number = StringProperty()
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.seconds_counter=0
		self.number=str(datetime.timedelta(seconds=self.seconds_counter))
		Clock.schedule_interval(self.UpdateTime,1)

	def increment_time(self, interval):
		#self.number += 1
		self.seconds_counter += 1
		self.number=str(datetime.timedelta(seconds=self.seconds_counter))
	def start(self,instance):
		id=str(instance.parent.parent.ids.tid.text)
		Clock.schedule_interval(self.increment_time, 1)
		instance.disabled=True   
	def stop(self): 
		Clock.schedule(self.increment_time) 

	def UpdateTime(self,*args):
		cime=str(time.ctime())
		hour=cime[11:13]
		minute=cime[14:16]
		second=cime[17:19]
		self.ids.time_label.text=(hour+":"+minute+":"+second)
#	def on_start(self,*args):
#		Clock.schedule_interval(self.update_time,1)
#	def update_time(self,*args):
#		self.tseconds = self.tseconds + 1
#		cseconds=datetime.timedelta(seconds=self.tseconds)
#		self.ids.stopwatch.text=str(cseconds)
#	def on_stop(self,*args):
#		self.ids.stopwatch.text="00:00"
#		self.tseconds=0		
	
	
		
	
class MainScreenScrlBox(BoxLayout):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		global tupcount
		global records
		conn=sqlite3.connect("schedular.db")
		cur = conn.cursor()
		try:
			cur.execute("SELECT * FROM Tasks ORDER BY Score DESC")
		except:
			print("you have no records!")
		records=cur.fetchall()
		conn.commit()
		conn.close()
		tupcount=0
		for i in records:
			tupcount=tupcount+1			
		for tuple in records:
			score=tuple[1]
			name=tuple[2]
			Desc=tuple[3]
			instr=tuple[13]
			id=tuple[0]
			st=tuple[7]
			cooltime=tuple[5]
			if (st==1):
				state="COMPLETED"
			else:
				state="PAUSED"
			cl=CustomBoxLayout()
			cl.ids.name.text=str("[b]TaskName: [/b]"+name)
			cl.ids.scr.text=("[b]Score: [/b]"+str(int(score)))
			cl.ids.decs.text=("[b]Description: [/b]"+str(Desc))
			cl.ids.instr.text=("[b]Instructions:[/b]\n"+str(instr))
			cl.ids.tid.text=("[b]Id: [/b]"+str(id))
			cl.ids.state.text=("[b]"+state+"[/b]")
			if (st==1):
				cl.ids.state.color=(0,1,0,1)
			else:
				cl.ids.state.color=(1,0,0,1)
			cl.ids.cooldown.text=("[b]Cool Down: [/b]"+str(cooltime))
			self.add_widget(cl)
			
		
class BurgerScreen(Screen):
	pass

class TaskScreen(Screen):
	#It has a ScrollView, Boxtemplt and a popup under it
	def Refresh(self,*args):
		global refresh
		print("refresh!!!")
		print(refresh)
		refresh=1
		print(refresh)
	pass

class TaskScreenScrlBox(BoxLayout):
	#There is also a kv code for this layout
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		global tupcount
		global records
		conn=sqlite3.connect("schedular.db")
		cur = conn.cursor()
		try:
			cur.execute("SELECT * FROM Tasks")
		except:
			print("you have no records!")
		records=cur.fetchall()
		conn.commit()
		conn.close()
		tupcount=0
		for i in records:
			tupcount=tupcount+1			
		for tuple in records:
			score=tuple[1]
			name=tuple[2]
			Desc=tuple[3]
			id=tuple[0]
			st=tuple[7]
			cooltime=tuple[5]
			if (st==1):
				state="COMPLETED"
			else:
				state="PAUSED"
			cs=CShowTask()
			cs.ids.name.text=str("[b]TaskName: [/b]"+name)
			cs.ids.scr.text=("[b]Score: [/b]"+str(int(score)))
			cs.ids.decs.text=("[b]Description: [/b]"+str(Desc))
			cs.ids.tid.text=("[b]Id: [/b]"+str(id))
			cs.ids.state.text=("[b]"+state+"[/b]")
			if (st==1):
				cs.ids.state.color=(0,1,0,1)
			else:
				cs.ids.state.color=(1,0,0,1)
			cs.ids.cooldown.text=("[b]Cool Down: [/b]"+str(cooltime))
			self.add_widget(cs)
			pd=Label(text="",size_hint_y=None,height=20)
			self.add_widget(pd)
		Clock.schedule_interval(self.rcheck,(1))
		

	def DisTask(self,*args):
				# query part
		print("DisTask")
		global records
		for tuple in records:
			name=tuple[2]
			Desc=tuple[3]
			lb=Label(text="Task Name:"+name,size_hint_y=None,color=(0,0,0,1))
			lb1=Label(text="Desc:"+Desc,size_hint_y=None,color=(0,0,0,1))
			bt=Button(text="Edit",size_hint_y=None)
			self.add_widget(lb)
			self.add_widget(lb1)
			self.add_widget(bt)
				
	def rcheck(self,*args):
		global tupcount
		global refresh
		print("rcheck")
		count = tupcount
		if (refresh== 1 and refresh != 0):
			self.DisTask()
			print("For")
			refresh = 0
		else:
			pass			
	
class AddTaskScreen(Screen):
	
	def Internet_check(self,checkbox,value):
		global ginternet
		if (value ==True):
			ginternet=True
			print(ginternet)
		else:
			ginternet=False
			print(ginternet)
	def Readable_check(self,checkbox,value):
		global greadable
		if (value == True):
			greadable=True
		else:
			greadable=False
	def Writeable_check(self,checkbox,value):
		global gwriteable
		if (value == True):
			gwriteable=True
		else:
			gwriteable=False
	def OtherReq_check(self,checkbox,value):
		global gotherreq
		if (value == True):
			gotherreq=True
		else:
			gotherreq=False		

	def Create_New_Task(self,*args):
		global gstate
		gstate = False
		gname=self.Task_name.text
		gdescpt=self.Descpt.text
		greqmnts=self.Other.text
		ginstruction=self.Instr.text
		glastpausedtime=str(datetime.datetime.now())
		gcooltime=self.Time.text
		gtotaltimetaken="00:00:00"
		conn=sqlite3.connect("schedular.db")
		cur=conn.cursor()
		cur.execute("INSERT INTO Tasks (score,name,descpt,lastpausedtime,cooltime,totaltimetaken,state,reqmnts,internet,readable,writeable,otherreq,instruction) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",(gscore,gname,gdescpt,glastpausedtime,gcooltime,gtotaltimetaken,gstate,greqmnts,ginternet,greadable,gwriteable,gotherreq,ginstruction))
		conn.commit()
		conn.close()
		print("name:",gname)
		print("descpt:",gdescpt)
		print("reqmnts:",greqmnts)
		print("internet:",ginternet)
		print("readable:",greadable)
		print("writeable:",gwriteable)
		print("other:",gotherreq)	
		print("score:",gscore)
		print("instruction:",ginstruction)
		conn=sqlite3.connect("schedular.db")
		cur = conn.cursor()
		cur.execute("SELECT * FROM Tasks")
		records=cur.fetchall()
		conn.commit()
		conn.close()
		word = ''
		i = 0
		for record in records:
			word=f'{records[i]}'
			print('')
			print(word)
			i= i+1
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.Task_name=TextInput(text="",size_hint=(.9,.04),pos_hint={'x':.06,'y':.885})
		self.add_widget(self.Task_name)
		self.Time=TextInput(text="hh-mm-ss",size_hint=(.9,.04),pos_hint={'x':.06,'y':.75})
		self.add_widget(self.Time)
		self.Other=TextInput(text="",size_hint=(.9,.08),pos_hint={'x':.06,'y':.6355})
		self.add_widget(self.Other)
		self.Descpt=TextInput(text="",size_hint=(.9,.045),pos_hint={'x':.06,'y':.56})
		self.add_widget(self.Descpt)
		self.Instr=TextInput(text="",size_hint=(.9,0.19),pos_hint={'x':.06,'y':.34})
		self.add_widget(self.Instr)
			
		self.Slider= Slider(min=0,max=10,size_hint=(.9,.08),pos_hint={'x':.06,'y':.22})
		self.add_widget(self.Slider)
		
		self.scr=Label(text="0",size_hint=(.1,.1),pos_hint={'x':.45,'y':.25},color=(0,0,0,1))
		self.add_widget(self.scr)
		def OnSliderChange(instance,text):
			global gscore
			self.scr.text=str(int(text))
			gscore=float(text)
			print(gscore)
		self.Slider.bind(value=OnSliderChange)
			
class Scrolltest(GridLayout):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		b=Button(text="h",size_hint=(1,None))
		self.add_widget(b)	
		
class Scrltest(ScrollView):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		pass
		
class Scrltest2(BoxLayout):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		
		l=Label(text=(str("ge"*100)),text_size=(self.width,None),size_hint_y=None)
		self.add_widget(l)
			
				
first=Builder.load_file('first.kv')

class FirstApp(App):
	def build(self):
		global records
		Clock.schedule_interval(self.updt_tupcount,(1))
		conn=sqlite3.connect("Schedular.db")
		cur=conn.cursor()
		#Execute during start of program
		cur.execute("CREATE TABLE if not exists Tasks(tid INTEGER PRIMARY KEY AUTOINCREMENT,score real,name text,descpt text,lastpausedtime text,cooltime text,totaltimetaken text,state boolean,reqmnts text,internet boolean,readable boolean,writeable boolean,otherreq boolean,instruction text) ")
		conn.commit()
		conn.close()
		global tupcount
		conn=sqlite3.connect("schedular.db")
		cur = conn.cursor()
		try:
			cur.execute("SELECT * FROM Tasks")
		except:
			print("you have no records!")
		records=cur.fetchall()
		conn.commit()
		conn.close()
		tupcount=0
		for i in records:
			tupcount=tupcount+1
		return first
	#def restart(self):
#	       self.root.clear_widgets()
#	       self.stop()
#	       return FirstApp().run()
# This is out of build method
	def updt_tupcount(self,*args):
		global tupcount
		global records
		conn=sqlite3.connect("schedular.db")
		cur = conn.cursor()
		try:
			cur.execute("SELECT * FROM Tasks")
		except:
			print("you have no records!")
		records=cur.fetchall()
		conn.commit()
		conn.close()
		tupcount=0
		for i in records:
			tupcount=tupcount+1
		#print(tupcount)
if __name__ == '__main__':
    from kivy.core.window import Window
    from kivy.utils import get_color_from_hex
    from kivy.core.text import LabelBase
    Window.clearcolor = get_color_from_hex('#ffffff')
    FirstApp().run()
# #02242b greenish black