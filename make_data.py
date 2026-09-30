import json
from pathlib import Path
import sys
from PIL import Image
base=Path(__file__).resolve().parent
source_dir=Path(sys.argv[1]) if len(sys.argv)>1 else base/'originals'
out=base/'dist'; (out/'sources').mkdir(exist_ok=True)
rooms=[]
files={'SD0002':'01','SI0038':'02','SI0025':'03','SI0024':'04','SI0203':'05','SI0202':'06','SI0201':'07','SI0001':'08','SI0002':'09','SI0003':'10'}
names={'SD0002':'Mac-Pool','SI0038':'Windows-Pool','SI0025':'PC-Pool','SI0024':'PC-Pool','SI0203':'IT-Pool 1','SI0202':'IT-Pool 2','SI0201':'IT-Pool 3','SI0001':'IT-Pool 6','SI0002':'IT-Pool 5','SI0003':'IT-Pool 4'}
for rid,prefix in files.items():
 f=next(source_dir.glob(prefix+'-*.jpg')); im=Image.open(f)
 im=im.crop((78,234,1517,620)) if prefix in ['01','02'] else im.crop((0,int(im.height*.70),im.width,im.height))
 im.save(out/'sources'/f'{rid}.jpg',quality=93)
 rooms.append(dict(id=rid,name=names[rid],source=f'sources/{rid}.jpg',sourceFile=f.name[3:],coverageEnd='18:00' if prefix in ['01','02'] else ('19:30' if rid in ['SI0024','SI0025'] else '20:00'),tentative=prefix in ['01','02'],events=[]))
def add(rid,day,start,end,title,uncertain=False):
 r=next(r for r in rooms if r['id']==rid); r['events'].append(dict(id=f'{rid}-{day}-{start}',day=day,start=start,end=end,title=title,uncertain=uncertain))
def slot(rid,day,n,title):
 times=[('08:00','09:30'),('10:00','11:30'),('12:15','13:45'),('14:30','16:00'),('16:30','18:00'),('18:30','20:00')];add(rid,day,*times[n],title)
# Paper plans, weekdays ISO 1=Monday through 5=Friday.
for rid in ['SI0001','SI0002','SI0003','SI0201','SI0202','SI0203']:slot(rid,3,0,'Systemzeit')
plans={
'SI0203':{2:{2:'Datenbanken (Praktikum) · Gr. 3 · MI3',3:'Elektrotechnik / Messen-Steuern-Regeln für den Anlagenbau'},3:{2:'Fortgeschrittenes Datenmanagement · Big Data und Business Intelligence',3:'Fortgeschrittenes Datenmanagement · Big Data und Business Intelligence'},4:{3:'Wissenschaftliche Arbeitstechniken',4:'Wissenschaftliche Arbeitstechniken'}},
'SI0202':{1:{2:'Antriebe (Praktikum)',3:'Antriebe (Praktikum)'},2:{2:'Antriebe (Praktikum)',3:'Antriebe (Praktikum)'},3:{2:'Regelungstechnik für Maschinenbau (Praktikum)'},4:{3:'Wissenschaftliche Arbeitstechniken',4:'Wissenschaftliche Arbeitstechniken'}},
'SI0201':{1:{1:'Konstruktion',2:'Simulation anisotroper Leichtbauwerkstoffe',3:'Simulation anisotroper Leichtbauwerkstoffe',4:'Konstruktion und CAD'},2:{2:'Programmierung 3 (MI) (Praktikum) · Gr. 2 · MI3',3:'Regelungstechnik für Maschinenbau (Praktikum)',4:'Konstruktion'},3:{2:'Modellierung und Simulation mechatronischer Systeme (Praktikum)'},4:{0:'Regelungstechnik für Maschinenbau (Praktikum)',3:'CAE für Kunststofftechnik'}},
'SI0001':{1:{2:'Datenbanken (Praktikum) · Gr. 2 · TI3',3:'Programmierung 1 (I) (Vorlesung) · TI1/BBI1/BAT3',4:'Programmierung 1 (I) (Praktikum) · Gr. 2 · BAT3'},2:{0:'Datenbanken (Praktikum) · Gr. 1 · MI3',1:'Datenbanken (Praktikum) · Gr. 2 · MI3',2:'Informatik für Maschinenbau (AFE1/MB1A)'},3:{1:'Datenbanken (Praktikum) · Gr. 1 · TI3/BBI3',2:'Programmierung 3 (MI) (Praktikum) · Gr. 1 · MI3',3:'Programmierung 1 (I) (Vorlesung) · TI1/BBI1/BAT3',4:'Objektorientierte Analyse und Design (Praktikum) · MI'},4:{1:'Objektorientierte Analyse und Design (Praktikum) · MI',2:'Objektorientierte Analyse und Design (Praktikum) · MI',3:'Programmierung 1 (I) (Praktikum) · Gr. 1 · MI1',4:'Programmierung 1 (I) (Praktikum) · Gr. 2 · BAT3'},5:{0:'Programmierung 3 (MI) (Praktikum) · Gr. 3 · MI3',1:'Programmierung 1 (I) (Praktikum) · Gr. 2 · MI1',2:'Programmierung 1 (E/Me) (Praktikum) · E1/ME1',3:'Programmierung 1 (E/Me) (Praktikum) · E1/ME1'}},
'SI0002':{1:{1:'Informatikanwendungen · BMIN1',3:'Programmierung 3 (TI) (Praktikum) · Gr. 2 · TI3',4:'Programmierung 1 (I) (Praktikum) · Gr. 1 · TI1/BBI1'},2:{0:'Modellbildung und Simulation',1:'Robotersysteme',2:'Informatik für Maschinenbau (AFE1/MB1A)',3:'Algorithmen und Datenstrukturen (Praktikum) · MI2'},3:{1:'Programmierung 3 (TI) (Praktikum) · Gr. 1 · TI3',3:'Programmierung 1 (I) (Praktikum) · Gr. 2 · MI1'},4:{1:'Informatikanwendungen · BMIN1',3:'Software Architektur – Konzepte und Anwendungen (Praktikum) · MI',4:'Programmierung 1 (I) (Praktikum) · Gr. 1 · TI1/BBI1'},5:{2:'Programmierung 2 (I) (Praktikum) · MI · Gr. 2',3:'Programmierung 2 (I) (Praktikum) · MI · Gr. 1'}},
'SI0003':{2:{2:'Informatik für Maschinenbau (AFE1/MB1A)',4:'Programmierung 1 (I) (Praktikum) · Gr. 4 · MI1'},3:{3:'Programmierung 1 (I) (Praktikum) · Gr. 3 · MI1'},4:{3:'Programmierung 1 (I) (Praktikum) · Gr. 4 · MI1'},5:{1:'Programmierung 1 (I) (Praktikum) · Gr. 3 · MI1',3:'Grundlagen Programmierung und Mikrorechnersysteme'}},
'SI0025':{1:{2:'Digitale Assistenz',3:'Internet of Things / Industrie 4.0'},3:{1:'Grundlagen der KI',2:'Embedded Systems'},4:{1:'Verteilte Systeme',2:'Verteilte Systeme'},5:{2:'Embedded Systems'}},
'SI0024':{2:{0:'Betriebssysteme',4:'Parallele und verteilte Algorithmen'},3:{1:'Grundlagen der KI',4:'OOAD'},4:{1:'Betriebssysteme',2:'Systems Engineering',3:'Betriebssysteme'},5:{1:'Grundlagen der KI'}},
'SD0002':{1:{0:'3D-Anwendungen_PR',1:'3D-Anwendungen_PR',4:'MIS-PR'},2:{1:'MIS-PR'},3:{2:'UE&UED-PR',3:'UE&UED-PR'},4:{1:'SP&3D-Animation_PR',2:'SP&3D-Animation_PR'}},
'SI0038':{1:{4:'Audio-u-Videotech_PR'},2:{1:'MIS-PR',2:'MIS-PR',3:'Mod-Anim-3D_SV',4:'Mod-Anim-3D_PR'},3:{0:'GrdlProg_PR',1:'GrdlProg_PR',2:'SP&3D-Animation_PR',3:'Computergrafik_PR',4:'Audio-u-Videotech_PR'},4:{1:'RMA_PR',2:'RMA_PR',3:'RMA_PR',4:'Audio-u-Videotech_PR'},5:{2:'Computergrafik_PR'}}}
for rid,days in plans.items():
 for day,slots in days.items():
  for n,title in slots.items(): slot(rid,day,n,title)
add('SI0025',2,'11:00','11:30','Digitale Assistenz')
add('SI0025',1,'16:30','19:30','Internet of Things / Industrie 4.0')
add('SI0024',2,'11:00','11:30','Betriebssysteme')
add('SI0024',2,'18:00','19:30','Parallele und verteilte Algorithmen · genaue Zeit unleserlich',True)
add('SD0002',2,'16:30','19:30','Grdl-film-Gestalt_PR')
for r in rooms:r['events'].sort(key=lambda e:(e['day'],e['start']))
data={'sourceDate':'2026-09-30','timezone':'Europe/Berlin','recurrence':'weekly-assumption','rooms':sorted(rooms,key=lambda r:r['id'])}
(out/'data.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
(out/'data.js').write_text('window.ROOM_DATA = '+json.dumps(data,ensure_ascii=False)+';\n')
print({r['id']:len(r['events']) for r in rooms});print('Total',sum(len(r['events']) for r in rooms))
