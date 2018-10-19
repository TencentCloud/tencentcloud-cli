# -*- coding: utf-8 -*-
DESC = "batch-2017-03-12"
INFO = {
  "DescribeComputeEnv": {
    "params": [
      {
        "name": "EnvId",
        "desc": "计算环境ID"
      }
    ],
    "desc": "用于查询计算环境的详细信息"
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
        "desc": "过滤条件"
      }
    ],
    "desc": "查看可用的CVM机型配置信息"
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
        "desc": "计算环境ID"
      },
      {
        "name": "Filters",
        "desc": "过滤条件"
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
  "TerminateJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "作业ID"
      }
    ],
    "desc": "用于终止作业。\n终止作业的效果相当于所含的所有任务实例进行TerminateTaskInstance操作。具体效果和用法可参考TerminateTaskInstance。"
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
  "DescribeCvmZoneInstanceConfigInfos": {
    "params": [
      {
        "name": "Filters",
        "desc": "过滤条件"
      }
    ],
    "desc": "获取批量计算可用区机型配置信息"
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
        "desc": "过滤条件"
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
        "desc": "任务模板ID"
      },
      {
        "name": "Filters",
        "desc": "过滤条件"
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
    "desc": "用于终止任务实例\n对于状态已经为SUCCEED、FAILED的TaskInstance，batch不做处理。\n对于状态为SUBMITTED、PENDING、RUNNABLE的TaskInstance，batch会将其置为FAILED状态。\n对于状态为STARTING、RUNNING、FAILED_INTERRUPTED的TaskInstance，batch会先终止CVM，然后将状态置为FAILED，因此具有一定耗时。特别是如果CVM正在创建中，此时无法立即销毁CVM，Batch会在旁路注册一个定时销毁操作，在CVM创建好之后异步销毁。\n对于状态为FAILED_INTERRUPTED的TaskInstance，TerminateTaskInstance操作实际成功之后，相关资源和配额才会释放。\n本接口只支持提交到匿名计算环境的作业（SubmitJob指定ComputeEnv，不指定EnvId）。对于提交到具名计算环境的作业（SubmitJob指定EnvId，不指定ComputeEnv），不支持TerminateTaskInstance和TerminateJob操作。"
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
      }
    ],
    "desc": "用于修改计算环境的期望节点数量"
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
        "desc": "计算环境ID"
      },
      {
        "name": "Filters",
        "desc": "过滤条件\n<li> zone - String - 是否必填：否 -（过滤条件）按照可用区过滤。</li>\n<li> env-id - String - 是否必填：否 -（过滤条件）按照计算环境ID过滤。</li>\n<li> env-name - String - 是否必填：否 -（过滤条件）按照计算环境名称过滤。</li>"
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
        "desc": "作业ID"
      },
      {
        "name": "Filters",
        "desc": "过滤条件"
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
  }
}