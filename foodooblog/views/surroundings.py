# Make this take are of the searching functionality


class ViewEnvironment(object):
    """Takes care of the environment of the view. Please make the
    instance you will be using session specific.
    """

    def __init__(self, copy=None):
        """If copy is porvided draw initial values from there
        """
        if copy is not None:
            self.environment = copy()
        else:
            self.environment = dict()

    def __call__(self, **kwargs):
        """Return the current environment enhanced with the kwargs provided.
        """
        return dict(self.environment.items() + kwargs.items())

    def update(**kwargs):
        """Add these items in the environment.
        """
        self.environment = dict(self.environment.items() + kwargs.items())

    def remove(*args):
        """Try to remove the arguments provided.
        """
        for k in args:
            if k in self.environment.keys():
                del self.environment[k]

environment_factory = ViewEnvironment()
