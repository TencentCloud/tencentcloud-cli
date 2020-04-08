# -*- coding: utf-8 -*-
DESC = "ecm-2019-07-19"
INFO = {
  "ResetInstancesMaxBandwidth": {
    "params": [
      {
        "name": "InstanceIdSet",
        "desc": "待重置带宽上限的实例ID列表。在单次请求的过程中，单个region下的请求实例数上限为100。"
      },
      {
        "name": "MaxBandwidthOut",
        "desc": "修改后的最大带宽上限。"
      }
    ],
    "desc": "重置实例的最大带宽上限。"
  },
  "DescribeModule": {
    "params": [
      {
        "name": "Filters",
        "desc": "过滤条件。\nmodule-name - string - 是否必填：否 - （过滤条件）按照模块名称过滤。\nmodule-id - string - 是否必填：否 - （过滤条件）按照模块ID过滤。\n每次请求的Filters的上限为10，Filter.Values的上限为5。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。关于Offset的更进一步介绍请参考 API 简介中的相关小节。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API 简介中的相关小节。"
      }
    ],
    "desc": "获取模块列表"
  },
  "DescribeConfig": {
    "params": [],
    "desc": "获取带宽硬盘等数据的限制"
  },
  "DescribeBaseOverview": {
    "params": [],
    "desc": "获取概览页统计的基本数据"
  },
  "ModifyModuleNetwork": {
    "params": [
      {
        "name": "ModuleId",
        "desc": "模块Id"
      },
      {
        "name": "DefaultBandwidth",
        "desc": "默认带宽上限"
      }
    ],
    "desc": "修改模块默认带宽上限"
  },
  "ModifyInstancesAttribute": {
    "params": [
      {
        "name": "InstanceIdSet",
        "desc": "待修改的实例ID列表。在单次请求的过程中，请求实例数上限为100。"
      },
      {
        "name": "InstanceName",
        "desc": "修改成功后显示的实例名称，不得超过60个字符，不传则名称显示为空。"
      }
    ],
    "desc": "修改实例的属性。"
  },
  "DescribeInstances": {
    "params": [
      {
        "name": "Filters",
        "desc": "过滤条件。\nzone      String      是否必填：否     （过滤条件）按照可用区中文名过滤,支持模糊匹配。\nmodule-id      String      是否必填：否     （过滤条件）按照模块ID过滤。\ninstance-id      String      是否必填：否      （过滤条件）按照实例ID过滤。\ninstance-name      String      是否必填：否      （过滤条件）按照实例名称过滤,支持模糊匹配。\nip-address      String      是否必填：否      （过滤条件）按照实例的内网/公网IP过滤。\ninstance-uuid   string 是否必填：否 （过滤条件）按照uuid过滤实例列表。\ninstance-state  string  是否必填：否 （过滤条件）按照实例状态更新实例列表。\ninternet-service-provider      String      是否必填：否      （过滤条件）按照实例公网IP所属的运营商进行过滤。\ntag-key      String      是否必填：否      （过滤条件）按照标签键进行过滤。\ntag:tag-key      String      是否必填：否      （过滤条件）按照标签键值对进行过滤。 tag-key使用具体的标签键进行替换。\n若不传Filters参数则表示查询所有相关的实例信息。\n单次请求的Filter.Values的上限为5。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20(如果查询结果数目大于等于20)，最大值为100。"
      }
    ],
    "desc": "获取实例的相关信息。"
  },
  "DescribeInstanceTypeConfig": {
    "params": [],
    "desc": "获取机型配置列表"
  },
  "TerminateInstances": {
    "params": [
      {
        "name": "InstanceIdSet",
        "desc": "待销毁的实例ID列表。"
      },
      {
        "name": "TerminateDelay",
        "desc": "是否定时销毁，默认为否。"
      },
      {
        "name": "TerminateTime",
        "desc": "定时销毁的时间，格式形如：\"2019-08-05 12:01:30\"，若非定时销毁，则此参数被忽略。"
      }
    ],
    "desc": "销毁实例"
  },
  "ModifyModuleImage": {
    "params": [
      {
        "name": "DefaultImageId",
        "desc": "默认镜像ID"
      },
      {
        "name": "ModuleId",
        "desc": "模块ID"
      }
    ],
    "desc": "ModifyModuleImage"
  },
  "CreateModule": {
    "params": [
      {
        "name": "ModuleName",
        "desc": "模块名称，如视频直播模块。限制：模块名称不得以空格开头，长度不得超过60个字符。"
      },
      {
        "name": "DefaultBandWidth",
        "desc": "默认带宽，单位：M。范围不得超过带宽上下限，详看DescribeConfig。"
      },
      {
        "name": "DefaultImageId",
        "desc": "默认镜像，如img-qsdf3ff2。"
      },
      {
        "name": "InstanceType",
        "desc": "机型ID。"
      },
      {
        "name": "DefaultSystemDiskSize",
        "desc": "默认系统盘大小，单位：G，默认大小为50G。范围不得超过系统盘上下限制，详看DescribeConfig。"
      },
      {
        "name": "DefaultDataDiskSize",
        "desc": "默认数据盘大小，单位：G。范围不得超过数据盘范围大小，详看DescribeConfig。"
      }
    ],
    "desc": "创建模块"
  },
  "ModifyModuleName": {
    "params": [
      {
        "name": "ModuleId",
        "desc": "模块ID。"
      },
      {
        "name": "ModuleName",
        "desc": "模块名称。"
      }
    ],
    "desc": "修改模块名称"
  },
  "DescribeInstancesDeniedActions": {
    "params": [
      {
        "name": "InstanceIdSet",
        "desc": "无"
      }
    ],
    "desc": "通过实例id获取当前禁止的操作"
  },
  "DescribePeakNetworkOverview": {
    "params": [
      {
        "name": "StartTime",
        "desc": "开始时间（xxxx-xx-xx）如2019-08-14，默认为一周之前的日期。"
      },
      {
        "name": "EndTime",
        "desc": "结束时间（xxxx-xx-xx）如2019-08-14，默认为昨天。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件。\nregion    String      是否必填：否     （过滤条件）按照region过滤,不支持模糊匹配。"
      }
    ],
    "desc": "获取网络峰值数据"
  },
  "DescribeNode": {
    "params": [],
    "desc": "获取节点列表"
  },
  "DescribeModuleDetail": {
    "params": [
      {
        "name": "ModuleId",
        "desc": "模块ID，如em-qn46snq8。"
      }
    ],
    "desc": "展示模块详细信息"
  },
  "ImportImage": {
    "params": [
      {
        "name": "ImageId",
        "desc": "镜像的Id。"
      },
      {
        "name": "ImageDescription",
        "desc": "镜像的描述。"
      },
      {
        "name": "SourceRegion",
        "desc": "源地域"
      }
    ],
    "desc": "从CVM产品导入镜像到ECM"
  },
  "ResetInstances": {
    "params": [
      {
        "name": "InstanceIdSet",
        "desc": "待重装的实例ID列表。"
      },
      {
        "name": "ImageId",
        "desc": "重装使用的镜像ID，若未指定，则使用各个实例当前的镜像进行重装。"
      },
      {
        "name": "Password",
        "desc": "密码设置，若未指定，则后续将以站内信的形式通知密码。"
      },
      {
        "name": "EnhancedService",
        "desc": "是否开启云监控和云镜服务，未指定时默认开启。"
      }
    ],
    "desc": "重装实例，若指定了ImageId参数，则使用指定的镜像重装；否则按照当前实例使用的镜像进行重装；若未指定密码，则密码通过站内信形式随后发送。"
  },
  "DescribePeakBaseOverview": {
    "params": [
      {
        "name": "StartTime",
        "desc": "开始时间（xxxx-xx-xx）如2019-08-14，默认为一周之前的日期。"
      },
      {
        "name": "EndTime",
        "desc": "结束时间（xxxx-xx-xx）如2019-08-14，默认为昨天。"
      }
    ],
    "desc": "CPU 内存 硬盘等基础信息峰值数据"
  },
  "DeleteModule": {
    "params": [
      {
        "name": "ModuleId",
        "desc": "模块ID。如：es-qn46snq8"
      }
    ],
    "desc": "删除业务模块"
  },
  "RebootInstances": {
    "params": [
      {
        "name": "InstanceIdSet",
        "desc": "待重启的实例ID列表。在单次请求的过程中，单个region下的请求实例数上限为100。"
      },
      {
        "name": "ForceReboot",
        "desc": "是否在正常重启失败后选择强制重启实例。取值范围：\nTRUE：表示在正常重启失败后进行强制重启；\nFALSE：表示在正常重启失败后不进行强制重启；\n默认取值：FALSE。"
      },
      {
        "name": "StopType",
        "desc": "关机类型。取值范围：\nSOFT：表示软关机\nHARD：表示硬关机\nSOFT_FIRST：表示优先软关机，失败再执行硬关机\n\n默认取值：SOFT。"
      }
    ],
    "desc": "只有状态为RUNNING的实例才可以进行此操作；接口调用成功时，实例会进入REBOOTING状态；重启实例成功时，实例会进入RUNNING状态；支持强制重启，强制重启的效果等同于关闭物理计算机的电源开关再重新启动。强制重启可能会导致数据丢失或文件系统损坏，请仅在服务器不能正常重启时使用。"
  },
  "DescribeImage": {
    "params": [
      {
        "name": "Filters",
        "desc": "过滤条件，每次请求的Filters的上限为10，详细的过滤条件如下：\nimage-id - String - 是否必填： 否 - （过滤条件）按照镜像ID进行过滤\nimage-type - String - 是否必填： 否 - （过滤条件）按照镜像类型进行过滤。取值范围：\nPRIVATE_IMAGE: 私有镜像 (本帐户创建的镜像) \nPUBLIC_IMAGE: 公共镜像 (腾讯云官方镜像)"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。关于Offset的更进一步介绍请参考 API 简介中的相关小节。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API 简介中的相关小节。"
      }
    ],
    "desc": "展示镜像列表"
  },
  "DeleteImage": {
    "params": [
      {
        "name": "ImageIDSet",
        "desc": "镜像ID列表。"
      }
    ],
    "desc": "删除镜像"
  }
}