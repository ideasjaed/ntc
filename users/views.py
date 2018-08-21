
#Django
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate,login


# Create your views here.

#models
from django.contrib.auth.models import User
from users.models import Usuarios

def login_view(request):
	"""Login view."""
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user:
			login(request, user)
			return redirect('home')
		else:
			return render(request,'users/login.html',{'error':'Usuario y contraseña invalida'})
	return render(request,'users/login.html')


def signup(request):

	if request.method == 'POST':
		nombre = request.POST['nombre']
		apellidos = request.POST['apellidos']
		email = request.POST['email']
		direccion = request.POST['direccion']
		ocupacion = request.POST['ocupacion']
		edad = request.POST['edad']
		estado_civil= request.POST['estado_civil']
		if request.POST.get('id_usuario'):
			usuario = Usuarios.objects.get(id= request.POST.get('id_usuario'))
			usuario.nombre = nombre
			usuario.apellidos= apellidos
			usuario.email= email
			usuario.direccion= direccion
			usuario.ocupacion=ocupacion
			usuario.edad=edad
			usuario.estado_civil= estado_civil
			usuario.save()
			return redirect('home')
		else:
			user = Usuarios(nombre= nombre,apellidos= apellidos,
						email=email, direccion=direccion,ocupacion=ocupacion,
						edad=edad,estado_civil=estado_civil)			
			user.save()
			return redirect('home')

	else:
		return render(request, 'users/signup.html')


def editar_usuario(request,pk):
	usuario = Usuarios.objects.get(id=pk)
	env = {
	'usuario':usuario
	}
	return render(request, 'users/signup.html',env)
