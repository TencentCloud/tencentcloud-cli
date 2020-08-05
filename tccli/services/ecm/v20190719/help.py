# -*- coding: utf-8 -*-
DESC = "ecm-2019-07-19"
INFO = {
  "ResetInstancesMaxBandwidth": {
    "params": [
      {
        "name": "InstanceIdSet",
        "desc": "待重置带宽上限的实例ID列表。在单次请求的过程中，单个region下的请求实例数上限为100。"
      },
      {
        "name": "MaxBandwidthOut",
        "desc": "修改后的最大带宽上限。"
      }
    ],
    "desc": "重置实例的最大带宽上限。"
  },
  "TerminateInstances": {
    "params": [
      {
        "name": "InstanceIdSet",
        "desc": "待销毁的实例ID列表。"
      },
      {
        "name": "TerminateDelay",
        "desc": "是否定时销毁，默认为否。"
      },
      {
        "name": "TerminateTime",
        "desc": "定时销毁的时间，格式形如：\"2019-08-05 12:01:30\"，若非定时销毁，则此参数被忽略。"
      }
    ],
    "desc": "销毁实例"
  },
  "DescribeModule": {
    "params": [
      {
        "name": "Filters",
        "desc": "过滤条件。\nmodule-name - string - 是否必填：否 - （过滤条件）按照模块名称过滤。\nmodule-id - string - 是否必填：否 - （过滤条件）按照模块ID过滤。\nimage-id      String      是否必填：否      （过滤条件）按照镜像ID过滤。\ninstance-family      String      是否必填：否      （过滤条件）按照机型family过滤。\n\n每次请求的Filters的上限为10，Filter.Values的上限为5。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。关于Offset的更进一步介绍请参考 API 简介中的相关小节。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API 简介中的相关小节。"
      },
      {
        "name": "OrderByField",
        "desc": "指定排序字段。目前支持的可选值如下\ninstance-num 按实例数量排序。\nnode-num 按节点数量排序。\ntimestamp 按实例创建时间排序。\n如果不传，默认按实例创建时间排序"
      },
      {
        "name": "OrderDirection",
        "desc": "指定排序是降序还是升序。0表示降序； 1表示升序。如果不传默认为降序"
      }
    ],
    "desc": "获取模块列表"
  },
  "DescribeModuleDetail": {
    "params": [
      {
        "name": "ModuleId",
        "desc": "模块ID，如em-qn46snq8。"
      }
    ],
    "desc": "展示模块详细信息"
  },
  "DescribeConfig": {
    "params": [],
    "desc": "获取带宽硬盘等数据的限制"
  },
  "DescribeBaseOverview": {
    "params": [],
    "desc": "获取概览页统计的基本数据"
  },
  "StartInstances": {
    "params": [
      {
        "name": "InstanceIdSet",
        "desc": "待开启的实例ID列表。在单次请求的过程中，单个region下的请求实例数上限为100。"
      }
    ],
    "desc": "只有状态为STOPPED的实例才可以进行此操作；接口调用成功时，实例会进入STARTING状态；启动实例成功时，实例会进入RUNNING状态。"
  },
  "ModifyModuleName": {
    "params": [
      {
        "name": "ModuleId",
        "desc": "模块ID。"
      },
      {
        "name": "ModuleName",
        "desc": "模块名称。"
      }
    ],
    "desc": "修改模块名称"
  },
  "DisassociateAddress": {
    "params": [
      {
        "name": "EcmRegion",
        "desc": "ECM 地域"
      },
      {
        "name": "AddressId",
        "desc": "标识 EIP 的唯一 ID。EIP 唯一 ID 形如：eip-11112222。"
      },
      {
        "name": "ReallocateNormalPublicIp",
        "desc": "表示解绑 EIP 之后是否分配普通公网 IP。取值范围：\nTRUE：表示解绑 EIP 之后分配普通公网 IP。\nFALSE：表示解绑 EIP 之后不分配普通公网 IP。\n默认取值：FALSE。\n\n只有满足以下条件时才能指定该参数：\n只有在解绑主网卡的主内网 IP 上的 EIP 时才能指定该参数。\n解绑 EIP 后重新分配普通公网 IP 操作一个账号每天最多操作 10 次；详情可通过 DescribeAddressQuota 接口获取。"
      }
    ],
    "desc": "解绑弹性公网IP（简称 EIP）\n只有状态为 BIND 和 BIND_ENI 的 EIP 才能进行解绑定操作。\nEIP 如果被封堵，则不能进行解绑定操作。"
  },
  "AttachNetworkInterface": {
    "params": [
      {
        "name": "NetworkInterfaceId",
        "desc": "弹性网卡实例ID，例如：eni-m6dyj72l。"
      },
      {
        "name": "InstanceId",
        "desc": "实例ID。形如：ein-r8hr2upy。"
      },
      {
        "name": "EcmRegion",
        "desc": "ECM 地域"
      }
    ],
    "desc": "弹性网卡绑定云主机"
  },
  "CreateVpc": {
    "params": [
      {
        "name": "VpcName",
        "desc": "vpc名称，最大长度不能超过60个字节。"
      },
      {
        "name": "CidrBlock",
        "desc": "vpc的cidr，只能为10.0.0.0/16，172.16.0.0/16，192.168.0.0/16这三个内网网段内。"
      },
      {
        "name": "EcmRegion",
        "desc": "ECM 地域"
      },
      {
        "name": "EnableMulticast",
        "desc": "是否开启组播。true: 开启, false: 不开启。"
      },
      {
        "name": "DnsServers",
        "desc": "DNS地址，最多支持4个"
      },
      {
        "name": "DomainName",
        "desc": "域名"
      },
      {
        "name": "Tags",
        "desc": "指定绑定的标签列表，例如：[{\"Key\": \"city\", \"Value\": \"shanghai\"}]"
      }
    ],
    "desc": "创建私有网络"
  },
  "DescribeAddressQuota": {
    "params": [
      {
        "name": "EcmRegion",
        "desc": "ECM 地域"
      }
    ],
    "desc": "查询您账户的弹性公网IP（简称 EIP）在当前地域的配额信息"
  },
  "ModifyModuleConfig": {
    "params": [
      {
        "name": "ModuleId",
        "desc": "模块ID。"
      },
      {
        "name": "InstanceType",
        "desc": "机型ID。"
      },
      {
        "name": "DefaultDataDiskSize",
        "desc": "默认数据盘大小，单位：G。范围不得超过数据盘范围大小，详看DescribeConfig。"
      }
    ],
    "desc": "修改模块配置，已关联实例的模块不支持调整配置。"
  },
  "DeleteVpc": {
    "params": [
      {
        "name": "VpcId",
        "desc": "VPC实例ID。可通过DescribeVpcs接口返回值中的VpcId获取。"
      },
      {
        "name": "EcmRegion",
        "desc": "ECM 地域"
      }
    ],
    "desc": "删除私有网络"
  },
  "DescribeSubnets": {
    "params": [
      {
        "name": "EcmRegion",
        "desc": "ECM 地域"
      },
      {
        "name": "SubnetIds",
        "desc": "子网实例ID查询。形如：subnet-pxir56ns。每次请求的实例的上限为100。参数不支持同时指定SubnetIds和Filters。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件，参数不支持同时指定SubnetIds和Filters。\nsubnet-id - String - （过滤条件）Subnet实例名称。\nvpc-id - String - （过滤条件）VPC实例ID，形如：vpc-f49l6u0z。\ncidr-block - String - （过滤条件）子网网段，形如: 192.168.1.0 。\nis-default - Boolean - （过滤条件）是否是默认子网。\nis-remote-vpc-snat - Boolean - （过滤条件）是否为VPC SNAT地址池子网。\nsubnet-name - String - （过滤条件）子网名称。\nzone - String - （过滤条件）可用区。\ntag-key - String -是否必填：否- （过滤条件）按照标签键进行过滤。\ntag:tag-key - String - 是否必填：否 - （过滤条件）按照标签键值对进行过滤。 tag-key使用具体的标签键进行替换。使用请参考示例"
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
    "desc": "查询子网列表"
  },
  "DeleteNetworkInterface": {
    "params": [
      {
        "name": "NetworkInterfaceId",
        "desc": "弹性网卡实例ID，例如：eni-m6dyj72l。"
      },
      {
        "name": "EcmRegion",
        "desc": "ECM 地域"
      }
    ],
    "desc": "删除弹性网卡"
  },
  "AllocateAddresses": {
    "params": [
      {
        "name": "EcmRegion",
        "desc": "ECM 地域"
      },
      {
        "name": "AddressCount",
        "desc": "EIP数量。默认值：1。"
      },
      {
        "name": "InternetServiceProvider",
        "desc": "CMCC：中国移动\nCTCC：中国电信\nCUCC：中国联通"
      },
      {
        "name": "InternetMaxBandwidthOut",
        "desc": "1 Mbps 至 5000 Mbps，默认值：1 Mbps。"
      },
      {
        "name": "Tags",
        "desc": "需要关联的标签列表。"
      }
    ],
    "desc": "申请一个或多个弹性公网IP（简称 EIP）"
  },
  "DescribeInstances": {
    "params": [
      {
        "name": "Filters",
        "desc": "过滤条件。\nzone      String      是否必填：否     （过滤条件）按照可用区英文标识符过滤。\nzone-name      String      是否必填：否     （过滤条件）按照可用区中文名过滤,支持模糊匹配。\nmodule-id      String      是否必填：否     （过滤条件）按照模块ID过滤。\ninstance-id      String      是否必填：否      （过滤条件）按照实例ID过滤。\ninstance-name      String      是否必填：否      （过滤条件）按照实例名称过滤,支持模糊匹配。\nip-address      String      是否必填：否      （过滤条件）按照实例的内网/公网IP过滤。\ninstance-uuid   string 是否必填：否 （过滤条件）按照uuid过滤实例列表。\ninstance-state  string  是否必填：否 （过滤条件）按照实例状态更新实例列表。\ninternet-service-provider      String      是否必填：否      （过滤条件）按照实例公网IP所属的运营商进行过滤。\ntag-key      String      是否必填：否      （过滤条件）按照标签键进行过滤。\ntag:tag-key      String      是否必填：否      （过滤条件）按照标签键值对进行过滤。 tag-key使用具体的标签键进行替换。\ninstance-family      String      是否必填：否      （过滤条件）按照机型family过滤。\nmodule-name      String      是否必填：否      （过滤条件）按照模块名称过滤,支持模糊匹配。\nimage-id      String      是否必填：否      （过滤条件）按照实例的镜像ID过滤。\n\n若不传Filters参数则表示查询所有相关的实例信息。\n单次请求的Filter.Values的上限为5。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20(如果查询结果数目大于等于20)，最大值为100。"
      },
      {
        "name": "OrderByField",
        "desc": "指定排序字段。目前支持的可选值如下\ntimestamp 按实例创建时间排序。\n注意：目前仅支持按创建时间排序，后续可能会有扩展。\n如果不传，默认按实例创建时间排序"
      },
      {
        "name": "OrderDirection",
        "desc": "指定排序是降序还是升序。0表示降序； 1表示升序。如果不传默认为降序"
      }
    ],
    "desc": "获取实例的相关信息。"
  },
  "DescribeInstanceTypeConfig": {
    "params": [],
    "desc": "获取机型配置列表"
  },
  "RunInstances": {
    "params": [
      {
        "name": "ZoneInstanceCountISPSet",
        "desc": "需要创建实例的可用区及创建数目及运营商的列表。在单次请求的过程中，单个region下的请求创建实例数上限为100"
      },
      {
        "name": "Password",
        "desc": "实例登录密码。不同操作系统类型密码复杂度限制不一样，具体如下：\nLinux实例密码必须8到30位，至少包括两项[a-z]，[A-Z]、[0-9] 和 [( ) ` ~ ! @ # $ % ^ & - + = | { } [ ] : ; ' , . ? / ]中的特殊符。Windows实例密码必须12到30位，至少包括三项[a-z]，[A-Z]，[0-9] 和 [( ) ` ~ ! @ # $ % ^ & - + = | { } [ ] : ; ' , . ? /]中的特殊符号。"
      },
      {
        "name": "InternetMaxBandwidthOut",
        "desc": "公网出带宽上限，单位：Mbps。如果未传该参数或者传的值为0，则使用模块下的默认值"
      },
      {
        "name": "ModuleId",
        "desc": "模块ID。如果未传该参数，则必须传ImageId，InstanceType，DataDiskSize，InternetMaxBandwidthOut参数"
      },
      {
        "name": "ImageId",
        "desc": "镜像ID。如果未传该参数或者传的值为空，则使用模块下的默认值"
      },
      {
        "name": "InstanceName",
        "desc": "实例显示名称。\n不指定实例显示名称则默认显示‘未命名’。\n购买多台实例，如果指定模式串{R:x}，表示生成数字[x, x+n-1]，其中n表示购买实例的数量，例如server\\_{R:3}，购买1台时，实例显示名称为server\\_3；购买2台时，实例显示名称分别为server\\_3，server\\_4。\n支持指定多个模式串{R:x}。\n购买多台实例，如果不指定模式串，则在实例显示名称添加后缀1、2...n，其中n表示购买实例的数量，例如server_，购买2台时，实例显示名称分别为server\\_1，server\\_2。\n如果购买的实例属于不同的地域或运营商，则上述规则在每个地域和运营商内独立计数。\n最多支持60个字符（包含模式串）。"
      },
      {
        "name": "HostName",
        "desc": "主机名称\n点号（.）和短横线（-）不能作为 HostName 的首尾字符，不能连续使用。\nWindows 实例：名字符长度为[2, 15]，允许字母（不限制大小写）、数字和短横线（-）组成，不支持点号（.），不能全是数字。\n其他类型（Linux 等）实例：字符长度为[2, 60]，允许支持多个点号，点之间为一段，每段允许字母（不限制大小写）、数字和短横线（-）组成。"
      },
      {
        "name": "ClientToken",
        "desc": "用于保证请求幂等性的字符串。目前为保留参数，请勿使用。"
      },
      {
        "name": "EnhancedService",
        "desc": "增强服务。通过该参数可以指定是否开启云安全、云监控等服务。若不指定该参数，则默认公共镜像开启云监控、云安全服务"
      },
      {
        "name": "TagSpecification",
        "desc": "标签列表"
      },
      {
        "name": "UserData",
        "desc": "提供给实例使用的用户数据，需要以 base64 方式编码，支持的最大数据大小为 16KB"
      },
      {
        "name": "InstanceType",
        "desc": "机型。如果未传该参数或者传的值为空，则使用模块下的默认值"
      },
      {
        "name": "DataDiskSize",
        "desc": "数据盘大小，单位是G。如果未传该参数或者传的值为0，则使用模块下的默认值"
      },
      {
        "name": "SecurityGroupIds",
        "desc": "实例所属安全组。该参数可以通过调用 DescribeSecurityGroups 的返回值中的sgId字段来获取。若不指定该参数，则绑定默认安全组。"
      },
      {
        "name": "SystemDiskSize",
        "desc": "系统盘大小，单位是G。如果未传该参数或者传的值为0，则使用模块下的默认值"
      }
    ],
    "desc": "创建ECM实例"
  },
  "DescribeCustomImageTask": {
    "params": [
      {
        "name": "Filters",
        "desc": "支持key,value查询\ntask-id: 异步任务ID\nimage-id: 镜像ID\nimage-name: 镜像名称"
      }
    ],
    "desc": "查询导入镜像任务"
  },
  "ImportImage": {
    "params": [
      {
        "name": "ImageId",
        "desc": "镜像的Id。"
      },
      {
        "name": "ImageDescription",
        "desc": "镜像的描述。"
      },
      {
        "name": "SourceRegion",
        "desc": "源地域"
      }
    ],
    "desc": "从CVM产品导入镜像到ECM"
  },
  "DescribeDefaultSubnet": {
    "params": [
      {
        "name": "EcmRegion",
        "desc": "ECM地域"
      },
      {
        "name": "Zone",
        "desc": "ECM可用区"
      }
    ],
    "desc": "查询可用区的默认子网"
  },
  "AssociateAddress": {
    "params": [
      {
        "name": "EcmRegion",
        "desc": "ECM 地域"
      },
      {
        "name": "AddressId",
        "desc": "标识 EIP 的唯一 ID。EIP 唯一 ID 形如：eip-11112222。"
      },
      {
        "name": "InstanceId",
        "desc": "要绑定的实例 ID。"
      },
      {
        "name": "NetworkInterfaceId",
        "desc": "要绑定的弹性网卡 ID。 弹性网卡 ID 形如：eni-11112222。NetworkInterfaceId 与 InstanceId 不可同时指定。弹性网卡 ID 可通过DescribeNetworkInterfaces接口返回值中的networkInterfaceId获取。"
      },
      {
        "name": "PrivateIpAddress",
        "desc": "要绑定的内网 IP。如果指定了 NetworkInterfaceId 则也必须指定 PrivateIpAddress ，表示将 EIP 绑定到指定弹性网卡的指定内网 IP 上。同时要确保指定的 PrivateIpAddress 是指定的 NetworkInterfaceId 上的一个内网 IP。指定弹性网卡的内网 IP 可通过DescribeNetworkInterfaces接口返回值中的privateIpAddress获取。"
      }
    ],
    "desc": "将弹性公网IP（简称 EIP）绑定到实例或弹性网卡的指定内网 IP 上。\n将 EIP 绑定到实例（CVM）上，其本质是将 EIP 绑定到实例上主网卡的主内网 IP 上。\n将 EIP 绑定到主网卡的主内网IP上，绑定过程会把其上绑定的普通公网 IP 自动解绑并释放。\n将 EIP 绑定到指定网卡的内网 IP上（非主网卡的主内网IP），则必须先解绑该 EIP，才能再绑定新的。\n将 EIP 绑定到NAT网关，请使用接口EipBindNatGateway\nEIP 如果欠费或被封堵，则不能被绑定。\n只有状态为 UNBIND 的 EIP 才能够被绑定。"
  },
  "DescribeTaskResult": {
    "params": [
      {
        "name": "EcmRegion",
        "desc": "ECM 地域"
      },
      {
        "name": "TaskId",
        "desc": "异步任务ID。"
      }
    ],
    "desc": "查询EIP异步任务执行结果"
  },
  "CreateModule": {
    "params": [
      {
        "name": "ModuleName",
        "desc": "模块名称，如视频直播模块。限制：模块名称不得以空格开头，长度不得超过60个字符。"
      },
      {
        "name": "DefaultBandWidth",
        "desc": "默认带宽，单位：M。范围不得超过带宽上下限，详看DescribeConfig。"
      },
      {
        "name": "DefaultImageId",
        "desc": "默认镜像，如img-qsdf3ff2。"
      },
      {
        "name": "InstanceType",
        "desc": "机型ID。"
      },
      {
        "name": "DefaultSystemDiskSize",
        "desc": "默认系统盘大小，单位：G，默认大小为50G。范围不得超过系统盘上下限制，详看DescribeConfig。"
      },
      {
        "name": "DefaultDataDiskSize",
        "desc": "默认数据盘大小，单位：G。范围不得超过数据盘范围大小，详看DescribeConfig。"
      }
    ],
    "desc": "创建模块"
  },
  "DescribeAddresses": {
    "params": [
      {
        "name": "EcmRegion",
        "desc": "ECM 地域"
      },
      {
        "name": "AddressIds",
        "desc": "标识 EIP 的唯一 ID 列表。EIP 唯一 ID 形如：eip-11112222。参数不支持同时指定AddressIds和Filters。"
      },
      {
        "name": "Filters",
        "desc": "每次请求的Filters的上限为10，Filter.Values的上限为5。参数不支持同时指定AddressIds和Filters。详细的过滤条件如下：\naddress-id - String - 是否必填：否 - （过滤条件）按照 EIP 的唯一 ID 过滤。EIP 唯一 ID 形如：eip-11112222。\naddress-name - String - 是否必填：否 - （过滤条件）按照 EIP 名称过滤。不支持模糊过滤。\naddress-ip - String - 是否必填：否 - （过滤条件）按照 EIP 的 IP 地址过滤。\naddress-status - String - 是否必填：否 - （过滤条件）按照 EIP 的状态过滤。取值范围：详见EIP状态列表。\ninstance-id - String - 是否必填：否 - （过滤条件）按照 EIP 绑定的实例 ID 过滤。实例 ID 形如：ins-11112222。\nprivate-ip-address - String - 是否必填：否 - （过滤条件）按照 EIP 绑定的内网 IP 过滤。\nnetwork-interface-id - String - 是否必填：否 - （过滤条件）按照 EIP 绑定的弹性网卡 ID 过滤。弹性网卡 ID 形如：eni-11112222。\nis-arrears - String - 是否必填：否 - （过滤条件）按照 EIP 是否欠费进行过滤。（TRUE：EIP 处于欠费状态|FALSE：EIP 费用状态正常）"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100。"
      }
    ],
    "desc": "查询弹性公网IP列表"
  },
  "DeleteSubnet": {
    "params": [
      {
        "name": "SubnetId",
        "desc": "子网实例ID。可通过DescribeSubnets接口返回值中的SubnetId获取。"
      },
      {
        "name": "EcmRegion",
        "desc": "ECM 地域"
      }
    ],
    "desc": "删除子网，若子网为可用区下的默认子网，则默认子网会回退到系统自动创建的默认子网，非用户最新创建的子网。若默认子网不满足需求，可调用设置默认子网接口设置。"
  },
  "ModifySubnetAttribute": {
    "params": [
      {
        "name": "SubnetId",
        "desc": "子网实例ID。形如：subnet-pxir56ns。"
      },
      {
        "name": "EcmRegion",
        "desc": "ECM 地域"
      },
      {
        "name": "SubnetName",
        "desc": "子网名称，最大长度不能超过60个字节。"
      },
      {
        "name": "EnableBroadcast",
        "desc": "子网是否开启广播。"
      }
    ],
    "desc": "修改子网属性"
  },
  "DescribeNetworkInterfaces": {
    "params": [
      {
        "name": "EcmRegion",
        "desc": "ECM 地域"
      },
      {
        "name": "NetworkInterfaceIds",
        "desc": "弹性网卡实例ID查询。形如：eni-pxir56ns。每次请求的实例的上限为100。参数不支持同时指定NetworkInterfaceIds和Filters。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件，参数不支持同时指定NetworkInterfaceIds和Filters。\nvpc-id - String - （过滤条件）VPC实例ID，形如：vpc-f49l6u0z。\nsubnet-id - String - （过滤条件）所属子网实例ID，形如：subnet-f49l6u0z。\nnetwork-interface-id - String - （过滤条件）弹性网卡实例ID，形如：eni-5k56k7k7。\nattachment.instance-id - String - （过滤条件）绑定的云服务器实例ID，形如：ins-3nqpdn3i。\ngroups.security-group-id - String - （过滤条件）绑定的安全组实例ID，例如：sg-f9ekbxeq。\nnetwork-interface-name - String - （过滤条件）网卡实例名称。\nnetwork-interface-description - String - （过滤条件）网卡实例描述。\naddress-ip - String - （过滤条件）内网IPv4地址。\ntag-key - String -是否必填：否- （过滤条件）按照标签键进行过滤。使用请参考示例2\ntag:tag-key - String - 是否必填：否 - （过滤条件）按照标签键值对进行过滤。 tag-key使用具体的标签键进行替换。使用请参考示例3。\nis-primary - Boolean - 是否必填：否 - （过滤条件）按照是否主网卡进行过滤。值为true时，仅过滤主网卡；值为false时，仅过滤辅助网卡；次过滤参数为提供时，同时过滤主网卡和辅助网卡。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100。"
      }
    ],
    "desc": "查询弹性网卡列表"
  },
  "MigrateNetworkInterface": {
    "params": [
      {
        "name": "EcmRegion",
        "desc": "ECM 地域"
      },
      {
        "name": "NetworkInterfaceId",
        "desc": "弹性网卡实例ID，例如：eni-m6dyj72l。"
      },
      {
        "name": "SourceInstanceId",
        "desc": "弹性网卡当前绑定的ECM实例ID。形如：ein-r8hr2upy。"
      },
      {
        "name": "DestinationInstanceId",
        "desc": "待迁移的目的ECM实例ID。"
      }
    ],
    "desc": "弹性网卡迁移"
  },
  "CreateImage": {
    "params": [
      {
        "name": "ImageName",
        "desc": "镜像名称。"
      },
      {
        "name": "InstanceId",
        "desc": "需要制作镜像的实例ID。"
      },
      {
        "name": "ImageDescription",
        "desc": "镜像描述。"
      },
      {
        "name": "ForcePoweroff",
        "desc": "是否执行强制关机以制作镜像。取值范围：\nTRUE：表示自动关机后制作镜像\nFALSE：表示开机状态制作，目前不支持，需要先手动关机\n默认取值：FALSE。"
      }
    ],
    "desc": "本接口(CreateImage)用于将实例的系统盘制作为新镜像，创建后的镜像可以用于创建实例。"
  },
  "ModifyModuleNetwork": {
    "params": [
      {
        "name": "ModuleId",
        "desc": "模块Id"
      },
      {
        "name": "DefaultBandwidth",
        "desc": "默认带宽上限"
      }
    ],
    "desc": "修改模块默认带宽上限"
  },
  "ResetInstancesPassword": {
    "params": [
      {
        "name": "InstanceIdSet",
        "desc": "待重置密码的实例ID列表。在单次请求的过程中，单个region下的请求实例数上限为100。"
      },
      {
        "name": "Password",
        "desc": "新密码，Linux实例密码必须8到16位，至少包括两项[a-z，A-Z]、[0-9]和[( ) ~ ~ ! @ # $ % ^ & * - + = _ | { } [ ] : ; ' < > , . ? /]中的符号。密码不允许以/符号开头。\nWindows实例密码必须12到16位，至少包括三项[a-z]，[A-Z]，[0-9]和[( ) ~ ~ ! @ # $ % ^ & * - + = _ | { } [ ] : ; ' < > , . ? /]中的符号。密码不允许以/符号开头。\n如果实例即包含Linux实例又包含Windows实例，则密码复杂度限制按照Windows实例的限制。"
      },
      {
        "name": "ForceStop",
        "desc": "是否强制关机，默认为false。"
      },
      {
        "name": "UserName",
        "desc": "待重置密码的实例的用户名，不得超过64个字符。若未指定用户名，则对于Linux而言，默认重置root用户的密码，对于Windows而言，默认重置administrator的密码。"
      }
    ],
    "desc": "重置处于运行中状态的实例的密码，需要显式指定强制关机参数ForceStop。如果没有显式指定强制关机参数，则只有处于关机状态的实例才允许执行重置密码操作。"
  },
  "ModifyImageAttribute": {
    "params": [
      {
        "name": "ImageId",
        "desc": "镜像ID，形如img-gvbnzy6f"
      },
      {
        "name": "ImageName",
        "desc": "设置新的镜像名称；必须满足下列限制：\n不得超过20个字符。\n- 镜像名称不能与已有镜像重复。"
      },
      {
        "name": "ImageDescription",
        "desc": "设置新的镜像描述；必须满足下列限制：\n- 不得超过60个字符。"
      }
    ],
    "desc": "本接口（ModifyImageAttribute）用于修改镜像属性。"
  },
  "DescribeInstancesDeniedActions": {
    "params": [
      {
        "name": "InstanceIdSet",
        "desc": "无"
      }
    ],
    "desc": "通过实例id获取当前禁止的操作"
  },
  "DescribeTaskStatus": {
    "params": [
      {
        "name": "TaskSet",
        "desc": "任务描述"
      }
    ],
    "desc": "本接口(DescribeTaskStatus)用于获取异步任务状态"
  },
  "CreateNetworkInterface": {
    "params": [
      {
        "name": "VpcId",
        "desc": "VPC实例ID。可通过DescribeVpcs接口返回值中的VpcId获取。"
      },
      {
        "name": "NetworkInterfaceName",
        "desc": "弹性网卡名称，最大长度不能超过60个字节。"
      },
      {
        "name": "SubnetId",
        "desc": "弹性网卡所在的子网实例ID，例如：subnet-0ap8nwca。"
      },
      {
        "name": "EcmRegion",
        "desc": "ECM 地域"
      },
      {
        "name": "NetworkInterfaceDescription",
        "desc": "弹性网卡描述，可任意命名，但不得超过60个字符。"
      },
      {
        "name": "SecondaryPrivateIpAddressCount",
        "desc": "新申请的内网IP地址个数，内网IP地址个数总和不能超过配数。"
      },
      {
        "name": "SecurityGroupIds",
        "desc": "指定绑定的安全组，例如：['sg-1dd51d']。"
      },
      {
        "name": "PrivateIpAddresses",
        "desc": "指定的内网IP信息，单次最多指定10个。"
      },
      {
        "name": "Tags",
        "desc": "指定绑定的标签列表，例如：[{\"Key\": \"city\", \"Value\": \"shanghai\"}]"
      }
    ],
    "desc": "创建弹性网卡"
  },
  "DescribePeakNetworkOverview": {
    "params": [
      {
        "name": "StartTime",
        "desc": "开始时间（xxxx-xx-xx）如2019-08-14，默认为一周之前的日期。"
      },
      {
        "name": "EndTime",
        "desc": "结束时间（xxxx-xx-xx）如2019-08-14，默认为昨天。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件。\nregion    String      是否必填：否     （过滤条件）按照region过滤,不支持模糊匹配。"
      }
    ],
    "desc": "获取网络峰值数据"
  },
  "StopInstances": {
    "params": [
      {
        "name": "InstanceIdSet",
        "desc": "需要关机的实例ID列表。在单次请求的过程中，单个region下的请求实例数上限为100。"
      },
      {
        "name": "ForceStop",
        "desc": "是否在正常关闭失败后选择强制关闭实例，默认为false，即否。"
      },
      {
        "name": "StopType",
        "desc": "实例的关闭模式。取值范围：\nSOFT_FIRST：表示在正常关闭失败后进行强制关闭;\nHARD：直接强制关闭;\nSOFT：仅软关机；\n默认为SOFT。"
      }
    ],
    "desc": "只有处于\"RUNNING\"状态的实例才能够进行关机操作；\n调用成功时，实例会进入STOPPING状态；关闭实例成功时，实例会进入STOPPED状态；\n支持强制关闭，强制关机的效果等同于关闭物理计算机的电源开关，强制关机可能会导致数据丢失或文件系统损坏，请仅在服务器不能正常关机时使用。"
  },
  "DescribeImportImageOs": {
    "params": [],
    "desc": "查询外部导入镜像支持的OS列表"
  },
  "CreateSecurityGroup": {
    "params": [
      {
        "name": "GroupName",
        "desc": "安全组名称，可任意命名，但不得超过60个字符。"
      },
      {
        "name": "GroupDescription",
        "desc": "安全组备注，最多100个字符。"
      },
      {
        "name": "Tags",
        "desc": "指定绑定的标签列表，例如：[{\"Key\": \"city\", \"Value\": \"shanghai\"}]"
      }
    ],
    "desc": "创建安全组"
  },
  "DescribeNode": {
    "params": [
      {
        "name": "Filters",
        "desc": "过滤条件，name取值为： InstanceFamily-实例系列"
      }
    ],
    "desc": "获取节点列表"
  },
  "ImportCustomImage": {
    "params": [
      {
        "name": "ImageName",
        "desc": "镜像名称"
      },
      {
        "name": "Architecture",
        "desc": "导入镜像的操作系统架构，x86_64 或 i386"
      },
      {
        "name": "OsType",
        "desc": "导入镜像的操作系统类型，通过DescribeImportImageOs获取"
      },
      {
        "name": "OsVersion",
        "desc": "导入镜像的操作系统版本，通过DescribeImportImageOs获取"
      },
      {
        "name": "ImageDescription",
        "desc": "镜像描述"
      },
      {
        "name": "InitFlag",
        "desc": "镜像启动方式，cloudinit或nbd， 默认cloudinit"
      },
      {
        "name": "ImageUrls",
        "desc": "镜像描述，多层镜像按顺序传入"
      }
    ],
    "desc": "导入自定义镜像，支持 RAW、VHD、QCOW2、VMDK 镜像格式"
  },
  "ReleaseAddresses": {
    "params": [
      {
        "name": "EcmRegion",
        "desc": "ECM 地域"
      },
      {
        "name": "AddressIds",
        "desc": "标识 EIP 的唯一 ID 列表。"
      }
    ],
    "desc": "释放一个或多个弹性公网IP（简称 EIP）。\n该操作不可逆，释放后 EIP 关联的 IP 地址将不再属于您的名下。\n只有状态为 UNBIND 的 EIP 才能进行释放操作。"
  },
  "DetachNetworkInterface": {
    "params": [
      {
        "name": "NetworkInterfaceId",
        "desc": "弹性网卡实例ID，例如：eni-m6dyj72l。"
      },
      {
        "name": "InstanceId",
        "desc": "实例ID。形如：ein-hcs7jkg4"
      },
      {
        "name": "EcmRegion",
        "desc": "ECM 地域"
      }
    ],
    "desc": "弹性网卡解绑云主机"
  },
  "AssignPrivateIpAddresses": {
    "params": [
      {
        "name": "NetworkInterfaceId",
        "desc": "弹性网卡实例ID，例如：eni-m6dyj72l。"
      },
      {
        "name": "EcmRegion",
        "desc": "ECM 地域"
      },
      {
        "name": "PrivateIpAddresses",
        "desc": "指定的内网IP信息，单次最多指定10个。与SecondaryPrivateIpAddressCount至少提供一个。"
      },
      {
        "name": "SecondaryPrivateIpAddressCount",
        "desc": "新申请的内网IP地址个数，与PrivateIpAddresses至少提供一个。内网IP地址个数总和不能超过配额数"
      }
    ],
    "desc": "弹性网卡申请内网 IP"
  },
  "ResetInstances": {
    "params": [
      {
        "name": "InstanceIdSet",
        "desc": "待重装的实例ID列表。"
      },
      {
        "name": "ImageId",
        "desc": "重装使用的镜像ID，若未指定，则使用各个实例当前的镜像进行重装。"
      },
      {
        "name": "Password",
        "desc": "密码设置，若未指定，则后续将以站内信的形式通知密码。"
      },
      {
        "name": "EnhancedService",
        "desc": "是否开启云监控和云镜服务，未指定时默认开启。"
      },
      {
        "name": "KeepData",
        "desc": "是否保留数据盘数据，取值\"true\"/\"false\"。默认为\"true\""
      }
    ],
    "desc": "重装实例，若指定了ImageId参数，则使用指定的镜像重装；否则按照当前实例使用的镜像进行重装；若未指定密码，则密码通过站内信形式随后发送。"
  },
  "DescribeInstanceVncUrl": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "一个操作的实例ID。可通过DescribeInstances API返回值中的InstanceId获取。"
      }
    ],
    "desc": "查询实例管理终端地址"
  },
  "DeleteImage": {
    "params": [
      {
        "name": "ImageIDSet",
        "desc": "镜像ID列表。"
      }
    ],
    "desc": "删除镜像"
  },
  "ModifyModuleImage": {
    "params": [
      {
        "name": "DefaultImageId",
        "desc": "默认镜像ID"
      },
      {
        "name": "ModuleId",
        "desc": "模块ID"
      }
    ],
    "desc": "ModifyModuleImage"
  },
  "ModifyInstancesAttribute": {
    "params": [
      {
        "name": "InstanceIdSet",
        "desc": "待修改的实例ID列表。在单次请求的过程中，请求实例数上限为100。"
      },
      {
        "name": "InstanceName",
        "desc": "修改成功后显示的实例名称，不得超过60个字符，不传则名称显示为空。"
      }
    ],
    "desc": "修改实例的属性。"
  },
  "DescribePeakBaseOverview": {
    "params": [
      {
        "name": "StartTime",
        "desc": "开始时间（xxxx-xx-xx）如2019-08-14，默认为一周之前的日期。"
      },
      {
        "name": "EndTime",
        "desc": "结束时间（xxxx-xx-xx）如2019-08-14，默认为昨天。"
      }
    ],
    "desc": "CPU 内存 硬盘等基础信息峰值数据"
  },
  "ModifyDefaultSubnet": {
    "params": [
      {
        "name": "EcmRegion",
        "desc": "ECM地域"
      },
      {
        "name": "Zone",
        "desc": "ECM可用区"
      },
      {
        "name": "VpcId",
        "desc": "私有网络ID"
      },
      {
        "name": "SubnetId",
        "desc": "子网ID"
      }
    ],
    "desc": "修改在一个可用区下创建实例时使用的默认子网（创建实例时，未填写VPC参数时使用的sunbetId）"
  },
  "ModifyAddressAttribute": {
    "params": [
      {
        "name": "EcmRegion",
        "desc": "ECM 地域"
      },
      {
        "name": "AddressId",
        "desc": "标识 EIP 的唯一 ID。EIP 唯一 ID 形如：eip-11112222。"
      },
      {
        "name": "AddressName",
        "desc": "修改后的 EIP 名称。长度上限为20个字符。"
      },
      {
        "name": "EipDirectConnection",
        "desc": "设定EIP是否直通，\"TRUE\"表示直通，\"FALSE\"表示非直通。注意该参数仅对EIP直通功能可见的用户可以设定。"
      }
    ],
    "desc": "修改弹性公网IP属性"
  },
  "DeleteModule": {
    "params": [
      {
        "name": "ModuleId",
        "desc": "模块ID。如：em-qn46snq8"
      }
    ],
    "desc": "删除业务模块"
  },
  "RebootInstances": {
    "params": [
      {
        "name": "InstanceIdSet",
        "desc": "待重启的实例ID列表。在单次请求的过程中，单个region下的请求实例数上限为100。"
      },
      {
        "name": "ForceReboot",
        "desc": "是否在正常重启失败后选择强制重启实例。取值范围：\nTRUE：表示在正常重启失败后进行强制重启；\nFALSE：表示在正常重启失败后不进行强制重启；\n默认取值：FALSE。"
      },
      {
        "name": "StopType",
        "desc": "关机类型。取值范围：\nSOFT：表示软关机\nHARD：表示硬关机\nSOFT_FIRST：表示优先软关机，失败再执行硬关机\n\n默认取值：SOFT。"
      }
    ],
    "desc": "只有状态为RUNNING的实例才可以进行此操作；接口调用成功时，实例会进入REBOOTING状态；重启实例成功时，实例会进入RUNNING状态；支持强制重启，强制重启的效果等同于关闭物理计算机的电源开关再重新启动。强制重启可能会导致数据丢失或文件系统损坏，请仅在服务器不能正常重启时使用。"
  },
  "DescribeVpcs": {
    "params": [
      {
        "name": "EcmRegion",
        "desc": "地域"
      },
      {
        "name": "VpcIds",
        "desc": "VPC实例ID。形如：vpc-f49l6u0z。每次请求的实例的上限为100。参数不支持同时指定VpcIds和Filters。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件，参数不支持同时指定VpcIds和Filters。\nvpc-name - String - （过滤条件）VPC实例名称。\nis-default - String - （过滤条件）是否默认VPC。\nvpc-id - String - （过滤条件）VPC实例ID形如：vpc-f49l6u0z。\ncidr-block - String - （过滤条件）vpc的cidr。\ntag-key - String -是否必填：否- （过滤条件）按照标签键进行过滤。\ntag:tag-key - String - 是否必填：否 - （过滤条件）按照标签键值对进行过滤。 tag-key使用具体的标签键进行替换。使用请参考示例"
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
    "desc": "查询私有网络列表"
  },
  "MigratePrivateIpAddress": {
    "params": [
      {
        "name": "EcmRegion",
        "desc": "ECM 地域"
      },
      {
        "name": "SourceNetworkInterfaceId",
        "desc": "当内网IP绑定的弹性网卡实例ID，例如：eni-11112222。"
      },
      {
        "name": "DestinationNetworkInterfaceId",
        "desc": "待迁移的目的弹性网卡实例ID。"
      },
      {
        "name": "PrivateIpAddress",
        "desc": "迁移的内网IP地址，例如：10.0.0.6。"
      }
    ],
    "desc": "弹性网卡内网IP迁移。\n该接口用于将一个内网IP从一个弹性网卡上迁移到另外一个弹性网卡，主IP地址不支持迁移。\n迁移前后的弹性网卡必须在同一个子网内。"
  },
  "DescribeImage": {
    "params": [
      {
        "name": "Filters",
        "desc": "过滤条件，每次请求的Filters的上限为10，详细的过滤条件如下：\nimage-id - String - 是否必填： 否 - （过滤条件）按照镜像ID进行过滤\nimage-type - String - 是否必填： 否 - （过滤条件）按照镜像类型进行过滤。取值范围：\nPRIVATE_IMAGE: 私有镜像 (本帐户创建的镜像) \nPUBLIC_IMAGE: 公共镜像 (腾讯云官方镜像)"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。关于Offset的更进一步介绍请参考 API 简介中的相关小节。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API 简介中的相关小节。"
      }
    ],
    "desc": "展示镜像列表"
  },
  "ModifyVpcAttribute": {
    "params": [
      {
        "name": "VpcId",
        "desc": "VPC实例ID。形如：vpc-f49l6u0z。"
      },
      {
        "name": "EcmRegion",
        "desc": "ECM 地域"
      },
      {
        "name": "VpcName",
        "desc": "私有网络名称，可任意命名，但不得超过60个字符。"
      }
    ],
    "desc": "修改私有网络（VPC）的相关属性"
  },
  "ModifyAddressesBandwidth": {
    "params": [
      {
        "name": "EcmRegion",
        "desc": "ECM 地域"
      },
      {
        "name": "AddressIds",
        "desc": "EIP唯一标识ID，形如'eip-xxxxxxx'"
      },
      {
        "name": "InternetMaxBandwidthOut",
        "desc": "调整带宽目标值"
      }
    ],
    "desc": "调整弹性公网IP带宽\n"
  },
  "RemovePrivateIpAddresses": {
    "params": [
      {
        "name": "EcmRegion",
        "desc": "ECM 地域。"
      },
      {
        "name": "NetworkInterfaceId",
        "desc": "弹性网卡实例ID，例如：eni-11112222。"
      },
      {
        "name": "PrivateIpAddresses",
        "desc": "指定的内网IP信息，单次最多指定10个。"
      }
    ],
    "desc": "弹性网卡退还内网 IP。\n退还弹性网卡上的辅助内网IP，接口自动解关联弹性公网 IP。不能退还弹性网卡的主内网IP。"
  },
  "CreateSubnet": {
    "params": [
      {
        "name": "VpcId",
        "desc": "待操作的VPC实例ID。可通过DescribeVpcs接口返回值中的VpcId获取。"
      },
      {
        "name": "SubnetName",
        "desc": "子网名称，最大长度不能超过60个字节。"
      },
      {
        "name": "CidrBlock",
        "desc": "子网网段，子网网段必须在VPC网段内，相同VPC内子网网段不能重叠。"
      },
      {
        "name": "Zone",
        "desc": "子网所在的可用区ID，不同子网选择不同可用区可以做跨可用区灾备。"
      },
      {
        "name": "EcmRegion",
        "desc": "ECM 地域"
      },
      {
        "name": "Tags",
        "desc": "指定绑定的标签列表，例如：[{\"Key\": \"city\", \"Value\": \"shanghai\"}]"
      }
    ],
    "desc": "创建子网，若创建成功，则此子网会成为此可用区的默认子网。"
  }
}