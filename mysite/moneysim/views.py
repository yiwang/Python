 #Create your views here.
import sys
from mysite.moneysim import p3
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponse 
from django.utils import simplejson

rr_srv = 10
seed_srv = 200

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def index(request):
    if not request.POST:
        return render_to_response('moneysim/index.html')
    
    
    rr = request.REQUEST["rr"]
    seed = request.REQUEST["seed"]
    
    if is_number(rr) and is_number(seed):
        rr_srv, seed_srv = rr,seed = float(rr),float(seed)
        p3.sim(rr,seed)
        response_dict = {'ok':1}    
        #return render_to_response('moneysim/index.html')
    else:
        response_dict = {'rr':rr_srv, 'seed':seed_srv}
    return HttpResponse(simplejson.dumps(response_dict),mimetype='application/javascript')
        
    
    
    


def result(request):
    
    print sys.path
    return render_to_response('moneysim/index.html')
