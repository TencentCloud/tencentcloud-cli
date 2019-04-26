# -*- coding: utf-8 -*-
DESC = "autoscaling-2018-04-19"
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
        "desc": "销毁策略，目前长度上限为1。取值包括 OLDEST_INSTANCE 和 NEWEST_INSTANCE，默认取值为 OLDEST_INSTANCE。\n<br><li> OLDEST_INSTANCE 优先销毁伸缩组中最旧的实例。\n<br><li> NEWEST_INSTANCE，优先销毁伸缩组中最新的实例。"
      },
      {
        "name": "Zones",
        "desc": "可用区列表，基础网络场景下必须指定可用区"
      },
      {
        "name": "RetryPolicy",
        "desc": "重试策略，取值包括 IMMEDIATE_RETRY 和 INCREMENTAL_INTERVALS，默认取值为 IMMEDIATE_RETRY。\n<br><li> IMMEDIATE_RETRY，立即重试，在较短时间内快速重试，连续失败超过一定次数（5次）后不再重试。\n<br><li> INCREMENTAL_INTERVALS，间隔递增重试，随着连续失败次数的增加，重试间隔逐渐增大，重试间隔从秒级到1天不等。"
      },
      {
        "name": "ZonesCheckPolicy",
        "desc": "可用区校验策略，取值包括 ALL 和 ANY，默认取值为ANY。\n<br><li> ALL，所有可用区（Zone）或子网（SubnetId）都可用则通过校验，否则校验报错。\n<br><li> ANY，存在任何一个可用区（Zone）或子网（SubnetId）可用则通过校验，否则校验报错。\n\n可用区或子网不可用的常见原因包括该可用区CVM实例类型售罄、该可用区CBS云盘售罄、该可用区配额不足、该子网IP不足等。\n如果 Zones/SubnetIds 中可用区或者子网不存在，则无论 ZonesCheckPolicy 采用何种取值，都会校验报错。"
      }
    ],
    "desc": "本接口（CreateAutoScalingGroup）用于创建伸缩组"
  },
  "ModifyScalingPolicy": {
    "params": [
      {
        "name": "AutoScalingPolicyId",
        "desc": "告警策略ID。"
      },
      {
        "name": "ScalingPolicyName",
        "desc": "告警策略名称。"
      },
      {
        "name": "AdjustmentType",
        "desc": "告警触发后，期望实例数修改方式。取值 ：<br><li>CHANGE_IN_CAPACITY：增加或减少若干期望实例数</li><li>EXACT_CAPACITY：调整至指定期望实例数</li> <li>PERCENT_CHANGE_IN_CAPACITY：按百分比调整期望实例数</li>"
      },
      {
        "name": "AdjustmentValue",
        "desc": "告警触发后，期望实例数的调整值。取值：<br><li>当 AdjustmentType 为 CHANGE_IN_CAPACITY 时，AdjustmentValue 为正数表示告警触发后增加实例，为负数表示告警触发后减少实例 </li> <li> 当 AdjustmentType 为 EXACT_CAPACITY 时，AdjustmentValue 的值即为告警触发后新的期望实例数，需要大于或等于0 </li> <li> 当 AdjustmentType 为 PERCENT_CHANGE_IN_CAPACITY 时，AdjusmentValue 为正数表示告警触发后按百分比增加实例，为负数表示告警触发后按百分比减少实例，单位是：%。"
      },
      {
        "name": "Cooldown",
        "desc": "冷却时间，单位为秒。"
      },
      {
        "name": "MetricAlarm",
        "desc": "告警监控指标。"
      },
      {
        "name": "NotificationUserGroupIds",
        "desc": "通知组ID，即为用户组ID集合，用户组ID可以通过[DescribeUserGroup](https://cloud.tencent.com/document/api/378/4404)查询。\n如果需要清空通知用户组，需要在列表中传入特定字符串 \"NULL\"。"
      }
    ],
    "desc": "本接口（ModifyScalingPolicy）用于修改告警触发策略。"
  },
  "DescribeNotificationConfigurations": {
    "params": [
      {
        "name": "AutoScalingNotificationIds",
        "desc": "按照一个或者多个通知ID查询。实例ID形如：asn-2sestqbr。每次请求的实例的上限为100。参数不支持同时指定`AutoScalingNotificationIds`和`Filters`。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件。\n<li> auto-scaling-notification-id - String - 是否必填：否 -（过滤条件）按照通知ID过滤。</li>\n<li> auto-scaling-group-id - String - 是否必填：否 -（过滤条件）按照伸缩组ID过滤。</li>\n每次请求的`Filters`的上限为10，`Filter.Values`的上限为5。参数不支持同时指定`AutoScalingNotificationIds`和`Filters`。"
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
    "desc": "本接口 (DescribeNotificationConfigurations) 用于查询一个或多个通知的详细信息。\n\n可以根据通知ID、伸缩组ID等信息来查询通知的详细信息。过滤信息详细请见过滤器`Filter`。\n如果参数为空，返回当前用户一定数量（Limit所指定的数量，默认为20）的通知。"
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
  "CreatePaiInstance": {
    "params": [
      {
        "name": "DomainName",
        "desc": "PAI实例的域名。"
      },
      {
        "name": "InternetAccessible",
        "desc": "公网带宽相关信息设置。"
      },
      {
        "name": "InitScript",
        "desc": "启动脚本的base64编码字符串。"
      },
      {
        "name": "Zones",
        "desc": "可用区列表。"
      },
      {
        "name": "VpcId",
        "desc": "VpcId。"
      },
      {
        "name": "SubnetIds",
        "desc": "子网列表。"
      },
      {
        "name": "InstanceName",
        "desc": "实例显示名称。"
      },
      {
        "name": "InstanceTypes",
        "desc": "实例机型列表。"
      },
      {
        "name": "LoginSettings",
        "desc": "实例登录设置。"
      },
      {
        "name": "InstanceChargeType",
        "desc": "实例计费类型。"
      },
      {
        "name": "InstanceChargePrepaid",
        "desc": "预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。若指定实例的付费模式为预付费则该参数必传。"
      }
    ],
    "desc": "本接口 (CreatePaiInstance) 用于创建一个指定配置的PAI实例。"
  },
  "DescribeLaunchConfigurations": {
    "params": [
      {
        "name": "LaunchConfigurationIds",
        "desc": "按照一个或者多个启动配置ID查询。启动配置ID形如：`asc-ouy1ax38`。每次请求的上限为100。参数不支持同时指定`LaunchConfigurationIds`和`Filters`"
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
    "desc": "本接口（DescribeLaunchConfigurations）用于查询启动配置的信息。\n\n* 可以根据启动配置ID、启动配置名称等信息来查询启动配置的详细信息。过滤信息详细请见过滤器`Filter`。\n* 如果参数为空，返回当前用户一定数量（`Limit`所指定的数量，默认为20）的启动配置。"
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
  "DescribeScalingPolicies": {
    "params": [
      {
        "name": "AutoScalingPolicyIds",
        "desc": "按照一个或者多个告警策略ID查询。告警策略ID形如：asp-i9vkg894。每次请求的实例的上限为100。参数不支持同时指定`AutoScalingPolicyIds`和`Filters`。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件。\n<li> auto-scaling-policy-id - String - 是否必填：否 -（过滤条件）按照告警策略ID过滤。</li>\n<li> auto-scaling-group-id - String - 是否必填：否 -（过滤条件）按照伸缩组ID过滤。</li>\n<li> scaling-policy-name - String - 是否必填：否 -（过滤条件）按照告警策略名称过滤。</li>\n每次请求的`Filters`的上限为10，`Filter.Values`的上限为5。参数不支持同时指定`AutoScalingPolicyIds`和`Filters`。"
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
    "desc": "本接口（DescribeScalingPolicies）用于查询告警触发策略。"
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
    "desc": "本接口（DetachInstances）用于从伸缩组移出 CVM 实例，本接口不会销毁实例。"
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
  "DeleteScalingPolicy": {
    "params": [
      {
        "name": "AutoScalingPolicyId",
        "desc": "待删除的告警策略ID。"
      }
    ],
    "desc": "本接口（DeleteScalingPolicy）用于删除告警触发策略。"
  },
  "CompleteLifecycleAction": {
    "params": [
      {
        "name": "LifecycleHookId",
        "desc": "生命周期挂钩ID"
      },
      {
        "name": "LifecycleActionResult",
        "desc": "生命周期动作的结果，取值范围为“CONTINUE”或“ABANDON”"
      },
      {
        "name": "InstanceId",
        "desc": "实例ID，“InstanceId”和“LifecycleActionToken”必须填充其中一个"
      },
      {
        "name": "LifecycleActionToken",
        "desc": "“InstanceId”和“LifecycleActionToken”必须填充其中一个"
      }
    ],
    "desc": "本接口（CompleteLifecycleAction）用于完成生命周期动作。\n\n* 用户通过调用本接口，指定一个具体的生命周期挂钩的结果（“CONITNUE”或者“ABANDON”）。如果一直不调用本接口，则生命周期挂钩会在超时后按照“DefaultResult”进行处理。\n"
  },
  "ModifyLoadBalancers": {
    "params": [
      {
        "name": "AutoScalingGroupId",
        "desc": "伸缩组ID"
      },
      {
        "name": "LoadBalancerIds",
        "desc": "传统负载均衡器ID列表，目前长度上限为1，LoadBalancerIds 和 ForwardLoadBalancers 二者同时最多只能指定一个"
      },
      {
        "name": "ForwardLoadBalancers",
        "desc": "应用型负载均衡器列表，目前长度上限为1，LoadBalancerIds 和 ForwardLoadBalancers 二者同时最多只能指定一个"
      }
    ],
    "desc": "本接口（ModifyLoadBalancers）用于修改伸缩组的负载均衡器。\n\n* 本接口用于为伸缩组指定新的负载均衡器配置，采用“完全覆盖”风格，无论之前配置如何，统一按照接口参数配置为新的负载均衡器。\n* 如果要为伸缩组清空负载均衡器，则在调用本接口时仅指定伸缩组ID，不指定具体负载均衡器。\n* 本接口会立即修改伸缩组的负载均衡器，并生成一个伸缩活动，异步修改存量实例的负载均衡器。"
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
  },
  "SetInstancesProtection": {
    "params": [
      {
        "name": "AutoScalingGroupId",
        "desc": "伸缩组ID。"
      },
      {
        "name": "InstanceIds",
        "desc": "实例ID。"
      },
      {
        "name": "ProtectedFromScaleIn",
        "desc": "实例是否需要移出保护。"
      }
    ],
    "desc": "本接口（SetInstancesProtection）用于设置实例移除保护。\n子机设置为移除保护之后，当发生不健康替换、报警策略、期望值变更等触发缩容时，将不对此子机缩容操作。"
  },
  "ModifyNotificationConfiguration": {
    "params": [
      {
        "name": "AutoScalingNotificationId",
        "desc": "待修改的通知ID。"
      },
      {
        "name": "NotificationTypes",
        "desc": "通知类型，即为需要订阅的通知类型集合，取值范围如下：\n<li>SCALE_OUT_SUCCESSFUL：扩容成功</li>\n<li>SCALE_OUT_FAILED：扩容失败</li>\n<li>SCALE_IN_SUCCESSFUL：缩容成功</li>\n<li>SCALE_IN_FAILED：缩容失败</li>\n<li>REPLACE_UNHEALTHY_INSTANCE_SUCCESSFUL：替换不健康子机成功</li>\n<li>REPLACE_UNHEALTHY_INSTANCE_FAILED：替换不健康子机失败</li>"
      },
      {
        "name": "NotificationUserGroupIds",
        "desc": "通知组ID，即为用户组ID集合，用户组ID可以通过[DescribeUserGroup](https://cloud.tencent.com/document/api/378/4404)查询。"
      }
    ],
    "desc": "本接口（ModifyNotificationConfiguration）用于修改通知。"
  },
  "CreateLaunchConfiguration": {
    "params": [
      {
        "name": "LaunchConfigurationName",
        "desc": "启动配置显示名称。名称仅支持中文、英文、数字、下划线、分隔符\"-\"、小数点，最大长度不能超60个字节。"
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
        "name": "InstanceType",
        "desc": "实例机型。不同实例机型指定了不同的资源规格，具体取值可通过调用接口 [DescribeInstanceTypeConfigs](https://cloud.tencent.com/document/api/213/15749) 来获得最新的规格表或参见[实例类型](https://cloud.tencent.com/document/product/213/11518)描述。\n`InstanceType`和`InstanceTypes`参数互斥，二者必填一个且只能填写一个。"
      },
      {
        "name": "SystemDisk",
        "desc": "实例系统盘配置信息。若不指定该参数，则按照系统默认值进行分配。"
      },
      {
        "name": "DataDisks",
        "desc": "实例数据盘配置信息。若不指定该参数，则默认不购买数据盘，最多支持指定11块数据盘。"
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
      },
      {
        "name": "InstanceTypes",
        "desc": "实例机型列表，不同实例机型指定了不同的资源规格，最多支持5种实例机型。\n`InstanceType`和`InstanceTypes`参数互斥，二者必填一个且只能填写一个。"
      },
      {
        "name": "InstanceTypesCheckPolicy",
        "desc": "实例类型校验策略，取值包括 ALL 和 ANY，默认取值为ANY。\n<br><li> ALL，所有实例类型（InstanceType）都可用则通过校验，否则校验报错。\n<br><li> ANY，存在任何一个实例类型（InstanceType）可用则通过校验，否则校验报错。\n\n实例类型不可用的常见原因包括该实例类型售罄、对应云盘售罄等。\n如果 InstanceTypes 中一款机型不存在或者已下线，则无论 InstanceTypesCheckPolicy 采用何种取值，都会校验报错。"
      },
      {
        "name": "InstanceTags",
        "desc": "标签列表。通过指定该参数，可以为扩容的实例绑定标签。最多支持指定10个标签。"
      }
    ],
    "desc": "本接口（CreateLaunchConfiguration）用于创建新的启动配置。\n\n* 启动配置，可以通过 `ModifyLaunchConfigurationAttributes` 修改少量字段。如需使用新的启动配置，建议重新创建启动配置。\n\n* 每个项目最多只能创建20个启动配置，详见[使用限制](https://cloud.tencent.com/document/product/377/3120)。\n"
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
        "desc": "销毁策略，目前长度上限为1。取值包括 OLDEST_INSTANCE 和 NEWEST_INSTANCE。\n<br><li> OLDEST_INSTANCE 优先销毁伸缩组中最旧的实例。\n<br><li> NEWEST_INSTANCE，优先销毁伸缩组中最新的实例。"
      },
      {
        "name": "VpcId",
        "desc": "VPC ID，基础网络则填空字符串。修改为具体VPC ID时，需指定相应的SubnetIds；修改为基础网络时，需指定相应的Zones。"
      },
      {
        "name": "Zones",
        "desc": "可用区列表"
      },
      {
        "name": "RetryPolicy",
        "desc": "重试策略，取值包括 IMMEDIATE_RETRY 和 INCREMENTAL_INTERVALS，默认取值为 IMMEDIATE_RETRY。\n<br><li> IMMEDIATE_RETRY，立即重试，在较短时间内快速重试，连续失败超过一定次数（5次）后不再重试。\n<br><li> INCREMENTAL_INTERVALS，间隔递增重试，随着连续失败次数的增加，重试间隔逐渐增大，重试间隔从秒级到1天不等。"
      },
      {
        "name": "ZonesCheckPolicy",
        "desc": "可用区校验策略，取值包括 ALL 和 ANY，默认取值为ANY。在伸缩组实际变更资源相关字段时（启动配置、可用区、子网）发挥作用。\n<br><li> ALL，所有可用区（Zone）或子网（SubnetId）都可用则通过校验，否则校验报错。\n<br><li> ANY，存在任何一个可用区（Zone）或子网（SubnetId）可用则通过校验，否则校验报错。\n\n可用区或子网不可用的常见原因包括该可用区CVM实例类型售罄、该可用区CBS云盘售罄、该可用区配额不足、该子网IP不足等。\n如果 Zones/SubnetIds 中可用区或者子网不存在，则无论 ZonesCheckPolicy 采用何种取值，都会校验报错。"
      }
    ],
    "desc": "本接口（ModifyAutoScalingGroup）用于修改伸缩组。"
  },
  "CreateNotificationConfiguration": {
    "params": [
      {
        "name": "AutoScalingGroupId",
        "desc": "伸缩组ID。"
      },
      {
        "name": "NotificationTypes",
        "desc": "通知类型，即为需要订阅的通知类型集合，取值范围如下：\n<li>SCALE_OUT_SUCCESSFUL：扩容成功</li>\n<li>SCALE_OUT_FAILED：扩容失败</li>\n<li>SCALE_IN_SUCCESSFUL：缩容成功</li>\n<li>SCALE_IN_FAILED：缩容失败</li>\n<li>REPLACE_UNHEALTHY_INSTANCE_SUCCESSFUL：替换不健康子机成功</li>\n<li>REPLACE_UNHEALTHY_INSTANCE_FAILED：替换不健康子机失败</li>"
      },
      {
        "name": "NotificationUserGroupIds",
        "desc": "通知组ID，即为用户组ID集合，用户组ID可以通过[DescribeUserGroup](https://cloud.tencent.com/document/api/378/4404)查询。"
      }
    ],
    "desc": "本接口（CreateNotificationConfiguration）用于创建通知。"
  },
  "DescribeAutoScalingInstances": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "待查询云服务器（CVM）的实例ID。参数不支持同时指定InstanceIds和Filters。"
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
    "desc": "本接口（DescribeAutoScalingInstances）用于查询弹性伸缩关联实例的信息。\n\n* 可以根据实例ID、伸缩组ID等信息来查询实例的详细信息。过滤信息详细请见过滤器`Filter`。\n* 如果参数为空，返回当前用户一定数量（`Limit`所指定的数量，默认为20）的实例。"
  },
  "CreateLifecycleHook": {
    "params": [
      {
        "name": "AutoScalingGroupId",
        "desc": "伸缩组ID"
      },
      {
        "name": "LifecycleHookName",
        "desc": "生命周期挂钩名称"
      },
      {
        "name": "LifecycleTransition",
        "desc": "进行生命周期挂钩的场景，取值范围包括“INSTANCE_LAUNCHING”和“INSTANCE_TERMINATING”"
      },
      {
        "name": "DefaultResult",
        "desc": "定义伸缩组在生命周期挂钩超时的情况下应采取的操作，取值范围是“CONTINUE”或“ABANDON”，默认值为“CONTINUE”"
      },
      {
        "name": "HeartbeatTimeout",
        "desc": "生命周期挂钩超时之前可以经过的最长时间（以秒为单位），范围从30到3600秒，默认值为300秒"
      },
      {
        "name": "NotificationMetadata",
        "desc": "弹性伸缩向通知目标发送的附加信息，默认值为''"
      },
      {
        "name": "NotificationTarget",
        "desc": "通知目标"
      }
    ],
    "desc": "本接口（CreateLifecycleHook）用于创建生命周期挂钩。\n\n* 您可以为生命周期挂钩配置消息通知，弹性伸缩会通知您的CMQ消息队列，通知内容形如：\n\n```\n{\n\t\"Service\": \"Tencent Cloud Auto Scaling\",\n\t\"Time\": \"2019-03-14T10:15:11Z\",\n\t\"AppId\": \"1251783334\",\n\t\"ActivityId\": \"asa-fznnvrja\",\n\t\"AutoScalingGroupId\": \"asg-rrrrtttt\",\n\t\"LifecycleHookId\": \"ash-xxxxyyyy\",\n\t\"LifecycleHookName\": \"my-hook\",\n\t\"LifecycleActionToken\": \"3080e1c9-0efe-4dd7-ad3b-90cd6618298f\",\n\t\"InstanceId\": \"ins-aaaabbbb\",\n\t\"LifecycleTransition\": \"INSTANCE_LAUNCHING\",\n\t\"NotificationMetadata\": \"\"\n}\n```"
  },
  "UpgradeLifecycleHook": {
    "params": [
      {
        "name": "LifecycleHookId",
        "desc": "生命周期挂钩ID"
      },
      {
        "name": "LifecycleHookName",
        "desc": "生命周期挂钩名称"
      },
      {
        "name": "LifecycleTransition",
        "desc": "进行生命周期挂钩的场景，取值范围包括“INSTANCE_LAUNCHING”和“INSTANCE_TERMINATING”"
      },
      {
        "name": "DefaultResult",
        "desc": "定义伸缩组在生命周期挂钩超时的情况下应采取的操作，取值范围是“CONTINUE”或“ABANDON”，默认值为“CONTINUE”"
      },
      {
        "name": "HeartbeatTimeout",
        "desc": "生命周期挂钩超时之前可以经过的最长时间（以秒为单位），范围从30到3600秒，默认值为300秒"
      },
      {
        "name": "NotificationMetadata",
        "desc": "弹性伸缩向通知目标发送的附加信息，默认值为''"
      },
      {
        "name": "NotificationTarget",
        "desc": "通知目标"
      }
    ],
    "desc": "本接口（UpgradeLifecycleHook）用于升级生命周期挂钩。\n\n* 本接口用于升级生命周期挂钩，采用“完全覆盖”风格，无论之前参数如何，统一按照接口参数设置为新的配置。对于非必填字段，不填写则按照默认值赋值。\n"
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
  "PreviewPaiDomainName": {
    "params": [
      {
        "name": "DomainNameType",
        "desc": "域名类型"
      }
    ],
    "desc": "本接口（PreviewPaiDomainName）用于预览PAI实例域名。\n"
  },
  "DescribePaiInstances": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "依据PAI实例的实例ID进行查询。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。"
      }
    ],
    "desc": "本接口（DescribePaiInstances）用于查询PAI实例信息。\n\n* 可以根据实例ID、实例域名等信息来查询PAI实例的详细信息。过滤信息详细请见过滤器`Filter`。\n* 如果参数为空，返回当前用户一定数量（`Limit`所指定的数量，默认为20）的PAI实例。"
  },
  "CreateScalingPolicy": {
    "params": [
      {
        "name": "AutoScalingGroupId",
        "desc": "伸缩组ID。"
      },
      {
        "name": "ScalingPolicyName",
        "desc": "告警触发策略名称。"
      },
      {
        "name": "AdjustmentType",
        "desc": "告警触发后，期望实例数修改方式。取值 ：<br><li>CHANGE_IN_CAPACITY：增加或减少若干期望实例数</li><li>EXACT_CAPACITY：调整至指定期望实例数</li> <li>PERCENT_CHANGE_IN_CAPACITY：按百分比调整期望实例数</li>"
      },
      {
        "name": "AdjustmentValue",
        "desc": "告警触发后，期望实例数的调整值。取值：<br><li>当 AdjustmentType 为 CHANGE_IN_CAPACITY 时，AdjustmentValue 为正数表示告警触发后增加实例，为负数表示告警触发后减少实例 </li> <li> 当 AdjustmentType 为 EXACT_CAPACITY 时，AdjustmentValue 的值即为告警触发后新的期望实例数，需要大于或等于0 </li> <li> 当 AdjustmentType 为 PERCENT_CHANGE_IN_CAPACITY 时，AdjusmentValue 为正数表示告警触发后按百分比增加实例，为负数表示告警触发后按百分比减少实例，单位是：%。"
      },
      {
        "name": "MetricAlarm",
        "desc": "告警监控指标。"
      },
      {
        "name": "Cooldown",
        "desc": "冷却时间，单位为秒。默认冷却时间300秒。"
      },
      {
        "name": "NotificationUserGroupIds",
        "desc": "通知组ID，即为用户组ID集合，用户组ID可以通过[DescribeUserGroup](https://cloud.tencent.com/document/api/378/4404)查询。"
      }
    ],
    "desc": "本接口（CreateScalingPolicy）用于创建告警触发策略。"
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
  "DeleteLifecycleHook": {
    "params": [
      {
        "name": "LifecycleHookId",
        "desc": "生命周期挂钩ID"
      }
    ],
    "desc": "本接口（DeleteLifecycleHook）用于删除生命周期挂钩。"
  },
  "DescribeLifecycleHooks": {
    "params": [
      {
        "name": "LifecycleHookIds",
        "desc": "按照一个或者多个生命周期挂钩ID查询。生命周期挂钩ID形如：`ash-8azjzxcl`。每次请求的上限为100。参数不支持同时指定`LifecycleHookIds`和`Filters`。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件。\n<li> lifecycle-hook-id - String - 是否必填：否 -（过滤条件）按照生命周期挂钩ID过滤。</li>\n<li> lifecycle-hook-name - String - 是否必填：否 -（过滤条件）按照生命周期挂钩名称过滤。</li>\n<li> auto-scaling-group-id - String - 是否必填：否 -（过滤条件）按照伸缩组ID过滤。</li>\n过滤条件。\n<li> lifecycle-hook-id - String - 是否必填：否 -（过滤条件）按照生命周期挂钩ID过滤。</li>\n<li> lifecycle-hook-name - String - 是否必填：否 -（过滤条件）按照生命周期挂钩名称过滤。</li>\n<li> auto-scaling-group-id - String - 是否必填：否 -（过滤条件）按照伸缩组ID过滤。</li>\n每次请求的`Filters`的上限为10，`Filter.Values`的上限为5。参数不支持同时指定`LifecycleHookIds `和`Filters`。"
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
    "desc": "本接口（DescribeLifecycleHooks）用于查询生命周期挂钩信息。\n\n* 可以根据伸缩组ID、生命周期挂钩ID或者生命周期挂钩名称等信息来查询生命周期挂钩的详细信息。过滤信息详细请见过滤器`Filter`。\n* 如果参数为空，返回当前用户一定数量（`Limit`所指定的数量，默认为20）的生命周期挂钩。"
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
  "DescribeAccountLimits": {
    "params": [],
    "desc": "本接口（DescribeAccountLimits）用于查询用户账户在弹性伸缩中的资源限制。"
  },
  "DescribeAutoScalingGroups": {
    "params": [
      {
        "name": "AutoScalingGroupIds",
        "desc": "按照一个或者多个伸缩组ID查询。伸缩组ID形如：`asg-nkdwoui0`。每次请求的上限为100。参数不支持同时指定`AutoScalingGroupIds`和`Filters`。"
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
    "desc": "本接口（DescribeAutoScalingGroups）用于查询伸缩组信息。\n\n* 可以根据伸缩组ID、伸缩组名称或者启动配置ID等信息来查询伸缩组的详细信息。过滤信息详细请见过滤器`Filter`。\n* 如果参数为空，返回当前用户一定数量（`Limit`所指定的数量，默认为20）的伸缩组。"
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
  "DescribeAutoScalingActivities": {
    "params": [
      {
        "name": "ActivityIds",
        "desc": "按照一个或者多个伸缩活动ID查询。伸缩活动ID形如：`asa-5l2ejpfo`。每次请求的上限为100。参数不支持同时指定`ActivityIds`和`Filters`。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件。\n<li> auto-scaling-group-id - String - 是否必填：否 -（过滤条件）按照伸缩组ID过滤。</li>\n<li> activity-status-code - String - 是否必填：否 -（过滤条件）按照伸缩活动状态过滤。（INIT：初始化中|RUNNING：运行中|SUCCESSFUL：活动成功|PARTIALLY_SUCCESSFUL：活动部分成功|FAILED：活动失败|CANCELLED：活动取消）</li>\n<li> activity-type - String - 是否必填：否 -（过滤条件）按照伸缩活动类型过滤。（SCALE_OUT：扩容活动|SCALE_IN：缩容活动|ATTACH_INSTANCES：添加实例|REMOVE_INSTANCES：销毁实例|DETACH_INSTANCES：移出实例|TERMINATE_INSTANCES_UNEXPECTEDLY：实例在CVM控制台被销毁|REPLACE_UNHEALTHY_INSTANCE：替换不健康实例|UPDATE_LOAD_BALANCERS：更新负载均衡器）</li>\n<li> activity-id - String - 是否必填：否 -（过滤条件）按照伸缩活动ID过滤。</li>\n每次请求的`Filters`的上限为10，`Filter.Values`的上限为5。参数不支持同时指定`ActivityIds`和`Filters`。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。"
      },
      {
        "name": "StartTime",
        "desc": "伸缩活动最早的开始时间，如果指定了ActivityIds，此参数将被忽略。取值为`UTC`时间，按照`ISO8601`标准，格式：`YYYY-MM-DDThh:mm:ssZ`。"
      },
      {
        "name": "EndTime",
        "desc": "伸缩活动最晚的结束时间，如果指定了ActivityIds，此参数将被忽略。取值为`UTC`时间，按照`ISO8601`标准，格式：`YYYY-MM-DDThh:mm:ssZ`。"
      }
    ],
    "desc": "本接口（DescribeAutoScalingActivities）用于查询伸缩组的伸缩活动记录。"
  },
  "DeleteNotificationConfiguration": {
    "params": [
      {
        "name": "AutoScalingNotificationId",
        "desc": "待删除的通知ID。"
      }
    ],
    "desc": "本接口（DeleteNotificationConfiguration）用于删除特定的通知。"
  },
  "DescribeScheduledActions": {
    "params": [
      {
        "name": "ScheduledActionIds",
        "desc": "按照一个或者多个定时任务ID查询。实例ID形如：asst-am691zxo。每次请求的实例的上限为100。参数不支持同时指定ScheduledActionIds和Filters。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件。\n<li> scheduled-action-id - String - 是否必填：否 -（过滤条件）按照定时任务ID过滤。</li>\n<li> scheduled-action-name - String - 是否必填：否 - （过滤条件） 按照定时任务名称过滤。</li>\n<li> auto-scaling-group-id - String - 是否必填：否 - （过滤条件） 按照伸缩组ID过滤。</li>"
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
    "desc": "本接口 (DescribeScheduledActions) 用于查询一个或多个定时任务的详细信息。\n\n* 可以根据定时任务ID、定时任务名称或者伸缩组ID等信息来查询定时任务的详细信息。过滤信息详细请见过滤器`Filter`。\n* 如果参数为空，返回当前用户一定数量（Limit所指定的数量，默认为20）的定时任务。"
  },
  "ModifyLaunchConfigurationAttributes": {
    "params": [
      {
        "name": "LaunchConfigurationId",
        "desc": "启动配置ID"
      },
      {
        "name": "ImageId",
        "desc": "指定有效的[镜像](https://cloud.tencent.com/document/product/213/4940)ID，格式形如`img-8toqc6s3`。镜像类型分为四种：<br/><li>公共镜像</li><li>自定义镜像</li><li>共享镜像</li><li>服务市场镜像</li><br/>可通过以下方式获取可用的镜像ID：<br/><li>`公共镜像`、`自定义镜像`、`共享镜像`的镜像ID可通过登录[控制台](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE)查询；`服务镜像市场`的镜像ID可通过[云市场](https://market.cloud.tencent.com/list)查询。</li><li>通过调用接口 [DescribeImages](https://cloud.tencent.com/document/api/213/15715) ，取返回信息中的`ImageId`字段。</li>"
      },
      {
        "name": "InstanceTypes",
        "desc": "实例类型列表，不同实例机型指定了不同的资源规格，最多支持5种实例机型。\n启动配置，通过 InstanceType 表示单一实例类型，通过 InstanceTypes 表示多实例类型。指定 InstanceTypes 成功启动配置后，原有的 InstanceType 自动失效。"
      },
      {
        "name": "InstanceTypesCheckPolicy",
        "desc": "实例类型校验策略，在实际修改 InstanceTypes 时发挥作用，取值包括 ALL 和 ANY，默认取值为ANY。\n<br><li> ALL，所有实例类型（InstanceType）都可用则通过校验，否则校验报错。\n<br><li> ANY，存在任何一个实例类型（InstanceType）可用则通过校验，否则校验报错。\n\n实例类型不可用的常见原因包括该实例类型售罄、对应云盘售罄等。\n如果 InstanceTypes 中一款机型不存在或者已下线，则无论 InstanceTypesCheckPolicy 采用何种取值，都会校验报错。"
      },
      {
        "name": "LaunchConfigurationName",
        "desc": "启动配置显示名称。名称仅支持中文、英文、数字、下划线、分隔符\"-\"、小数点，最大长度不能超60个字节。"
      },
      {
        "name": "UserData",
        "desc": "经过 Base64 编码后的自定义数据，最大长度不超过16KB。如果要清空UserData，则指定其为空字符串"
      }
    ],
    "desc": "本接口（ModifyLaunchConfigurationAttributes）用于修改启动配置部分属性。\n\n* 修改启动配置后，已经使用该启动配置扩容的存量实例不会发生变更，此后使用该启动配置的新增实例会按照新的配置进行扩容。\n* 本接口支持修改部分简单类型。"
  }
}