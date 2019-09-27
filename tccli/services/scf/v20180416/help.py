# -*- coding: utf-8 -*-
DESC = "scf-2018-04-16"
INFO = {
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
      },
      {
        "name": "Namespace",
        "desc": "函数所属命名空间"
      },
      {
        "name": "Role",
        "desc": "函数绑定的角色"
      },
      {
        "name": "ClsLogsetId",
        "desc": "函数日志投递到的CLS LogsetID"
      },
      {
        "name": "ClsTopicId",
        "desc": "函数日志投递到的CLS TopicID"
      },
      {
        "name": "Type",
        "desc": "函数类型，默认值为Event，创建触发器函数请填写Event，创建HTTP函数级服务请填写HTTP"
      },
      {
        "name": "CodeSource",
        "desc": "CodeSource 代码来源，支持以下'ZipFile', 'Cos', 'Demo', 'TempCos', 'Git'之一，使用Git来源必须指定此字段"
      }
    ],
    "desc": "该接口根据传入参数创建新的函数。"
  },
  "ListVersionByFunction": {
    "params": [
      {
        "name": "FunctionName",
        "desc": "函数ID"
      },
      {
        "name": "Namespace",
        "desc": "命名空间"
      }
    ],
    "desc": "该接口根据传入的参数查询函数的版本。"
  },
  "UpdateNamespace": {
    "params": [
      {
        "name": "Namespace",
        "desc": "命名空间名称"
      },
      {
        "name": "Description",
        "desc": "命名空间描述"
      }
    ],
    "desc": "更新命名空间"
  },
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
      },
      {
        "name": "Namespace",
        "desc": "函数所属命名空间"
      }
    ],
    "desc": "该接口根据传入参数删除函数。"
  },
  "PublishVersion": {
    "params": [
      {
        "name": "FunctionName",
        "desc": "发布函数的名称"
      },
      {
        "name": "Description",
        "desc": "函数的描述"
      },
      {
        "name": "Namespace",
        "desc": "函数的命名空间"
      }
    ],
    "desc": "该接口用于用户发布新版本函数。"
  },
  "ListNamespaces": {
    "params": [
      {
        "name": "Limit",
        "desc": "返回数据长度，默认值为 20"
      },
      {
        "name": "Offset",
        "desc": "数据的偏移量，默认值为 0"
      },
      {
        "name": "Orderby",
        "desc": "根据哪个字段进行返回结果排序,支持以下字段：Name,Updatetime"
      },
      {
        "name": "Order",
        "desc": "以升序还是降序的方式返回结果，可选值 ASC 和 DESC"
      }
    ],
    "desc": "列出命名空间列表"
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
        "name": "Namespace",
        "desc": "函数所属命名空间"
      },
      {
        "name": "ShowCode",
        "desc": "是否显示代码, TRUE表示显示代码，FALSE表示不显示代码,大于1M的入口文件不会显示"
      }
    ],
    "desc": "该接口获取某个函数的详细信息，包括名称、代码、处理方法、关联触发器和超时时间等字段。"
  },
  "GetFunctionAddress": {
    "params": [
      {
        "name": "FunctionName",
        "desc": "函数的名称"
      },
      {
        "name": "Qualifier",
        "desc": "函数的版本"
      },
      {
        "name": "Namespace",
        "desc": "函数的命名空间"
      }
    ],
    "desc": "该接口用于获取函数代码包的下载地址。"
  },
  "DeleteNamespace": {
    "params": [
      {
        "name": "Namespace",
        "desc": "命名空间名称"
      }
    ],
    "desc": "该接口根据传入的参数创建命名空间。"
  },
  "CreateTrigger": {
    "params": [
      {
        "name": "FunctionName",
        "desc": "新建触发器绑定的函数名称"
      },
      {
        "name": "TriggerName",
        "desc": "新建触发器名称。如果是定时触发器，名称支持英文字母、数字、连接符和下划线，最长100个字符；如果是cos触发器，需要是对应cos存储桶适用于XML API的访问域名(例如:5401-5ff414-12345.cos.ap-shanghai.myqcloud.com);如果是其他触发器，见具体触发器绑定参数的说明"
      },
      {
        "name": "Type",
        "desc": "触发器类型，目前支持 cos 、cmq、 timer、 ckafka类型"
      },
      {
        "name": "TriggerDesc",
        "desc": "触发器对应的参数，如果是 timer 类型的触发器其内容是 Linux cron 表达式。如果是cos类型的触发器，其内容是json字符串 {\"event\":\"cos:ObjectCreated:*\",\"filter\":{\"Prefix\":\"\",\"Suffix\":\"\"}},其中event是触发的cos事件，fitler中Prefix是对应的文件前缀过滤条件，Suffix是后缀过滤条件，如果不需要filter条件可不传。如果是其他触发器，见具体触发器说明"
      },
      {
        "name": "Namespace",
        "desc": "函数的命名空间"
      },
      {
        "name": "Qualifier",
        "desc": "函数的版本"
      },
      {
        "name": "Enable",
        "desc": "触发器的初始是能状态 OPEN表示开启 CLOSE表示关闭"
      }
    ],
    "desc": "该接口根据参数输入设置新的触发方式。"
  },
  "CreateNamespace": {
    "params": [
      {
        "name": "Namespace",
        "desc": "命名空间名称"
      },
      {
        "name": "Description",
        "desc": "命名空间描述"
      }
    ],
    "desc": "该接口根据传入的参数创建命名空间。"
  },
  "CopyFunction": {
    "params": [
      {
        "name": "FunctionName",
        "desc": "要复制的函数的名称"
      },
      {
        "name": "NewFunctionName",
        "desc": "新函数的名称"
      },
      {
        "name": "Namespace",
        "desc": "要复制的函数所在的命名空间，默认为default"
      },
      {
        "name": "TargetNamespace",
        "desc": "将函数复制到的命名空间，默认为default"
      },
      {
        "name": "Description",
        "desc": "新函数的描述"
      },
      {
        "name": "TargetRegion",
        "desc": "要将函数复制到的地域，不填则默认为当前地域"
      },
      {
        "name": "Override",
        "desc": "如果目标Namespace下已有同名函数，是否覆盖，默认为否\n（注意：如果选择覆盖，会导致同名函数被删除，请慎重操作）\nTRUE：覆盖同名函数\nFALSE：不覆盖同名函数"
      },
      {
        "name": "CopyConfiguration",
        "desc": "是否复制函数的属性，包括环境变量、内存、超时、函数描述、标签、VPC等，默认为是。\nTRUE：复制函数配置\nFALSE：不复制函数配置"
      }
    ],
    "desc": "复制一个函数，您可以选择将复制出的新函数放置在特定的Region和Namespace。\n注：本接口**不会**复制函数的以下对象或属性：\n1. 函数的触发器\n2. 除了$LATEST以外的其它版本\n3. 函数配置的日志投递到的CLS目标。\n\n如有需要，您可以在复制后手动配置新函数。"
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
        "name": "Namespace",
        "desc": "函数所属命名空间"
      },
      {
        "name": "VpcConfig",
        "desc": "函数的私有网络配置"
      },
      {
        "name": "Role",
        "desc": "函数绑定的角色"
      },
      {
        "name": "ClsLogsetId",
        "desc": "日志投递到的cls日志集ID"
      },
      {
        "name": "ClsTopicId",
        "desc": "日志投递到的cls Topic ID"
      },
      {
        "name": "Publish",
        "desc": "在更新时是否同步发布新版本，默认为：FALSE，不发布"
      },
      {
        "name": "L5Enable",
        "desc": "是否开启L5访问能力，TRUE 为开启，FALSE为关闭"
      }
    ],
    "desc": "该接口根据传入参数更新函数配置。"
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
      },
      {
        "name": "Namespace",
        "desc": "命名空间"
      },
      {
        "name": "Description",
        "desc": "函数描述，支持模糊搜索"
      },
      {
        "name": "Filters",
        "desc": "过滤条件。\n- tag:tag-key - String - 是否必填：否 - （过滤条件）按照标签键值对进行过滤。 tag-key使用具体的标签键进行替换。\n\n每次请求的Filters的上限为10，Filter.Values的上限为5。"
      }
    ],
    "desc": "该接口根据传入的查询参数返回相关函数信息。"
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
        "name": "Namespace",
        "desc": "函数所属命名空间"
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
        "desc": "以升序还是降序的方式对日志进行排序，可选值 desc和 asc"
      },
      {
        "name": "OrderBy",
        "desc": "根据某个字段排序日志,支持以下字段：function_name, duration, mem_usage, start_time"
      },
      {
        "name": "Filter",
        "desc": "日志过滤条件。可用来区分正确和错误日志，filter.retCode=not0 表示只返回错误日志，filter.retCode=is0 表示只返回正确日志，不传，则返回所有日志"
      },
      {
        "name": "Namespace",
        "desc": "函数的命名空间"
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
      },
      {
        "name": "SearchContext",
        "desc": "服务日志相关参数，第一页日志 Offset 为空字符串，后续分页按响应字段里的SearchContext填写"
      }
    ],
    "desc": "该接口根据指定的日志查询条件返回函数运行日志。"
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
        "name": "Namespace",
        "desc": "函数所属命名空间"
      },
      {
        "name": "CosBucketRegion",
        "desc": "对象存储的地域，注：北京分为ap-beijing和ap-beijing-1"
      },
      {
        "name": "EnvId",
        "desc": "函数所属环境"
      },
      {
        "name": "Publish",
        "desc": "在更新时是否同步发布新版本，默认为：FALSE，不发布"
      },
      {
        "name": "Code",
        "desc": "函数代码"
      },
      {
        "name": "CodeSource",
        "desc": "代码来源方式，支持以下'ZipFile', 'Cos', 'Inline', 'TempCos', 'Git' 之一，使用Git来源必须指定此字段"
      }
    ],
    "desc": "该接口根据传入参数更新函数代码。"
  }
}