from django.shortcuts import render
import json
import requests
from django.views.generic import View

class HomeView(View):
    def get(self,request,*args,**kwargs):
        combined=[]
        state = [] 
        conf = [] 
        delconf = [] 
        act = [] 
        delact = [] 
        rec = [] 
        delrec = [] 
        dth = [] 
        deldth = [] 
        cfr = [] 
        rr = []
        rdr = []
        request1 = requests.get('https://api.covid19india.org/data.json')
        y = json.loads(request1.text)
        for i in range(38):
            act.append(int(y['statewise'][i]['active']))
            state.append(y['statewise'][i]['state'])
            conf.append(int(y['statewise'][i]['confirmed']))
            rec.append(int(y['statewise'][i]['recovered']))
            dth.append(int(y['statewise'][i]['deaths']))
            delconf.append(int(y['statewise'][i]['deltaconfirmed']))
            deldth.append(int(y['statewise'][i]['deltadeaths']))
            delrec.append(int(y['statewise'][i]['deltarecovered']))
            delact.append(delconf[i]-deldth[i]-delrec[i])
            try:
                cfr.append(round(100*dth[i]/conf[i], 2))
            except:
                cfr.append(float('0.0'))
            try:
                if rec[i]==0 and conf[i]!=0:
                    rr.append('No Recoveries Yet')
                else:
                    rr.append(round(100*rec[i]/conf[i],2))
            except:
                rr.append('No cases confirmed')
            try:
                rdr.append(round(rec[i]/dth[i], 2))
            except:
                rdr.append('No deaths occured')
        state[0] = 'India'
        for i in range(38):
            join=[]
            data = zip([state[i]],[conf[i]],[delconf[i]],[act[i]],[delact[i]],[rec[i]],[delrec[i]],[dth[i]],[cfr[i]],[rr[i]],[rdr[i]])
            #join.extend([state[i],conf[i],delconf[i],act[i],delact[i],rec[i],delrec[i],dth[i],cfr[i],rr[i],rdr[i]])
            combined.append(data)
        context = {
            
        }
        return render(request,'index.html',context)


def about(request):
    return render(request,'about.html')
