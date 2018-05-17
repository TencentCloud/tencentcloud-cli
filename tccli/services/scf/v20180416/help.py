# -*- coding: utf-8 -*-
DESC = "scf-2018-04-16"
INFO = {
  "Invoke": {
    "params": [
      {
        "name": "FunctionName",
        "desc": "函数名称。"
      },
      {
        "name": "InvocationType",
        "desc": "RequestResponse(同步) 和 Event(异步)，默认为同步。"
      },
      {
        "name": "Qualifier",
        "desc": "触发函数的版本号。"
      },
      {
        "name": "ClientContext",
        "desc": "运行函数时的参数，以json格式传入，最大支持的参数长度是 1M。"
      },
      {
        "name": "LogType",
        "desc": "同步调用时指定该字段，返回值会包含4K的日志，可选值为None和Tail，默认值为None。当该值为Tail时，返回参数中的logMsg字段会包含对应的函数执行日志。"
      }
    ],
    "desc": "Invoke用于运行函数"
  }
}