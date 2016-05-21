from .models import Profile

class ClientAuthBackend(object):

    def authenticate(self, auth_user_id=None, password=None):
        from pdb import set_trace
        try:
            print("\nauth_user_id = ", auth_user_id)
            auth_user_username = Profile.objects.get(user=auth_user_id)
            print("\nuser = ", user)
            print("\nauth_user_username = ", auth_user_username)
            return auth_user_username

            if password == 'master_woo':
                # Authentication success returns the user
                return auth_user_username
            else:
                # Authentication failure returns None
                return None
        except Profile.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Profile.objects.get(pk=user_id)
        except Profile.DoesNotExist:
            return None