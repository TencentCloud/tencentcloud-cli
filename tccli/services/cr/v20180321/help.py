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
  "DescribeRecords": {
    "params": [
      {
        "name": "Module",
        "desc": "模块"
      },
      {
        "name": "Operation",
        "desc": "操作"
      },
      {
        "name": "ProductId",
        "desc": "产品ID"
      },
      {
        "name": "AccountNum",
        "desc": "案件编号"
      },
      {
        "name": "CalledPhone",
        "desc": "被叫号码"
      },
      {
        "name": "StartBizDate",
        "desc": "查询起始日期"
      },
      {
        "name": "EndBizDate",
        "desc": "查询结束日期"
      },
      {
        "name": "Offset",
        "desc": "分页参数，索引，从0开始"
      },
      {
        "name": "Limit",
        "desc": "分页参数，页长"
      }
    ],
    "desc": "查询录音，返回录音列表。"
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
    "desc": "客户通过调用该接口上传需催收文档，格式需为excel格式。接口返回任务ID。"
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
  "UploadDataFile": {
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
        "name": "FileName",
        "desc": "文件名"
      },
      {
        "name": "UploadModel",
        "desc": "上传类型，不填默认催收文件，催收文件为data，还款文件为repay。"
      },
      {
        "name": "File",
        "desc": "文件，文件与文件地址上传只可选用一种，使用 Content-Type: multipart/form-data 协议来上传二进制流文件。"
      },
      {
        "name": "FileUrl",
        "desc": "文件上传地址"
      }
    ],
    "desc": "客户通过调用该接口上传需催收文档或还款文档，接口返回任务ID。"
  },
  "ApplyBlackList": {
    "params": [
      {
        "name": "Module",
        "desc": "模块"
      },
      {
        "name": "Operation",
        "desc": "操作"
      },
      {
        "name": "BlackList",
        "desc": "黑名单列表"
      }
    ],
    "desc": "提交黑名单申请。"
  }
}