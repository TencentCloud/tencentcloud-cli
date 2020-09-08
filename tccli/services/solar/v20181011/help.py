# -*- coding: utf-8 -*-
DESC = "solar-2018-10-11"
INFO = {
  "DescribeSubProject": {
    "params": [
      {
        "name": "SubProjectId",
        "desc": "子项目id"
      }
    ],
    "desc": "子项目详情"
  },
  "DescribeProjectStock": {
    "params": [
      {
        "name": "SubProjectId",
        "desc": "子项目id"
      }
    ],
    "desc": "项目库存详情"
  },
  "DescribeProject": {
    "params": [
      {
        "name": "ProjectId",
        "desc": "项目ID"
      }
    ],
    "desc": "项目详情展示"
  },
  "DescribeResourceTemplateHeaders": {
    "params": [
      {
        "name": "WxAppId",
        "desc": "微信公众号appId"
      }
    ],
    "desc": "素材查询服务号模板的列表（样例）"
  },
  "DescribeCustomer": {
    "params": [
      {
        "name": "UserId",
        "desc": "用户ID"
      }
    ],
    "desc": "客户档案查询客户详情"
  },
  "SendWxTouchTask": {
    "params": [
      {
        "name": "GroupId",
        "desc": "客户分组ID"
      },
      {
        "name": "DistinctFlag",
        "desc": "去除今日已发送的客户"
      },
      {
        "name": "IsSendNow",
        "desc": "是否立马发送"
      },
      {
        "name": "SendDate",
        "desc": "发送时间，一般为0"
      },
      {
        "name": "TaskName",
        "desc": "任务名称"
      },
      {
        "name": "WxTouchType",
        "desc": "微信触达类型，text, news, smallapp, tmplmsg"
      },
      {
        "name": "Title",
        "desc": "标题"
      },
      {
        "name": "Content",
        "desc": "文本内容"
      },
      {
        "name": "NewsId",
        "desc": "图文素材ID"
      },
      {
        "name": "SmallProgramId",
        "desc": "小程序卡片ID"
      },
      {
        "name": "TemplateId",
        "desc": "模板消息ID"
      },
      {
        "name": "WxAppId",
        "desc": "微信公众号appId"
      }
    ],
    "desc": "发送企业微信触达任务"
  },
  "CreateProject": {
    "params": [
      {
        "name": "ProjectName",
        "desc": "项目名称"
      },
      {
        "name": "ProjectOrg",
        "desc": "项目机构"
      },
      {
        "name": "ProjectBudget",
        "desc": "项目预算"
      },
      {
        "name": "ProjectIntroduction",
        "desc": "项目简介"
      },
      {
        "name": "ProjectOrgId",
        "desc": "所属部门ID"
      }
    ],
    "desc": "创建项目"
  },
  "ReplenishProjectStock": {
    "params": [
      {
        "name": "SubProjectId",
        "desc": "项目id"
      },
      {
        "name": "PrizeId",
        "desc": "奖品id"
      },
      {
        "name": "PrizeNum",
        "desc": "奖品数量"
      },
      {
        "name": "PoolIndex",
        "desc": "奖池索引"
      },
      {
        "name": "PoolName",
        "desc": "奖池名称"
      }
    ],
    "desc": "补充子项目库存"
  },
  "DescribeProjects": {
    "params": [
      {
        "name": "PageNo",
        "desc": "页码"
      },
      {
        "name": "PageSize",
        "desc": "页面大小"
      },
      {
        "name": "SearchWord",
        "desc": "过滤规则"
      },
      {
        "name": "Filters",
        "desc": "部门范围过滤"
      },
      {
        "name": "ProjectStatus",
        "desc": "项目状态, 0:编辑中 1:运营中 2:已下线 3:已删除 4:审批中"
      }
    ],
    "desc": "项目列表展示"
  },
  "OffLineProject": {
    "params": [
      {
        "name": "ProjectId",
        "desc": "项目ID"
      }
    ],
    "desc": "下线项目"
  },
  "ExpireFlow": {
    "params": [
      {
        "name": "FlowId",
        "desc": "工单ID"
      }
    ],
    "desc": "把审批中的工单置为已失效"
  },
  "DeleteProject": {
    "params": [
      {
        "name": "ProjectId",
        "desc": "项目ID"
      }
    ],
    "desc": "删除项目"
  },
  "CheckStaffChUser": {
    "params": [
      {
        "name": "UserId",
        "desc": "员工ID"
      },
      {
        "name": "OperateType",
        "desc": "渠道状态：checkpass审核通过, checkreject审核拒绝, enableoperate启用, stopoperate停用"
      }
    ],
    "desc": "员工渠道更改员工状态"
  },
  "DescribeCustomers": {
    "params": [
      {
        "name": "QueryType",
        "desc": "查询类型，0.个人，1负责部门，2.指定部门"
      },
      {
        "name": "GroupId",
        "desc": "分组ID"
      },
      {
        "name": "MarkFlag",
        "desc": "是否星级标记 1是 0否"
      },
      {
        "name": "TagIds",
        "desc": "客户标签，多个标签用逗号隔开"
      },
      {
        "name": "RelChannelFlag",
        "desc": "员工标识筛选，0：非员工，1：员工"
      },
      {
        "name": "NeedPhoneFlag",
        "desc": "必须存在手机 1是 0否"
      },
      {
        "name": "Province",
        "desc": "省份"
      },
      {
        "name": "City",
        "desc": "城市"
      },
      {
        "name": "Sex",
        "desc": "性别 1男 2女"
      },
      {
        "name": "KeyWord",
        "desc": "城市"
      },
      {
        "name": "Offset",
        "desc": "查询开始位置"
      },
      {
        "name": "Limit",
        "desc": "每页记录条数"
      },
      {
        "name": "SubProjectId",
        "desc": "子项目ID"
      }
    ],
    "desc": "查询客户档案列表"
  },
  "ModifyProject": {
    "params": [
      {
        "name": "ProjectId",
        "desc": "项目ID"
      },
      {
        "name": "ProjectName",
        "desc": "项目名称"
      },
      {
        "name": "ProjectBudget",
        "desc": "项目预算"
      },
      {
        "name": "ProjectOrg",
        "desc": "项目机构"
      },
      {
        "name": "ProjectIntroduction",
        "desc": "项目简介"
      },
      {
        "name": "ProjectOrgId",
        "desc": "项目机构Id"
      }
    ],
    "desc": "修改项目"
  },
  "CreateSubProject": {
    "params": [
      {
        "name": "ProjectId",
        "desc": "所属项目id"
      },
      {
        "name": "SubProjectName",
        "desc": "子项目名称"
      }
    ],
    "desc": "创建子项目"
  },
  "CopyActivityChannel": {
    "params": [
      {
        "name": "ActivityId",
        "desc": "活动ID"
      },
      {
        "name": "ChannelFrom",
        "desc": "来源渠道ID"
      },
      {
        "name": "ChannelTo",
        "desc": "目的渠道id"
      }
    ],
    "desc": "复制活动渠道的策略"
  }
}