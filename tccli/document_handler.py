# -*- coding:utf-8 -*-

from tccli.loaders import *


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

    def useage(self):
        self.doc.style.h2('Useage')
        useage = self._cli_data.get_useage()
        self.doc.doc_description_indent(useage)

    def options(self):
        self.doc.style.h2('Options')
        options = self._cli_data.get_options()
        for option in options:
            self.doc.doc_title_indent(option)
            self.doc.doc_description_indent(options[option])

    def available_services(self):
        available_services = self._cli_data.get_available_services().keys()
        self.doc.style.h2('Available Services')
        for service in sorted(available_services):
            self.doc.doc_title_indent(service)
            version = self._cli_data.get_service_default_version(service)
            description = self._cli_data.get_service_description(service, version)
            if not description:
                self.doc.style.new_line()
                continue
            self.doc.doc_description_indent(description)

    def doc_help(self):
        self.doc.style.h1("tccli")
        self.description()
        self.configure()
        self.useage()
        self.options()
        self.available_services()


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
        self.doc.style.new_line()
        self.doc.doc_description_indent(u"默认只展示最新版本信息，查看其它版本帮助信息加 --version xxxx-xx-xx")

    def description(self):
        self.doc.style.h2('Description')
        description = self._cli_data.get_service_description(self._service, self._version)
        description = description if description else ""
        self.doc.doc_title_indent("%s-%s\n" % (self._service, self._version))
        self.doc.doc_description_indent(description)

    def useage(self):
        self.doc.style.h2('Useage')
        useage = self._cli_data.get_service_useage(self._service)
        self.doc.doc_description_indent(useage)

    def options(self):
        self.doc.style.h2('Options')
        options = self._cli_data.get_service_options(self._service)
        for option in options:
            self.doc.doc_title_indent('%s' % option)
            self.doc.doc_description_indent(options[option])

    def available_actions(self):
        actions_info = self._cli_data.get_actions_info(self._service, self._version)
        self.doc.style.h2('Available Actions')
        for action in actions_info:
            self.doc.doc_title_indent(action)
            self.doc.doc_description_indent(actions_info[action]["name"])

    def doc_help(self):
        self.doc.style.h1(self._service)
        self.available_versions()
        self.description()
        self.useage()
        self.options()
        self.available_actions()


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

    def useage(self):
        self.doc.style.h2('Useage')
        useage = self._cli_data.get_action_useage(self._service, self._action)
        self.doc.doc_description_indent(useage)

    def options(self):
        self.doc.style.h2('Options')
        options = self._cli_data.get_action_options(self._service, self._action)
        for option in options:
            self.doc.doc_title_indent(option)
            self.doc.doc_description_indent(options[option])

    def _json_format(self, param_info):
        self._recur_json_format(param_info)

    def _recur_json_format(self, param_info):
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
            return "Array of %s" % PARAM_TYPE_MAP.get(param["type_name"], param["type_name"])
        return PARAM_TYPE_MAP.get(param["type_name"], param["type_name"])

    def _recur_complex_object_doc(self, param_info):
        if param_info["members"] in BASE_TYPE:
            return

        self.doc.style.indent()
        for subparam, subparaminfo in param_info["members"].items():
            self.doc.style.new_line()
            self.doc.doc_title('--%s (%s | %s)' % (subparam, self._param_type(subparaminfo), subparaminfo["required"]))
            self.doc.doc_description('%s' % subparaminfo["document"])
            self.doc.style.new_line()
            if subparaminfo["members"] not in BASE_TYPE:
                self._recur_complex_object_doc(subparaminfo)
        self.doc.style.dedent()
        self.doc.style.new_line()

    def _complex_object_doc(self, param_info):
        if param_info["members"] in BASE_TYPE:
            return
        self._recur_complex_object_doc(param_info)

    def available_parameter(self):
        params_info = self._cli_data.get_param_info(self._service, self._version, self._action)
        self.doc.style.h2('Available Params')
        if not params_info:
            self.doc.style.indent()
            self.doc.doc_title(u'无')
            self.doc.style.new_line()

        for param, param_info in params_info.items():
            self.doc.style.new_line()
            self.doc.style.indent()
            self.doc.doc_title('--%s (%s | %s)' % (param, self._param_type(param_info), param_info["required"]))
            self.doc.doc_description('%s' % param_info["document"])
            self.doc.style.new_line()
            self._unfold_complex_object(param_info)
            self.doc.style.new_line()
            self._complex_object_doc(param_info)
            self.doc.style.dedent()

    def doc_help(self):
        self.doc.style.h1(self._action)
        self.description()
        self.useage()
        self.options()
        self.available_parameter()

