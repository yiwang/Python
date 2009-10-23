 #Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
 
def index(request):
#    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    return render_to_response('moneysim/index.html', {'latest_poll_list': 3})


#--------------------------------------------------------- def details(request):
    #-------------------------------------------------------------- [more stuff]
    #---------------------------------------------------------- if request.POST:
                #---------------------------- # Get all the mark for this recipe
        #------- list_mark = Mark.objects.values('mark').filter(recipe__pk=r.id)
                #--------------------------------------- # loop to get the total
        #------------------------------------------------------------- total = 0
        #--------------------------------------------- for element in list_mark:
            #------------------------------------------- total+= element['mark']
                #---------------------------------------------------- # round it
        # #--------------------- total = round((float(total) /  len(list_mark)),1)
                #-------------------------------------------- # update the total
        #--------------------------------------------------- r.total_mark= total
        #-------------------------------------------------- # save the user mark
                #------------------------------------------------------ r.save()
#------------------------------------------------------------------------------ 
                #------------------------ # Now the intersting part for this tut
        #---------------------------------------------------- import simple_json
                #------------ # it was a french string, if we dont't use unicode
                #---------- # the result at the output of json in Dojo is wrong.
        #--------------------------------- message = unicode( message, "utf-8" )
                #------------------------------------------------------------- #
        #- jsonList = simple_json.dumps((my_mark, total, form_message ,message))
        #----------------------------------------- return HttpResponse(jsonList)
          # #[more stuff, if not POST return render_to_response('recettes/details.html' ...]
