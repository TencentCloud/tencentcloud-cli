# -*- coding: utf-8 -*-
DESC = "tcr-2019-09-24"
INFO = {
  "ModifyNamespace": {
    "params": [
      {
        "name": "RegistryId",
        "desc": "实例Id"
      },
      {
        "name": "NamespaceName",
        "desc": "命名空间名称"
      },
      {
        "name": "IsPublic",
        "desc": "访问级别，True为公开，False为私有"
      }
    ],
    "desc": "更新命名空间信息，当前仅支持修改命名空间访问级别"
  },
  "DescribeImageFilterPersonal": {
    "params": [
      {
        "name": "RepoName",
        "desc": "仓库名称"
      },
      {
        "name": "Tag",
        "desc": "Tag名"
      }
    ],
    "desc": "用于在个人版中查询与指定tag镜像内容相同的tag列表"
  },
  "CreateImageLifecyclePersonal": {
    "params": [
      {
        "name": "RepoName",
        "desc": "仓库名称"
      },
      {
        "name": "Type",
        "desc": "keep_last_days:保留最近几天的数据;keep_last_nums:保留最近多少个"
      },
      {
        "name": "Val",
        "desc": "策略值"
      }
    ],
    "desc": "用于在个人版中创建清理策略"
  },
  "DescribeImagePersonal": {
    "params": [
      {
        "name": "RepoName",
        "desc": "仓库名称"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0"
      },
      {
        "name": "Limit",
        "desc": "返回最大数量，默认 20, 最大值 100"
      },
      {
        "name": "Tag",
        "desc": "tag名称，可根据输入搜索"
      }
    ],
    "desc": "用于获取个人版镜像仓库tag列表"
  },
  "DescribeImageLifecyclePersonal": {
    "params": [
      {
        "name": "RepoName",
        "desc": "仓库名称"
      }
    ],
    "desc": "用于获取个人版仓库中自动清理策略"
  },
  "DescribeImages": {
    "params": [
      {
        "name": "RegistryId",
        "desc": "实例ID"
      },
      {
        "name": "NamespaceName",
        "desc": "命名空间名称"
      },
      {
        "name": "RepositoryName",
        "desc": "镜像仓库名称"
      },
      {
        "name": "ImageVersion",
        "desc": "指定镜像版本(Tag)，不填默认返回仓库内全部容器镜像"
      },
      {
        "name": "Limit",
        "desc": "每页个数，用于分页，默认20"
      },
      {
        "name": "Offset",
        "desc": "页数，默认值为1"
      }
    ],
    "desc": "查询镜像版本列表或指定容器镜像信息"
  },
  "CreateNamespace": {
    "params": [
      {
        "name": "RegistryId",
        "desc": "实例ID"
      },
      {
        "name": "NamespaceName",
        "desc": "命名空间的名称"
      },
      {
        "name": "IsPublic",
        "desc": "是否公开，true为公开，fale为私有"
      }
    ],
    "desc": "用于在企业版中创建命名空间"
  },
  "ModifyRepository": {
    "params": [
      {
        "name": "RegistryId",
        "desc": "实例ID"
      },
      {
        "name": "NamespaceName",
        "desc": "命名空间名称"
      },
      {
        "name": "RepositoryName",
        "desc": "镜像仓库名称"
      },
      {
        "name": "BriefDescription",
        "desc": "仓库简短描述"
      },
      {
        "name": "Description",
        "desc": "仓库详细描述"
      }
    ],
    "desc": "更新镜像仓库信息，可修改仓库描述信息"
  },
  "DeleteNamespace": {
    "params": [
      {
        "name": "RegistryId",
        "desc": "实例ID"
      },
      {
        "name": "NamespaceName",
        "desc": "命名空间的名称"
      }
    ],
    "desc": "删除命名空间"
  },
  "DeleteRepository": {
    "params": [
      {
        "name": "RegistryId",
        "desc": "实例Id"
      },
      {
        "name": "NamespaceName",
        "desc": "命名空间的名称"
      },
      {
        "name": "RepositoryName",
        "desc": "仓库名称的名称"
      }
    ],
    "desc": "删除镜像仓库"
  },
  "DescribeRepositories": {
    "params": [
      {
        "name": "RegistryId",
        "desc": "实例Id"
      },
      {
        "name": "NamespaceName",
        "desc": "指定命名空间，不填写默认为查询所有命名空间下镜像仓库"
      },
      {
        "name": "RepositoryName",
        "desc": "指定镜像仓库，不填写默认查询指定命名空间下所有镜像仓库"
      },
      {
        "name": "Offset",
        "desc": "页数，用于分页"
      },
      {
        "name": "Limit",
        "desc": "每页个数，用于分页"
      },
      {
        "name": "SortBy",
        "desc": "基于字段排序，支持的值有-creation_time,-name, -update_time"
      }
    ],
    "desc": "查询镜像仓库列表或指定镜像仓库信息"
  },
  "DescribeInstances": {
    "params": [
      {
        "name": "Registryids",
        "desc": "实例ID列表(为空时，\n表示获取账号下所有实例)"
      },
      {
        "name": "Offset",
        "desc": "偏移量,默认0"
      },
      {
        "name": "Limit",
        "desc": "最大输出条数，默认20，最大为100"
      },
      {
        "name": "Filters",
        "desc": "过滤条件"
      },
      {
        "name": "AllRegion",
        "desc": "获取所有地域的实例，默认为False"
      }
    ],
    "desc": "查询实例信息"
  },
  "ModifyRepositoryInfoPersonal": {
    "params": [
      {
        "name": "RepoName",
        "desc": "仓库名称"
      },
      {
        "name": "Description",
        "desc": "仓库描述"
      }
    ],
    "desc": "用于在个人版镜像仓库中更新容器镜像描述"
  },
  "DescribeRepositoryPersonal": {
    "params": [
      {
        "name": "RepoName",
        "desc": "仓库名字"
      }
    ],
    "desc": "查询个人版仓库信息"
  },
  "DescribeNamespacePersonal": {
    "params": [
      {
        "name": "Namespace",
        "desc": "命名空间，支持模糊查询"
      },
      {
        "name": "Limit",
        "desc": "单页数量"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      }
    ],
    "desc": "查询个人版命名空间信息"
  },
  "DeleteRepositoryPersonal": {
    "params": [
      {
        "name": "RepoName",
        "desc": "仓库名称"
      }
    ],
    "desc": "用于个人版镜像仓库中删除"
  },
  "DescribeWebhookTriggerLog": {
    "params": [
      {
        "name": "RegistryId",
        "desc": "实例 Id"
      },
      {
        "name": "Namespace",
        "desc": "命名空间"
      },
      {
        "name": "Id",
        "desc": "触发器 Id"
      },
      {
        "name": "Limit",
        "desc": "分页单页数量"
      },
      {
        "name": "Offset",
        "desc": "分页偏移量"
      }
    ],
    "desc": "获取触发器日志"
  },
  "DescribeImageManifests": {
    "params": [
      {
        "name": "RegistryId",
        "desc": "实例ID"
      },
      {
        "name": "NamespaceName",
        "desc": "命名空间名称"
      },
      {
        "name": "RepositoryName",
        "desc": "镜像仓库名称"
      },
      {
        "name": "ImageVersion",
        "desc": "镜像版本"
      }
    ],
    "desc": "查询容器镜像Manifest信息"
  },
  "DescribeInstanceToken": {
    "params": [
      {
        "name": "RegistryId",
        "desc": "实例 ID"
      },
      {
        "name": "Limit",
        "desc": "分页单页数量"
      },
      {
        "name": "Offset",
        "desc": "分页偏移量"
      }
    ],
    "desc": "查询长期访问凭证信息"
  },
  "ManageImageLifecycleGlobalPersonal": {
    "params": [
      {
        "name": "Type",
        "desc": "global_keep_last_days:全局保留最近几天的数据;global_keep_last_nums:全局保留最近多少个"
      },
      {
        "name": "Val",
        "desc": "策略值"
      }
    ],
    "desc": "用于设置个人版全局镜像版本自动清理策略"
  },
  "DescribeApplicationTriggerLogPersonal": {
    "params": [
      {
        "name": "RepoName",
        "desc": "仓库名称"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0"
      },
      {
        "name": "Limit",
        "desc": "返回最大数量，默认 20, 最大值 100"
      },
      {
        "name": "Order",
        "desc": "升序或降序"
      },
      {
        "name": "OrderBy",
        "desc": "按某列排序"
      }
    ],
    "desc": "用于查询应用更新触发器触发日志"
  },
  "DeleteInstanceToken": {
    "params": [
      {
        "name": "RegistryId",
        "desc": "实例 ID"
      },
      {
        "name": "TokenId",
        "desc": "访问凭证 ID"
      }
    ],
    "desc": "删除长期访问凭证"
  },
  "ModifyUserPasswordPersonal": {
    "params": [
      {
        "name": "Password",
        "desc": "更新后的密码"
      }
    ],
    "desc": "修改个人用户登录密码"
  },
  "DeleteApplicationTriggerPersonal": {
    "params": [
      {
        "name": "TriggerName",
        "desc": "触发器名称"
      }
    ],
    "desc": "用于删除应用更新触发器"
  },
  "DescribeWebhookTrigger": {
    "params": [
      {
        "name": "RegistryId",
        "desc": "实例Id"
      },
      {
        "name": "Limit",
        "desc": "分页单页数量"
      },
      {
        "name": "Offset",
        "desc": "分页偏移量"
      },
      {
        "name": "Namespace",
        "desc": "命名空间"
      }
    ],
    "desc": "查询触发器"
  },
  "DeleteImagePersonal": {
    "params": [
      {
        "name": "RepoName",
        "desc": "仓库名称"
      },
      {
        "name": "Tag",
        "desc": "Tag名"
      }
    ],
    "desc": "用于在个人版中删除tag"
  },
  "ModifyWebhookTrigger": {
    "params": [
      {
        "name": "RegistryId",
        "desc": "实例Id"
      },
      {
        "name": "Trigger",
        "desc": "触发器参数"
      },
      {
        "name": "Namespace",
        "desc": "命名空间"
      }
    ],
    "desc": "更新触发器"
  },
  "ModifyInstanceToken": {
    "params": [
      {
        "name": "TokenId",
        "desc": "实例长期访问凭证 ID"
      },
      {
        "name": "Enable",
        "desc": "启用或禁用实例长期访问凭证"
      },
      {
        "name": "RegistryId",
        "desc": "实例 ID"
      }
    ],
    "desc": "更新实例内指定长期访问凭证的启用状态"
  },
  "CreateInstance": {
    "params": [
      {
        "name": "RegistryName",
        "desc": "企业版实例名称"
      },
      {
        "name": "RegistryType",
        "desc": "企业版实例类型"
      }
    ],
    "desc": "创建实例"
  },
  "BatchDeleteImagePersonal": {
    "params": [
      {
        "name": "RepoName",
        "desc": "仓库名称"
      },
      {
        "name": "Tags",
        "desc": "Tag列表"
      }
    ],
    "desc": "用于在个人版镜像仓库中批量删除Tag"
  },
  "CreateWebhookTrigger": {
    "params": [
      {
        "name": "RegistryId",
        "desc": "实例 Id"
      },
      {
        "name": "Trigger",
        "desc": "触发器参数"
      },
      {
        "name": "Namespace",
        "desc": "命名空间"
      }
    ],
    "desc": "创建触发器"
  },
  "CreateApplicationTriggerPersonal": {
    "params": [
      {
        "name": "RepoName",
        "desc": "触发器关联的镜像仓库，library/test格式"
      },
      {
        "name": "TriggerName",
        "desc": "触发器名称"
      },
      {
        "name": "InvokeMethod",
        "desc": "触发方式，\"all\"全部触发，\"taglist\"指定tag触发，\"regex\"正则触发"
      },
      {
        "name": "ClusterId",
        "desc": "应用所在TKE集群ID"
      },
      {
        "name": "Namespace",
        "desc": "应用所在TKE集群命名空间"
      },
      {
        "name": "WorkloadType",
        "desc": "应用所在TKE集群工作负载类型,支持Deployment、StatefulSet、DaemonSet、CronJob、Job。"
      },
      {
        "name": "WorkloadName",
        "desc": "应用所在TKE集群工作负载名称"
      },
      {
        "name": "ContainerName",
        "desc": "应用所在TKE集群工作负载下容器名称"
      },
      {
        "name": "ClusterRegion",
        "desc": "应用所在TKE集群地域"
      },
      {
        "name": "InvokeExpr",
        "desc": "触发方式对应的表达式"
      }
    ],
    "desc": "用于创建应用更新触发器"
  },
  "DescribeImageLifecycleGlobalPersonal": {
    "params": [],
    "desc": "用于获取个人版全局镜像版本自动清理策略"
  },
  "DescribeUserQuotaPersonal": {
    "params": [],
    "desc": "查询个人用户配额"
  },
  "DeleteWebhookTrigger": {
    "params": [
      {
        "name": "RegistryId",
        "desc": "实例Id"
      },
      {
        "name": "Namespace",
        "desc": "命名空间"
      },
      {
        "name": "Id",
        "desc": "触发器 Id"
      }
    ],
    "desc": "删除触发器"
  },
  "ModifyApplicationTriggerPersonal": {
    "params": [
      {
        "name": "RepoName",
        "desc": "触发器关联的镜像仓库，library/test格式"
      },
      {
        "name": "TriggerName",
        "desc": "触发器名称"
      },
      {
        "name": "InvokeMethod",
        "desc": "触发方式，\"all\"全部触发，\"taglist\"指定tag触发，\"regex\"正则触发"
      },
      {
        "name": "InvokeExpr",
        "desc": "触发方式对应的表达式"
      },
      {
        "name": "ClusterId",
        "desc": "应用所在TKE集群ID"
      },
      {
        "name": "Namespace",
        "desc": "应用所在TKE集群命名空间"
      },
      {
        "name": "WorkloadType",
        "desc": "应用所在TKE集群工作负载类型,支持Deployment、StatefulSet、DaemonSet、CronJob、Job。"
      },
      {
        "name": "WorkloadName",
        "desc": "应用所在TKE集群工作负载名称"
      },
      {
        "name": "ContainerName",
        "desc": "应用所在TKE集群工作负载下容器名称"
      },
      {
        "name": "ClusterRegion",
        "desc": "应用所在TKE集群地域数字ID，如1（广州）、16（成都）"
      },
      {
        "name": "NewTriggerName",
        "desc": "新触发器名称"
      }
    ],
    "desc": "用于修改应用更新触发器"
  },
  "DescribeFavorRepositoryPersonal": {
    "params": [
      {
        "name": "RepoName",
        "desc": "仓库名称"
      },
      {
        "name": "Limit",
        "desc": "分页Limit"
      },
      {
        "name": "Offset",
        "desc": "Offset用于分页"
      }
    ],
    "desc": "查询个人收藏仓库"
  },
  "DescribeRepositoryOwnerPersonal": {
    "params": [
      {
        "name": "Offset",
        "desc": "偏移量，默认为0"
      },
      {
        "name": "Limit",
        "desc": "返回最大数量，默认 20, 最大值 100"
      },
      {
        "name": "RepoName",
        "desc": "仓库名称"
      }
    ],
    "desc": "用于在个人版中获取用户全部的镜像仓库列表"
  },
  "DescribeNamespaces": {
    "params": [
      {
        "name": "RegistryId",
        "desc": "实例Id"
      },
      {
        "name": "NamespaceName",
        "desc": "指定命名空间，不填写默认查询所有命名空间"
      },
      {
        "name": "Limit",
        "desc": "每页个数"
      },
      {
        "name": "Offset",
        "desc": "页偏移"
      }
    ],
    "desc": "查询命名空间列表或指定命名空间信息"
  },
  "DescribeInstanceStatus": {
    "params": [
      {
        "name": "RegistryIds",
        "desc": "实例ID的数组"
      }
    ],
    "desc": "查询实例当前状态以及过程信息"
  },
  "CreateRepositoryPersonal": {
    "params": [
      {
        "name": "RepoName",
        "desc": "仓库名称"
      },
      {
        "name": "Public",
        "desc": "是否公共,1:公共,0:私有"
      },
      {
        "name": "Description",
        "desc": "仓库描述"
      }
    ],
    "desc": "用于在个人版仓库中创建镜像仓库"
  },
  "BatchDeleteRepositoryPersonal": {
    "params": [
      {
        "name": "RepoNames",
        "desc": "仓库名称数组"
      }
    ],
    "desc": "用于个人版镜像仓库中批量删除镜像仓库"
  },
  "DuplicateImagePersonal": {
    "params": [
      {
        "name": "SrcImage",
        "desc": "源镜像名称，不包含domain。例如： tencentyun/foo:v1"
      },
      {
        "name": "DestImage",
        "desc": "目的镜像名称，不包含domain。例如： tencentyun/foo:latest"
      }
    ],
    "desc": "用于在个人版镜像仓库中复制镜像版本"
  },
  "DescribeRepositoryFilterPersonal": {
    "params": [
      {
        "name": "RepoName",
        "desc": "搜索镜像名"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0"
      },
      {
        "name": "Limit",
        "desc": "返回最大数量，默认 20，最大100"
      },
      {
        "name": "Public",
        "desc": "筛选条件：1表示public，0表示private"
      },
      {
        "name": "Namespace",
        "desc": "命名空间"
      }
    ],
    "desc": "用于在个人版镜像仓库中，获取满足输入搜索条件的用户镜像仓库"
  },
  "ValidateNamespaceExistPersonal": {
    "params": [
      {
        "name": "Namespace",
        "desc": "命名空间名称"
      }
    ],
    "desc": "查询个人版用户命名空间是否存在"
  },
  "CreateRepository": {
    "params": [
      {
        "name": "RegistryId",
        "desc": "实例ID"
      },
      {
        "name": "NamespaceName",
        "desc": "命名空间名称"
      },
      {
        "name": "RepositoryName",
        "desc": "仓库名称"
      },
      {
        "name": "BriefDescription",
        "desc": "仓库简短描述"
      },
      {
        "name": "Description",
        "desc": "仓库详细描述"
      }
    ],
    "desc": "用于企业版创建镜像仓库"
  },
  "CreateNamespacePersonal": {
    "params": [
      {
        "name": "Namespace",
        "desc": "命名空间名称"
      }
    ],
    "desc": "创建个人版镜像仓库命名空间，此命名空间全局唯一"
  },
  "CreateUserPersonal": {
    "params": [
      {
        "name": "Password",
        "desc": "用户密码"
      }
    ],
    "desc": "创建个人用户"
  },
  "DeleteImageLifecycleGlobalPersonal": {
    "params": [],
    "desc": "用于删除个人版全局镜像版本自动清理策略"
  },
  "DeleteNamespacePersonal": {
    "params": [
      {
        "name": "Namespace",
        "desc": "命名空间名称"
      }
    ],
    "desc": "删除共享版命名空间"
  },
  "ModifyRepositoryAccessPersonal": {
    "params": [
      {
        "name": "RepoName",
        "desc": "仓库名称"
      },
      {
        "name": "Public",
        "desc": "默认值为0"
      }
    ],
    "desc": "用于更新个人版镜像仓库的访问属性"
  },
  "DeleteImageLifecyclePersonal": {
    "params": [
      {
        "name": "RepoName",
        "desc": "仓库名称"
      }
    ],
    "desc": "用于在个人版镜像仓库中删除仓库Tag自动清理策略"
  },
  "ValidateRepositoryExistPersonal": {
    "params": [
      {
        "name": "RepoName",
        "desc": "仓库名称"
      }
    ],
    "desc": "用于判断个人版仓库是否存在"
  },
  "CreateInstanceToken": {
    "params": [
      {
        "name": "RegistryId",
        "desc": "实例Id"
      },
      {
        "name": "TokenType",
        "desc": "访问凭证类型，longterm 为长期访问凭证，temp 为临时访问凭证，默认是临时访问凭证，有效期1小时"
      },
      {
        "name": "Desc",
        "desc": "长期访问凭证描述信息"
      }
    ],
    "desc": "创建实例的临时或长期访问凭证"
  },
  "DescribeApplicationTriggerPersonal": {
    "params": [
      {
        "name": "RepoName",
        "desc": "仓库名称"
      },
      {
        "name": "TriggerName",
        "desc": "触发器名称"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0"
      },
      {
        "name": "Limit",
        "desc": "返回最大数量，默认 20, 最大值 100"
      }
    ],
    "desc": "用于查询应用更新触发器"
  }
}