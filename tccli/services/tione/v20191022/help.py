# -*- coding: utf-8 -*-
DESC = "tione-2019-10-22"
INFO = {
  "DescribeTrainingJob": {
    "params": [
      {
        "name": "TrainingJobName",
        "desc": "训练任务名称"
      }
    ],
    "desc": "查询训练任务"
  },
  "StopNotebookInstance": {
    "params": [
      {
        "name": "NotebookInstanceName",
        "desc": "Notebook实例名称"
      }
    ],
    "desc": "停止Notebook实例"
  },
  "UpdateNotebookInstance": {
    "params": [
      {
        "name": "NotebookInstanceName",
        "desc": "Notebook实例名称"
      },
      {
        "name": "RoleArn",
        "desc": "角色的资源描述"
      },
      {
        "name": "RootAccess",
        "desc": "Root访问权限"
      },
      {
        "name": "VolumeSizeInGB",
        "desc": "数据卷大小(GB)"
      },
      {
        "name": "InstanceType",
        "desc": "算力资源类型"
      }
    ],
    "desc": "更新Notebook实例"
  },
  "DescribeNotebookInstance": {
    "params": [
      {
        "name": "NotebookInstanceName",
        "desc": "Notebook实例名称"
      }
    ],
    "desc": "查询Notebook实例详情"
  },
  "CreatePresignedNotebookInstanceUrl": {
    "params": [
      {
        "name": "NotebookInstanceName",
        "desc": "Notebook实例名称"
      },
      {
        "name": "SessionExpirationDurationInSeconds",
        "desc": "session有效时间，秒"
      }
    ],
    "desc": "创建Notebook授权Url"
  },
  "CreateNotebookInstance": {
    "params": [
      {
        "name": "NotebookInstanceName",
        "desc": "Notebook实例名称"
      },
      {
        "name": "InstanceType",
        "desc": "Notebook算力类型"
      },
      {
        "name": "RoleArn",
        "desc": "角色的资源描述"
      },
      {
        "name": "DirectInternetAccess",
        "desc": "外网访问权限，可取值Enabled/Disabled"
      },
      {
        "name": "RootAccess",
        "desc": "Root用户权限，可取值Enabled/Disabled"
      },
      {
        "name": "SecurityGroupIds",
        "desc": "安全组ID"
      },
      {
        "name": "SubnetId",
        "desc": "子网ID"
      },
      {
        "name": "VolumeSizeInGB",
        "desc": "数据卷大小(GB)"
      },
      {
        "name": "Tags",
        "desc": "Notebook标签"
      }
    ],
    "desc": "创建Notebook实例"
  },
  "DescribeNotebookInstances": {
    "params": [
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "Limit",
        "desc": "限制数目"
      },
      {
        "name": "SortBy",
        "desc": "排序字段"
      },
      {
        "name": "SortOrder",
        "desc": "排序方式"
      },
      {
        "name": "CreationTimeAfter",
        "desc": "创建时间晚于"
      },
      {
        "name": "CreationTimeBefore",
        "desc": "创建时间早于"
      },
      {
        "name": "LastModifiedTimeAfter",
        "desc": "最近修改时间晚于"
      },
      {
        "name": "LastModifiedTimeBefore",
        "desc": "最近修改时间早于"
      },
      {
        "name": "NameContains",
        "desc": "根据名称过滤"
      },
      {
        "name": "StatusEquals",
        "desc": "根据状态过滤"
      },
      {
        "name": "MaxResults",
        "desc": "最大返回个数"
      }
    ],
    "desc": "查询Notebook实例列表"
  },
  "CreateTrainingJob": {
    "params": [
      {
        "name": "TrainingJobName",
        "desc": "训练任务名称"
      },
      {
        "name": "AlgorithmSpecification",
        "desc": "算法镜像配置"
      },
      {
        "name": "InputDataConfig",
        "desc": "输入数据配置"
      },
      {
        "name": "OutputDataConfig",
        "desc": "输出数据配置"
      },
      {
        "name": "ResourceConfig",
        "desc": "资源实例配置"
      },
      {
        "name": "StoppingCondition",
        "desc": "中止条件"
      },
      {
        "name": "VpcConfig",
        "desc": "私有网络配置"
      },
      {
        "name": "HyperParameters",
        "desc": "算法超级参数"
      },
      {
        "name": "RoleName",
        "desc": "角色名称"
      },
      {
        "name": "EnvConfig",
        "desc": "环境变量配置"
      }
    ],
    "desc": "创建训练任务"
  },
  "StartNotebookInstance": {
    "params": [
      {
        "name": "NotebookInstanceName",
        "desc": "Notebook实例名称"
      }
    ],
    "desc": "启动Notebook实例"
  },
  "StopTrainingJob": {
    "params": [
      {
        "name": "TrainingJobName",
        "desc": "训练任务名称"
      }
    ],
    "desc": "停止训练任务"
  },
  "DeleteNotebookInstance": {
    "params": [
      {
        "name": "NotebookInstanceName",
        "desc": "Notebook实例名称"
      }
    ],
    "desc": "删除notebook实例"
  }
}