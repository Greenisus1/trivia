#!/usr/bin/env python3
"""Generated offline learning quiz: arithmetic, geometry, Python, words and logic."""
import curses,random
from ui import put,run
TOPICS=('Arithmetic','Geometry','Python basics','Word puzzles','Logic')
def questions(seed=0):
 rng=random.Random(seed);items=[]
 def add(topic,q,answer,wrong,explanation):
  options=[str(answer)]+[str(x) for x in wrong];rng.shuffle(options);items.append((topic,q,options,options.index(str(answer)),explanation))
 for a,b in ((4,7),(12,3),(9,8),(11,6)):
  add(0,f'{a} + {b} = ?',a+b,[a+b-1,a*b,a+b+2],'Add the two whole numbers.')
  add(1,f'Rectangle width {a}, height {b}: area?',a*b,[2*(a+b),a+b,a*b+1],'Area = width multiplied by height.')
  add(1,f'Square side {a}: perimeter?',4*a,[4*a-1,2*a,4*a+1],'A square has four equal sides.')
 for text in ('snake','pizza','planet','learning'):
  add(3,f'How many letters in "{text}"?',len(text),[len(text)-1,len(text)+1,len(text)+2],'Count each letter once.')
  add(3,f'Which is "{text}" reversed?',text[::-1],[text,text[1:]+text[0],text[0]+text[:0:-1]],'Read the word from its last letter to its first.')
 for value in (False,True):
  add(4,f'NOT {value} = ?',not value,[value,'unknown','both'],'NOT flips a true/false value.')
 for a,b in ((True,False),(False,False),(True,True)):
  add(4,f'{a} AND {b} = ?',a and b,[not(a and b),'unknown','both'],'AND is true only when both values are true.')
 for expression,answer in (('len([2,4,6])',3),('2 ** 3',8),('7 // 2',3),('10 % 3',1),('sum([1,2,3])',6),('len("hello")',5)):
  add(2,f'Python: {expression} = ?',answer,[answer+1,answer-1,answer+3],'Verified with the Python3 expression in the bundled test.')
 return items

def loop(s):
 bank=questions();topic=0;mode='menu';current=None;order=[];score=0;count=0;feedback=''
 while True:
  h,w=s.getmaxyx();s.erase();put(s,0,1,'LEARNING TRIVIA',curses.A_BOLD);put(s,h-1,1,'Arrows/1-4 select | Enter confirm | M topics | Esc/q exit')
  if w<60 or h<22:
   put(s,2,1,'Resize to60x22. Esc/q exits.');s.refresh();key=s.getch()
   if key in (27,ord('q')):return
   continue
  if mode=='menu':
   put(s,2,2,'Choose a topic:')
   for i,label in enumerate(TOPICS+('Mixed topics',)):put(s,4+i*2,4,label,curses.A_REVERSE if i==topic else 0)
  elif mode=='end':put(s,3,2,f'Finished! {score}/{count} correct. M returns to topics.')
  elif current:
   label,q,options,answer,explanation=current;put(s,2,2,TOPICS[label]+f' - question {count+1}/'+str(count+len(order)+(0 if feedback else 1)));put(s,4,2,q)
   for i,opt in enumerate(options):put(s,6+i*2,4,str(i+1)+'. '+opt,curses.A_REVERSE if i==topic else 0)
   put(s,h-4,2,feedback)
   if feedback:put(s,h-3,2,'Enter for next question.')
  s.refresh();key=s.getch()
  if key in (27,ord('q')):return
  if key==ord('m'):mode='menu';topic=0;feedback='';continue
  if mode=='menu':
   if key==curses.KEY_UP:topic=(topic-1)%6
   elif key==curses.KEY_DOWN:topic=(topic+1)%6
   elif key in (10,13):
    order=[q for q in bank if topic==5 or q[0]==topic];random.shuffle(order);score=count=0;current=order.pop();topic=0;mode='quiz';feedback=''
  elif mode=='quiz':
   if key==curses.KEY_UP:topic=(topic-1)%4
   elif key==curses.KEY_DOWN:topic=(topic+1)%4
   elif ord('1')<=key<=ord('4') and not feedback:topic=key-ord('1')
   elif key in (10,13):
    if feedback:
     if order:current=order.pop();topic=0;feedback=''
     else:mode='end'
    else:
     correct=topic==current[3];score+=int(correct);count+=1;feedback=('Correct! ' if correct else 'Answer: '+current[2][current[3]]+'. ')+current[4]
if __name__=='__main__':
 import sys
 if '--version' in sys.argv:print('1.0.0')
 else:raise SystemExit(run(loop))
