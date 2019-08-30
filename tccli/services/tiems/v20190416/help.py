# -*- coding: utf-8 -*-
DESC = "tiems-2019-04-16"
INFO = {
  "CreateService": {
    "params": [
      {
        "name": "Scaler",
        "desc": "扩缩容配置"
      },
      {
        "name": "ServiceConfigId",
        "desc": "服务配置Id"
      },
      {
        "name": "Name",
        "desc": "服务名称"
      },
      {
        "name": "ScaleMode",
        "desc": "扩缩容方式，支持AUTO, MANUAL，分别表示自动扩缩容和手动扩缩容"
      },
      {
        "name": "Cluster",
        "desc": "集群，不填则使用默认集群。"
      }
    ],
    "desc": "创建服务"
  },
  "DeleteServiceConfig": {
    "params": [
      {
        "name": "ServiceConfigId",
        "desc": "服务配置Id (deprecated)"
      },
      {
        "name": "ServiceConfigName",
        "desc": "服务配置名称"
      }
    ],
    "desc": "删除服务配置"
  },
  "CreateServiceConfig": {
    "params": [
      {
        "name": "Name",
        "desc": "配置名称"
      },
      {
        "name": "Runtime",
        "desc": "运行环境"
      },
      {
        "name": "ModelUri",
        "desc": "模型地址，支持cos路径，格式为 cos://bucket名-appid.cos.region名.myqcloud.com/模型文件夹路径。为模型文件的上一层文件夹地址。"
      },
      {
        "name": "Cpu",
        "desc": "处理器配置, 单位为1/1000核；范围[100, 256000]"
      },
      {
        "name": "Memory",
        "desc": "内存配置, 单位为1M；范围[100, 256000]"
      },
      {
        "name": "TflopUnits",
        "desc": "GPU算力配置，单位为1/100 tflops，范围 [0, 256000]"
      },
      {
        "name": "GpuMemory",
        "desc": "显存配置, 单位为1M，范围 [0, 256000]"
      }
    ],
    "desc": "创建服务配置"
  },
  "DescribeServiceConfigs": {
    "params": [
      {
        "name": "Filters",
        "desc": "筛选选项，支持按照name等进行筛选"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为1000"
      },
      {
        "name": "Order",
        "desc": "输出列表的排列顺序。取值范围：ASC：升序排列 DESC：降序排列"
      },
      {
        "name": "OrderField",
        "desc": "排序的依据字段， 取值范围 \"CREATE_TIME\", \"UPDATE_TIME\", \"NAME\""
      }
    ],
    "desc": "描述服务配置"
  },
  "DeleteService": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "服务Id"
      }
    ],
    "desc": "删除服务"
  },
  "DescribeServices": {
    "params": [
      {
        "name": "Filters",
        "desc": "筛选选项，支持按照name等字段进行筛选"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100"
      },
      {
        "name": "Order",
        "desc": "输出列表的排列顺序。取值范围：ASC：升序排列 DESC：降序排列"
      },
      {
        "name": "OrderField",
        "desc": "排序的依据字段， 取值范围 \"CREATE_TIME\" \"UPDATE_TIME\""
      }
    ],
    "desc": "描述服务"
  },
  "DescribeRuntimes": {
    "params": [],
    "desc": "描述服务运行环境"
  },
  "UpdateService": {
    "params": [
      {
        "name": "ServiceId",
        "desc": "服务Id"
      },
      {
        "name": "Scaler",
        "desc": "扩缩容配置"
      },
      {
        "name": "ServiceConfigId",
        "desc": "服务配置Id"
      },
      {
        "name": "ScaleMode",
        "desc": "支持AUTO, MANUAL，分别表示自动扩缩容，手动扩缩容"
      },
      {
        "name": "ServiceAction",
        "desc": "支持STOP(停止) RESUME(重启)"
      }
    ],
    "desc": "更新服务"
  }
}