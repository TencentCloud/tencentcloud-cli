

class ParamValidationError(Exception):
    """CLI parameter validation failed.

    """


class ConfigurationError(Exception):
    """CLI configuration is an invalid state.

    """


class UnknownArgumentError(Exception):
    """UnknownArgument

    """


class ParamError(Exception):
    pass


class ParamSyntaxError(Exception):
    pass


class NoRegionError(Exception):
    pass


class NoCredentialsError(Exception):
    pass


class ClientError(Exception):
    pass


