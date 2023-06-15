# -*- coding:utf-8 -*-

from tccli.loaders import Loader, BASE_TYPE, CLI_BASE_TYPE


class BaseDocumentHandler(object):
    def __init__(self, doc):
        self.doc = doc
        self._cli_data = Loader()


class CLIDocumentHandler(BaseDocumentHandler):

    def __init__(self, doc):
        super(CLIDocumentHandler, self).__init__(doc)

    def description(self):
        self.doc.style.h2('Description')
        description = self._cli_data.get_description()
        self.doc.doc_description_indent(description)

    def configure(self):
        self.doc.style.h2('Configure')
        configure = self._cli_data.get_configure()
        self.doc.doc_description_indent(configure)

    def usage(self):
        self.doc.style.h2('Usage')
        usage = self._cli_data.get_usage()
        self.doc.doc_description_indent(usage)

    def options(self):
        self.doc.style.h2('Options')
        options = self._cli_data.get_options()
        for option in options:
            self.doc.doc_title_indent("%-12s| %s" % (option, options[option]))
            # self.doc.doc_description_indent(options[option])
        self.doc.style.new_line()

    def available_services(self, detailed=False):
        available_services = self._cli_data.get_available_services().keys()
        self.doc.style.h2('Available Services')
        if not detailed:
            self.doc.style.indent()
            self.doc.write(self.doc.style.spaces())
            for service in sorted(available_services):
                self.doc.write("[%s] " % service)
            self.doc.style.dedent()
            self.doc.style.new_line()
            self.doc.style.new_line()
            self.doc.write('Use `tccli help --detail` to see more information')
            self.doc.style.new_line()
        else:
            for service in sorted(available_services):
                self.doc.doc_title_indent(service)
                version = self._cli_data.get_service_default_version(service)
                description = self._cli_data.get_service_description(service, version)
                if not description:
                    self.doc.style.new_line()
                    continue
                self.doc.doc_description_indent(description)

    def doc_help(self, detailed=False):
        # self.doc.style.h1("tccli")
        # self.description()
        # self.configure()
        self.usage()
        self.options()
        self.available_services(detailed)


class ServiceDocumentHandler(BaseDocumentHandler):

    def __init__(self, doc, service, version):
        super(ServiceDocumentHandler, self).__init__(doc)
        self._service = service
        self._version = version

    def available_versions(self):
        self.doc.style.h2('Available Versions')
        versions = self._cli_data.get_available_services()[self._service]
        for version in versions:
            self.doc.doc_title_indent(version)
        # self.doc.style.new_line()
        self.doc.doc_description_indent(u"默认只展示最新版本信息，查看其它版本帮助信息加 --version xxxx-xx-xx")

    def description(self):
        self.doc.style.h2('Description')
        description = self._cli_data.get_service_description(self._service, self._version)
        description = description if description else ""
        # self.doc.doc_title_indent("%s-%s\n" % (self._service, self._version))
        self.doc.doc_description_indent(description)

    def usage(self):
        self.doc.style.h2('Usage')
        usage = self._cli_data.get_service_usage(self._service)
        self.doc.doc_description_indent(usage)

    def options(self):
        self.doc.style.h2('Options')
        options = self._cli_data.get_service_options(self._service)
        for option in options:
            self.doc.doc_title_indent('%s' % option)
            self.doc.doc_description_indent(options[option])

    def available_actions(self, detail=False):
        actions_info = self._cli_data.get_actions_info(self._service, self._version)
        self.doc.style.h2('Available Actions')
        if not detail:
            self.doc.style.indent()
            self.doc.write(self.doc.style.spaces())
            for action in actions_info:
                self.doc.write("<%s> " % action)
            self.doc.style.new_line()
            self.doc.style.new_line()
            self.doc.write('Use `tccli %s help --detail` to see more information.' % self._service)
            self.doc.style.new_line()
        else:
            for action in actions_info:
                self.doc.doc_title_indent(action)
                self.doc.doc_description_indent(actions_info[action]["name"])

    def doc_help(self, detail=False):
        # self.doc.style.h1(self._service)
        self.available_versions()
        self.description()
        self.usage()
        self.options()
        self.available_actions(detail)


class ActionDocumentHandler(BaseDocumentHandler):

    def __init__(self, doc, service, version, action):
        super(ActionDocumentHandler, self).__init__(doc)
        self._service = service
        self._version = version
        self._action = action

    def description(self):
        self.doc.style.h2('Description')
        description = self._cli_data.get_action_description(self._service, self._version, self._action)
        self.doc.doc_title_indent("%s-%s-%s\n" % (self._service, self._version, self._action))
        self.doc.doc_description_indent(description)

    def usage(self):
        self.doc.style.h2('Usage')
        usage = self._cli_data.get_action_usage(self._service, self._action)
        self.doc.doc_description_indent(usage)

    def options(self, detail=False):
        self.doc.style.h2('Options')
        options = self._cli_data.get_action_options(self._service, self._action)
        keys = sorted(options)
        keys.insert(0, keys.pop())
        if not detail:
            self.doc.style.indent()
            self.doc.write(self.doc.style.spaces())
            for option in keys:
                self.doc.write("[%s] " % option)
            self.doc.style.dedent()
            self.doc.style.new_line()
            self.doc.style.new_line()
        else:
            for option in keys:
                self.doc.doc_title_indent(option)
                self.doc.doc_description_indent(options[option])

    def _json_format(self, param_info):
        if param_info["type"] == "Array":
            param_info["members"] = param_info["members"][0]
            if param_info["members"] in BASE_TYPE:
                if self.doc.style.indentation > 2:
                    self.doc.write('[%s ...]' % (param_info["members"]))
                else:
                    self.doc.doc_description('[%s ...]' % (param_info["members"]))
            else:
                self.doc.write('[') if self.doc.style.indentation > 2 \
                    else self.doc.doc_description('[')
                self.doc.style.indent()
                self.doc.style.new_line()
                self._handle_object_members(param_info["members"], param_info["type"])
                self.doc.style.new_line()
                self.doc.doc_description('...')
                self.doc.style.dedent()
                self.doc.style.new_line()
                self.doc.doc_description(']')
        else:
            if param_info["members"] not in BASE_TYPE:
                self._handle_object_members(param_info["members"], param_info["type"])

    def _handle_object_members(self, param_info, param_type):
        if param_type == "Array" or self.doc.style.indentation == 2:
            self.doc.doc_description('{')
        else:
            self.doc.write('{')
        self.doc.style.indent()
        self.doc.style.new_line()
        for idx, param in enumerate(param_info):
            if param_info[param]["type"] in CLI_BASE_TYPE:
                self.doc.doc_description('"%s": %s' % (param, param_info[param]["type"]))
            elif param_info[param]["type"] == "Array":
                self.doc.doc_description('"%s": ' % param)
                self._json_format(param_info[param])
            else:
                self.doc.doc_description('"%s": ' % param)
                self._json_format(param_info[param])
            if idx < len(param_info) - 1:
                self.doc.write(',')
                self.doc.style.new_line()
        self.doc.style.dedent()
        self.doc.style.new_line()
        self.doc.doc_description('}')

    def _unfold_complex_object(self, param_info):
        if not param_info["type"] == "Array" and param_info["members"] in BASE_TYPE:
            return

        self.doc.style.new_line()
        self.doc.doc_title('JSON Syntax')
        self.doc.style.new_line()
        self.doc.style.indent()
        self._json_format(param_info)
        self.doc.style.dedent()

    def _param_type(self, param):
        if param["type"] == "Array":
            return "Array of %s" % param["type_name"]
        return param["type_name"]

    def _complex_object_doc(self, param_info, option):
        if param_info["members"] in BASE_TYPE:
            return
        self.doc.style.indent()
        for sub_param, sub_param_info in param_info["members"].items():
            self.doc.style.new_line()
            self._doc_title(option, sub_param, sub_param_info)
            self.doc.doc_description('%s' % sub_param_info["document"])
            self.doc.style.new_line()
            if sub_param_info["members"] not in BASE_TYPE:
                self._complex_object_doc(sub_param_info, option)
        self.doc.style.dedent()
        self.doc.style.new_line()

    def get_param_info_method(self):
        param_info_method = {
            "Available Parameters": self._cli_data.get_param_info,
            "Output Parameter": self._cli_data.get_output_param_info
        }
        return param_info_method

    @property
    def param_info_method(self):
        return self.get_param_info_method()

    def _doc_title(self, option, param, param_info):
        if option == "Available Parameters":
            self.doc.doc_title('--%s (%s | %s)' % (param, self._param_type(param_info), param_info.get("required")))
        else:
            self.doc.doc_title('%s -> (%s)' % (param, self._param_type(param_info)))

    def _base_parameter(self, option, detail=False):
        params_info = self.param_info_method[option](self._service, self._version, self._action)
        self.doc.style.h2(option)

        if not params_info:
            self.doc.style.indent()
            self.doc.doc_title(u'无')
            # self.doc.style.new_line()

        if not detail:
            for param, param_info in params_info.items():
                self._doc_title(option, param, param_info)
            self.doc.style.new_line()
            if option == "Output Parameter":
                self.doc.write('Use `tccli %s %s help --detail` to see more information.' % (self._service, self._action))
                self.doc.style.new_line()
        else:
            for param, param_info in params_info.items():
                self.doc.style.new_line()
                self.doc.style.indent()
                self._doc_title(option, param, param_info)
                self.doc.doc_description('%s' % param_info["document"])
                self.doc.style.new_line()
                self._unfold_complex_object(param_info)
                self.doc.style.new_line()
                self._complex_object_doc(param_info, option)
                self.doc.style.dedent()

    def available_parameter(self, detail=False):
        self._base_parameter("Available Parameters", detail)

    def output_parameter(self, detail=False):
        self._base_parameter("Output Parameter", detail)

    def input_example(self, input_param):
        self.doc.style.new_line()
        self.doc.doc_description("Input:")
        self.doc.style.new_line()
        self.doc.style.indent()
        self.doc.doc_description("tccli %s %s --cli-unfold-argument " % (self._service, self._action))
        self.doc.style.indent()
        if input_param:
            self.doc.write(" \\")
            for param in input_param[:-1]:
                self.doc.style.new_line()
                self.doc.doc_description(param + " \\")
            self.doc.style.new_line()
            self.doc.doc_description(input_param[-1])
        self.doc.style.dedent()
        self.doc.style.dedent()

    def output_example(self, output_param):
        self.doc.style.new_line()
        self.doc.doc_description("Output:")
        self.doc.style.new_line()
        self.doc.style.indent()
        self.doc.doc_description(output_param)
        self.doc.style.dedent()

    def example(self):
        self.doc.style.h2('Examples')
        examples = self._cli_data.generate_cli_example(self._service, self._version, self._action)
        self.doc.style.indent()
        for idx, example in enumerate(examples):
            self.doc.style.new_line()
            self.doc.doc_title("Example %s: " % str(idx+1) + example["title"])
            self.doc.style.new_line()
            self.doc.doc_description(example["document"])
            self.doc.style.new_line()
            self.input_example(example["input"])
            self.doc.style.new_line()
            self.output_example(example["output"])
            self.doc.style.new_line()
        self.doc.style.dedent()

    def doc_help(self, detail=False):
        # self.doc.style.h1(self._action)
        if detail:
            self.description()
        self.usage()
        self.options(detail)
        self.available_parameter(detail)
        if detail:
            self.example()
        self.output_parameter(detail)

