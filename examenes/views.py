#Django
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

#Models
from users.models import Usuarios
from examenes.models import Examen

@login_required
def inicio(request):
	user = Usuarios.objects.all()
	tipo_examen = Examen.TIPO_EXAMEN
	env = {
	'user':user,
	'tipo_examen':tipo_examen,
	}
	return render(request, 'examenes/index.html',env)




def send_email(request):
    subject = request.POST.get('Examenes a responder', 'Examenes a responder')
    list_tipo = request.POST.getlist('tipo_examen[]')
    message =''
    for x in list_tipo:
    	message = message +','+x
    from_email = request.POST.get('ideas.jaed@gmail.com', 'ideas.jaed@gmail.com')
    sd = request.POST['email_cliente']
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email,[sd])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/menu/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')


@login_required
def notify_email(request, slug):
    """ Send notification email to original owner of device who lost it """
    grab = Item.objects.get(slug=slug)
    if request.method == "POST":
        form = NotifyEmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = request.user.email
            recipients = [grab.created_by.email]
            recipients.append(sender)
 
            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/notify/thanks')  # Redirect after POST
    else:
        form = NotifyEmailForm()  # An unbound form
    return render(request, 'send-mail.html', {'form': form, 'object': slug, })


