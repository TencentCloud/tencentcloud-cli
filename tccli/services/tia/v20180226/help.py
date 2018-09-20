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
        "desc": "要部署模型的路径名"
      },
      {
        "name": "Description",
        "desc": "关于模型的描述"
      },
      {
        "name": "Cluster",
        "desc": "指定集群的名称（集群模式下必填）"
      },
      {
        "name": "RuntimeVersion",
        "desc": "运行环境镜像的标签"
      },
      {
        "name": "Replicas",
        "desc": "要部署的模型副本数目（集群模式下选填）"
      },
      {
        "name": "Expose",
        "desc": "暴露外网或内网，默认暴露外网（集群模式下选填）"
      },
      {
        "name": "ServType",
        "desc": "部署模式（无服务器函数模式/集群模式）"
      },
      {
        "name": "RuntimeConf",
        "desc": "部署模型的其他配置信息"
      }
    ],
    "desc": "在指定的集群上部署一个模型，用以提供服务。"
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
        "desc": "运行任务的集群"
      },
      {
        "name": "RuntimeVersion",
        "desc": "运行任务的环境"
      },
      {
        "name": "PackageDir",
        "desc": "挂载的路径，支持nfs,cos(cos只在tia运行环境中支持)"
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
        "desc": "运行任务的配置信息"
      },
      {
        "name": "MasterType",
        "desc": "（ScaleTier为Custom时）master机器类型"
      },
      {
        "name": "WorkerType",
        "desc": "（ScaleTier为Custom时）worker机器类型"
      },
      {
        "name": "ParameterServerType",
        "desc": "（ScaleTier为Custom时）parameter server机器类型"
      },
      {
        "name": "WorkerCount",
        "desc": "（ScaleTier为Custom时）worker机器数量"
      },
      {
        "name": "ParameterServerCount",
        "desc": "（ScaleTier为Custom时）parameter server机器数量"
      },
      {
        "name": "Debug",
        "desc": "启动debug mode，默认为false"
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
        "desc": "模型所在集群名称"
      },
      {
        "name": "ServType",
        "desc": "模型类型"
      }
    ],
    "desc": "描述Model"
  },
  "ListModels": {
    "params": [
      {
        "name": "Cluster",
        "desc": "部署模型的集群"
      },
      {
        "name": "Limit",
        "desc": "分页参数，返回数量"
      },
      {
        "name": "Offset",
        "desc": "分页参数，起始位置"
      },
      {
        "name": "ServType",
        "desc": "模型类型"
      }
    ],
    "desc": "列举某个指定集群上运行的模型。"
  },
  "QueryLogs": {
    "params": [
      {
        "name": "JobName",
        "desc": "任务名称"
      },
      {
        "name": "Cluster",
        "desc": "集群名称"
      },
      {
        "name": "StartTime",
        "desc": "查询日志的开始时间"
      },
      {
        "name": "EndTime",
        "desc": "查询日志的结束时间"
      },
      {
        "name": "Limit",
        "desc": "单次要返回的日志条数"
      },
      {
        "name": "Context",
        "desc": "加载更多使用，透传上次返回的context值，获取后续的日志内容，使用context翻页最多能获取10000条日志"
      }
    ],
    "desc": "查询日志"
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
        "desc": "要删除的模型所在的集群名称"
      },
      {
        "name": "ServType",
        "desc": "模型类型"
      }
    ],
    "desc": "删除一个指定的Model"
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