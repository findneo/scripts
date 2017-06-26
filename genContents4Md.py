#-*-coding:utf-8-*-
import re,sys
d={"#":1,"##":2,"###":3,"####":4,"#####":5,"######":6}
pattern='#+\s'
def usage():
	print "usage:"
	print "python script.py srcFilename.md"
	print "then you will get a res.md with contents "
	print "under the same path as srcFile\nenjoy!"
def ganMenu(filename):
  headId=0
  targetname="res.md"
  with open(targetname,'w+') as f2:
      with open(filename,'r') as f:
          for i in f.readlines():
            if not re.match(pattern,i.strip(' \t\n')): 
              continue
            i=i.strip(' \t\n') 
            head=i.split(' ')[0]
            f2.write('['+i[len(head):].strip(' \t\n')+'](#id'+str(headId)+')   \n')
            headId+=1
      headId=0     
      with open(filename,'r') as f  :
        for i in f.readlines():
            if not re.match(pattern,i.strip(' \t\n')):   
              f2.write(i)
            else:
              i=i.strip(' \t\n')
              head=i.split(' ')[0]
              if head in d.keys():
                menu=''.join(['<h',str(len(head)),' id=id',str(headId),'>',i[len(head):].strip(' \t\n'),'</h',str(len(head)),'>   \n'])
                f2.write(menu)
                headId+=1

if __name__ == '__main__':
	try:
		ganMenu(sys.argv[1])   
	except:
		usage()

            
          
