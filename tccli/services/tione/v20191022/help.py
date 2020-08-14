# -*- coding: utf-8 -*-
DESC = "tione-2019-10-22"
INFO = {
  "UpdateNotebookInstance": {
    "params": [
      {
        "name": "NotebookInstanceName",
        "desc": "Notebook实例名称\n规则：“^\\[a-zA-Z0-9\\](-\\*\\[a-zA-Z0-9\\])\\*$”"
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
      },
      {
        "name": "LifecycleScriptsName",
        "desc": "notebook生命周期脚本名称"
      },
      {
        "name": "DisassociateLifecycleScript",
        "desc": "是否解绑生命周期脚本，默认 false。\n该值为true时，LifecycleScriptsName将被忽略"
      },
      {
        "name": "DefaultCodeRepository",
        "desc": "默认存储库名称\n可以是已创建的存储库名称或者已https://开头的公共git库"
      },
      {
        "name": "AdditionalCodeRepositories",
        "desc": "其他存储库列表\n每个元素可以是已创建的存储库名称或者已https://开头的公共git库"
      },
      {
        "name": "DisassociateDefaultCodeRepository",
        "desc": "是否取消关联默认存储库，默认false\n该值为true时，DefaultCodeRepository将被忽略"
      },
      {
        "name": "DisassociateAdditionalCodeRepositories",
        "desc": "是否取消关联其他存储库，默认false\n该值为true时，AdditionalCodeRepositories将被忽略"
      },
      {
        "name": "ClsAccess",
        "desc": "已弃用，请使用ClsConfig配置。是否开启CLS日志服务，可取值Enabled/Disabled"
      },
      {
        "name": "AutoStopping",
        "desc": "自动停止，可取值Enabled/Disabled\n取值为Disabled的时候StoppingCondition将被忽略\n取值为Enabled的时候读取StoppingCondition作为自动停止的配置"
      },
      {
        "name": "StoppingCondition",
        "desc": "自动停止配置，只在AutoStopping为Enabled的时候生效"
      },
      {
        "name": "ClsConfig",
        "desc": "接入日志的配置，默认使用免费日志服务。"
      }
    ],
    "desc": "更新Notebook实例"
  },
  "DescribeNotebookLifecycleScripts": {
    "params": [
      {
        "name": "Offset",
        "desc": "偏移量，默认为0"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20"
      },
      {
        "name": "Filters",
        "desc": "过滤条件。\ninstance-name - String - 是否必填：否 -（过滤条件）按照名称过滤。\nsearch-by-name - String - 是否必填：否 -（过滤条件）按照名称检索，模糊匹配。"
      },
      {
        "name": "SortOrder",
        "desc": "排序规则。默认取Descending\nDescending 按更新时间降序\nAscending 按更新时间升序"
      }
    ],
    "desc": "查看notebook生命周期脚本列表"
  },
  "StartNotebookInstance": {
    "params": [
      {
        "name": "NotebookInstanceName",
        "desc": "Notebook实例名称"
      },
      {
        "name": "AutoStopping",
        "desc": "自动停止，可取值Enabled/Disabled\n取值为Disabled的时候StoppingCondition将被忽略\n取值为Enabled的时候读取StoppingCondition作为自动停止的配置"
      },
      {
        "name": "StoppingCondition",
        "desc": "自动停止配置，只在AutoStopping为Enabled的时候生效"
      }
    ],
    "desc": "启动Notebook实例"
  },
  "DeleteNotebookInstance": {
    "params": [
      {
        "name": "NotebookInstanceName",
        "desc": "Notebook实例名称"
      }
    ],
    "desc": "删除notebook实例"
  },
  "DescribeNotebookLifecycleScript": {
    "params": [
      {
        "name": "NotebookLifecycleScriptsName",
        "desc": "生命周期脚本名称"
      }
    ],
    "desc": "查看notebook生命周期脚本详情"
  },
  "CreatePresignedNotebookInstanceUrl": {
    "params": [
      {
        "name": "NotebookInstanceName",
        "desc": "Notebook实例名称\n规则：“^\\[a-zA-Z0-9\\](-\\*\\[a-zA-Z0-9\\])\\*$”"
      },
      {
        "name": "SessionExpirationDurationInSeconds",
        "desc": "session有效时间，秒，取值范围[1800, 43200]"
      }
    ],
    "desc": "创建Notebook授权Url"
  },
  "CreateCodeRepository": {
    "params": [
      {
        "name": "CodeRepositoryName",
        "desc": "存储库名称"
      },
      {
        "name": "GitConfig",
        "desc": "Git相关配置"
      },
      {
        "name": "GitSecret",
        "desc": "Git凭证"
      }
    ],
    "desc": "创建存储库"
  },
  "UpdateNotebookLifecycleScript": {
    "params": [
      {
        "name": "NotebookLifecycleScriptsName",
        "desc": "notebook生命周期脚本名称"
      },
      {
        "name": "CreateScript",
        "desc": "创建脚本，base64编码\nbase64后的脚本长度不能超过16384个字符"
      },
      {
        "name": "StartScript",
        "desc": "启动脚本，base64编码\nbase64后的脚本长度不能超过16384个字符"
      }
    ],
    "desc": "更新notebook生命周期脚本"
  },
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
  "CreateNotebookInstance": {
    "params": [
      {
        "name": "NotebookInstanceName",
        "desc": "Notebook实例名称，不能超过63个字符\n规则：“^\\[a-zA-Z0-9\\](-\\*\\[a-zA-Z0-9\\])\\*$”"
      },
      {
        "name": "InstanceType",
        "desc": "Notebook算力类型\n参考https://cloud.tencent.com/document/product/851/41239"
      },
      {
        "name": "VolumeSizeInGB",
        "desc": "数据卷大小(GB)\n用户持久化Notebook实例的数据"
      },
      {
        "name": "DirectInternetAccess",
        "desc": "外网访问权限，可取值Enabled/Disabled\n开启后，Notebook实例可以具有访问外网80，443端口的权限"
      },
      {
        "name": "RootAccess",
        "desc": "Root用户权限，可取值Enabled/Disabled\n开启后，Notebook实例可以切换至root用户执行命令"
      },
      {
        "name": "SubnetId",
        "desc": "子网ID\n如果需要Notebook实例访问VPC内的资源，则需要选择对应的子网"
      },
      {
        "name": "LifecycleScriptsName",
        "desc": "生命周期脚本名称\n必须是已存在的生命周期脚本，具体参考https://cloud.tencent.com/document/product/851/43140"
      },
      {
        "name": "DefaultCodeRepository",
        "desc": "默认存储库名称\n可以是已创建的存储库名称或者已https://开头的公共git库\n参考https://cloud.tencent.com/document/product/851/43139"
      },
      {
        "name": "AdditionalCodeRepositories",
        "desc": "其他存储库列表\n每个元素可以是已创建的存储库名称或者已https://开头的公共git库\n参考https://cloud.tencent.com/document/product/851/43139"
      },
      {
        "name": "ClsAccess",
        "desc": "已弃用，请使用ClsConfig配置。\n是否开启CLS日志服务，可取值Enabled/Disabled，默认为Disabled\n开启后，Notebook运行的日志会收集到CLS中，CLS会产生费用，请根据需要选择"
      },
      {
        "name": "StoppingCondition",
        "desc": "自动停止配置\n选择定时停止Notebook实例"
      },
      {
        "name": "AutoStopping",
        "desc": "自动停止，可取值Enabled/Disabled\n取值为Disabled的时候StoppingCondition将被忽略\n取值为Enabled的时候读取StoppingCondition作为自动停止的配置"
      },
      {
        "name": "ClsConfig",
        "desc": "接入日志的配置，默认接入免费日志"
      }
    ],
    "desc": "创建Notebook实例"
  },
  "DescribeCodeRepository": {
    "params": [
      {
        "name": "CodeRepositoryName",
        "desc": "存储库名称"
      }
    ],
    "desc": "查询存储库详情"
  },
  "CreateNotebookLifecycleScript": {
    "params": [
      {
        "name": "NotebookLifecycleScriptsName",
        "desc": "Notebook生命周期脚本名称"
      },
      {
        "name": "CreateScript",
        "desc": "创建脚本，base64编码\nbase64后的脚本长度不能超过16384个字符"
      },
      {
        "name": "StartScript",
        "desc": "启动脚本，base64编码\nbase64后的脚本长度不能超过16384个字符"
      }
    ],
    "desc": "创建Notebook生命周期脚本"
  },
  "DeleteCodeRepository": {
    "params": [
      {
        "name": "CodeRepositoryName",
        "desc": "存储库名称"
      }
    ],
    "desc": "删除存储库"
  },
  "DescribeNotebookSummary": {
    "params": [],
    "desc": "查询Notebook概览数据"
  },
  "DescribeTrainingJobs": {
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
        "name": "CreationTimeAfter",
        "desc": "创建时间晚于"
      },
      {
        "name": "CreationTimeBefore",
        "desc": "创建时间早于"
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
        "name": "Filters",
        "desc": "过滤条件。\ninstance-name - String - 是否必填：否 -（过滤条件）按照名称过滤。\nsearch-by-name - String - 是否必填：否 -（过滤条件）按照名称检索，模糊匹配。"
      }
    ],
    "desc": "查询训练任务列表"
  },
  "DeleteNotebookLifecycleScript": {
    "params": [
      {
        "name": "NotebookLifecycleScriptsName",
        "desc": "生命周期脚本名称"
      },
      {
        "name": "Forcible",
        "desc": "是否忽略已关联的 notebook 实例强行删除生命周期脚本，默认 false"
      }
    ],
    "desc": "删除Notebook生命周期脚本"
  },
  "DescribeNotebookInstance": {
    "params": [
      {
        "name": "NotebookInstanceName",
        "desc": "Notebook实例名称\n规则：“^\\[a-zA-Z0-9\\](-\\*\\[a-zA-Z0-9\\])\\*$”"
      }
    ],
    "desc": "查询Notebook实例详情"
  },
  "UpdateCodeRepository": {
    "params": [
      {
        "name": "CodeRepositoryName",
        "desc": "查询存储库名称"
      },
      {
        "name": "GitSecret",
        "desc": "Git凭证"
      }
    ],
    "desc": "更新存储库"
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
        "name": "SortOrder",
        "desc": "排序规则。默认取Descending\nDescending 按更新时间降序\nAscending 按更新时间升序"
      },
      {
        "name": "Filters",
        "desc": "过滤条件。\ninstance-name - String - 是否必填：否 -（过滤条件）按照名称过滤。\nsearch-by-name - String - 是否必填：否 -（过滤条件）按照名称检索，模糊匹配。\nlifecycle-name - String - 是否必填：否 -（过滤条件）按照生命周期脚本名称过滤。\ndefault-code-repo-name - String - 是否必填：否 -（过滤条件）按照默认存储库名称过滤。\nadditional-code-repo-name - String - 是否必填：否 -（过滤条件）按照其他存储库名称过滤。\nbilling-status - String - 是否必填：否 - （过滤条件）按照计费状态过滤，可取以下值\n   StorageOnly：仅存储计费的实例\n   Computing：计算和存储都计费的实例"
      },
      {
        "name": "SortBy",
        "desc": "【废弃字段】排序字段"
      }
    ],
    "desc": "查询Notebook实例列表"
  },
  "CreateTrainingJob": {
    "params": [
      {
        "name": "AlgorithmSpecification",
        "desc": "算法镜像配置"
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
        "name": "TrainingJobName",
        "desc": "训练任务名称"
      },
      {
        "name": "InputDataConfig",
        "desc": "输入数据配置"
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
        "name": "EnvConfig",
        "desc": "环境变量配置"
      },
      {
        "name": "RoleName",
        "desc": "角色名称"
      },
      {
        "name": "RetryWhenResourceInsufficient",
        "desc": "在资源不足（ResourceInsufficient）时后台不定时尝试重新创建训练任务。可取值Enabled/Disabled\n默认值为Disabled即不重新尝试。设为Enabled时重新尝试有一定的时间期限，定义在 StoppingCondition 中 MaxWaitTimeInSecond中 ，默认值为1天，超过该期限创建失败。"
      }
    ],
    "desc": "创建训练任务"
  },
  "DescribeCodeRepositories": {
    "params": [
      {
        "name": "Offset",
        "desc": "偏移量，默认为0"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20"
      },
      {
        "name": "Filters",
        "desc": "过滤条件。\ninstance-name - String - 是否必填：否 -（过滤条件）按照名称过滤。\nsearch-by-name - String - 是否必填：否 -（过滤条件）按照名称检索，模糊匹配。"
      },
      {
        "name": "SortOrder",
        "desc": "排序规则。默认取Descending\nDescending 按更新时间降序\nAscending 按更新时间升序"
      }
    ],
    "desc": "查询存储库列表"
  },
  "StopTrainingJob": {
    "params": [
      {
        "name": "TrainingJobName",
        "desc": "训练任务名称"
      }
    ],
    "desc": "停止训练任务"
  }
}