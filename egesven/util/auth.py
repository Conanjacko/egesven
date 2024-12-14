from django.contrib.auth import get_user_model
from django.contrib.sessions.models import Session
from django.shortcuts import redirect


def session_required(view_func):
    """
    Decorador para asegurar que el usuario esté autenticado utilizando la cookie 'sessionid'.
    Si no está autenticado, se redirige al usuario a la página de login.
    """

    def _wrapped_view(request, *args, **kwargs):
        sessionid = request.COOKIES.get("sessionid")

        if sessionid:
            try:
                session = Session.objects.get(session_key=sessionid)
                user_id = session.get_decoded().get("_auth_user_id")

                if user_id:
                    User = get_user_model()
                    user = User.objects.get(id=user_id)

                    if user.is_authenticated:
                        return view_func(request, *args, **kwargs)
            except (Session.DoesNotExist, User.DoesNotExist):
                pass

        return redirect("landing")

    return _wrapped_view
