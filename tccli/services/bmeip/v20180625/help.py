# -*- coding: utf-8 -*-
DESC = "bmeip-2018-06-25"
INFO = {
  "UnbindRs": {
    "params": [
      {
        "name": "EipId",
        "desc": "Eip实例ID"
      },
      {
        "name": "InstanceId",
        "desc": "物理服务器实例ID"
      }
    ],
    "desc": "解绑黑石EIP"
  },
  "BindHosted": {
    "params": [
      {
        "name": "EipId",
        "desc": "Eip实例ID，可通过DescribeBmEip 接口返回字段中的 eipId获取。Eip和EipId参数必须要填写一个。"
      },
      {
        "name": "InstanceId",
        "desc": "托管机器实例ID"
      }
    ],
    "desc": "BindHosted接口用于绑定黑石弹性公网IP到黑石托管机器上"
  },
  "DeleteEipAcl": {
    "params": [
      {
        "name": "AclId",
        "desc": "待删除的 ACL 实例 ID"
      }
    ],
    "desc": "删除弹性公网IP ACL"
  },
  "CreateEipAcl": {
    "params": [
      {
        "name": "AclName",
        "desc": "ACL 名称"
      },
      {
        "name": "Status",
        "desc": "ACL 状态 0：无状态，1：有状态"
      }
    ],
    "desc": "创建黑石弹性公网 EIPACL"
  },
  "CreateEip": {
    "params": [
      {
        "name": "GoodsNum",
        "desc": "申请数量，默认为1, 最大 20"
      },
      {
        "name": "PayMode",
        "desc": "EIP计费方式，flow-流量计费；bandwidth-带宽计费"
      },
      {
        "name": "Bandwidth",
        "desc": "带宽设定值（只在带宽计费时生效）"
      },
      {
        "name": "SetType",
        "desc": "EIP模式，目前支持tunnel和fullnat"
      },
      {
        "name": "Exclusive",
        "desc": "是否使用独占集群，0：不使用，1：使用。默认为0"
      },
      {
        "name": "VpcId",
        "desc": "EIP归属私有网络ID，例如vpc-k7j1t2x1"
      },
      {
        "name": "IpList",
        "desc": "指定申请的IP列表"
      }
    ],
    "desc": "创建黑石弹性公网IP"
  },
  "ModifyEipAcl": {
    "params": [
      {
        "name": "AclId",
        "desc": "ACL 实例 ID"
      },
      {
        "name": "AclName",
        "desc": "ACL 名称"
      },
      {
        "name": "Status",
        "desc": "ACL 状态。0：无状态 1：有状态"
      },
      {
        "name": "Type",
        "desc": "规则类型（in/out）。in：入站规则 out：出站规则"
      },
      {
        "name": "Rules",
        "desc": "ACL规则列表"
      }
    ],
    "desc": "修改弹性公网IP ACL"
  },
  "DescribeEipQuota": {
    "params": [],
    "desc": "查询黑石EIP 限额"
  },
  "BindRs": {
    "params": [
      {
        "name": "EipId",
        "desc": "Eip实例ID"
      },
      {
        "name": "InstanceId",
        "desc": "物理服务器实例ID"
      }
    ],
    "desc": "绑定黑石EIP"
  },
  "DescribeEipTask": {
    "params": [
      {
        "name": "TaskId",
        "desc": "EIP查询任务ID"
      }
    ],
    "desc": "黑石EIP查询任务状态"
  },
  "UnbindRsList": {
    "params": [
      {
        "name": "EipRsList",
        "desc": "物理机绑定的EIP列表"
      }
    ],
    "desc": "批量解绑物理机弹性公网IP接口"
  },
  "DeleteEip": {
    "params": [
      {
        "name": "EipIds",
        "desc": "Eip实例ID列表"
      }
    ],
    "desc": "释放黑石弹性公网IP"
  },
  "ModifyEipCharge": {
    "params": [
      {
        "name": "PayMode",
        "desc": "EIP计费方式，flow-流量计费；bandwidth-带宽计费"
      },
      {
        "name": "EipIds",
        "desc": "Eip实例ID列表"
      },
      {
        "name": "Bandwidth",
        "desc": "带宽设定值（只在带宽计费时生效）"
      }
    ],
    "desc": "黑石EIP修改计费方式"
  },
  "ModifyEipName": {
    "params": [
      {
        "name": "EipId",
        "desc": "Eip实例ID，可通过/v2/DescribeEip 接口返回字段中的 eipId获取"
      },
      {
        "name": "EipName",
        "desc": "EIP 实例别名"
      }
    ],
    "desc": "更新黑石EIP名称"
  },
  "BindEipAcls": {
    "params": [
      {
        "name": "EipIdAclIdList",
        "desc": "待关联的 EIP 与 ACL关系列表"
      }
    ],
    "desc": "此接口用于为某个 EIP 关联 ACL。"
  },
  "UnbindHosted": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "托管机器实例ID"
      },
      {
        "name": "EipId",
        "desc": "Eip实例ID，可通过DescribeBmEip 接口返回字段中的 eipId获取。Eip和EipId参数必须要填写一个。"
      },
      {
        "name": "Eip",
        "desc": "弹性IP。Eip和EipId参数必须要填写一个。"
      }
    ],
    "desc": "UnbindHosted接口用于解绑托管机器上的EIP"
  },
  "UnbindEipAcls": {
    "params": [
      {
        "name": "EipIdAclIdList",
        "desc": "待解关联的 EIP 与 ACL列表"
      }
    ],
    "desc": "解绑弹性公网IP ACL"
  },
  "DescribeEips": {
    "params": [
      {
        "name": "EipIds",
        "desc": "EIP实例ID列表"
      },
      {
        "name": "Eips",
        "desc": "EIP IP 列表"
      },
      {
        "name": "InstanceIds",
        "desc": "主机实例ID 列表"
      },
      {
        "name": "SearchKey",
        "desc": "EIP名称,模糊匹配"
      },
      {
        "name": "Status",
        "desc": "状态列表, 默认所有"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0"
      },
      {
        "name": "Limit",
        "desc": "返回EIP数量，默认 20, 最大值 100"
      },
      {
        "name": "OrderField",
        "desc": "排序字段，支持： EipId,Eip,Status, InstanceId,CreatedAt"
      },
      {
        "name": "Order",
        "desc": "排序方式 0:递增 1:递减(默认)"
      },
      {
        "name": "PayMode",
        "desc": "计费模式,流量：flow，带宽：bandwidth"
      },
      {
        "name": "VpcId",
        "desc": "EIP归属VpcId，例如vpc-k7j1t2x1"
      },
      {
        "name": "BindTypes",
        "desc": "绑定类型，-1：未绑定，0：物理机，1：nat网关，2：虚拟IP, 3:托管机器"
      },
      {
        "name": "ExclusiveTag",
        "desc": "独占标志，0：共享，1：独占"
      },
      {
        "name": "AclId",
        "desc": "EIP ACL实例ID"
      },
      {
        "name": "BindAcl",
        "desc": "搜索条件，是否绑定了EIP ACL， 0：未绑定，1：绑定"
      }
    ],
    "desc": "黑石EIP查询接口"
  },
  "BindVpcIp": {
    "params": [
      {
        "name": "EipId",
        "desc": "Eip实例ID"
      },
      {
        "name": "VpcId",
        "desc": "EIP归属VpcId，例如vpc-k7j1t2x1"
      },
      {
        "name": "VpcIp",
        "desc": "绑定的VPC内IP地址"
      }
    ],
    "desc": "黑石EIP绑定VPCIP"
  },
  "UnbindVpcIp": {
    "params": [
      {
        "name": "EipId",
        "desc": "Eip实例ID"
      },
      {
        "name": "VpcId",
        "desc": "EIP归属VpcId，例如vpc-k7j1t2x1"
      },
      {
        "name": "VpcIp",
        "desc": "绑定的VPC内IP地址"
      }
    ],
    "desc": "黑石EIP解绑VPCIP"
  },
  "DescribeEipAcls": {
    "params": [
      {
        "name": "AclName",
        "desc": "ACL 名称，支持模糊查找"
      },
      {
        "name": "AclIds",
        "desc": "ACL 实例 ID 列表，数组下标从 0 开始"
      },
      {
        "name": "Offset",
        "desc": "分页参数。偏移量，默认为 0"
      },
      {
        "name": "Limit",
        "desc": "分页参数。每一页的 EIPACL 列表数目"
      },
      {
        "name": "EipIds",
        "desc": "EIP实例ID列表"
      },
      {
        "name": "EipIps",
        "desc": "EIP IP地址列表"
      },
      {
        "name": "EipNames",
        "desc": "EIP名称列表"
      },
      {
        "name": "OrderField",
        "desc": "排序字段"
      },
      {
        "name": "Order",
        "desc": "排序方式，取值：0:增序(默认)，1:降序"
      },
      {
        "name": "AclNames",
        "desc": "ACL名称列表，支持模糊查找"
      }
    ],
    "desc": "查询弹性公网IP ACL"
  }
}