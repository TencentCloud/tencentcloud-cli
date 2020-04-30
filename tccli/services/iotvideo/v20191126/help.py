# -*- coding: utf-8 -*-
DESC = "iotvideo-2019-11-26"
INFO = {
  "DescribeOtaVersions": {
    "params": [
      {
        "name": "Offset",
        "desc": "分页偏移量"
      },
      {
        "name": "Limit",
        "desc": "每页数量，0<取值范围<=100"
      },
      {
        "name": "ProductId",
        "desc": "产品ID，为空时查询客户所有产品的版本信息"
      },
      {
        "name": "OtaVersion",
        "desc": "版本号，支持模糊匹配"
      },
      {
        "name": "PubStatus",
        "desc": "版本类型 1未发布 2测试发布 3正式发布 4禁用"
      }
    ],
    "desc": "本接口（DescribeOtaVersions）用于查询固件版本信息列表。"
  },
  "DisableOtaVersion": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品ID"
      },
      {
        "name": "OtaVersion",
        "desc": "固件版本号，格式为x.y.z， x，y 范围0-63，z范围1~524288"
      },
      {
        "name": "Operator",
        "desc": "操作人"
      }
    ],
    "desc": "本接口（DisableOtaVersion）用于禁用固件版本。"
  },
  "DescribeBindDev": {
    "params": [
      {
        "name": "AccessId",
        "desc": "终端用户在IoT Video上的唯一标识ID"
      }
    ],
    "desc": "本接口（DescribeBindDev）用于查询终端用户绑定的设备列表。"
  },
  "DescribeIotDataType": {
    "params": [
      {
        "name": "TypeId",
        "desc": "自定义数据类型的标识符，为空则返回全量自定义类型的列表"
      }
    ],
    "desc": "本接口（DescribeIotDataType）用于查询自定义的物模型数据类型。"
  },
  "DisableDevice": {
    "params": [
      {
        "name": "Tids",
        "desc": "设备TID ≤100"
      }
    ],
    "desc": "本接口（DisableDevice）用于禁用设备，可进行批量操作，每次操作最多100台设备。"
  },
  "DeleteTraceIds": {
    "params": [
      {
        "name": "Tids",
        "desc": "设备TID列表"
      }
    ],
    "desc": "本接口（DeleteTraceIds）用于将设备从日志跟踪白名单中删除，该接口可批量操作，最多支持同时操作100台设备。"
  },
  "DescribeRegistrationStatus": {
    "params": [
      {
        "name": "CunionIds",
        "desc": "终端用户的唯一ID列表，0<元素数量<=100"
      }
    ],
    "desc": "本接口（DescribeRegistrationStatus）用于查询终端用户的注册状态。"
  },
  "DescribeDevice": {
    "params": [
      {
        "name": "Tid",
        "desc": "设备TID"
      }
    ],
    "desc": "本接口（DescribeDevice）获取设备信息。"
  },
  "RunTestOtaVersion": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品ID"
      },
      {
        "name": "OtaVersion",
        "desc": "固件版本号，格式为x.y.z， x，y 范围0-63，z范围1~524288"
      },
      {
        "name": "Tids",
        "desc": "指定可升级的设备TID"
      },
      {
        "name": "Operator",
        "desc": "操作人"
      }
    ],
    "desc": "本接口（RunTestOtaVersion）用于固件版本测试发布。"
  },
  "DescribeProduct": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品ID"
      }
    ],
    "desc": "本接口（DescribeProduct）用于获取单个产品的详细信息。"
  },
  "SendOnlineMsg": {
    "params": [
      {
        "name": "Tid",
        "desc": "设备TID"
      },
      {
        "name": "Wakeup",
        "desc": "如果设备处于休眠状态，是否唤醒设备"
      },
      {
        "name": "WaitResp",
        "desc": "等待回应类型\n0：不等待设备回应直接响应请求;\n1：要求设备确认消息已接收,或等待超时后返回;\n2：要求设备进行响应处理,收到设备的响应数据后,将设备响应数据回应给请求方;"
      },
      {
        "name": "MsgTopic",
        "desc": "消息主题"
      },
      {
        "name": "MsgContent",
        "desc": "消息内容，最大长度不超过8k字节"
      }
    ],
    "desc": "本接口（SendOnlineMsg）用于向设备发送在线消息。\n注意：\n若设备当前不在线,会直接返回错误;\n若设备网络出现异常时,消息发送可能超时,超时等待最长时间为3秒.waitresp非0情况下,会导致本接口阻塞3秒。"
  },
  "DescribeBindUsr": {
    "params": [
      {
        "name": "Tid",
        "desc": "设备TID"
      },
      {
        "name": "AccessId",
        "desc": "设备主人的AccessId"
      }
    ],
    "desc": "本接口（DescribeBindUsr）用于查询设备被分享的所有用户列表。"
  },
  "ModifyDeviceAction": {
    "params": [
      {
        "name": "Tid",
        "desc": "设备TID"
      },
      {
        "name": "Wakeup",
        "desc": "如果设备处于休眠状态，是否唤醒设备"
      },
      {
        "name": "Branch",
        "desc": "物模型的分支路径"
      },
      {
        "name": "Value",
        "desc": "写入的物模型数据，如果是json需要转义成字符串"
      },
      {
        "name": "IsNum",
        "desc": "Value字段的类型是否为数值（float、int）"
      }
    ],
    "desc": "本接口（ModifyDeviceAction）用于修改设备物模型的行为（Action）。\n\n可对ctlVal数据属性进行写入,如:Action.takePhoto.ctlVal,设备在线且成功发送到设备才返回,物模型写入数据时,不需要传入时标信息,平台以当前时标作为数据的时标更新物模型中的时标信息。\n注意:\n  1.若设备当前不在线,会直接返回错误\n  2.若设备网络出现异常时,消息发送可能超时,超时等待最长时间为3秒\n  3.value的内容必须与实际物模型的定义一致"
  },
  "CreateIotDataType": {
    "params": [
      {
        "name": "IotDataType",
        "desc": "用户自定义数据类型，json格式的字符串"
      }
    ],
    "desc": "本接口（CreateIotDataType）用于创建自定义物模型数据类型。"
  },
  "CreateDevices": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品ID"
      },
      {
        "name": "Number",
        "desc": "创建设备的数量，数量范围1-100"
      },
      {
        "name": "NamePrefix",
        "desc": "设备名称前缀，支持英文、数字，不超过10字符"
      },
      {
        "name": "Operator",
        "desc": "操作人"
      }
    ],
    "desc": "本接口（CreateDevices）用于批量创建新的物联网视频通信设备。\n注意：腾讯云不会对设备私钥进行保存，请自行保管好您的设备私钥。"
  },
  "CreateProduct": {
    "params": [
      {
        "name": "ProductModel",
        "desc": "产器型号(APP产品,为APP包名)"
      },
      {
        "name": "Features",
        "desc": "设备功能码（ypsxth:音频双向通话 ，spdxth:视频单向通话）"
      },
      {
        "name": "ProductName",
        "desc": "产品名称\n仅支持中文、英文、数字、下划线，不超过32个字符"
      },
      {
        "name": "ProductDescription",
        "desc": "产品描述信息\n不支持单引号、双引号、退格符、回车符、换行符、制表符、反斜杠、下划线、“%”、“#”、“$”，不超过128字符"
      },
      {
        "name": "ChipManufactureId",
        "desc": "主芯片产商ID"
      },
      {
        "name": "ChipId",
        "desc": "主芯片ID"
      }
    ],
    "desc": "本接口（CreateProduct）用于创建一个新的物联网智能视频产品。"
  },
  "CreateIotModel": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品ID"
      },
      {
        "name": "IotModel",
        "desc": "物模型json串"
      }
    ],
    "desc": "本接口（CreateIotModel）用于定义的物模型提交。\n该接口实现了物模型草稿箱的功能，保存用户最后一次编辑的物模型数据。"
  },
  "DeleteIotDataType": {
    "params": [
      {
        "name": "TypeId",
        "desc": "自定义数据类型的标识符"
      }
    ],
    "desc": "本接口（DeleteIotDataType）用于删除自定义物模型数据类型。"
  },
  "CreateAppUsr": {
    "params": [
      {
        "name": "CunionId",
        "desc": "标识用户的唯一ID，防止同一个用户多次注册"
      }
    ],
    "desc": "本接口（CreateAppUsr）用于接收由厂商云发送过来的注册请求,建立厂商云终端用户与IoT Video终端用户的映射关系。"
  },
  "DescribeIotModel": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品ID"
      },
      {
        "name": "Revision",
        "desc": "物模型版本号， -1表示最新编辑的（未发布）"
      }
    ],
    "desc": "本接口（DescribeIotModel）用于获取物模型定义详情。"
  },
  "DescribeProducts": {
    "params": [
      {
        "name": "Limit",
        "desc": "分页大小，当前页面中显示的最大数量，值范围 1-100"
      },
      {
        "name": "Offset",
        "desc": "分页偏移，Offset从0开始"
      },
      {
        "name": "ProductModel",
        "desc": "产器型号(APP产品,为APP包名)"
      },
      {
        "name": "StartTime",
        "desc": "开始时间 ，UNIX 时间戳，单位秒"
      },
      {
        "name": "EndTime",
        "desc": "结束时间 ，UNIX 时间戳，单位秒"
      }
    ],
    "desc": "本接口（DescribeProducts）用于列出用户账号下的物联网智能视频产品列表。"
  },
  "CreateTraceIds": {
    "params": [
      {
        "name": "Tids",
        "desc": "设备TID列表"
      }
    ],
    "desc": "本接口（CreateTraceIds）用于将设备加到日志跟踪白名单。"
  },
  "RunIotModel": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品ID"
      },
      {
        "name": "IotModel",
        "desc": "物模型定义，json格式的字符串"
      }
    ],
    "desc": "本接口（RunIotModel）用于对定义的物模型进行发布。"
  },
  "DescribeMessageQueue": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品ID"
      }
    ],
    "desc": "本接口（DescribeMessageQueue）用于查询物联网智能视频产品转发消息配置。"
  },
  "CreateBinding": {
    "params": [
      {
        "name": "AccessId",
        "desc": "终端用户在IoT Video上的唯一标识ID"
      },
      {
        "name": "Tid",
        "desc": "设备TID"
      },
      {
        "name": "Role",
        "desc": "用户角色，owner：主人，guest：访客"
      },
      {
        "name": "ForceBind",
        "desc": "是否踢掉之前的主人，true：踢掉；false：不踢掉。当role为guest时，可以不填"
      }
    ],
    "desc": "本接口（CreateBinding）用于终端用户和设备进行绑定，具体的应用场景如下：\n    终端用户与设备具有“强关联”关系。用户与设备绑定之后，用户终端即具备了该设备的访问权限,访问或操作设备时，无需获取设备访问Token。"
  },
  "CreateDevToken": {
    "params": [
      {
        "name": "AccessId",
        "desc": "客户的终端用户在IoT Video上的唯一标识ID"
      },
      {
        "name": "Tids",
        "desc": "设备TID列表,0<元素数量<=100"
      },
      {
        "name": "TtlMinutes",
        "desc": "Token的TTL(time to alive)分钟数"
      }
    ],
    "desc": "本接口（CreateDevToken）用于以下场景：\n终端用户与设备没有强绑定关联关系;\n允许终端用户短时或一次性临时访问设备;\n当终端用户与设备有强绑定关系时，可以不用调用此接口"
  },
  "DeleteOtaVersion": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品ID"
      },
      {
        "name": "OtaVersion",
        "desc": "固件版本号，格式为x.y.z， x，y 范围0-63，z范围1~524288"
      },
      {
        "name": "Operator",
        "desc": "操作人"
      }
    ],
    "desc": "本接口（DeleteOtaVersion）用于删除固件版本信息。"
  },
  "DeleteAppUsr": {
    "params": [
      {
        "name": "AccessId",
        "desc": "客户的终端用户在IoT Video上的唯一标识ID"
      }
    ],
    "desc": "本接口（DeleteAppUsr）用于删除终端用户。"
  },
  "ModifyProduct": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品ID"
      },
      {
        "name": "ProductName",
        "desc": "产品名称"
      },
      {
        "name": "ProductDescription",
        "desc": "产品描述"
      },
      {
        "name": "ChipManufactureId",
        "desc": "主芯片产商ID"
      },
      {
        "name": "ChipId",
        "desc": "主芯片ID"
      }
    ],
    "desc": "本接口（ModifyProduct）用于编辑物联网智能视频产品的相关信息。"
  },
  "DeleteProduct": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品ID"
      }
    ],
    "desc": "本接口（DeleteProduct）用于删除一个物联网智能视频产品。"
  },
  "DescribeLogs": {
    "params": [
      {
        "name": "Tid",
        "desc": "设备TID"
      },
      {
        "name": "Limit",
        "desc": "当前分页的最大条数,0<取值范围<=100"
      },
      {
        "name": "Offset",
        "desc": "分页偏移量,取值范围>0"
      },
      {
        "name": "LogType",
        "desc": "日志类型 1.在线状态变更 2.ProConst变更 3.ProWritable变更 4.Action控制 5.ProReadonly变更 6.Event事件"
      },
      {
        "name": "StartTime",
        "desc": "查询的起始时间 UNIX时间戳，单位秒"
      },
      {
        "name": "DataObject",
        "desc": "物模型对象索引，用于模糊查询，字符长度<=255，每层节点的字符长度<=16"
      },
      {
        "name": "EndTime",
        "desc": "查询的结束时间 UNIX时间戳，单位秒"
      }
    ],
    "desc": "本接口（DescribeLogs）用于查询设备日志列表。\n设备日志最长保留时长为15天,超期自动清除。"
  },
  "DeleteDevice": {
    "params": [
      {
        "name": "Tids",
        "desc": "设备TID列表"
      }
    ],
    "desc": "本接口（DeleteDevice）用于删除设备，可进行批量操作，每次操作最多100台设备。"
  },
  "DescribeTraceStatus": {
    "params": [
      {
        "name": "Tids",
        "desc": "设备TID列表"
      }
    ],
    "desc": "本接口（DescribeTraceStatus）用于查询指定设备是否在白名单中。"
  },
  "RunOtaVersion": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品ID"
      },
      {
        "name": "OtaVersion",
        "desc": "固件版本号，格式为x.y.z， x，y 范围0-63，z范围1~524288"
      },
      {
        "name": "GrayValue",
        "desc": "灰度值,取值范围0-100，为0时相当于暂停发布"
      },
      {
        "name": "OldVersions",
        "desc": "指定的旧版本"
      },
      {
        "name": "Operator",
        "desc": "操作人"
      }
    ],
    "desc": "本接口（RunOtaVersion）用于固件版本正式发布。"
  },
  "DescribeRunLog": {
    "params": [
      {
        "name": "Tid",
        "desc": "设备TID"
      }
    ],
    "desc": "本接口（DescribeRunLog）用于获取设备运行日志。"
  },
  "SetMessageQueue": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品ID"
      },
      {
        "name": "MsgQueueType",
        "desc": "消息队列类型 1-CMQ; 2-Ckafka"
      },
      {
        "name": "MsgType",
        "desc": "消息类型,整型值（0-31）之间以“,”分隔\n0：在线状态变更\n1.固件版本变更\n2.设置参数变更\n3.控制状态变更\n4.状态信息变更\n5.事件发布"
      },
      {
        "name": "Topic",
        "desc": "消息队列主题，不超过32字符"
      },
      {
        "name": "Instance",
        "desc": "kafka消息队列的实例名，不超过64字符"
      },
      {
        "name": "MsgRegion",
        "desc": "消息地域，不超过32字符"
      }
    ],
    "desc": "本接口（SetMessageQueue）用于配置物联网智能视频产品的转发消息队列。"
  },
  "DisableDeviceStream": {
    "params": [
      {
        "name": "Tids",
        "desc": "设备TID列表"
      }
    ],
    "desc": "本接口（DisableDeviceStream）用于停止设备推流，可进行批量操作，每次操作最多100台设备。"
  },
  "CreateUploadPath": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品ID"
      },
      {
        "name": "FileName",
        "desc": "固件文件名"
      }
    ],
    "desc": "本接口（CreateUploadPath）用于获取固件上传路径。"
  },
  "DescribeModelDataRet": {
    "params": [
      {
        "name": "TaskId",
        "desc": "任务ID"
      }
    ],
    "desc": "本接口（DescribeModelDataRet）用于根据TaskId获取对设备物模型操作最终响应的结果。"
  },
  "DescribePubVersions": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品ID"
      }
    ],
    "desc": "本接口（DescribePubVersions）用于获取某一产品发布过的全部固件版本。"
  },
  "RunDeviceStream": {
    "params": [
      {
        "name": "Tids",
        "desc": "设备TID 列表"
      }
    ],
    "desc": "本接口（RunDeviceStream）用于开启设备推流，可进行批量操作，每次操作最多100台设备。"
  },
  "DescribeDevices": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品ID"
      },
      {
        "name": "ReturnModel",
        "desc": "是否返回全量数据\n当该值为false时，返回值中的设备物模型、固件版本、在线状态、最后在线时间字段等字段，都将返回数据类型的零值。"
      },
      {
        "name": "Limit",
        "desc": "分页数量,0<取值范围<=100"
      },
      {
        "name": "Offset",
        "desc": "分页偏移，取值＞0"
      },
      {
        "name": "OtaVersion",
        "desc": "指定固件版本号，为空查询此产品下所有设备"
      },
      {
        "name": "DeviceName",
        "desc": "设备名称，支持左前缀模糊匹配"
      }
    ],
    "desc": "本接口（DescribeDevices）用于获取设备信息列表。"
  },
  "CreateGencode": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品ID"
      },
      {
        "name": "Revision",
        "desc": "物模型发布版本号，-1代表最新编辑（未发布）的版本"
      }
    ],
    "desc": "本接口（CreateGencode）用于生成设备物模型源代码"
  },
  "DescribeDeviceModel": {
    "params": [
      {
        "name": "Tid",
        "desc": "设备TID"
      },
      {
        "name": "Branch",
        "desc": "物模型的分支路径"
      }
    ],
    "desc": "本接口（DescribeDeviceModel）用于获取设备物模型。"
  },
  "DescribeIotModels": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品ID"
      }
    ],
    "desc": "本接口（DescribeIotModels）用于列出物模型历史版本列表。"
  },
  "DeleteBinding": {
    "params": [
      {
        "name": "AccessId",
        "desc": "终端用户在IoT Video上的唯一标识ID"
      },
      {
        "name": "Tid",
        "desc": "设备TID"
      },
      {
        "name": "Role",
        "desc": "用户角色，owner：主人，guest：访客"
      }
    ],
    "desc": "本接口（DeleteBinding）用于终端用户和设备进行解绑定。"
  },
  "CreateStorage": {
    "params": [
      {
        "name": "PkgId",
        "desc": "云存套餐ID"
      },
      {
        "name": "Tid",
        "desc": "设备TID"
      },
      {
        "name": "UserTag",
        "desc": "用户唯一标识，由厂商保证内部唯一性"
      }
    ],
    "desc": "本接口（CreateStorage）用于购买云存套餐。"
  },
  "DescribeTraceIds": {
    "params": [],
    "desc": "本接口（DescribeTraceIds）用于查询设备日志跟踪白名单。"
  },
  "DeleteMessageQueue": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品ID"
      }
    ],
    "desc": "本接口（DeleteMessageQueue）用于删除物联网智能视频产品的转发消息配置信息。"
  },
  "ModifyDeviceProperty": {
    "params": [
      {
        "name": "Tid",
        "desc": "设备TID"
      },
      {
        "name": "Wakeup",
        "desc": "如果设备处于休眠状态，是否唤醒设备"
      },
      {
        "name": "Branch",
        "desc": "物模型的分支路径"
      },
      {
        "name": "Value",
        "desc": "写入的物模型数据，如果是json需要转义成字符串"
      },
      {
        "name": "IsNum",
        "desc": "Value字段是否为数值（float、int）"
      }
    ],
    "desc": "本接口（ModifyDeviceProperty）用于修改设备物模型的属性（ProWritable）。\n可对setVal数据属性进行写入,如:\nProWritable.Pos.setVal\n对于嵌套类型的可写属性，可以仅对其部分数据内容进行写入，如:\nProWritable.Pos.setVal.x;\n可写属性云端写入成功即返回;云端向设备端发布属性变更参数;若当前设备不在线,在设备下次上线时会自动更新这些属性参数;\n物模型写入数据时,不需要传入时标信息,平台以当前时标作为数据的时标更新物模型中的时标信息。"
  },
  "RunDevice": {
    "params": [
      {
        "name": "Tids",
        "desc": "TID列表 ≤100"
      }
    ],
    "desc": "本接口（RunDevice）用于启用设备，可进行批量操作，每次操作最多100台设备。"
  },
  "UploadOtaVersion": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品ID"
      },
      {
        "name": "OtaVersion",
        "desc": "固件版本号，格式为x.y.z， x，y 范围0-63，z范围1~524288"
      },
      {
        "name": "VersionUrl",
        "desc": "固件版本URL"
      },
      {
        "name": "FileSize",
        "desc": "文件大小，单位：byte"
      },
      {
        "name": "Md5",
        "desc": "文件md5校验码（32字符）"
      },
      {
        "name": "Operator",
        "desc": "操作人"
      }
    ],
    "desc": "本接口（UploadOtaVersion）接收上传到控制台的固件版本信息。"
  },
  "CreateUsrToken": {
    "params": [
      {
        "name": "AccessId",
        "desc": "终端用户在IoT Video上的唯一标识ID"
      },
      {
        "name": "UniqueId",
        "desc": "终端唯一ID，用于区分同一个用户的多个终端"
      },
      {
        "name": "TtlMinutes",
        "desc": "Token的TTL(time to alive)分钟数"
      }
    ],
    "desc": "本接口（CreateUsrToken）用于终端用户获取IoT Video平台的accessToken，初始化SDK,连接到IoT Video接入服务器。"
  },
  "UpgradeDevice": {
    "params": [
      {
        "name": "Tid",
        "desc": "设备TID"
      },
      {
        "name": "OtaVersion",
        "desc": "固件版本号"
      },
      {
        "name": "UpgradeNow",
        "desc": "是否立即升级"
      }
    ],
    "desc": "本接口（UpgradeDevice）用于对设备进行固件升级。\n该接口向指定的设备下发固件更新指令,可将固件升级到任意版本(可实现固件降级)。\n警告:使能UpgradeNow参数存在一定的风险性！建议仅在debug场景下使用!"
  }
}