# -*- coding: utf-8 -*-
DESC = "cloudhsm-2019-11-12"
INFO = {
  "ModifyVsmAttributes": {
    "params": [
      {
        "name": "ResourceId",
        "desc": "资源Id"
      },
      {
        "name": "Type",
        "desc": "UpdateResourceName-修改资源名称,\nUpdateSgIds-修改安全组名称,\nUpdateNetWork-修改网络,\nDefault-默认不修改"
      },
      {
        "name": "ResourceName",
        "desc": "资源名称"
      },
      {
        "name": "SgIds",
        "desc": "安全组Id"
      },
      {
        "name": "VpcId",
        "desc": "VpcId"
      },
      {
        "name": "SubnetId",
        "desc": "子网Id"
      }
    ],
    "desc": "修改VSM属性"
  },
  "DescribeVsmAttributes": {
    "params": [
      {
        "name": "ResourceId",
        "desc": "资源Id"
      }
    ],
    "desc": "获取VSM属性"
  },
  "DescribeVsms": {
    "params": [
      {
        "name": "Offset",
        "desc": "偏移"
      },
      {
        "name": "Limit",
        "desc": "最大数量"
      },
      {
        "name": "SearchWord",
        "desc": "查询关键字"
      }
    ],
    "desc": "获取用户VSM列表"
  },
  "DescribeVpc": {
    "params": [
      {
        "name": "Offset",
        "desc": "返回偏移量。"
      },
      {
        "name": "Limit",
        "desc": "返回数量。"
      },
      {
        "name": "SearchWord",
        "desc": "搜索关键字"
      }
    ],
    "desc": "查询用户的私有网络列表"
  },
  "DescribeHSMByVpcId": {
    "params": [
      {
        "name": "VpcId",
        "desc": "VPC标识符"
      }
    ],
    "desc": "通过VpcId获取Hsm资源数"
  },
  "DescribeHSMBySubnetId": {
    "params": [
      {
        "name": "SubnetId",
        "desc": "Subnet标识符"
      }
    ],
    "desc": "通过SubnetId获取Hsm资源数"
  },
  "DescribeUsg": {
    "params": [
      {
        "name": "Offset",
        "desc": "偏移量，当Offset和Limit均为0时将一次性返回用户所有的安全组列表。"
      },
      {
        "name": "Limit",
        "desc": "返回量，当Offset和Limit均为0时将一次性返回用户所有的安全组列表。"
      },
      {
        "name": "SearchWord",
        "desc": "搜索关键字"
      }
    ],
    "desc": "根据用户的AppId获取用户安全组列表"
  },
  "DescribeSubnet": {
    "params": [
      {
        "name": "Limit",
        "desc": "返回数量。"
      },
      {
        "name": "Offset",
        "desc": "偏移量。"
      },
      {
        "name": "VpcId",
        "desc": "查询指定VpcId下的子网信息。"
      },
      {
        "name": "SearchWord",
        "desc": "查找关键字"
      }
    ],
    "desc": "查询子网列表"
  },
  "InquiryPriceBuyVsm": {
    "params": [
      {
        "name": "GoodsNum",
        "desc": "需购买实例的数量"
      },
      {
        "name": "PayMode",
        "desc": "付费模式：0表示按需计费/后付费，1表示预付费"
      },
      {
        "name": "TimeSpan",
        "desc": "商品的时间大小"
      },
      {
        "name": "TimeUnit",
        "desc": "商品的时间单位"
      },
      {
        "name": "Currency",
        "desc": "货币类型，默认为CNY"
      },
      {
        "name": "Type",
        "desc": "默认为CREATE，可选RENEW"
      }
    ],
    "desc": "购买询价接口"
  },
  "DescribeUsgRule": {
    "params": [
      {
        "name": "SgIds",
        "desc": "根据安全组Id获取安全组详情"
      }
    ],
    "desc": "获取安全组详情"
  }
}