# -*- coding: utf-8 -*-
DESC = "cfs-2019-07-19"
INFO = {
  "CreateCfsFileSystem": {
    "params": [
      {
        "name": "Zone",
        "desc": "可用区名称，例如ap-beijing-1，请参考 [概览](https://cloud.tencent.com/document/product/582/13225) 文档中的地域与可用区列表"
      },
      {
        "name": "NetInterface",
        "desc": "网络类型，值为 VPC，BASIC；其中 VPC 为私有网络，BASIC 为基础网络"
      },
      {
        "name": "PGroupId",
        "desc": "权限组 ID"
      },
      {
        "name": "Protocol",
        "desc": "文件系统协议类型， 值为 NFS、CIFS; 若留空则默认为 NFS协议"
      },
      {
        "name": "StorageType",
        "desc": "文件系统存储类型，值为 SD ；其中 SD 为标准型存储， HP为性能存储。"
      },
      {
        "name": "VpcId",
        "desc": "私有网络（VPC） ID，若网络类型选择的是VPC，该字段为必填。"
      },
      {
        "name": "SubnetId",
        "desc": "子网 ID，若网络类型选择的是VPC，该字段为必填。"
      },
      {
        "name": "MountIP",
        "desc": "指定IP地址，仅VPC网络支持；若不填写、将在该子网下随机分配 IP"
      },
      {
        "name": "FsName",
        "desc": "用户自定义文件系统名称"
      },
      {
        "name": "ResourceTags",
        "desc": "文件系统标签"
      }
    ],
    "desc": "用于添加新文件系统"
  },
  "DeleteCfsPGroup": {
    "params": [
      {
        "name": "PGroupId",
        "desc": "权限组 ID"
      }
    ],
    "desc": "本接口（DeleteCfsPGroup）用于删除权限组。"
  },
  "DeleteMountTarget": {
    "params": [
      {
        "name": "FileSystemId",
        "desc": "文件系统 ID"
      },
      {
        "name": "MountTargetId",
        "desc": "挂载点 ID"
      }
    ],
    "desc": "本接口（DeleteMountTarget）用于删除挂载点"
  },
  "DescribeCfsRules": {
    "params": [
      {
        "name": "PGroupId",
        "desc": "权限组 ID"
      }
    ],
    "desc": "本接口（DescribeCfsRules）用于查询权限组规则列表。"
  },
  "UpdateCfsFileSystemPGroup": {
    "params": [
      {
        "name": "PGroupId",
        "desc": "权限组 ID"
      },
      {
        "name": "FileSystemId",
        "desc": "文件系统 ID"
      }
    ],
    "desc": "本接口（UpdateCfsFileSystemPGroup）用于更新文件系统所使用的权限组"
  },
  "DescribeAvailableZoneInfo": {
    "params": [],
    "desc": "本接口（DescribeAvailableZoneInfo）用于查询区域的可用情况。"
  },
  "UpdateCfsFileSystemName": {
    "params": [
      {
        "name": "FileSystemId",
        "desc": "文件系统 ID"
      },
      {
        "name": "FsName",
        "desc": "用户自定义文件系统名称"
      }
    ],
    "desc": "本接口（UpdateCfsFileSystemName）用于更新文件系统名"
  },
  "DescribeCfsPGroups": {
    "params": [],
    "desc": "本接口（DescribeCfsPGroups）用于查询权限组列表。"
  },
  "CreateCfsPGroup": {
    "params": [
      {
        "name": "Name",
        "desc": "权限组名称，1-64个字符且只能为中文，字母，数字，下划线或横线"
      },
      {
        "name": "DescInfo",
        "desc": "权限组描述信息，1-255个字符"
      }
    ],
    "desc": "本接口（CreateCfsPGroup）用于创建权限组"
  },
  "DescribeMountTargets": {
    "params": [
      {
        "name": "FileSystemId",
        "desc": "文件系统 ID"
      }
    ],
    "desc": "本接口（DescribeMountTargets）用于查询文件系统挂载点信息"
  },
  "UpdateCfsFileSystemSizeLimit": {
    "params": [
      {
        "name": "FsLimit",
        "desc": "文件系统容量限制大小，输入范围0-1073741824, 单位为GB；其中输入值为0时，表示不限制文件系统容量。"
      },
      {
        "name": "FileSystemId",
        "desc": "文件系统ID"
      }
    ],
    "desc": "本接口（UpdateCfsFileSystemSizeLimit）用于更新文件系统存储容量限制。"
  },
  "DescribeCfsFileSystems": {
    "params": [
      {
        "name": "FileSystemId",
        "desc": "文件系统 ID"
      },
      {
        "name": "VpcId",
        "desc": "私有网络（VPC） ID"
      },
      {
        "name": "SubnetId",
        "desc": "子网 ID"
      }
    ],
    "desc": "本接口（DescribeCfsFileSystems）用于查询文件系统"
  },
  "SignUpCfsService": {
    "params": [],
    "desc": "本接口（SignUpCfsService）用于开通CFS服务。"
  },
  "CreateCfsRule": {
    "params": [
      {
        "name": "PGroupId",
        "desc": "权限组 ID"
      },
      {
        "name": "AuthClientIp",
        "desc": "可以填写单个 IP 或者单个网段，例如 10.1.10.11 或者 10.10.1.0/24。默认来访地址为*表示允许所有。同时需要注意，此处需填写 CVM 的内网 IP。"
      },
      {
        "name": "Priority",
        "desc": "规则优先级，参数范围1-100。 其中 1 为最高，100为最低"
      },
      {
        "name": "RWPermission",
        "desc": "读写权限, 值为 RO、RW；其中 RO 为只读，RW 为读写，不填默认为只读"
      },
      {
        "name": "UserPermission",
        "desc": "用户权限，值为 all_squash、no_all_squash、root_squash、no_root_squash。其中all_squash为所有访问用户都会被映射为匿名用户或用户组；no_all_squash为访问用户会先与本机用户匹配，匹配失败后再映射为匿名用户或用户组；root_squash为将来访的root用户映射为匿名用户或用户组；no_root_squash为来访的root用户保持root帐号权限。不填默认为root_squash。"
      }
    ],
    "desc": "本接口（CreateCfsRule）用于创建权限组规则。"
  },
  "DeleteCfsFileSystem": {
    "params": [
      {
        "name": "FileSystemId",
        "desc": "文件系统 ID。说明，进行删除文件系统操作前需要先调用 DeleteMountTarget 接口删除该文件系统的挂载点，否则会删除失败。"
      }
    ],
    "desc": "用于删除文件系统"
  },
  "UpdateCfsRule": {
    "params": [
      {
        "name": "PGroupId",
        "desc": "权限组 ID"
      },
      {
        "name": "RuleId",
        "desc": "规则 ID"
      },
      {
        "name": "AuthClientIp",
        "desc": "可以填写单个 IP 或者单个网段，例如 10.1.10.11 或者 10.10.1.0/24。默认来访地址为*表示允许所有。同时需要注意，此处需填写 CVM 的内网 IP。"
      },
      {
        "name": "RWPermission",
        "desc": "读写权限, 值为RO、RW；其中 RO 为只读，RW 为读写，不填默认为只读"
      },
      {
        "name": "UserPermission",
        "desc": "用户权限，值为all_squash、no_all_squash、root_squash、no_root_squash。其中all_squash为所有访问用户都会被映射为匿名用户或用户组；no_all_squash为访问用户会先与本机用户匹配，匹配失败后再映射为匿名用户或用户组；root_squash为将来访的root用户映射为匿名用户或用户组；no_root_squash为来访的root用户保持root帐号权限。不填默认为root_squash。"
      },
      {
        "name": "Priority",
        "desc": "规则优先级，参数范围1-100。 其中 1 为最高，100为最低"
      }
    ],
    "desc": "本接口（UpdateCfsRule）用于更新权限规则。"
  },
  "UpdateCfsPGroup": {
    "params": [
      {
        "name": "PGroupId",
        "desc": "权限组 ID"
      },
      {
        "name": "Name",
        "desc": "权限组名称，1-64个字符且只能为中文，字母，数字，下划线或横线"
      },
      {
        "name": "DescInfo",
        "desc": "权限组描述信息，1-255个字符"
      }
    ],
    "desc": "本接口（UpdateCfsPGroup）更新权限组信息。"
  },
  "DeleteCfsRule": {
    "params": [
      {
        "name": "PGroupId",
        "desc": "权限组 ID"
      },
      {
        "name": "RuleId",
        "desc": "规则 ID"
      }
    ],
    "desc": "本接口（DeleteCfsRule）用于删除权限组规则。"
  },
  "DescribeCfsFileSystemClients": {
    "params": [
      {
        "name": "FileSystemId",
        "desc": "文件系统 ID。"
      }
    ],
    "desc": "查询挂载该文件系统的客户端。此功能需要客户端安装CFS监控插件。"
  },
  "DescribeCfsServiceStatus": {
    "params": [],
    "desc": "本接口（DescribeCfsServiceStatus）用于查询用户使用CFS的服务状态。"
  }
}