# -*- coding: utf-8 -*-
DESC = "tia-2018-02-26"
INFO = {
  "CreateModel": {
    "params": [
      {
        "name": "Name",
        "desc": "模型名称"
      },
      {
        "name": "Model",
        "desc": "要部署的模型文件路径名"
      },
      {
        "name": "Description",
        "desc": "关于模型的描述"
      },
      {
        "name": "Cluster",
        "desc": "部署目标集群的名称，`集群模式` 必填"
      },
      {
        "name": "RuntimeVersion",
        "desc": "运行环境镜像的标签，详见 [Serving 环境](https://cloud.tencent.com/document/product/851/17320#serving-.E7.8E.AF.E5.A2.83)"
      },
      {
        "name": "Replicas",
        "desc": "要部署的模型副本数目，`集群模式` 选填"
      },
      {
        "name": "Expose",
        "desc": "暴露外网或内网，默认暴露外网，`集群模式` 选填"
      },
      {
        "name": "ServType",
        "desc": "部署模式，取值 `serverless` 即为 `无服务器模式`，否则为 `集群模式` 下服务的运行规模，形如 `2U4G1P`，详见 [自定义的训练规模](https://cloud.tencent.com/document/product/851/17319#.E8.87.AA.E5.AE.9A.E4.B9.89.E7.9A.84.E8.AE.AD.E7.BB.83.E8.A7.84.E6.A8.A1)"
      },
      {
        "name": "RuntimeConf",
        "desc": "`无服务器模式` 可选的其他配置信息，详见 [利用无服务器函数部署](https://cloud.tencent.com/document/product/851/17049#.E5.88.A9.E7.94.A8.E6.97.A0.E6.9C.8D.E5.8A.A1.E5.99.A8.E5.87.BD.E6.95.B0.E9.83.A8.E7.BD.B2)"
      }
    ],
    "desc": "部署模型，用以对外提供服务。有两种部署模式：`无服务器模式` 和 `集群模式`。`无服务器模式` 下，模型文件被部署到无服务器云函数，即 [SCF](https://cloud.tencent.com/product/scf)，用户可以在其控制台上进一步操作。`集群模式` 下，模型文件被部署到 TI-A 的计算集群中。"
  },
  "ListJobs": {
    "params": [
      {
        "name": "Cluster",
        "desc": "运行任务的集群"
      },
      {
        "name": "Limit",
        "desc": "分页参数，返回数量"
      },
      {
        "name": "Offset",
        "desc": "分页参数，起始位置"
      }
    ],
    "desc": "列举训练任务"
  },
  "CreateJob": {
    "params": [
      {
        "name": "Name",
        "desc": "任务名称"
      },
      {
        "name": "Cluster",
        "desc": "运行任务的集群，详见 [使用集群](https://cloud.tencent.com/document/product/851/17317)"
      },
      {
        "name": "RuntimeVersion",
        "desc": "运行任务的环境，详见 [运行环境](https://cloud.tencent.com/document/product/851/17320)"
      },
      {
        "name": "PackageDir",
        "desc": "挂载的路径，支持 NFS，[CFS](https://cloud.tencent.com/product/cfs) 和 [COS](https://cloud.tencent.com/product/cos)，其中 COS 只在 [TI-A 定制环境](https://cloud.tencent.com/document/product/851/17320#ti-a-.E5.AE.9A.E5.88.B6.E7.8E.AF.E5.A2.83) 中支持"
      },
      {
        "name": "Command",
        "desc": "任务启动命令"
      },
      {
        "name": "Args",
        "desc": "任务启动参数"
      },
      {
        "name": "ScaleTier",
        "desc": "运行任务的配置信息，详见 [训练规模](https://cloud.tencent.com/document/product/851/17319)"
      },
      {
        "name": "MasterType",
        "desc": "Master 机器类型，ScaleTier 取值为 `CUSTOM` 时必填，详见 [训练规模](https://cloud.tencent.com/document/product/851/17319)"
      },
      {
        "name": "WorkerType",
        "desc": "Worker 机器类型，ScaleTier 取值为 `CUSTOM` 时必填，详见 [训练规模](https://cloud.tencent.com/document/product/851/17319)"
      },
      {
        "name": "ParameterServerType",
        "desc": "Parameter server 机器类型，ScaleTier 取值为 `CUSTOM` 时必填,详见 [训练规模](https://cloud.tencent.com/document/product/851/17319)"
      },
      {
        "name": "WorkerCount",
        "desc": "Worker 机器数量，ScaleTier 取值为 `CUSTOM` 时必填,详见 [训练规模](https://cloud.tencent.com/document/product/851/17319)"
      },
      {
        "name": "ParameterServerCount",
        "desc": "Parameter server 机器数量，ScaleTier 取值为 `CUSTOM` 时必填,详见 [训练规模](https://cloud.tencent.com/document/product/851/17319)"
      },
      {
        "name": "Debug",
        "desc": "启动 debug 模式，默认为 false"
      },
      {
        "name": "RuntimeConf",
        "desc": "运行任务的其他配置信息"
      }
    ],
    "desc": "创建训练任务"
  },
  "DescribeModel": {
    "params": [
      {
        "name": "Name",
        "desc": "模型名称"
      },
      {
        "name": "Cluster",
        "desc": "模型所在集群名称，`集群模式` 必填"
      },
      {
        "name": "ServType",
        "desc": "模型类型，取值 `serverless` 即为 `无服务器模式`，否则为 `集群模式`"
      }
    ],
    "desc": "描述已经部署的某个模型。而模型部署有两种模式：`无服务器模式` 和 `集群模式`。`无服务器模式` 下，模型文件被部署到无服务器云函数，即 [SCF](https://cloud.tencent.com/product/scf)，用户可以在其控制台上进一步操作。`集群模式` 下，模型文件被部署到 TI-A 的计算集群中。"
  },
  "ListModels": {
    "params": [
      {
        "name": "Cluster",
        "desc": "部署模型的集群， `集群模式` 必填"
      },
      {
        "name": "Limit",
        "desc": "分页参数，返回数量上限"
      },
      {
        "name": "Offset",
        "desc": "分页参数，分页起始位置"
      },
      {
        "name": "ServType",
        "desc": "部署类型，取值 `serverless` 即为 `无服务器模式`，否则为 `集群模式`。"
      }
    ],
    "desc": "用以列举已经部署的模型。而部署有两种模式：`无服务器模式` 和 `集群模式`。`无服务器模式` 下，模型文件被部署到无服务器云函数，即 [SCF](https://cloud.tencent.com/product/scf)，用户可以在其控制台上进一步操作。`集群模式` 下，模型文件被部署到 TI-A 的计算集群中。不同部署模式下的模型分开列出。"
  },
  "QueryLogs": {
    "params": [
      {
        "name": "JobName",
        "desc": "任务的名称"
      },
      {
        "name": "Cluster",
        "desc": "任务所在集群的名称"
      },
      {
        "name": "StartTime",
        "desc": "查询日志的开始时间，格式：2019-01-01 00:00:00"
      },
      {
        "name": "EndTime",
        "desc": "查询日志的结束时间，格式：2019-01-01 00:00:00"
      },
      {
        "name": "Limit",
        "desc": "单次要返回的日志条数上限"
      },
      {
        "name": "Context",
        "desc": "加载更多日志时使用，透传上次返回的 Context 值，获取后续的日志内容；使用 Context 翻页最多能获取 10000 条日志"
      }
    ],
    "desc": "查询 TI-A 训练任务的日志"
  },
  "DeleteJob": {
    "params": [
      {
        "name": "Name",
        "desc": "任务名称"
      },
      {
        "name": "Cluster",
        "desc": "运行任务的集群"
      }
    ],
    "desc": "删除训练任务"
  },
  "DeleteModel": {
    "params": [
      {
        "name": "Name",
        "desc": "要删除的模型名称"
      },
      {
        "name": "Cluster",
        "desc": "要删除的模型所在的集群名称，`集群模式` 必填"
      },
      {
        "name": "ServType",
        "desc": "模型类型，取值 `serverless` 即为 `无服务器模式`，否则为 `集群模式`"
      }
    ],
    "desc": "删除指定的部署模型。模型有两种部署模式：`无服务器模式` 和 `集群模式`。`无服务器模式` 下，模型文件被部署到无服务器云函数，即 [SCF](https://cloud.tencent.com/product/scf)，用户可以在其控制台上进一步操作。`集群模式` 下，模型文件被部署到 TI-A 的计算集群中。"
  },
  "DescribeJob": {
    "params": [
      {
        "name": "Name",
        "desc": "任务名称"
      },
      {
        "name": "Cluster",
        "desc": "运行任务的集群"
      }
    ],
    "desc": "获取训练任务详情"
  },
  "InstallAgent": {
    "params": [
      {
        "name": "Cluster",
        "desc": "集群名称"
      },
      {
        "name": "TiaVersion",
        "desc": "Agent版本, 用于私有集群的agent安装，默认为“private-training”"
      },
      {
        "name": "Update",
        "desc": "是否允许更新Agent"
      }
    ],
    "desc": "安装agent"
  }
}