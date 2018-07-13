# -*- coding: utf-8 -*-
DESC = "cr-2018-03-21"
INFO = {
  "DownloadReport": {
    "params": [
      {
        "name": "Module",
        "desc": "模块名"
      },
      {
        "name": "Operation",
        "desc": "操作名"
      },
      {
        "name": "ReportDate",
        "desc": "报告日期"
      }
    ],
    "desc": "客户调用该接口下载指定日期的催收报告"
  },
  "DescribeTaskStatus": {
    "params": [
      {
        "name": "Module",
        "desc": "模块名"
      },
      {
        "name": "Operation",
        "desc": "操作名"
      },
      {
        "name": "TaskId",
        "desc": "任务ID"
      }
    ],
    "desc": "客户调用该接口查看任务执行状态。输入任务ID，输出任务执行状态或者结果"
  },
  "UploadFile": {
    "params": [
      {
        "name": "Module",
        "desc": "模块名"
      },
      {
        "name": "Operation",
        "desc": "操作名"
      },
      {
        "name": "FileUrl",
        "desc": "文件上传地址，要求地址协议为HTTPS，且URL端口必须为443"
      },
      {
        "name": "FileName",
        "desc": "文件名"
      },
      {
        "name": "FileDate",
        "desc": "文件日期"
      }
    ],
    "desc": "客户通过调用该接口上传需催收文档，格式需为csv或者excel格式。接口返回任务ID。"
  }
}