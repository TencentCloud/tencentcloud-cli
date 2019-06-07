# -*- coding: utf-8 -*-
DESC = "msp-2018-03-19"
INFO = {
  "ListMigrationTask": {
    "params": [
      {
        "name": "Offset",
        "desc": "记录起始数，默认值为0"
      },
      {
        "name": "Limit",
        "desc": "记录条数，默认值为10"
      },
      {
        "name": "ProjectId",
        "desc": "项目ID，默认值为空"
      }
    ],
    "desc": "获取迁移任务列表"
  },
  "RegisterMigrationTask": {
    "params": [
      {
        "name": "TaskType",
        "desc": "任务类型，取值database（数据库迁移）、file（文件迁移）、host（主机迁移）"
      },
      {
        "name": "TaskName",
        "desc": "任务名称"
      },
      {
        "name": "ServiceSupplier",
        "desc": "服务提供商名称"
      },
      {
        "name": "SrcInfo",
        "desc": "迁移任务源信息"
      },
      {
        "name": "DstInfo",
        "desc": "迁移任务目的信息"
      },
      {
        "name": "CreateTime",
        "desc": "迁移任务创建时间"
      },
      {
        "name": "UpdateTime",
        "desc": "迁移任务更新时间"
      },
      {
        "name": "MigrateClass",
        "desc": "迁移类别，如数据库迁移中mysql:mysql代表从mysql迁移到mysql，文件迁移中oss:cos代表从阿里云oss迁移到腾讯云cos"
      },
      {
        "name": "SrcAccessType",
        "desc": "源实例接入类型，数据库迁移时填写值为：extranet(外网),cvm(cvm自建实例),dcg(专线接入的实例),vpncloud(云vpn接入的实例),vpnselfbuild(自建vpn接入的实例)，cdb(云上cdb实例)"
      },
      {
        "name": "SrcDatabaseType",
        "desc": "源实例数据库类型，数据库迁移时填写，取值为mysql,redis,percona,mongodb,postgresql,sqlserver,mariadb 之一"
      },
      {
        "name": "DstAccessType",
        "desc": "目标实例接入类型，数据库迁移时填写值为：extranet(外网),cvm(cvm自建实例),dcg(专线接入的实例),vpncloud(云vpn接入的实例),vpnselfbuild(自建vpn接入的实例)，cdb(云上cdb实例)"
      },
      {
        "name": "DstDatabaseType",
        "desc": "目标实例数据库类型,数据库迁移时填写，取值为mysql,redis,percona,mongodb,postgresql,sqlserver,mariadb 之一"
      }
    ],
    "desc": "注册迁移任务"
  },
  "ModifyMigrationTaskStatus": {
    "params": [
      {
        "name": "Status",
        "desc": "任务状态，取值为unstart，migrating，finish，fail之一，分别代表该迁移任务状态为迁移未开始，迁移中，迁移完成，迁移失败"
      },
      {
        "name": "TaskId",
        "desc": "任务ID，例如msp-jitoh33n"
      }
    ],
    "desc": "更新迁移任务状态"
  },
  "DeregisterMigrationTask": {
    "params": [
      {
        "name": "TaskId",
        "desc": "任务ID"
      }
    ],
    "desc": "取消注册迁移任务"
  },
  "DescribeMigrationTask": {
    "params": [
      {
        "name": "TaskId",
        "desc": "任务ID，例如msp-jitoh33n"
      }
    ],
    "desc": "获取指定迁移任务详情"
  },
  "ModifyMigrationTaskBelongToProject": {
    "params": [
      {
        "name": "TaskId",
        "desc": "任务ID，例如msp-jitoh33n"
      },
      {
        "name": "ProjectId",
        "desc": "项目ID，例如10005"
      }
    ],
    "desc": "更改迁移任务所属项目"
  },
  "ListMigrationProject": {
    "params": [
      {
        "name": "Offset",
        "desc": "记录起始数，默认值为0"
      },
      {
        "name": "Limit",
        "desc": "返回条数，默认值为500"
      }
    ],
    "desc": "获取迁移项目名称列表"
  }
}