# -*- coding: utf-8 -*-
DESC = "bm-2018-04-23"
INFO = {
  "UnbindPsaTag": {
    "params": [
      {
        "name": "PsaId",
        "desc": "预授权规则ID"
      },
      {
        "name": "TagKey",
        "desc": "需要解绑的标签key"
      },
      {
        "name": "TagValue",
        "desc": "需要解绑的标签value"
      }
    ],
    "desc": "解除标签与预授权规则的绑定"
  },
  "ModifyPsaRegulation": {
    "params": [
      {
        "name": "PsaId",
        "desc": "预授权规则ID"
      },
      {
        "name": "PsaName",
        "desc": "预授权规则别名"
      },
      {
        "name": "RepairLimit",
        "desc": "维修中的实例上限"
      },
      {
        "name": "PsaDescription",
        "desc": "预授权规则备注"
      },
      {
        "name": "TaskTypeIds",
        "desc": "预授权规则关联故障类型ID列表"
      }
    ],
    "desc": "允许修改规则信息及关联故障类型"
  },
  "DescribePsaRegulations": {
    "params": [
      {
        "name": "Limit",
        "desc": "数量限制"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "PsaIds",
        "desc": "规则ID过滤，支持模糊查询"
      },
      {
        "name": "PsaNames",
        "desc": "规则别名过滤，支持模糊查询"
      },
      {
        "name": "Tags",
        "desc": "标签过滤"
      },
      {
        "name": "OrderField",
        "desc": "排序字段，取值支持：CreateTime"
      },
      {
        "name": "Order",
        "desc": "排序方式 0:递增(默认) 1:递减"
      }
    ],
    "desc": "获取预授权规则列表"
  },
  "DescribeRepairTaskConstant": {
    "params": [],
    "desc": "维修任务配置获取"
  },
  "BindPsaTag": {
    "params": [
      {
        "name": "PsaId",
        "desc": "预授权规则ID"
      },
      {
        "name": "TagKey",
        "desc": "需要绑定的标签key"
      },
      {
        "name": "TagValue",
        "desc": "需要绑定的标签value"
      }
    ],
    "desc": "为预授权规则绑定标签"
  },
  "DescribeTaskOperationLog": {
    "params": [
      {
        "name": "TaskId",
        "desc": "维修任务ID"
      },
      {
        "name": "OrderField",
        "desc": "排序字段，目前支持：OperationTime"
      },
      {
        "name": "Order",
        "desc": "排序方式 0:递增(默认) 1:递减"
      }
    ],
    "desc": "获取维修任务操作日志"
  },
  "DeletePsaRegulation": {
    "params": [
      {
        "name": "PsaId",
        "desc": "预授权规则ID"
      }
    ],
    "desc": "删除预授权规则"
  },
  "DescribeTaskInfo": {
    "params": [
      {
        "name": "Offset",
        "desc": "开始位置"
      },
      {
        "name": "Limit",
        "desc": "数据条数"
      },
      {
        "name": "StartDate",
        "desc": "时间过滤下限"
      },
      {
        "name": "EndDate",
        "desc": "时间过滤上限"
      },
      {
        "name": "TaskStatus",
        "desc": "任务状态ID过滤"
      },
      {
        "name": "OrderField",
        "desc": "排序字段，目前支持：CreateTime，AuthTime，EndTime"
      },
      {
        "name": "Order",
        "desc": "排序方式 0:递增(默认) 1:递减"
      },
      {
        "name": "TaskIds",
        "desc": "任务ID过滤"
      },
      {
        "name": "InstanceIds",
        "desc": "实例ID过滤"
      },
      {
        "name": "Aliases",
        "desc": "实例别名过滤"
      },
      {
        "name": "TaskTypeIds",
        "desc": "故障类型ID过滤"
      }
    ],
    "desc": "获取用户维修任务列表及详细信息<br>\n<br>\nTaskStatus（任务状态ID）与状态中文名的对应关系如下：<br>\n1：未授权<br>\n2：处理中<br>\n3：待确认<br>\n4：未授权-暂不处理<br>\n5：已恢复<br>\n6：待确认-未恢复<br>"
  },
  "RepairTaskControl": {
    "params": [
      {
        "name": "TaskId",
        "desc": "维修任务ID"
      },
      {
        "name": "Operate",
        "desc": "操作"
      }
    ],
    "desc": "此接口用于操作维修任务<br>\n入参TaskId为维修任务ID<br>\n入参Operate表示对维修任务的操作，支持如下取值：<br>\nAuthorizeRepair（授权维修）<br>\nIgnore（暂不提醒）<br>\nConfirmRecovered（维修完成后，确认故障恢复）<br>\nConfirmUnRecovered（维修完成后，确认故障未恢复）<br>\n<br>\n操作约束（当前任务状态(TaskStatus)->对应可执行的操作）：<br>\n未授权(1)->授权维修；暂不处理<br>\n暂不处理(4)->授权维修<br>\n待确认(3)->确认故障恢复；确认故障未恢复<br>\n未恢复(6)->确认故障恢复<br>\n<br>\n对于Ping不可达故障的任务，还允许：<br>\n未授权->确认故障恢复<br>\n暂不处理->确认故障恢复<br>\n<br>\n处理中与已恢复状态的任务不允许进行操作。<br>\n<br>\n详细信息请访问：https://cloud.tencent.com/document/product/386/18190"
  },
  "CreatePsaRegulation": {
    "params": [
      {
        "name": "PsaName",
        "desc": "规则别名"
      },
      {
        "name": "TaskTypeIds",
        "desc": "关联的故障类型ID列表"
      },
      {
        "name": "RepairLimit",
        "desc": "维修实例上限，默认为5"
      },
      {
        "name": "PsaDescription",
        "desc": "规则备注"
      }
    ],
    "desc": "创建预授权规则"
  }
}