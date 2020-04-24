# -*- coding: utf-8 -*-
DESC = "cr-2018-03-21"
INFO = {
  "DownloadReport": {
    "params": [
      {
        "name": "Module",
        "desc": "模块名，本接口取值：Report"
      },
      {
        "name": "Operation",
        "desc": "操作名，本接口取值：DownloadReport"
      },
      {
        "name": "ReportDate",
        "desc": "报告日期，格式为YYYY-MM-DD"
      },
      {
        "name": "InstId",
        "desc": "实例ID，不传默认为系统分配的初始实例。"
      }
    ],
    "desc": "用于下载结果报表。当日23:00后，可获取当日到期/逾期提醒结果，次日00:30后，可获取昨日回访结果。"
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
  "ApplyBlackList": {
    "params": [
      {
        "name": "Module",
        "desc": "模块名，本接口取值：account"
      },
      {
        "name": "Operation",
        "desc": "操作名，本接口取值：ApplyBlackList"
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
    "desc": "提交黑名单后，黑名单中有效期内的号码将停止拨打，适用于到期/逾期提醒、回访场景。"
  },
  "DescribeRecords": {
    "params": [
      {
        "name": "Module",
        "desc": "模块名，本接口取值：Record"
      },
      {
        "name": "Operation",
        "desc": "操作名，本接口取值：List"
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
        "desc": "查询起始日期，格式为YYYY-MM-DD"
      },
      {
        "name": "EndBizDate",
        "desc": "查询结束日期，格式为YYYY-MM-DD"
      },
      {
        "name": "Offset",
        "desc": "分页参数，索引，默认为0"
      },
      {
        "name": "Limit",
        "desc": "分页参数，页长，默认为20"
      },
      {
        "name": "InstId",
        "desc": "实例ID，不传默认为系统分配的初始实例"
      }
    ],
    "desc": "用于获取指定案件的录音地址，次日早上8:00后可查询前日录音。"
  },
  "DescribeCreditResult": {
    "params": [
      {
        "name": "Module",
        "desc": "模块名，本接口取值：Credit"
      },
      {
        "name": "Operation",
        "desc": "操作名，本接口取值：Get"
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
        "desc": "请求日期，格式为YYYY-MM-DD"
      }
    ],
    "desc": "根据信审任务ID和请求日期，获取相关信审结果。"
  },
  "DownloadDialogueText": {
    "params": [
      {
        "name": "Module",
        "desc": "模块名，本接口取值：Report"
      },
      {
        "name": "Operation",
        "desc": "操作名，本接口取值：DownloadTextReport"
      },
      {
        "name": "ReportDate",
        "desc": "报告日期，格式为YYYY-MM-DD"
      },
      {
        "name": "InstId",
        "desc": "实例ID"
      }
    ],
    "desc": "用于获取指定案件的对话文本内容，次日早上8:00后可查询前日对话文本内容。"
  },
  "DescribeTaskStatus": {
    "params": [
      {
        "name": "Module",
        "desc": "模块名，本接口取值：Task"
      },
      {
        "name": "Operation",
        "desc": "操作名，本接口取值：DescribeTaskStatus"
      },
      {
        "name": "TaskId",
        "desc": "任务ID，\"上传文件\"接口返回的DataResId，形如abc-xyz123"
      },
      {
        "name": "InstId",
        "desc": "实例ID，不传默认为系统分配的初始实例。"
      }
    ],
    "desc": "根据上传文件接口的输出参数DataResId，获取相关上传结果。"
  },
  "UploadDataFile": {
    "params": [
      {
        "name": "Module",
        "desc": "模块名，本接口取值：Data"
      },
      {
        "name": "Operation",
        "desc": "操作名，本接口取值：Upload"
      },
      {
        "name": "FileName",
        "desc": "文件名"
      },
      {
        "name": "UploadModel",
        "desc": "<p>上传类型，不填默认到期/逾期提醒文件，取值范围：</p><ul style=\"margin-bottom:0px;\"><li>data：到期/逾期提醒文件</li><li>repay：到期/逾期提醒停拨文件</li><li>callback：回访文件</li><li>callstop：回访停拨文件</li><li>blacklist：黑名单文件</li></ul>"
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
    "desc": "上传文件，接口返回数据任务ID，支持xlsx、xls、csv、zip格式。"
  },
  "QueryInstantData": {
    "params": [
      {
        "name": "Module",
        "desc": "模块名，本接口取值：Data"
      },
      {
        "name": "Operation",
        "desc": "操作名，本接口取值：Query"
      },
      {
        "name": "ProductId",
        "desc": "产品ID"
      },
      {
        "name": "InstanceId",
        "desc": "实例ID，不传默认为系统分配的初始实例"
      },
      {
        "name": "QueryModel",
        "desc": "查询类型：callRecord 通话记录"
      },
      {
        "name": "Data",
        "desc": "查询参数"
      }
    ],
    "desc": "实时数据查询"
  },
  "DownloadRecordList": {
    "params": [
      {
        "name": "Module",
        "desc": "模块名，本接口取值：Record"
      },
      {
        "name": "Operation",
        "desc": "操作名，本接口取值：DownloadList"
      },
      {
        "name": "BizDate",
        "desc": "录音日期，格式为YYYY-MM-DD"
      },
      {
        "name": "InstId",
        "desc": "实例ID"
      }
    ],
    "desc": "<p>用于获取录音下载链接清单，次日早上8:00后可查询前日录音清单。</p>\n<p>注意：录音清单中的录音下载链接仅次日20:00之前有效，请及时下载。</p>"
  },
  "UploadDataJson": {
    "params": [
      {
        "name": "Module",
        "desc": "模块名，本接口取值：Data"
      },
      {
        "name": "Operation",
        "desc": "操作名，本接口取值：UploadJson"
      },
      {
        "name": "Data",
        "desc": "报文信息"
      },
      {
        "name": "UploadModel",
        "desc": "<p>上传类型，不填默认到期/逾期提醒数据，取值范围：</p><ul style=\"margin-bottom:0px;\"><li>data：到期/逾期提醒数据</li><li>repay：到期/逾期提醒停拨数据</li></ul>"
      },
      {
        "name": "InstanceId",
        "desc": "实例ID，不传默认为系统分配的初始实例。"
      }
    ],
    "desc": "上传Json格式数据，接口返回数据任务ID"
  },
  "ApplyCreditAudit": {
    "params": [
      {
        "name": "Module",
        "desc": "模块名，本接口取值：Credit"
      },
      {
        "name": "Operation",
        "desc": "操作名，本接口取值：Apply"
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