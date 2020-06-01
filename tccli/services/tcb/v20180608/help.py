# -*- coding: utf-8 -*-
DESC = "tcb-2018-06-08"
INFO = {
  "CreateHostingDomain": {
    "params": [
      {
        "name": "EnvId",
        "desc": "环境ID"
      },
      {
        "name": "Domain",
        "desc": "域名"
      },
      {
        "name": "CertId",
        "desc": "证书ID"
      }
    ],
    "desc": "创建托管域名"
  },
  "DescribeEndUsers": {
    "params": [
      {
        "name": "EnvId",
        "desc": "开发者的环境ID"
      },
      {
        "name": "UUIds",
        "desc": "按照 uuid 列表过滤，最大个数为100"
      }
    ],
    "desc": "获取终端用户列表"
  },
  "CreateAuthDomain": {
    "params": [
      {
        "name": "EnvId",
        "desc": "环境ID"
      },
      {
        "name": "Domains",
        "desc": "安全域名"
      }
    ],
    "desc": "增加安全域名"
  },
  "DescribeAuthDomains": {
    "params": [
      {
        "name": "EnvId",
        "desc": "环境ID"
      }
    ],
    "desc": "获取安全域名列表"
  },
  "ReinstateEnv": {
    "params": [
      {
        "name": "EnvId",
        "desc": "环境ID"
      }
    ],
    "desc": "针对已隔离的免费环境，可以通过本接口将其恢复访问。"
  },
  "DescribeDatabaseACL": {
    "params": [
      {
        "name": "EnvId",
        "desc": "环境ID"
      },
      {
        "name": "CollectionName",
        "desc": "集合名称"
      }
    ],
    "desc": "获取数据库权限"
  },
  "DescribePostpayPackageFreeQuotas": {
    "params": [
      {
        "name": "EnvId",
        "desc": "环境ID"
      },
      {
        "name": "FreeQuotaType",
        "desc": "免费额度类型标识"
      }
    ],
    "desc": "获取后付费免费额度"
  },
  "CommonServiceAPI": {
    "params": [
      {
        "name": "Service",
        "desc": "Service名，需要转发访问的接口名"
      },
      {
        "name": "JSONData",
        "desc": "需要转发的云API参数，要转成JSON格式"
      }
    ],
    "desc": "TCB云API统一入口"
  },
  "CheckTcbService": {
    "params": [],
    "desc": "检查是否开通Tcb服务"
  },
  "DeleteEndUser": {
    "params": [
      {
        "name": "EnvId",
        "desc": "环境ID"
      },
      {
        "name": "UserList",
        "desc": "用户列表，每一项都是uuid"
      }
    ],
    "desc": "删除终端用户"
  },
  "DescribeEndUserLoginStatistic": {
    "params": [
      {
        "name": "EnvId",
        "desc": "环境id"
      },
      {
        "name": "Source",
        "desc": "终端用户来源\n<li> qcloud </li>\n<li>miniapp</li>"
      }
    ],
    "desc": "获取环境终端用户新增与登录信息"
  },
  "DescribeQuotaData": {
    "params": [
      {
        "name": "EnvId",
        "desc": "环境ID"
      },
      {
        "name": "MetricName",
        "desc": "<li> 指标名: </li>\n<li> StorageSizepkg: 当月存储空间容量, 单位MB </li>\n<li> StorageReadpkg: 当月存储读请求次数 </li>\n<li> StorageWritepkg: 当月存储写请求次数 </li>\n<li> StorageCdnOriginFluxpkg: 当月CDN回源流量, 单位字节 </li>\n<li> StorageCdnOriginFluxpkgDay: 当日CDN回源流量, 单位字节 </li>\n<li> StorageReadpkgDay: 当日存储读请求次数 </li>\n<li> StorageWritepkgDay: 当日写请求次数 </li>\n<li> CDNFluxpkg: 当月CDN流量, 单位为字节 </li>\n<li> CDNFluxpkgDay: 当日CDN流量, 单位为字节 </li>\n<li> FunctionInvocationpkg: 当月云函数调用次数 </li>\n<li> FunctionGBspkg: 当月云函数资源使用量, 单位Mb*Ms </li>\n<li> FunctionFluxpkg: 当月云函数流量, 单位千字节(KB) </li>\n<li> FunctionInvocationpkgDay: 当日云函数调用次数 </li>\n<li> FunctionGBspkgDay: 当日云函数资源使用量, 单位Mb*Ms </li>\n<li> FunctionFluxpkgDay: 当日云函数流量, 单位千字节(KB) </li>\n<li> DbSizepkg: 当月数据库容量大小, 单位MB </li>\n<li> DbReadpkg: 当日数据库读请求数 </li>\n<li> DbWritepkg: 当日数据库写请求数 </li>\n<li> StaticFsFluxPkgDay: 当日静态托管流量 </li>\n<li> StaticFsFluxPkg: 当月静态托管流量</li>\n<li> StaticFsSizePkg: 当月静态托管容量 </li>\n<li> TkeCpuUsedPkg: 当月容器托管CPU使用量，单位核 </li>\n<li> TkeMemUsedPkg: 当月容器托管内存使用量，单位MB </li>"
      },
      {
        "name": "ResourceID",
        "desc": "资源ID, 目前仅对云函数、容器托管相关的指标有意义。云函数(FunctionInvocationpkg, FunctionGBspkg, FunctionFluxpkg)、容器托管（服务名称）。如果想查询某个云函数的指标则在ResourceId中传入函数名; 如果只想查询整个namespace的指标, 则留空或不传。"
      }
    ],
    "desc": "查询指定指标的配额使用量"
  },
  "DescribeExtraPkgBillingInfo": {
    "params": [
      {
        "name": "EnvId",
        "desc": "已购买增值包的环境ID"
      }
    ],
    "desc": "获取增值包计费相关信息"
  },
  "ModifyEnv": {
    "params": [
      {
        "name": "EnvId",
        "desc": "环境ID"
      },
      {
        "name": "Alias",
        "desc": "环境备注名，要以a-z开头，不能包含 a-zA-z0-9- 以外的字符"
      }
    ],
    "desc": "更新环境信息"
  },
  "DescribeEndUserStatistic": {
    "params": [
      {
        "name": "EnvId",
        "desc": "环境id"
      }
    ],
    "desc": "获取终端用户总量与平台分布情况"
  },
  "DestroyEnv": {
    "params": [
      {
        "name": "EnvId",
        "desc": "环境Id"
      },
      {
        "name": "IsForce",
        "desc": "针对预付费 删除隔离中的环境时要传true 正常环境直接跳过隔离期删除"
      }
    ],
    "desc": "销毁环境"
  },
  "DescribeEnvs": {
    "params": [
      {
        "name": "EnvId",
        "desc": "环境ID，如果传了这个参数则只返回该环境的相关信息"
      },
      {
        "name": "IsVisible",
        "desc": "指定Channels字段为可见渠道列表或不可见渠道列表\n如只想获取渠道A的环境 就填写IsVisible= true,Channels = [\"A\"], 过滤渠道A拉取其他渠道环境时填写IsVisible= false,Channels = [\"A\"]"
      },
      {
        "name": "Channels",
        "desc": "渠道列表，代表可见或不可见渠道由IsVisible参数指定"
      }
    ],
    "desc": "获取环境列表，含环境下的各个资源信息。尤其是各资源的唯一标识，是请求各资源的关键参数"
  },
  "DestroyStaticStore": {
    "params": [
      {
        "name": "EnvId",
        "desc": "环境ID"
      },
      {
        "name": "CdnDomain",
        "desc": "cdn域名"
      }
    ],
    "desc": "销毁静态托管资源，该接口创建异步销毁任务，资源最终状态可从DestroyStaticStore接口查看"
  },
  "ModifyDatabaseACL": {
    "params": [
      {
        "name": "EnvId",
        "desc": "环境ID"
      },
      {
        "name": "CollectionName",
        "desc": "集合名称"
      },
      {
        "name": "AclTag",
        "desc": "权限标签。包含以下取值：\n<li> READONLY：所有用户可读，仅创建者和管理员可写</li>\n<li> PRIVATE：仅创建者及管理员可读写</li>\n<li> ADMINWRITE：所有用户可读，仅管理员可写</li>\n<li> ADMINONLY：仅管理员可读写</li>"
      }
    ],
    "desc": "修改数据库权限"
  },
  "CreateStaticStore": {
    "params": [
      {
        "name": "EnvId",
        "desc": "环境ID"
      }
    ],
    "desc": "创建静态托管资源，包括COS和CDN，异步任务创建，查看创建结果需要根据DescribeStaticStore接口来查看"
  },
  "DescribeEnvLimit": {
    "params": [],
    "desc": "查询环境个数上限"
  },
  "DescribeEnvFreeQuota": {
    "params": [
      {
        "name": "EnvId",
        "desc": "环境ID"
      },
      {
        "name": "ResourceTypes",
        "desc": "资源类型：可选值：CDN, COS, FLEXDB, HOSTING, SCF\n不传则返回全部资源指标"
      }
    ],
    "desc": "查询后付费免费配额信息"
  }
}