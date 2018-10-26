# -*- coding: utf-8 -*-
DESC = "as-2018-04-19"
INFO = {
  "CreateAutoScalingGroup": {
    "params": [
      {
        "name": "AutoScalingGroupName",
        "desc": "伸缩组名称，在您账号中必须唯一。名称仅支持中文、英文、数字、下划线、分隔符\"-\"、小数点，最大长度不能超55个字节。"
      },
      {
        "name": "LaunchConfigurationId",
        "desc": "启动配置ID"
      },
      {
        "name": "MaxSize",
        "desc": "最大实例数，取值范围为0-2000。"
      },
      {
        "name": "MinSize",
        "desc": "最小实例数，取值范围为0-2000。"
      },
      {
        "name": "VpcId",
        "desc": "VPC ID，基础网络则填空字符串"
      },
      {
        "name": "DefaultCooldown",
        "desc": "默认冷却时间，单位秒，默认值为300"
      },
      {
        "name": "DesiredCapacity",
        "desc": "期望实例数，大小介于最小实例数和最大实例数之间"
      },
      {
        "name": "LoadBalancerIds",
        "desc": "传统负载均衡器ID列表，目前长度上限为1，LoadBalancerIds 和 ForwardLoadBalancers 二者同时最多只能指定一个"
      },
      {
        "name": "ProjectId",
        "desc": "项目ID"
      },
      {
        "name": "ForwardLoadBalancers",
        "desc": "应用型负载均衡器列表，目前长度上限为1，LoadBalancerIds 和 ForwardLoadBalancers 二者同时最多只能指定一个"
      },
      {
        "name": "SubnetIds",
        "desc": "子网ID列表，VPC场景下必须指定子网"
      },
      {
        "name": "TerminationPolicies",
        "desc": "销毁策略，目前长度上限为1"
      },
      {
        "name": "Zones",
        "desc": "可用区列表，基础网络场景下必须指定可用区"
      }
    ],
    "desc": "本接口（CreateAutoScalingGroup）用于创建伸缩组"
  },
  "DeleteScheduledAction": {
    "params": [
      {
        "name": "ScheduledActionId",
        "desc": "待删除的定时任务ID。"
      }
    ],
    "desc": "本接口（DeleteScheduledAction）用于删除特定的定时任务。"
  },
  "DescribeAccountLimits": {
    "params": [],
    "desc": "本接口（DescribeAccountLimits）用于查询用户账户在弹性伸缩中的资源限制。"
  },
  "DetachInstances": {
    "params": [
      {
        "name": "AutoScalingGroupId",
        "desc": "伸缩组ID"
      },
      {
        "name": "InstanceIds",
        "desc": "CVM实例ID列表"
      }
    ],
    "desc": "本接口（DettachInstances）用于从伸缩组移出 CVM 实例，本接口不会被销毁实例。"
  },
  "CreateScheduledAction": {
    "params": [
      {
        "name": "AutoScalingGroupId",
        "desc": "伸缩组ID"
      },
      {
        "name": "ScheduledActionName",
        "desc": "定时任务名称。名称仅支持中文、英文、数字、下划线、分隔符\"-\"、小数点，最大长度不能超60个字节。同一伸缩组下必须唯一。"
      },
      {
        "name": "MaxSize",
        "desc": "当定时任务触发时，设置的伸缩组最大实例数。"
      },
      {
        "name": "MinSize",
        "desc": "当定时任务触发时，设置的伸缩组最小实例数。"
      },
      {
        "name": "DesiredCapacity",
        "desc": "当定时任务触发时，设置的伸缩组期望实例数。"
      },
      {
        "name": "StartTime",
        "desc": "定时任务的首次触发时间，取值为`北京时间`（UTC+8），按照`ISO8601`标准，格式：`YYYY-MM-DDThh:mm:ss+08:00`。"
      },
      {
        "name": "EndTime",
        "desc": "定时任务的结束时间，取值为`北京时间`（UTC+8），按照`ISO8601`标准，格式：`YYYY-MM-DDThh:mm:ss+08:00`。<br><br>此参数与`Recurrence`需要同时指定，到达结束时间之后，定时任务将不再生效。"
      },
      {
        "name": "Recurrence",
        "desc": "定时任务的重复方式。为标准[Cron](https://zh.wikipedia.org/wiki/Cron)格式<br><br>此参数与`EndTime`需要同时指定。"
      }
    ],
    "desc": "本接口（CreateScheduledAction）用于创建定时任务。"
  },
  "CreateLaunchConfiguration": {
    "params": [
      {
        "name": "LaunchConfigurationName",
        "desc": "启动配置显示名称。名称仅支持中文、英文、数字、下划线、分隔符\"-\"、小数点，最大长度不能超60个字节。"
      },
      {
        "name": "InstanceType",
        "desc": "实例机型。不同实例机型指定了不同的资源规格，具体取值可通过调用接口 [DescribeInstanceTypeConfigs](https://cloud.tencent.com/document/api/213/15749) 来获得最新的规格表或参见[实例类型](https://cloud.tencent.com/document/product/213/11518)描述。"
      },
      {
        "name": "ImageId",
        "desc": "指定有效的[镜像](https://cloud.tencent.com/document/product/213/4940)ID，格式形如`img-8toqc6s3`。镜像类型分为四种：<br/><li>公共镜像</li><li>自定义镜像</li><li>共享镜像</li><li>服务市场镜像</li><br/>可通过以下方式获取可用的镜像ID：<br/><li>`公共镜像`、`自定义镜像`、`共享镜像`的镜像ID可通过登录[控制台](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE)查询；`服务镜像市场`的镜像ID可通过[云市场](https://market.cloud.tencent.com/list)查询。</li><li>通过调用接口 [DescribeImages](https://cloud.tencent.com/document/api/213/15715) ，取返回信息中的`ImageId`字段。</li>"
      },
      {
        "name": "ProjectId",
        "desc": "实例所属项目ID。该参数可以通过调用 [DescribeProject](https://cloud.tencent.com/document/api/378/4400) 的返回值中的`projectId`字段来获取。不填为默认项目。"
      },
      {
        "name": "SystemDisk",
        "desc": "实例系统盘配置信息。若不指定该参数，则按照系统默认值进行分配。"
      },
      {
        "name": "DataDisks",
        "desc": "实例数据盘配置信息。若不指定该参数，则默认不购买数据盘，当前仅支持购买的时候指定一个数据盘。"
      },
      {
        "name": "InternetAccessible",
        "desc": "公网带宽相关信息设置。若不指定该参数，则默认公网带宽为0Mbps。"
      },
      {
        "name": "LoginSettings",
        "desc": "实例登录设置。通过该参数可以设置实例的登录方式密码、密钥或保持镜像的原始登录设置。默认情况下会随机生成密码，并以站内信方式知会到用户。"
      },
      {
        "name": "SecurityGroupIds",
        "desc": "实例所属安全组。该参数可以通过调用 [DescribeSecurityGroups](https://cloud.tencent.com/document/api/215/15808) 的返回值中的`SecurityGroupId`字段来获取。若不指定该参数，则默认不绑定安全组。"
      },
      {
        "name": "EnhancedService",
        "desc": "增强服务。通过该参数可以指定是否开启云安全、云监控等服务。若不指定该参数，则默认开启云监控、云安全服务。"
      },
      {
        "name": "UserData",
        "desc": "经过 Base64 编码后的自定义数据，最大长度不超过16KB。"
      },
      {
        "name": "InstanceChargeType",
        "desc": "实例计费类型，CVM默认值按照POSTPAID_BY_HOUR处理。\n<br><li>POSTPAID_BY_HOUR：按小时后付费\n<br><li>SPOTPAID：竞价付费"
      },
      {
        "name": "InstanceMarketOptions",
        "desc": "实例的市场相关选项，如竞价实例相关参数，若指定实例的付费模式为竞价付费则该参数必传。"
      }
    ],
    "desc": "本接口（CreateLaunchConfiguration）用于创建新的启动配置。\n\n* 启动配置无法编辑更改。如需使用新的启动配置，只能重新创建启动配置。\n\n* 每个项目最多只能创建20个启动配置，详见[使用限制](https://cloud.tencent.com/document/product/377/3120)。\n"
  },
  "ModifyAutoScalingGroup": {
    "params": [
      {
        "name": "AutoScalingGroupId",
        "desc": "伸缩组ID"
      },
      {
        "name": "AutoScalingGroupName",
        "desc": "伸缩组名称，在您账号中必须唯一。名称仅支持中文、英文、数字、下划线、分隔符\"-\"、小数点，最大长度不能超55个字节。"
      },
      {
        "name": "DefaultCooldown",
        "desc": "默认冷却时间，单位秒，默认值为300"
      },
      {
        "name": "DesiredCapacity",
        "desc": "期望实例数，大小介于最小实例数和最大实例数之间"
      },
      {
        "name": "LaunchConfigurationId",
        "desc": "启动配置ID"
      },
      {
        "name": "MaxSize",
        "desc": "最大实例数，取值范围为0-2000。"
      },
      {
        "name": "MinSize",
        "desc": "最小实例数，取值范围为0-2000。"
      },
      {
        "name": "ProjectId",
        "desc": "项目ID"
      },
      {
        "name": "SubnetIds",
        "desc": "子网ID列表"
      },
      {
        "name": "TerminationPolicies",
        "desc": "销毁策略，目前长度上限为1"
      },
      {
        "name": "VpcId",
        "desc": "VPC ID，基础网络则填空字符串。修改为具体VPC ID时，需指定相应的SubnetIds；修改为基础网络时，需指定相应的Zones。"
      },
      {
        "name": "Zones",
        "desc": "可用区列表"
      }
    ],
    "desc": "本接口（ModifyAutoScalingGroup）用于修改伸缩组。"
  },
  "EnableAutoScalingGroup": {
    "params": [
      {
        "name": "AutoScalingGroupId",
        "desc": "伸缩组ID"
      }
    ],
    "desc": "本接口（EnableAutoScalingGroup）用于启用指定伸缩组。"
  },
  "RemoveInstances": {
    "params": [
      {
        "name": "AutoScalingGroupId",
        "desc": "伸缩组ID"
      },
      {
        "name": "InstanceIds",
        "desc": "CVM实例ID列表"
      }
    ],
    "desc": "本接口（RemoveInstances）用于从伸缩组删除 CVM 实例。根据当前的产品逻辑，如果实例由弹性伸缩自动创建，则实例会被销毁；如果实例系创建后加入伸缩组的，则会从伸缩组中移除，保留实例。"
  },
  "DescribeAutoScalingGroups": {
    "params": [
      {
        "name": "AutoScalingGroupIds",
        "desc": "按照一个或者多个伸缩组ID查询。伸缩组ID形如：`asg-nkdwoui0`。每次请求的上限为100。参数不支持同时指定`AutoScalingGroups`和`Filters`。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件。\n<li> auto-scaling-group-id - String - 是否必填：否 -（过滤条件）按照伸缩组ID过滤。</li>\n<li> auto-scaling-group-name - String - 是否必填：否 -（过滤条件）按照伸缩组名称过滤。</li>\n<li> launch-configuration-id - String - 是否必填：否 -（过滤条件）按照启动配置ID过滤。</li>\n每次请求的`Filters`的上限为10，`Filter.Values`的上限为5。参数不支持同时指定`AutoScalingGroupIds`和`Filters`。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。"
      }
    ],
    "desc": "本接口（DescribeAutoScalingGroups）用于查询伸缩组信息。"
  },
  "ModifyScheduledAction": {
    "params": [
      {
        "name": "ScheduledActionId",
        "desc": "待修改的定时任务ID"
      },
      {
        "name": "ScheduledActionName",
        "desc": "定时任务名称。名称仅支持中文、英文、数字、下划线、分隔符\"-\"、小数点，最大长度不能超60个字节。同一伸缩组下必须唯一。"
      },
      {
        "name": "MaxSize",
        "desc": "当定时任务触发时，设置的伸缩组最大实例数。"
      },
      {
        "name": "MinSize",
        "desc": "当定时任务触发时，设置的伸缩组最小实例数。"
      },
      {
        "name": "DesiredCapacity",
        "desc": "当定时任务触发时，设置的伸缩组期望实例数。"
      },
      {
        "name": "StartTime",
        "desc": "定时任务的首次触发时间，取值为`北京时间`（UTC+8），按照`ISO8601`标准，格式：`YYYY-MM-DDThh:mm:ss+08:00`。"
      },
      {
        "name": "EndTime",
        "desc": "定时任务的结束时间，取值为`北京时间`（UTC+8），按照`ISO8601`标准，格式：`YYYY-MM-DDThh:mm:ss+08:00`。<br>此参数与`Recurrence`需要同时指定，到达结束时间之后，定时任务将不再生效。"
      },
      {
        "name": "Recurrence",
        "desc": "定时任务的重复方式。为标准[Cron](https://zh.wikipedia.org/wiki/Cron)格式<br>此参数与`EndTime`需要同时指定。"
      }
    ],
    "desc": "本接口（ModifyScheduledAction）用于修改定时任务。"
  },
  "DeleteAutoScalingGroup": {
    "params": [
      {
        "name": "AutoScalingGroupId",
        "desc": "伸缩组ID"
      }
    ],
    "desc": "本接口（DeleteAutoScalingGroup）用于删除指定伸缩组，删除前提是伸缩组内无实例且当前未在执行伸缩活动。"
  },
  "DeleteLaunchConfiguration": {
    "params": [
      {
        "name": "LaunchConfigurationId",
        "desc": "需要删除的启动配置ID。"
      }
    ],
    "desc": "本接口（DeleteLaunchConfiguration）用于删除启动配置。\n\n* 若启动配置在伸缩组中属于生效状态，则该启动配置不允许删除。\n"
  },
  "DescribeLaunchConfigurations": {
    "params": [
      {
        "name": "LaunchConfigurationIds",
        "desc": "按照一个或者多个启动配置ID查询。启动配置ID形如：`asc-ouy1ax38`。每次请求的上限为100。参数不支持同时指定`LaunchConfigurationIds`和`Filters`。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件。\n<li> launch-configuration-id - String - 是否必填：否 -（过滤条件）按照启动配置ID过滤。</li>\n<li> launch-configuration-name - String - 是否必填：否 -（过滤条件）按照启动配置名称过滤。</li>\n每次请求的`Filters`的上限为10，`Filter.Values`的上限为5。参数不支持同时指定`LaunchConfigurationIds`和`Filters`。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。"
      }
    ],
    "desc": "本接口（DescribeLaunchConfigurations）用于查询启动配置的信息。"
  },
  "DisableAutoScalingGroup": {
    "params": [
      {
        "name": "AutoScalingGroupId",
        "desc": "伸缩组ID"
      }
    ],
    "desc": "本接口（DisableAutoScalingGroup）用于停用指定伸缩组。"
  },
  "DescribeAutoScalingInstances": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "待查询的云主机（CVM）实例ID。参数不支持同时指定InstanceIds和Filters。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件。\n<li> instance-id - String - 是否必填：否 -（过滤条件）按照实例ID过滤。</li>\n<li> auto-scaling-group-id - String - 是否必填：否 -（过滤条件）按照伸缩组ID过滤。</li>\n每次请求的`Filters`的上限为10，`Filter.Values`的上限为5。参数不支持同时指定`InstanceIds`和`Filters`。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。"
      }
    ],
    "desc": "本接口（DescribeAutoScalingInstances）用于查询弹性伸缩关联实例的信息。\n\n"
  },
  "DescribeScheduledActions": {
    "params": [
      {
        "name": "ScheduledActionIds",
        "desc": "按照一个或者多个定时任务ID查询。实例ID形如：asst-am691zxo。每次请求的实例的上限为100。参数不支持同时指定ScheduledActionIds和Filters。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件。\n* scheduled-action-id - String - 是否必填：否 -（过滤条件）按照定时任务ID过滤。\n* scheduled-action-name - String - 是否必填：否 - （过滤条件） 按照定时任务名称过滤。\n* auto-scaling-group-id - String - 是否必填：否 - （过滤条件） 按照伸缩组ID过滤。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。关于Offset的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。"
      }
    ],
    "desc": "本接口 (DescribeScheduledActions) 用于查询一个或多个定时任务的详细信息。\n\n* 可以根据定时任务ID、定时任务名称或者伸缩组ID等信息来查询定时任务的详细信息。过滤信息详细请见过滤器Filter。\n* 如果参数为空，返回当前用户一定数量（Limit所指定的数量，默认为20）的定时任务。"
  },
  "AttachInstances": {
    "params": [
      {
        "name": "AutoScalingGroupId",
        "desc": "伸缩组ID"
      },
      {
        "name": "InstanceIds",
        "desc": "CVM实例ID列表"
      }
    ],
    "desc": "本接口（AttachInstances）用于将 CVM 实例添加到伸缩组。\n"
  },
  "ModifyDesiredCapacity": {
    "params": [
      {
        "name": "AutoScalingGroupId",
        "desc": "伸缩组ID"
      },
      {
        "name": "DesiredCapacity",
        "desc": "期望实例数"
      }
    ],
    "desc": "本接口（ModifyDesiredCapacity）用于修改指定伸缩组的期望实例数"
  }
}