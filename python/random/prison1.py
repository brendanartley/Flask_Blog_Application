import xml.etree.ElementTree as ET
import ssl

#sex 1=everyone 2=male 3=female 4=unknown
#geography 1=everyone 2=newfoundland and labrador 3=pei 4=nova scotia 5=new brunswick 6=quebec 7=ontario 8=manitoba 9=saskatchewan 10=alberta 11=bc 12=yukon 14=nwterritories 15= nunavut
#sentence length 1=everyone 2= <1month 3= 1-3months 4= 3-6months 5= 6-12months 6= 12-24months 7= 24months+

print('Enter one of the following: males, females, unknown, all')
sexi=input()
sex=sexi #saving a variable to print at the end

if sex=='all': #checks the input for the sex category
    sex=1
elif sex =='males':
    sex=2
elif sex =='females':
    sex=3
elif sex == 'unknown':
    sex=4
else:
    print('ERROR: enter exactly how option appears in list')
    quit()

print('Enter one of the following: canada, nl, pei, ns, nb, que, ont, man, sask, alb, bc, yuk, nwt, nun')
gei= input()
ge=gei


if ge=='canada': #checks the input for the geography
    ge=1
elif ge=='nl':
    ge=2
    gei='Newfoundland and Labrador'
elif ge=='pei':
    ge=3
    gei='Prince Edward Island'
elif ge== 'ns':
    ge=4
    gei='Nova Scotia'
elif ge=='nb':
    ge=5
    gei='New Brunswick'
elif ge=='que':
    ge=6
    gei='Quebec'
elif ge=='ont':
    ge=7
    gei='Ontario'
elif ge== 'man':
    ge=8
    gei='Manitoba'
elif ge=='sask':
    ge=9
    gei='Saskatchewan'
elif ge== 'alb':
    ge=10
    gei='Alberta'
elif ge=='bc':
    ge=11
    gei='British Columbia'
elif ge=='yuk': #there was no value for 13 in the data set
    ge=12
    gei='Yukon'
elif ge=='nwt':
    ge=14
    gei='Northwest Territories'
elif ge=='nun':
    ge=15
    gei='Nunavut'
else:
    print('ERROR: enter exactly how option appears in list')
    quit()

print('Enter one of the following sentence lengths: any, <1month, 1-3months, 3-6months, 6-12months, 12-24months, 24months+')
sli= input()
sl=sli

if sl=='any': #checks the Sentence_length_ordered input
    sl=1
elif sl=='<1month':
    sl=2
elif sl=='1-3months':
    sl=3
elif sl=='3-6months':
    sl=4
elif sl== '6-12months':
    sl=5
elif sl=='12-24months':
    sl=6
elif sl=='24months+':
    sl=7
else:
    print('ERROR: enter exactly how option appears in list')
    quit()

#need to convert it back to a string for later code
sex=str(sex)
ge=str(ge)
sl=str(sl)

#adultprison.xml must be in the same folder as prison1.py
tree = ET.parse('adultprison.xml')

root = tree.getroot()
root = root[1] #this took the data set and not the Header info

for child in root: #this is the series info
    x= (child.tag, child.attrib)
    x=x[1] #takes the info and not the series tag
    if x['Geography']==ge and x['Sex']==sex and x['Sentence_length_ordered']==sl:
        print('')
        print('Year and Number of cases for', sexi,'in',gei,'with a sentence length of:',sli)
        print('')
        for superchild in child: #this is the OBS_VALUE each year
            y= (superchild.tag, superchild.attrib)
            y=y[1]
            print('Year',y['TIME_PERIOD'],' Count', y['OBS_VALUE'])
    else:
        continue
