
from tccli.exceptions import ParamError
from tccli.loaders import *


class BaseArgument(object):

    def __init__(self, name):
        self._name = name

    def add_to_arg_map(self, argument_map):
        argument_map[self.name] = self

    def add_to_parser(self, parser):
        pass

    def add_to_params(self, parameters, value):
        pass

    @property
    def name(self):
        return self._name

    @property
    def cli_name(self):
        return '--' + self._name

    @property
    def cli_type_name(self):
        raise NotImplementedError("cli_type_name")

    @property
    def required(self):
        raise NotImplementedError("required")

    @property
    def documentation(self):
        raise NotImplementedError("documentation")

    @property
    def cli_type(self):
        raise NotImplementedError("cli_type")

    @property
    def py_name(self):
        return self._name.replace('-', '_')

    @property
    def choices(self):
        return None

    @property
    def synopsis(self):
        return ''

    @property
    def positional_arg(self):
        return False

    @property
    def nargs(self):
        return None

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def group_name(self):
        return None


class CustomArgument(BaseArgument):

    def __init__(self, name, help_text='', dest=None, default=None,
                 action=None, required=None, choices=None, nargs=None,
                 cli_type_name=None, group_name=None, positional_arg=False,
                 no_paramfile=False, argument_model=None, synopsis='',
                 const=None):
        self._name = name
        self._help = help_text
        self._dest = dest
        self._default = default
        self._action = action
        self._required = required
        self._nargs = nargs
        self._const = const
        self._cli_type_name = cli_type_name
        self._group_name = group_name
        self._positional_arg = positional_arg
        self._choices = [] if choices is None else choices
        self._synopsis = synopsis

        self.no_paramfile = no_paramfile

    @property
    def cli_arg_name(self):
        if self._positional_arg:
            return self._name
        else:
            return '--' + self._name

    def add_to_parser(self, parser):
        cli_arg_name = self.cli_arg_name
        kwargs = {}
        if self._dest is not None:
            kwargs['dest'] = self._dest
        if self._action is not None:
            kwargs['action'] = self._action
        if self._default is not None:
            kwargs['default'] = self._default
        if self._choices:
            kwargs['choices'] = self._choices
        if self._required is not None:
            kwargs['required'] = self._required
        if self._nargs is not None:
            kwargs['nargs'] = self._nargs
        if self._const is not None:
            kwargs['const'] = self._const
        parser.add_argument(cli_arg_name, **kwargs)

    @property
    def required(self):
        if self._required is None:
            return False
        return self._required

    @required.setter
    def required(self, value):
        self._required = value

    @property
    def documentation(self):
        return self._help

    @property
    def cli_type(self):
        cli_type = str
        if self._action in ['store_true', 'store_false']:
            cli_type = bool
        return cli_type

    @property
    def choices(self):
        return self._choices

    @property
    def group_name(self):
        return self._group_name

    @property
    def synopsis(self):
        return self._synopsis

    @property
    def positional_arg(self):
        return self._positional_arg

    @property
    def nargs(self):
        return self._nargs


class CLIArgument(BaseArgument):
    TYPE_MAP = {
        'Array': str,
        'String': str,
        'Float': float,
        'Integer': int,
        'Timestamp': str,
        'Boolean': str
    }

    def __init__(self, name, argument_model, action_model,
                 is_required=False):
        self._name = name
        self.argument_model = argument_model
        self._required = is_required
        self._operation_model = action_model
        self._documentation = argument_model["document"]

    @property
    def name(self):
        return self._name

    @property
    def required(self):
        return self._required

    @required.setter
    def required(self, value):
        self._required = value

    @property
    def documentation(self):
        return self._documentation

    @documentation.setter
    def documentation(self, value):
        self._documentation = value

    @property
    def cli_type_name(self):
        return self.argument_model.type_name

    @property
    def cli_type(self):
        return self.TYPE_MAP.get(self.argument_model["type"], str)

    def add_to_parser(self, parser):
        cli_name = self.cli_name
        parser.add_argument(
            cli_name,
            help=self.documentation,
            type=self.cli_type,
            required=self.required)

    def add_to_params(self, parameters, value):
        if value is None:
            return
        else:
            value = self._unpack_param(value)
            parameters[self._name] = value

    def _unpack_param(self, value):
        if self.argument_model["type"] == "Boolean":
            try:
                if str(value) == 'False':
                    return False
                elif str(value) == 'True':
                    return True
                else:
                    raise ValueError
            except ValueError as e:
                raise ParamError(
                    self.cli_name, "Invalid Boolean: %s\n "
                                   "Boolean received: %s\n "
                                   "Boolean only take values: True/False"
                                   % (e, value))
        elif self.argument_model["type"] in CLI_BASE_TYPE:
            return value
        else:
            try:
                return json.loads(value.encode("utf8"))
            except ValueError as e:
                raise ParamError(
                    self.cli_name, "Invalid JSON: %s\n "
                                   "JSON received: %s" % (e, value))


class ListArgument(CLIArgument):

    @property
    def nargs(self):
        return '*'

    def add_to_parser(self, parser):
        cli_name = self.cli_name
        parser.add_argument(cli_name,
                            nargs=self.nargs,
                            type=self.cli_type,
                            required=self.required)


class BooleanArgument(CLIArgument):
    def __init__(self, name, argument_model, action_model,
                 is_required=False, action='store_true', dest=None,
                 group_name=None, default=None):
        super(BooleanArgument, self).__init__(name,
                                              argument_model,
                                              action_model,
                                              is_required)
        self._action = action
        if dest is None:
            self._destination = self.py_name
        else:
            self._destination = dest
        if group_name is None:
            self._group_name = self.name
        else:
            self._group_name = group_name
        self._default = default

    def add_to_params(self, parameters, value):
        if value is not None:
            parameters[self.name] = value

    def add_to_arg_map(self, argument_map):
        argument_map[self.name] = self

    def add_to_parser(self, parser):
        parser.add_argument(self.cli_name,
                            help=self.documentation,
                            action=self._action,
                            default=self._default,
                            dest=self._destination)

    @property
    def group_name(self):
        return self._group_name
