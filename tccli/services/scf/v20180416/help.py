# -*- coding: utf-8 -*-
DESC = "scf-2018-04-16"
INFO = {
  "Invoke": {
    "params": [
      {
        "name": "FunctionName",
        "desc": "函数名称"
      },
      {
        "name": "InvocationType",
        "desc": "RequestResponse(同步) 和 Event(异步)，默认为同步"
      },
      {
        "name": "Qualifier",
        "desc": "触发函数的版本号"
      },
      {
        "name": "ClientContext",
        "desc": "运行函数时的参数，以json格式传入，最大支持的参数长度是 1M"
      },
      {
        "name": "LogType",
        "desc": "同步调用时指定该字段，返回值会包含4K的日志，可选值为None和Tail，默认值为None。当该值为Tail时，返回参数中的logMsg字段会包含对应的函数执行日志"
      },
      {
        "name": "Namespace",
        "desc": "命名空间"
      }
    ],
    "desc": "该接口用于运行函数。"
  },
  "DeleteFunction": {
    "params": [
      {
        "name": "FunctionName",
        "desc": "要删除的函数名称"
      }
    ],
    "desc": "该接口根据传入参数删除函数。"
  },
  "GetFunction": {
    "params": [
      {
        "name": "FunctionName",
        "desc": "需要获取详情的函数名称"
      },
      {
        "name": "Qualifier",
        "desc": "函数的版本号"
      },
      {
        "name": "ShowCode",
        "desc": "是否显示代码, TRUE表示显示代码，FALSE表示不显示代码,大于1M的入口文件不会显示"
      }
    ],
    "desc": "该接口获取某个函数的详细信息，包括名称、代码、处理方法、关联触发器和超时时间等字段。"
  },
  "ListFunctions": {
    "params": [
      {
        "name": "Order",
        "desc": "以升序还是降序的方式返回结果，可选值 ASC 和 DESC"
      },
      {
        "name": "Orderby",
        "desc": "根据哪个字段进行返回结果排序,支持以下字段：AddTime, ModTime, FunctionName"
      },
      {
        "name": "Offset",
        "desc": "数据偏移量，默认值为 0"
      },
      {
        "name": "Limit",
        "desc": "返回数据长度，默认值为 20"
      },
      {
        "name": "SearchKey",
        "desc": "支持FunctionName模糊匹配"
      }
    ],
    "desc": "该接口根据传入的查询参数返回相关函数信息。"
  },
  "CreateTrigger": {
    "params": [
      {
        "name": "FunctionName",
        "desc": "新建触发器绑定的函数名称"
      },
      {
        "name": "TriggerName",
        "desc": "新建触发器名称。如果是定时触发器，名称支持英文字母、数字、连接符和下划线，最长100个字符；如果是其他触发器，见具体触发器绑定参数的说明"
      },
      {
        "name": "Type",
        "desc": "触发器类型，目前支持 cos 、cmq、 timers、 ckafka类型"
      },
      {
        "name": "TriggerDesc",
        "desc": "触发器对应的参数，如果是 timer 类型的触发器其内容是 Linux cron 表达式，如果是其他触发器，见具体触发器说明"
      },
      {
        "name": "Qualifier",
        "desc": "函数的版本"
      }
    ],
    "desc": "该接口根据参数输入设置新的触发方式。"
  },
  "UpdateFunctionConfiguration": {
    "params": [
      {
        "name": "FunctionName",
        "desc": "要修改的函数名称"
      },
      {
        "name": "Description",
        "desc": "函数描述。最大支持 1000 个英文字母、数字、空格、逗号和英文句号，支持中文"
      },
      {
        "name": "MemorySize",
        "desc": "函数运行时内存大小，默认为 128 M，可选范 128 M-1536 M"
      },
      {
        "name": "Timeout",
        "desc": "函数最长执行时间，单位为秒，可选值范 1-300 秒，默认为 3 秒"
      },
      {
        "name": "Runtime",
        "desc": "函数运行环境，目前仅支持 Python2.7，Python3.6，Nodejs6.10，PHP5， PHP7，Golang1 和 Java8"
      },
      {
        "name": "Environment",
        "desc": "函数的环境变量"
      },
      {
        "name": "VpcConfig",
        "desc": "函数的私有网络配置"
      }
    ],
    "desc": "该接口根据传入参数更新函数配置。"
  },
  "GetFunctionLogs": {
    "params": [
      {
        "name": "FunctionName",
        "desc": "函数的名称"
      },
      {
        "name": "Offset",
        "desc": "数据的偏移量，Offset+Limit不能大于10000"
      },
      {
        "name": "Limit",
        "desc": "返回数据的长度，Offset+Limit不能大于10000"
      },
      {
        "name": "Order",
        "desc": "以升序还是降序的方式对日志进行排序，可选值 desc和 acs"
      },
      {
        "name": "OrderBy",
        "desc": "根据某个字段排序日志,支持以下字段：startTime、functionName、requestId、duration和 memUsage"
      },
      {
        "name": "Filter",
        "desc": "日志过滤条件。可用来区分正确和错误日志，filter.retCode=not0 表示只返回错误日志，filter.retCode=is0 表示只返回正确日志，不传，则返回所有日志"
      },
      {
        "name": "Qualifier",
        "desc": "函数的版本"
      },
      {
        "name": "FunctionRequestId",
        "desc": "执行该函数对应的requestId"
      },
      {
        "name": "StartTime",
        "desc": "查询的具体日期，例如：2017-05-16 20:00:00，只能与endtime相差一天之内"
      },
      {
        "name": "EndTime",
        "desc": "查询的具体日期，例如：2017-05-16 20:59:59，只能与startTime相差一天之内"
      }
    ],
    "desc": "该接口根据设置的日志查询条件返回函数日志。"
  },
  "CreateFunction": {
    "params": [
      {
        "name": "FunctionName",
        "desc": "创建的函数名称，函数名称支持26个英文字母大小写、数字、连接符和下划线，第一个字符只能以字母开头，最后一个字符不能为连接符或者下划线，名称长度2-60"
      },
      {
        "name": "Code",
        "desc": "函数的代码. 注意：不能同时指定Cos与ZipFile"
      },
      {
        "name": "Handler",
        "desc": "函数处理方法名称，名称格式支持 \"文件名称.方法名称\" 形式，文件名称和函数名称之间以\".\"隔开，文件名称和函数名称要求以字母开始和结尾，中间允许插入字母、数字、下划线和连接符，文件名称和函数名字的长度要求是 2-60 个字符"
      },
      {
        "name": "Description",
        "desc": "函数描述,最大支持 1000 个英文字母、数字、空格、逗号、换行符和英文句号，支持中文"
      },
      {
        "name": "MemorySize",
        "desc": "函数运行时内存大小，默认为 128M，可选范围 128MB-1536MB，并且以 128MB 为阶梯"
      },
      {
        "name": "Timeout",
        "desc": "函数最长执行时间，单位为秒，可选值范围 1-300 秒，默认为 3 秒"
      },
      {
        "name": "Environment",
        "desc": "函数的环境变量"
      },
      {
        "name": "Runtime",
        "desc": "函数运行环境，目前仅支持 Python2.7，Python3.6，Nodejs6.10， PHP5， PHP7，Golang1 和 Java8，默认Python2.7"
      },
      {
        "name": "VpcConfig",
        "desc": "函数的私有网络配置"
      }
    ],
    "desc": "该接口根据传入参数创建新的函数。"
  },
  "DeleteTrigger": {
    "params": [
      {
        "name": "FunctionName",
        "desc": "函数的名称"
      },
      {
        "name": "TriggerName",
        "desc": "要删除的触发器名称"
      },
      {
        "name": "Type",
        "desc": "要删除的触发器类型，目前支持 cos 、cmq、 timer、ckafka 类型"
      },
      {
        "name": "TriggerDesc",
        "desc": "如果删除的触发器类型为 COS 触发器，该字段为必填值，存放 JSON 格式的数据 {\"event\":\"cos:ObjectCreated:*\"}，数据内容和 SetTrigger 接口中该字段的格式相同；如果删除的触发器类型为定时触发器或 CMQ 触发器，可以不指定该字段"
      },
      {
        "name": "Qualifier",
        "desc": "函数的版本信息"
      }
    ],
    "desc": "该接口根据参数传入删除已有的触发方式。"
  },
  "UpdateFunctionCode": {
    "params": [
      {
        "name": "Handler",
        "desc": "函数处理方法名称。名称格式支持“文件名称.函数名称”形式，文件名称和函数名称之间以\".\"隔开，文件名称和函数名称要求以字母开始和结尾，中间允许插入字母、数字、下划线和连接符，文件名称和函数名字的长度要求 2-60 个字符"
      },
      {
        "name": "FunctionName",
        "desc": "要修改的函数名称"
      },
      {
        "name": "CosBucketName",
        "desc": "对象存储桶名称"
      },
      {
        "name": "CosObjectName",
        "desc": "对象存储对象路径"
      },
      {
        "name": "ZipFile",
        "desc": "包含函数代码文件及其依赖项的 zip 格式文件，使用该接口时要求将 zip 文件的内容转成 base64 编码，最大支持20M"
      },
      {
        "name": "CosBucketRegion",
        "desc": "对象存储的地域，地域为北京时需要传入ap-beijing,北京一区时需要传递ap-beijing-1，其他的地域不需要传递。"
      }
    ],
    "desc": "该接口根据传入参数更新函数代码。"
  }
}