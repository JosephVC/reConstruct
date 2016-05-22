from .models import Profile

class ClientAuthBackend(object):

    def authenticate(self, username=None, password=None):
        try:
            user = Profile.objects.get(user_id=username)
            return user

            if password == 'master':
                # Authentication success by returning the user
                return user
            else:
                # Authentication fails if None is returned
                return None
        except Profile.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Profile.objects.get(pk=user_id)
        except Profile.DoesNotExist:
            return None