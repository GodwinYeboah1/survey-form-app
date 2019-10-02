from django.shortcuts import render,redirect

# Create your views here.
def index(req):
    return render(req, 'survey_form/index.html')

def process(req):
    req.session['fullname'] = req.POST['fullname']
    req.session['Locations'] = req.POST['Locations']
    req.session['fav_lang'] = req.POST['fav_lang']
    req.session['comment'] = req.POST['comment']
    return redirect('/result')

def result(req):
    # if counter variable is not in the req session object
    if 'counter' is not req.session:
        # set the counter variable to zero
        req.session['counter'] = 0
    req.session['counter'] = 1 + req.session['counter']

    data_obj = {
        'counter': req.session['counter'],
        'fullname': req.session['fullname'],
        'locations': req.session['Locations'],
        'fav_lang': req.session['fav_lang'],
        'comment': req.session['comment']
    }
    return render(req, 'survey_form/result.html', data_obj)

def reset(req):
    # clears variable in the session 
    req.session.clear()
    return redirect('/')