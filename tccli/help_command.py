# -*- coding:utf-8 -*-

import sys
from tccli.style import Document
from tccli.loaders import Loader
from tccli.document_handler import CLIDocumentHandler, ServiceDocumentHandler, ActionDocumentHandler


class BaseHelpCommand(object):

    def __init__(self):
        self.doc = Document()
        self._cli_data = Loader()

    def _get_document_handler(self):
        pass

    def _get_service_version(self, parsed_globals):
        pass

    def _service_version(self, service_name, parsed_globals):
        if hasattr(parsed_globals, "action_version"):
            version = vars(parsed_globals)["action_version"]
            if version is None:
                version = self._cli_data.get_service_default_version(service_name)
            available_version_list = self._cli_data.get_available_services()[service_name]
            if version not in available_version_list:
                raise Exception("available versions: %s" % " ".join(available_version_list))
            self._version = version

    def __call__(self, args, parsed_globals):
        #if args:
        #    raise UnknownArgumentError("Unknown options: %s" % ', '.join(args))

        self._get_service_version(parsed_globals)
        document_handle = self._get_document_handler()
        document_handle.doc_help()
        sys.stdout.write(self.doc.getvalue())


class CLIHelpCommand(BaseHelpCommand):

    def __init__(self):
        super(CLIHelpCommand, self).__init__()

    def _get_service_version(self, parsed_globals):
        pass

    def _get_document_handler(self):
        return CLIDocumentHandler(self.doc)


class ServiceHelpCommand(BaseHelpCommand):

    def __init__(self, service_name, version):
        self._service_name = service_name
        self._version = version
        super(ServiceHelpCommand, self).__init__()

    def _get_service_version(self, parsed_globals):
        self._service_version(self._service_name, parsed_globals)

    def _get_document_handler(self):
        return ServiceDocumentHandler(self.doc, self._service_name, self._version)


class ActionHelpCommand(BaseHelpCommand):

    def __init__(self, service_name, version, action_name):
        self._service_name = service_name
        self._version = version
        self._action_name = action_name
        super(ActionHelpCommand, self).__init__()

    def _get_service_version(self, parsed_globals):
        self._service_version(self._service_name, parsed_globals)

    def _get_document_handler(self):
        return ActionDocumentHandler(self.doc, self._service_name, self._version, self._action_name)


