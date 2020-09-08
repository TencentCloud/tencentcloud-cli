# -*- coding: utf-8 -*-
DESC = "batch-2017-03-12"
INFO = {
  "DescribeCvmZoneInstanceConfigInfos": {
    "params": [
      {
        "name": "Filters",
        "desc": "过滤条件。\n<li> zone - String - 是否必填：否 -（过滤条件）按照可用区过滤。</li>\n<li> instance-family String - 是否必填：否 -（过滤条件）按照机型系列过滤。实例机型系列形如：S1、I1、M1等。</li>\n<li> instance-type - String - 是否必填：否 - （过滤条件）按照机型过滤。</li>\n<li> instance-charge-type - String - 是否必填：否 -（过滤条件）按照实例计费模式过滤。 ( POSTPAID_BY_HOUR：表示后付费，即按量计费机型 | SPOTPAID：表示竞价付费机型。 )  </li>"
      }
    ],
    "desc": "获取批量计算可用区机型配置信息"
  },
  "CreateTaskTemplate": {
    "params": [
      {
        "name": "TaskTemplateName",
        "desc": "任务模板名称"
      },
      {
        "name": "TaskTemplateInfo",
        "desc": "任务模板内容，参数要求与任务一致"
      },
      {
        "name": "TaskTemplateDescription",
        "desc": "任务模板描述"
      }
    ],
    "desc": "用于创建任务模板"
  },
  "DescribeJobSubmitInfo": {
    "params": [
      {
        "name": "JobId",
        "desc": "作业ID"
      }
    ],
    "desc": "用于查询指定作业的提交信息，其返回内容包括 JobId 和 SubmitJob 接口中作为输入参数的作业提交信息"
  },
  "TerminateComputeNode": {
    "params": [
      {
        "name": "EnvId",
        "desc": "计算环境ID"
      },
      {
        "name": "ComputeNodeId",
        "desc": "计算节点ID"
      }
    ],
    "desc": "用于销毁计算节点。\n对于状态为CREATED、CREATION_FAILED、RUNNING和ABNORMAL的节点，允许销毁处理。"
  },
  "DeleteJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "作业ID"
      }
    ],
    "desc": "用于删除作业记录。\n删除作业的效果相当于删除作业相关的所有信息。删除成功后，作业相关的所有信息都无法查询。\n待删除的作业必须处于完结状态，且其内部包含的所有任务实例也必须处于完结状态，否则会禁止操作。完结状态，是指处于 SUCCEED 或 FAILED 状态。"
  },
  "DescribeAvailableCvmInstanceTypes": {
    "params": [
      {
        "name": "Filters",
        "desc": "过滤条件。\n<li> zone - String - 是否必填：否 -（过滤条件）按照可用区过滤。</li>\n<li> instance-family String - 是否必填：否 -（过滤条件）按照机型系列过滤。实例机型系列形如：S1、I1、M1等。</li>"
      }
    ],
    "desc": "查看可用的CVM机型配置信息"
  },
  "AttachInstances": {
    "params": [
      {
        "name": "EnvId",
        "desc": "计算环境ID"
      },
      {
        "name": "Instances",
        "desc": "加入计算环境实例列表"
      }
    ],
    "desc": "此接口可将已存在实例添加到计算环境中。\n实例需要满足如下条件：<br/>\n1.实例不在批量计算系统中。<br/>\n2.实例状态要求处于运行中。<br/>\n3.支持预付费实例，按小时后付费实例，专享子机实例。不支持竞价实例。<br/>\n\n此接口会将加入到计算环境中的实例重设UserData和重装操作系统。"
  },
  "CreateComputeEnv": {
    "params": [
      {
        "name": "ComputeEnv",
        "desc": "计算环境信息"
      },
      {
        "name": "Placement",
        "desc": "位置信息"
      },
      {
        "name": "ClientToken",
        "desc": "用于保证请求幂等性的字符串。该字符串由用户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。"
      }
    ],
    "desc": "用于创建计算环境"
  },
  "DescribeComputeEnvs": {
    "params": [
      {
        "name": "EnvIds",
        "desc": "计算环境ID列表，与Filters参数不能同时指定。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件\n<li> zone - String - 是否必填：否 -（过滤条件）按照可用区过滤。</li>\n<li> env-id - String - 是否必填：否 -（过滤条件）按照计算环境ID过滤。</li>\n<li> env-name - String - 是否必填：否 -（过滤条件）按照计算环境名称过滤。</li>\n<li> resource-type - String - 是否必填：否 -（过滤条件）按照计算资源类型过滤，取值CVM或者CPM(黑石)。</li>\n与EnvIds参数不能同时指定。"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "Limit",
        "desc": "返回数量"
      }
    ],
    "desc": "用于查看计算环境列表"
  },
  "DetachInstances": {
    "params": [
      {
        "name": "EnvId",
        "desc": "计算环境ID"
      },
      {
        "name": "InstanceIds",
        "desc": "实例ID列表"
      }
    ],
    "desc": "将添加到计算环境中的实例从计算环境中移出。若是由批量计算自动创建的计算节点实例则不允许移出。"
  },
  "DescribeTaskLogs": {
    "params": [
      {
        "name": "JobId",
        "desc": "作业ID"
      },
      {
        "name": "TaskName",
        "desc": "任务名称"
      },
      {
        "name": "TaskInstanceIndexes",
        "desc": "任务实例集合"
      },
      {
        "name": "Offset",
        "desc": "起始任务实例"
      },
      {
        "name": "Limit",
        "desc": "最大任务实例数"
      }
    ],
    "desc": "用于获取任务多个实例标准输出和标准错误日志。"
  },
  "TerminateJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "作业ID"
      }
    ],
    "desc": "用于终止作业。\n当作业处于“SUBMITTED”状态时，禁止终止操作；当作业处于“SUCCEED”状态时，终止操作不会生效。\n终止作业是一个异步过程。整个终止过程的耗时和任务总数成正比。终止的效果相当于所含的所有任务实例进行TerminateTaskInstance操作。具体效果和用法可参考TerminateTaskInstance。"
  },
  "DescribeTask": {
    "params": [
      {
        "name": "JobId",
        "desc": "作业ID"
      },
      {
        "name": "TaskName",
        "desc": "任务名称"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "Limit",
        "desc": "返回数量。默认取值100，最大取值1000。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件，详情如下：\n<li> task-instance-type - String - 是否必填： 否 - 按照任务实例状态进行过滤（SUBMITTED：已提交；PENDING：等待中；RUNNABLE：可运行；STARTING：启动中；RUNNING：运行中；SUCCEED：成功；FAILED：失败；FAILED_INTERRUPTED：失败后保留实例）。</li>"
      }
    ],
    "desc": "用于查询指定任务的详细信息，包括任务内部的任务实例信息。"
  },
  "DescribeComputeEnv": {
    "params": [
      {
        "name": "EnvId",
        "desc": "计算环境ID"
      }
    ],
    "desc": "用于查询计算环境的详细信息"
  },
  "DescribeJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "作业标识"
      }
    ],
    "desc": "用于查看一个作业的详细信息，包括内部任务（Task）和依赖（Dependence）信息。"
  },
  "DescribeComputeEnvActivities": {
    "params": [
      {
        "name": "EnvId",
        "desc": "计算环境ID"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "Limit",
        "desc": "返回数量"
      },
      {
        "name": "Filters",
        "desc": "过滤条件\n<li> compute-node-id - String - 是否必填：否 -（过滤条件）按照计算节点ID过滤。</li>"
      }
    ],
    "desc": "用于查询计算环境的活动信息"
  },
  "TerminateComputeNodes": {
    "params": [
      {
        "name": "EnvId",
        "desc": "计算环境ID"
      },
      {
        "name": "ComputeNodeIds",
        "desc": "计算节点ID列表"
      }
    ],
    "desc": "用于批量销毁计算节点，不允许重复销毁同一个节点。"
  },
  "DescribeTaskTemplates": {
    "params": [
      {
        "name": "TaskTemplateIds",
        "desc": "任务模板ID列表，与Filters参数不能同时指定。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件\n<li> task-template-name - String - 是否必填：否 -（过滤条件）按照任务模板名称过滤。</li>\n与TaskTemplateIds参数不能同时指定。"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "Limit",
        "desc": "返回数量"
      }
    ],
    "desc": "用于查询任务模板信息"
  },
  "DescribeInstanceCategories": {
    "params": [],
    "desc": "目前对CVM现有实例族分类，每一类包含若干实例族。该接口用于查询实例分类信息。"
  },
  "DeleteTaskTemplates": {
    "params": [
      {
        "name": "TaskTemplateIds",
        "desc": "用于删除任务模板信息"
      }
    ],
    "desc": "用于删除任务模板信息"
  },
  "TerminateTaskInstance": {
    "params": [
      {
        "name": "JobId",
        "desc": "作业ID"
      },
      {
        "name": "TaskName",
        "desc": "任务名称"
      },
      {
        "name": "TaskInstanceIndex",
        "desc": "任务实例索引"
      }
    ],
    "desc": "用于终止任务实例。\n对于状态已经为“SUCCEED”和“FAILED”的任务实例，不做处理。\n对于状态为“SUBMITTED”、“PENDING”、“RUNNABLE”的任务实例，状态将置为“FAILED”状态。\n对于状态为“STARTING”、“RUNNING”、“FAILED_INTERRUPTED”的任务实例，分区两种情况：如果未显示指定计算环境，会先销毁CVM服务器，然后将状态置为“FAILED”，具有一定耗时；如果指定了计算环境EnvId，任务实例状态置为“FAILED”，并重启执行该任务的CVM服务器，具有一定的耗时。\n对于状态为“FAILED_INTERRUPTED”的任务实例，终止操作实际成功之后，相关资源和配额才会释放。"
  },
  "ModifyComputeEnv": {
    "params": [
      {
        "name": "EnvId",
        "desc": "计算环境ID"
      },
      {
        "name": "DesiredComputeNodeCount",
        "desc": "计算节点期望个数"
      },
      {
        "name": "EnvName",
        "desc": "计算环境名称"
      },
      {
        "name": "EnvDescription",
        "desc": "计算环境描述"
      },
      {
        "name": "EnvData",
        "desc": "计算环境属性数据"
      }
    ],
    "desc": "用于修改计算环境属性"
  },
  "CreateCpmComputeEnv": {
    "params": [
      {
        "name": "ComputeEnv",
        "desc": "计算环境信息"
      },
      {
        "name": "Placement",
        "desc": "位置信息"
      },
      {
        "name": "ClientToken",
        "desc": "用于保证请求幂等性的字符串。该字符串由用户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。"
      }
    ],
    "desc": "创建黑石计算环境"
  },
  "DescribeComputeEnvCreateInfo": {
    "params": [
      {
        "name": "EnvId",
        "desc": "计算环境ID"
      }
    ],
    "desc": "查看计算环境的创建信息。"
  },
  "SubmitJob": {
    "params": [
      {
        "name": "Placement",
        "desc": "作业所提交的位置信息。通过该参数可以指定作业关联CVM所属可用区等信息。"
      },
      {
        "name": "Job",
        "desc": "作业信息"
      },
      {
        "name": "ClientToken",
        "desc": "用于保证请求幂等性的字符串。该字符串由用户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。"
      }
    ],
    "desc": "用于提交一个作业"
  },
  "DescribeComputeEnvCreateInfos": {
    "params": [
      {
        "name": "EnvIds",
        "desc": "计算环境ID列表，与Filters参数不能同时指定。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件\n<li> zone - String - 是否必填：否 -（过滤条件）按照可用区过滤。</li>\n<li> env-id - String - 是否必填：否 -（过滤条件）按照计算环境ID过滤。</li>\n<li> env-name - String - 是否必填：否 -（过滤条件）按照计算环境名称过滤。</li>\n与EnvIds参数不能同时指定。"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "Limit",
        "desc": "返回数量"
      }
    ],
    "desc": "用于查看计算环境创建信息列表，包括名称、描述、类型、环境参数、通知及期望节点数等。"
  },
  "DescribeJobs": {
    "params": [
      {
        "name": "JobIds",
        "desc": "作业ID列表，与Filters参数不能同时指定。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件\n<li> job-id - String - 是否必填：否 -（过滤条件）按照作业ID过滤。</li>\n<li> job-name - String - 是否必填：否 -（过滤条件）按照作业名称过滤。</li>\n<li> job-state - String - 是否必填：否 -（过滤条件）按照作业状态过滤。</li>\n<li> zone - String - 是否必填：否 -（过滤条件）按照可用区过滤。</li>\n与JobIds参数不能同时指定。"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "Limit",
        "desc": "返回数量"
      }
    ],
    "desc": "用于查询若干个作业的概览信息"
  },
  "DescribeCpmOsInfo": {
    "params": [
      {
        "name": "DeviceClassCode",
        "desc": "黑石设备类型代号。 可以从[DescribeDeviceClass](https://cloud.tencent.com/document/api/386/32911)查询设备类型列表。"
      }
    ],
    "desc": "创建黑石计算环境时，查询批量计算环境支持的黑石操作系统信息"
  },
  "DeleteComputeEnv": {
    "params": [
      {
        "name": "EnvId",
        "desc": "计算环境ID"
      }
    ],
    "desc": "用于删除计算环境"
  },
  "ModifyTaskTemplate": {
    "params": [
      {
        "name": "TaskTemplateId",
        "desc": "任务模板ID"
      },
      {
        "name": "TaskTemplateName",
        "desc": "任务模板名称"
      },
      {
        "name": "TaskTemplateDescription",
        "desc": "任务模板描述"
      },
      {
        "name": "TaskTemplateInfo",
        "desc": "任务模板信息"
      }
    ],
    "desc": "用于修改任务模板"
  },
  "RetryJobs": {
    "params": [
      {
        "name": "JobIds",
        "desc": "作业ID列表。"
      }
    ],
    "desc": "用于重试作业中失败的任务实例。\n当且仅当作业处于“FAILED”状态，支持重试操作。重试操作成功后，作业会按照“DAG”中指定的任务依赖关系，依次重试各个任务中失败的任务实例。任务实例的历史信息将被重置，如同首次运行一样，参与后续的调度和执行。"
  }
}