# -*- coding: utf-8 -*-
DESC = "tcb-2018-06-08"
INFO = {
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
  "DescribeEnvs": {
    "params": [
      {
        "name": "EnvId",
        "desc": "环境ID，如果传了这个参数则只返回该环境的相关信息"
      }
    ],
    "desc": "获取环境列表，含环境下的各个资源信息。尤其是各资源的唯一标识，是请求各资源的关键参数"
  },
  "CreateMysqlInstance": {
    "params": [
      {
        "name": "EnvId",
        "desc": "环境名称"
      },
      {
        "name": "Alias",
        "desc": "实例别名"
      },
      {
        "name": "Memory",
        "desc": "实例内存大小，单位：MB"
      },
      {
        "name": "Volume",
        "desc": "实例硬盘大小，单位：GB"
      },
      {
        "name": "EngineVersion",
        "desc": "MySQL 版本，值包括：5.7"
      }
    ],
    "desc": "创建mysql实例"
  },
  "OfflineMysqlInstance": {
    "params": [
      {
        "name": "EnvId",
        "desc": "环境id"
      },
      {
        "name": "Alias",
        "desc": "实例别名"
      }
    ],
    "desc": "下线mysql实例"
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
  "UpgradeMysqlInstance": {
    "params": [
      {
        "name": "EnvId",
        "desc": "环境id"
      },
      {
        "name": "Alias",
        "desc": "实例别名"
      },
      {
        "name": "Memory",
        "desc": "实例内存大小，单位：MB"
      },
      {
        "name": "Volume",
        "desc": "实例硬盘大小，单位：GB"
      },
      {
        "name": "EngineVersion",
        "desc": "MySQL 版本，值包括: 5.7"
      }
    ],
    "desc": "升级mysql实例"
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
  "IsolateMysqlInstance": {
    "params": [
      {
        "name": "EnvId",
        "desc": "环境id"
      },
      {
        "name": "Alias",
        "desc": "实例别名"
      }
    ],
    "desc": "隔离mysql实例"
  }
}