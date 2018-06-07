# -*- coding: utf-8 -*-
DESC = "cis-2018-04-08"
INFO = {
  "DescribeContainerInstances": {
    "params": [
      {
        "name": "Offset",
        "desc": "偏移量，默认为0"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为10"
      },
      {
        "name": "Filters",
        "desc": "过滤条件。\n- Zone - String - 是否必填：否 -（过滤条件）按照可用区过滤。\n- VpcId - String - 是否必填：否 -（过滤条件）按照VpcId过滤。\n- InstanceName - String - 是否必填：否 -（过滤条件）按照容器实例名称做模糊查询。"
      }
    ],
    "desc": "此接口（DescribeContainerInstances）查询容器实例列表"
  },
  "CreateContainerInstance": {
    "params": [
      {
        "name": "Zone",
        "desc": "可用区"
      },
      {
        "name": "VpcId",
        "desc": "vpcId"
      },
      {
        "name": "SubnetId",
        "desc": "subnetId"
      },
      {
        "name": "InstanceName",
        "desc": "容器实例名称，由小写字母、数字和 - 组成，由小写字母开头，小写字母或数字结尾，且长度不超过 40个字符"
      },
      {
        "name": "RestartPolicy",
        "desc": "重启策略（Always,OnFailure,Never）"
      },
      {
        "name": "Containers",
        "desc": "容器列表"
      }
    ],
    "desc": "此接口（CreateContainerInstance）用于创建容器实例"
  },
  "InquiryPriceCreateCis": {
    "params": [
      {
        "name": "Zone",
        "desc": "可用区"
      },
      {
        "name": "Cpu",
        "desc": "CPU，单位：核"
      },
      {
        "name": "Memory",
        "desc": "内存，单位：Gi"
      }
    ],
    "desc": "此接口（InquiryPriceCreateCis）用于查询容器实例价格"
  },
  "DescribeContainerInstance": {
    "params": [
      {
        "name": "InstanceName",
        "desc": "容器实例名称"
      }
    ],
    "desc": "此接口（DescribeContainerInstance）用于获取容器实例详情"
  },
  "DescribeContainerInstanceEvents": {
    "params": [
      {
        "name": "InstanceName",
        "desc": "容器实例名称"
      }
    ],
    "desc": "此接口（DescribeContainerInstanceEvents）用于查询容器实例事件列表"
  },
  "DeleteContainerInstance": {
    "params": [
      {
        "name": "InstanceName",
        "desc": "容器实例名称"
      }
    ],
    "desc": "此接口（DeleteContainerInstance）用于删除容器实例"
  },
  "DescribeContainerLog": {
    "params": [
      {
        "name": "InstanceName",
        "desc": "容器实例名称"
      },
      {
        "name": "ContainerName",
        "desc": "容器名称"
      },
      {
        "name": "Tail",
        "desc": "日志显示尾部行数"
      },
      {
        "name": "SinceTime",
        "desc": "日志起始时间"
      }
    ],
    "desc": "此接口（DescribeContainerLog）用于获取容器日志信息"
  }
}