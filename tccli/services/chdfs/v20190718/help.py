# -*- coding: utf-8 -*-
DESC = "chdfs-2019-07-18"
INFO = {
  "DescribeMountPoint": {
    "params": [
      {
        "name": "MountPointId",
        "desc": "挂载点ID"
      }
    ],
    "desc": "查看挂载点详细信息。"
  },
  "ModifyFileSystem": {
    "params": [
      {
        "name": "FileSystemId",
        "desc": "文件系统ID"
      },
      {
        "name": "FileSystemName",
        "desc": "文件系统名称"
      },
      {
        "name": "Description",
        "desc": "文件系统描述"
      },
      {
        "name": "CapacityQuota",
        "desc": "文件系统容量（byte），下限为1G，上限为1P，且必须是1G的整数倍\n注意：修改的文件系统容量不能小于当前使用量"
      }
    ],
    "desc": "修改文件系统属性，仅限于创建成功的文件系统。"
  },
  "DeleteFileSystem": {
    "params": [
      {
        "name": "FileSystemId",
        "desc": "文件系统ID"
      }
    ],
    "desc": "删除文件系统，不允许删除非空文件系统。"
  },
  "DeleteAccessRules": {
    "params": [
      {
        "name": "AccessRuleIds",
        "desc": "多个权限规则ID，上限为10"
      }
    ],
    "desc": "批量删除权限规则。"
  },
  "DeleteAccessGroup": {
    "params": [
      {
        "name": "AccessGroupId",
        "desc": "权限组ID"
      }
    ],
    "desc": "删除权限组。"
  },
  "DescribeFileSystem": {
    "params": [
      {
        "name": "FileSystemId",
        "desc": "文件系统ID"
      }
    ],
    "desc": "查看文件系统详细信息。"
  },
  "ModifyMountPoint": {
    "params": [
      {
        "name": "MountPointId",
        "desc": "挂载点ID"
      },
      {
        "name": "MountPointName",
        "desc": "挂载点名称"
      },
      {
        "name": "MountPointStatus",
        "desc": "挂载点状态"
      },
      {
        "name": "AccessGroupId",
        "desc": "权限组ID"
      }
    ],
    "desc": "修改挂载点属性。"
  },
  "DescribeFileSystems": {
    "params": [
      {
        "name": "Offset",
        "desc": "偏移量，默认为0"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为所有"
      }
    ],
    "desc": "查看文件系统列表。"
  },
  "CreateMountPoint": {
    "params": [
      {
        "name": "MountPointName",
        "desc": "挂载点名称"
      },
      {
        "name": "FileSystemId",
        "desc": "文件系统ID"
      },
      {
        "name": "AccessGroupId",
        "desc": "权限组ID"
      },
      {
        "name": "VpcId",
        "desc": "VPC网络ID"
      },
      {
        "name": "MountPointStatus",
        "desc": "挂载点状态（1：打开；2：关闭）"
      },
      {
        "name": "VpcType",
        "desc": "VPC网络类型（1：CVM；2：黑石1.0；3：黑石2.0）"
      }
    ],
    "desc": "创建文件系统挂载点，仅限于创建成功的文件系统。"
  },
  "DescribeMountPoints": {
    "params": [
      {
        "name": "FileSystemId",
        "desc": "文件系统ID\n注意：若根据AccessGroupId查看挂载点列表，则无需设置FileSystemId"
      },
      {
        "name": "AccessGroupId",
        "desc": "权限组ID\n注意：若根据FileSystemId查看挂载点列表，则无需设置AccessGroupId"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为所有"
      }
    ],
    "desc": "通过文件系统ID或者权限组ID查看挂载点列表。"
  },
  "ModifyAccessGroup": {
    "params": [
      {
        "name": "AccessGroupId",
        "desc": "权限组ID"
      },
      {
        "name": "AccessGroupName",
        "desc": "权限组名称"
      },
      {
        "name": "Description",
        "desc": "权限组描述"
      }
    ],
    "desc": "修改权限组属性。"
  },
  "ModifyAccessRules": {
    "params": [
      {
        "name": "AccessRules",
        "desc": "多个权限规则，上限为10"
      }
    ],
    "desc": "批量修改权限规则属性，需要指定权限规则ID。"
  },
  "DescribeAccessRules": {
    "params": [
      {
        "name": "AccessGroupId",
        "desc": "权限组ID"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为所有"
      }
    ],
    "desc": "通过权限组ID查看权限规则列表。"
  },
  "DescribeAccessGroups": {
    "params": [
      {
        "name": "Filters",
        "desc": "过滤条件，Name可选“AccessGroupId“和“AccessGroupName”，Values上限为10"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为所有"
      }
    ],
    "desc": "查看权限组列表。"
  },
  "CreateAccessGroup": {
    "params": [
      {
        "name": "AccessGroupName",
        "desc": "权限组名称"
      },
      {
        "name": "Description",
        "desc": "权限组描述"
      }
    ],
    "desc": "创建权限组。"
  },
  "CreateFileSystem": {
    "params": [
      {
        "name": "FileSystemName",
        "desc": "文件系统名称"
      },
      {
        "name": "CapacityQuota",
        "desc": "文件系统容量（byte），下限为1G，上限为1P，且必须是1G的整数倍"
      },
      {
        "name": "Description",
        "desc": "文件系统描述"
      }
    ],
    "desc": "创建文件系统（异步）。"
  },
  "CreateAccessRules": {
    "params": [
      {
        "name": "AccessRules",
        "desc": "多个权限规则，上限为10"
      },
      {
        "name": "AccessGroupId",
        "desc": "权限组ID"
      }
    ],
    "desc": "批量创建权限规则，权限规则ID和创建时间无需填写。"
  },
  "DeleteMountPoint": {
    "params": [
      {
        "name": "MountPointId",
        "desc": "挂载点ID"
      }
    ],
    "desc": "删除挂载点。"
  }
}