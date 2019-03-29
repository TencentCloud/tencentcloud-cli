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
      },
      {
        "name": "InstId",
        "desc": "实例ID，不传默认为系统分配的初始实例。"
      }
    ],
    "desc": "用于下载当日催收和回访结果报表。当日23:00后，可获取当日催收结果，次日00:30后，可获取昨日回访结果。"
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
      },
      {
        "name": "InstId",
        "desc": "实例ID，不传默认为系统分配的初始实例"
      }
    ],
    "desc": "用于获取指定案件的录音地址，次日早上8:00后可查询前日录音。"
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
  "DescribeCreditResult": {
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
        "name": "InstId",
        "desc": "实例ID"
      },
      {
        "name": "ProductId",
        "desc": "产品ID，形如P******。"
      },
      {
        "name": "CaseId",
        "desc": "信审任务ID"
      },
      {
        "name": "RequestDate",
        "desc": "请求日期"
      }
    ],
    "desc": "根据信审任务ID和请求日期，获取相关信审结果。"
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
        "desc": "任务ID，形如abc-a0b1c2xyz"
      }
    ],
    "desc": "根据上传文件接口的输出参数DataResId，获取相关上传结果。"
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
        "desc": "<p>上传类型，不填默认催收文件，取值范围：</p><ul style=\"margin-bottom:0px;\"><li>data：催收文件</li><li>repay：还款文件</li><li>callback：回访文件</li></ul>"
      },
      {
        "name": "File",
        "desc": "文件，文件与文件地址上传只可选用一种，必须使用multipart/form-data协议来上传二进制流文件，建议使用xlsx格式，大小不超过5MB。"
      },
      {
        "name": "FileUrl",
        "desc": "文件上传地址，文件与文件地址上传只可选用一种，大小不超过50MB。"
      },
      {
        "name": "InstId",
        "desc": "实例ID，不传默认为系统分配的初始实例。"
      }
    ],
    "desc": "<p>该接口包含上传下列文件：</p>\n<ol style=\"margin-bottom:10px;\">\n  <li>入催文件：用于每天入催文件的上传</li>\n  <li>回访文件：用于每天贷中回访文件的上传</li>\n  <li>还款文件：实时上传当前已还款客户，用于还款客户的实时停催</li>\n</ol>\n接口返回数据任务ID，支持xlsx、xls、csv、zip格式，文档大小不超过50MB。"
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
      },
      {
        "name": "InstId",
        "desc": "实例ID，不传默认为系统分配的初始实例"
      }
    ],
    "desc": "加入黑名单的客户，将停止拨打。用于：\n将客户进行黑名单的增加和移除，用于对某些客户阶段性停催。\n"
  },
  "ApplyCreditAudit": {
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
        "name": "InstId",
        "desc": "实例ID"
      },
      {
        "name": "ProductId",
        "desc": "产品ID，形如P******。"
      },
      {
        "name": "CaseId",
        "desc": "信审任务ID，同一天内，同一InstId下，同一CaseId只能调用一次。"
      },
      {
        "name": "CallbackUrl",
        "desc": "回调地址"
      },
      {
        "name": "Data",
        "desc": "JSON格式的业务字段。"
      }
    ],
    "desc": "提交信审外呼申请，返回当次请求日期。"
  }
}