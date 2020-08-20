# -*- coding: utf-8 -*-
import os
import json
import tccli.options_define as OptionsDefine
import tccli.format_output as FormatOutput
from tccli.nice_command import NiceCommand
import tccli.error_msg as ErrorMsg
import tccli.help_template as HelpTemplate
from tccli import __version__
from tccli.utils import Utils
from tccli.configure import Configure
from tencentcloud.common import credential
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.ocr.v20181119 import ocr_client as ocr_client_v20181119
from tencentcloud.ocr.v20181119 import models as models_v20181119
from tccli.services.ocr import v20181119
from tccli.services.ocr.v20181119 import help as v20181119_help


def doInsuranceBillOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("InsuranceBillOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.InsuranceBillOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.InsuranceBillOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doVerifyBasicBizLicense(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("VerifyBasicBizLicense", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),
        "ImageConfig": argv.get("--ImageConfig"),
        "RegNum": argv.get("--RegNum"),
        "Name": argv.get("--Name"),
        "Address": argv.get("--Address"),
        "RegCapital": Utils.try_to_json(argv, "--RegCapital"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.VerifyBasicBizLicenseRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.VerifyBasicBizLicense(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doVatInvoiceVerify(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("VatInvoiceVerify", g_param[OptionsDefine.Version])
        return

    param = {
        "InvoiceCode": argv.get("--InvoiceCode"),
        "InvoiceNo": argv.get("--InvoiceNo"),
        "InvoiceDate": argv.get("--InvoiceDate"),
        "Additional": argv.get("--Additional"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.VatInvoiceVerifyRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.VatInvoiceVerify(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doQueryBarCode(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("QueryBarCode", g_param[OptionsDefine.Version])
        return

    param = {
        "BarCode": argv.get("--BarCode"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.QueryBarCodeRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.QueryBarCode(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doEnterpriseLicenseOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("EnterpriseLicenseOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.EnterpriseLicenseOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.EnterpriseLicenseOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doBusinessCardOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("BusinessCardOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),
        "Config": argv.get("--Config"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.BusinessCardOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.BusinessCardOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doIDCardOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("IDCardOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),
        "CardSide": argv.get("--CardSide"),
        "Config": argv.get("--Config"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.IDCardOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.IDCardOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doTollInvoiceOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("TollInvoiceOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.TollInvoiceOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.TollInvoiceOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doMLIDCardOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("MLIDCardOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),
        "RetImage": Utils.try_to_json(argv, "--RetImage"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.MLIDCardOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.MLIDCardOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doQrcodeOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("QrcodeOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.QrcodeOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.QrcodeOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doGeneralAccurateOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("GeneralAccurateOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.GeneralAccurateOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.GeneralAccurateOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doFlightInvoiceOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("FlightInvoiceOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.FlightInvoiceOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.FlightInvoiceOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doMixedInvoiceDetect(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("MixedInvoiceDetect", g_param[OptionsDefine.Version])
        return

    param = {
        "ReturnImage": Utils.try_to_json(argv, "--ReturnImage"),
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.MixedInvoiceDetectRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.MixedInvoiceDetect(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doShipInvoiceOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ShipInvoiceOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ShipInvoiceOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ShipInvoiceOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doMLIDPassportOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("MLIDPassportOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "RetImage": Utils.try_to_json(argv, "--RetImage"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.MLIDPassportOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.MLIDPassportOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doVatRollInvoiceOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("VatRollInvoiceOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.VatRollInvoiceOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.VatRollInvoiceOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doQuotaInvoiceOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("QuotaInvoiceOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.QuotaInvoiceOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.QuotaInvoiceOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doVinOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("VinOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.VinOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.VinOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doGeneralFastOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("GeneralFastOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.GeneralFastOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.GeneralFastOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doPropOwnerCertOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("PropOwnerCertOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.PropOwnerCertOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.PropOwnerCertOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doBizLicenseOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("BizLicenseOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.BizLicenseOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.BizLicenseOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doGeneralHandwritingOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("GeneralHandwritingOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),
        "Scene": argv.get("--Scene"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.GeneralHandwritingOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.GeneralHandwritingOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doWaybillOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("WaybillOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.WaybillOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.WaybillOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doInvoiceGeneralOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("InvoiceGeneralOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.InvoiceGeneralOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.InvoiceGeneralOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doHKIDCardOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("HKIDCardOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "DetectFake": Utils.try_to_json(argv, "--DetectFake"),
        "ReturnHeadImage": Utils.try_to_json(argv, "--ReturnHeadImage"),
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.HKIDCardOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.HKIDCardOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doVatInvoiceOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("VatInvoiceOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.VatInvoiceOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.VatInvoiceOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doVerifyBizLicense(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("VerifyBizLicense", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),
        "ImageConfig": argv.get("--ImageConfig"),
        "RegNum": argv.get("--RegNum"),
        "Name": argv.get("--Name"),
        "Address": argv.get("--Address"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.VerifyBizLicenseRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.VerifyBizLicense(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDutyPaidProofOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DutyPaidProofOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DutyPaidProofOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DutyPaidProofOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doGeneralBasicOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("GeneralBasicOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),
        "Scene": argv.get("--Scene"),
        "LanguageType": argv.get("--LanguageType"),
        "IsPdf": Utils.try_to_json(argv, "--IsPdf"),
        "PdfPageNumber": Utils.try_to_json(argv, "--PdfPageNumber"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.GeneralBasicOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.GeneralBasicOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doPermitOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("PermitOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.PermitOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.PermitOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doOrgCodeCertOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("OrgCodeCertOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.OrgCodeCertOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.OrgCodeCertOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doFinanBillSliceOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("FinanBillSliceOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.FinanBillSliceOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.FinanBillSliceOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doBusInvoiceOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("BusInvoiceOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.BusInvoiceOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.BusInvoiceOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doTableOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("TableOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.TableOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.TableOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doRideHailingDriverLicenseOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("RideHailingDriverLicenseOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.RideHailingDriverLicenseOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.RideHailingDriverLicenseOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doHmtResidentPermitOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("HmtResidentPermitOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),
        "CardSide": argv.get("--CardSide"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.HmtResidentPermitOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.HmtResidentPermitOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doArithmeticOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ArithmeticOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ArithmeticOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ArithmeticOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doLicensePlateOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("LicensePlateOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.LicensePlateOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.LicensePlateOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doEstateCertOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("EstateCertOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.EstateCertOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.EstateCertOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doClassifyDetectOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ClassifyDetectOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),
        "DiscernType": Utils.try_to_json(argv, "--DiscernType"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ClassifyDetectOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ClassifyDetectOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doSealOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("SealOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.SealOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.SealOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doTrainTicketOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("TrainTicketOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.TrainTicketOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.TrainTicketOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doTextDetect(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("TextDetect", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.TextDetectRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.TextDetect(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doGeneralEfficientOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("GeneralEfficientOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.GeneralEfficientOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.GeneralEfficientOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doTaxiInvoiceOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("TaxiInvoiceOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.TaxiInvoiceOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.TaxiInvoiceOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doVehicleRegCertOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("VehicleRegCertOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.VehicleRegCertOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.VehicleRegCertOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doInstitutionOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("InstitutionOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.InstitutionOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.InstitutionOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doEnglishOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("EnglishOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),
        "EnableCoordPoint": Utils.try_to_json(argv, "--EnableCoordPoint"),
        "EnableCandWord": Utils.try_to_json(argv, "--EnableCandWord"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.EnglishOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.EnglishOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doResidenceBookletOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ResidenceBookletOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ResidenceBookletOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ResidenceBookletOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doBankCardOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("BankCardOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.BankCardOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.BankCardOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCarInvoiceOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CarInvoiceOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CarInvoiceOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CarInvoiceOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDriverLicenseOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DriverLicenseOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),
        "CardSide": argv.get("--CardSide"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DriverLicenseOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DriverLicenseOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doMainlandPermitOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("MainlandPermitOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),
        "RetProfile": Utils.try_to_json(argv, "--RetProfile"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.MainlandPermitOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.MainlandPermitOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doFormulaOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("FormulaOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.FormulaOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.FormulaOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doPassportOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("PassportOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),
        "Type": argv.get("--Type"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.PassportOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.PassportOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doFinanBillOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("FinanBillOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.FinanBillOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.FinanBillOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doMixedInvoiceOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("MixedInvoiceOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),
        "Types": Utils.try_to_json(argv, "--Types"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.MixedInvoiceOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.MixedInvoiceOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doEduPaperOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("EduPaperOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),
        "Config": argv.get("--Config"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.EduPaperOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.EduPaperOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doRideHailingTransportLicenseOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("RideHailingTransportLicenseOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.RideHailingTransportLicenseOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.RideHailingTransportLicenseOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doVehicleLicenseOCR(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("VehicleLicenseOCR", g_param[OptionsDefine.Version])
        return

    param = {
        "ImageBase64": argv.get("--ImageBase64"),
        "ImageUrl": argv.get("--ImageUrl"),
        "CardSide": argv.get("--CardSide"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.OcrClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.VehicleLicenseOCRRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.VehicleLicenseOCR(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


CLIENT_MAP = {
    "v20181119": ocr_client_v20181119,

}

MODELS_MAP = {
    "v20181119": models_v20181119,

}

ACTION_MAP = {
    "InsuranceBillOCR": doInsuranceBillOCR,
    "VerifyBasicBizLicense": doVerifyBasicBizLicense,
    "VatInvoiceVerify": doVatInvoiceVerify,
    "QueryBarCode": doQueryBarCode,
    "EnterpriseLicenseOCR": doEnterpriseLicenseOCR,
    "BusinessCardOCR": doBusinessCardOCR,
    "IDCardOCR": doIDCardOCR,
    "TollInvoiceOCR": doTollInvoiceOCR,
    "MLIDCardOCR": doMLIDCardOCR,
    "QrcodeOCR": doQrcodeOCR,
    "GeneralAccurateOCR": doGeneralAccurateOCR,
    "FlightInvoiceOCR": doFlightInvoiceOCR,
    "MixedInvoiceDetect": doMixedInvoiceDetect,
    "ShipInvoiceOCR": doShipInvoiceOCR,
    "MLIDPassportOCR": doMLIDPassportOCR,
    "VatRollInvoiceOCR": doVatRollInvoiceOCR,
    "QuotaInvoiceOCR": doQuotaInvoiceOCR,
    "VinOCR": doVinOCR,
    "GeneralFastOCR": doGeneralFastOCR,
    "PropOwnerCertOCR": doPropOwnerCertOCR,
    "BizLicenseOCR": doBizLicenseOCR,
    "GeneralHandwritingOCR": doGeneralHandwritingOCR,
    "WaybillOCR": doWaybillOCR,
    "InvoiceGeneralOCR": doInvoiceGeneralOCR,
    "HKIDCardOCR": doHKIDCardOCR,
    "VatInvoiceOCR": doVatInvoiceOCR,
    "VerifyBizLicense": doVerifyBizLicense,
    "DutyPaidProofOCR": doDutyPaidProofOCR,
    "GeneralBasicOCR": doGeneralBasicOCR,
    "PermitOCR": doPermitOCR,
    "OrgCodeCertOCR": doOrgCodeCertOCR,
    "FinanBillSliceOCR": doFinanBillSliceOCR,
    "BusInvoiceOCR": doBusInvoiceOCR,
    "TableOCR": doTableOCR,
    "RideHailingDriverLicenseOCR": doRideHailingDriverLicenseOCR,
    "HmtResidentPermitOCR": doHmtResidentPermitOCR,
    "ArithmeticOCR": doArithmeticOCR,
    "LicensePlateOCR": doLicensePlateOCR,
    "EstateCertOCR": doEstateCertOCR,
    "ClassifyDetectOCR": doClassifyDetectOCR,
    "SealOCR": doSealOCR,
    "TrainTicketOCR": doTrainTicketOCR,
    "TextDetect": doTextDetect,
    "GeneralEfficientOCR": doGeneralEfficientOCR,
    "TaxiInvoiceOCR": doTaxiInvoiceOCR,
    "VehicleRegCertOCR": doVehicleRegCertOCR,
    "InstitutionOCR": doInstitutionOCR,
    "EnglishOCR": doEnglishOCR,
    "ResidenceBookletOCR": doResidenceBookletOCR,
    "BankCardOCR": doBankCardOCR,
    "CarInvoiceOCR": doCarInvoiceOCR,
    "DriverLicenseOCR": doDriverLicenseOCR,
    "MainlandPermitOCR": doMainlandPermitOCR,
    "FormulaOCR": doFormulaOCR,
    "PassportOCR": doPassportOCR,
    "FinanBillOCR": doFinanBillOCR,
    "MixedInvoiceOCR": doMixedInvoiceOCR,
    "EduPaperOCR": doEduPaperOCR,
    "RideHailingTransportLicenseOCR": doRideHailingTransportLicenseOCR,
    "VehicleLicenseOCR": doVehicleLicenseOCR,

}

AVAILABLE_VERSION_LIST = [
    v20181119.version,

]
AVAILABLE_VERSIONS = {
     'v' + v20181119.version.replace('-', ''): {"help": v20181119_help.INFO,"desc": v20181119_help.DESC},

}


def ocr_action(argv, arglist):
    if "help" in argv:
        versions = sorted(AVAILABLE_VERSIONS.keys())
        opt_v = "--" + OptionsDefine.Version
        version = versions[-1]
        if opt_v in argv:
            version = 'v' + argv[opt_v].replace('-', '')
        if version not in versions:
            print("available versions: %s" % " ".join(AVAILABLE_VERSION_LIST))
            return
        action_str = ""
        docs = AVAILABLE_VERSIONS[version]["help"]
        desc = AVAILABLE_VERSIONS[version]["desc"]
        for action, info in docs.items():
            action_str += "        %s\n" % action
            action_str += Utils.split_str("        ", info["desc"], 120)
        helpstr = HelpTemplate.SERVICE % {"name": "ocr", "desc": desc, "actions": action_str}
        print(helpstr)
    else:
        print(ErrorMsg.FEW_ARG)


def version_merge():
    help_merge = {}
    for v in AVAILABLE_VERSIONS:
        for action in AVAILABLE_VERSIONS[v]["help"]:
            if action not in help_merge:
                help_merge[action] = {}
            help_merge[action]["cb"] = ACTION_MAP[action]
            help_merge[action]["params"] = []
            for param in AVAILABLE_VERSIONS[v]["help"][action]["params"]:
                if param["name"] not in help_merge[action]["params"]:
                    help_merge[action]["params"].append(param["name"])
    return help_merge


def register_arg(command):
    cmd = NiceCommand("ocr", ocr_action)
    command.reg_cmd(cmd)
    cmd.reg_opt("help", "bool")
    cmd.reg_opt(OptionsDefine.Version, "string")
    help_merge = version_merge()

    for actionName, action in help_merge.items():
        c = NiceCommand(actionName, action["cb"])
        cmd.reg_cmd(c)
        c.reg_opt("help", "bool")
        for param in action["params"]:
            c.reg_opt("--" + param, "string")

        for opt in OptionsDefine.ACTION_GLOBAL_OPT:
            stropt = "--" + opt
            c.reg_opt(stropt, "string")


def parse_global_arg(argv):
    params = {}
    for opt in OptionsDefine.ACTION_GLOBAL_OPT:
        stropt = "--" + opt
        if stropt in argv:
            params[opt] = argv[stropt]
        else:
            params[opt] = None
    if params[OptionsDefine.Version]:
        params[OptionsDefine.Version] = "v" + params[OptionsDefine.Version].replace('-', '')

    config_handle = Configure()
    profile = config_handle.profile
    if ("--" + OptionsDefine.Profile) in argv:
        profile = argv[("--" + OptionsDefine.Profile)]

    is_conexist, conf_path = config_handle._profile_existed(profile + "." + config_handle.configure)
    is_creexist, cred_path = config_handle._profile_existed(profile + "." + config_handle.credential)
    config = {}
    cred = {}
    if is_conexist:
        config = config_handle._load_json_msg(conf_path)
    if is_creexist:
        cred = config_handle._load_json_msg(cred_path)
    if os.environ.get(OptionsDefine.ENV_SECRET_ID):
        cred[OptionsDefine.SecretId] = os.environ.get(OptionsDefine.ENV_SECRET_ID)
    if os.environ.get(OptionsDefine.ENV_SECRET_KEY):
        cred[OptionsDefine.SecretKey] = os.environ.get(OptionsDefine.ENV_SECRET_KEY)
    if os.environ.get(OptionsDefine.ENV_REGION):
        config[OptionsDefine.Region] = os.environ.get(OptionsDefine.ENV_REGION)

    for param in params.keys():
        if param == OptionsDefine.Version:
            continue
        if params[param] is None:
            if param in [OptionsDefine.SecretKey, OptionsDefine.SecretId]:
                if param in cred:
                    params[param] = cred[param]
                else:
                    raise Exception("%s is invalid" % param)
            else:
                if param in config:
                    params[param] = config[param]
                elif param == OptionsDefine.Region:
                    raise Exception("%s is invalid" % OptionsDefine.Region)
    try:
        if params[OptionsDefine.Version] is None:
            version = config["ocr"][OptionsDefine.Version]
            params[OptionsDefine.Version] = "v" + version.replace('-', '')

        if params[OptionsDefine.Endpoint] is None:
            params[OptionsDefine.Endpoint] = config["ocr"][OptionsDefine.Endpoint]
    except Exception as err:
        raise Exception("config file:%s error, %s" % (conf_path, str(err)))
    versions = sorted(AVAILABLE_VERSIONS.keys())
    if params[OptionsDefine.Version] not in versions:
        raise Exception("available versions: %s" % " ".join(AVAILABLE_VERSION_LIST))
    return params


def show_help(action, version):
    docs = AVAILABLE_VERSIONS[version]["help"][action]
    desc = AVAILABLE_VERSIONS[version]["desc"]
    docstr = ""
    for param in docs["params"]:
        docstr += "        %s\n" % ("--" + param["name"])
        docstr += Utils.split_str("        ", param["desc"], 120)

    helpmsg = HelpTemplate.ACTION % {"name": action, "service": "ocr", "desc": desc, "params": docstr}
    print(helpmsg)


def get_actions_info():
    config = Configure()
    new_version = max(AVAILABLE_VERSIONS.keys())
    version = new_version
    try:
        profile = config._load_json_msg(os.path.join(config.cli_path, "default.configure"))
        version = profile["ocr"]["version"]
        version = "v" + version.replace('-', '')
    except Exception:
        pass
    if version not in AVAILABLE_VERSIONS.keys():
        version = new_version
    return AVAILABLE_VERSIONS[version]["help"]
