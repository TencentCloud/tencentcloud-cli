# -*- coding: utf-8 -*-
DESC = "organization-2018-12-25"
INFO = {
  "DenyOrganizationInvitation": {
    "params": [
      {
        "name": "Id",
        "desc": "邀请ID"
      }
    ],
    "desc": "拒绝企业组织邀请"
  },
  "ListOrganizationInvitations": {
    "params": [
      {
        "name": "Invited",
        "desc": "是否被邀请。1：被邀请，0：发出的邀请"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "Limit",
        "desc": "限制数目"
      }
    ],
    "desc": "获取邀请信息列表"
  },
  "UpdateOrganizationNode": {
    "params": [
      {
        "name": "NodeId",
        "desc": "企业组织单元ID"
      },
      {
        "name": "Name",
        "desc": "名称"
      },
      {
        "name": "ParentNodeId",
        "desc": "父单元ID"
      }
    ],
    "desc": "更新企业组织单元"
  },
  "AcceptOrganizationInvitation": {
    "params": [
      {
        "name": "Id",
        "desc": "邀请ID"
      }
    ],
    "desc": "接受加入企业组织邀请"
  },
  "DeleteOrganization": {
    "params": [],
    "desc": "删除企业组织"
  },
  "GetOrganization": {
    "params": [],
    "desc": "获取企业组织信息"
  },
  "ListOrganizationNodes": {
    "params": [],
    "desc": "获取企业组织单元列表"
  },
  "UpdateOrganizationMember": {
    "params": [
      {
        "name": "MemberUin",
        "desc": "成员UIN"
      },
      {
        "name": "Name",
        "desc": "名称"
      },
      {
        "name": "Remark",
        "desc": "备注"
      }
    ],
    "desc": "更新企业成员信息"
  },
  "QuitOrganization": {
    "params": [
      {
        "name": "OrgId",
        "desc": "企业组织ID"
      }
    ],
    "desc": "退出企业组织"
  },
  "DeleteOrganizationNodes": {
    "params": [
      {
        "name": "NodeIds",
        "desc": "组织单元ID列表"
      }
    ],
    "desc": "批量删除企业组织单元"
  },
  "ListOrganizationMembers": {
    "params": [
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "Limit",
        "desc": "限制数目"
      }
    ],
    "desc": "获取企业组织成员列表"
  },
  "DeleteOrganizationMemberFromNode": {
    "params": [
      {
        "name": "MemberUin",
        "desc": "被删除成员UIN"
      },
      {
        "name": "NodeId",
        "desc": "组织单元ID"
      }
    ],
    "desc": "删除企业组织成员"
  },
  "AddOrganizationNode": {
    "params": [
      {
        "name": "ParentNodeId",
        "desc": "父组织单元ID"
      },
      {
        "name": "Name",
        "desc": "组织单元名字"
      }
    ],
    "desc": "添加企业组织单元"
  },
  "SendOrganizationInvitation": {
    "params": [
      {
        "name": "InviteUin",
        "desc": "被邀请账户UIN"
      },
      {
        "name": "Name",
        "desc": "名称"
      },
      {
        "name": "Remark",
        "desc": "备注"
      }
    ],
    "desc": "发送企业组织邀请"
  },
  "MoveOrganizationMembersToNode": {
    "params": [
      {
        "name": "NodeId",
        "desc": "组织单元ID"
      },
      {
        "name": "Uins",
        "desc": "成员UIN列表"
      }
    ],
    "desc": "移动成员到指定企业组织单元"
  },
  "GetOrganizationMember": {
    "params": [
      {
        "name": "MemberUin",
        "desc": "组织成员UIN"
      }
    ],
    "desc": "获取企业组织成员"
  },
  "DeleteOrganizationMembers": {
    "params": [
      {
        "name": "Uins",
        "desc": "被删除成员的UIN列表"
      }
    ],
    "desc": "批量删除企业组织成员"
  },
  "ListOrganizationNodeMembers": {
    "params": [
      {
        "name": "NodeId",
        "desc": "企业组织单元ID"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "Limit",
        "desc": "限制数目"
      }
    ],
    "desc": "获取企业组织单元成员列表"
  },
  "CancelOrganizationInvitation": {
    "params": [
      {
        "name": "Id",
        "desc": "邀请ID"
      }
    ],
    "desc": "取消企业组织邀请"
  },
  "CreateOrganization": {
    "params": [
      {
        "name": "OrgType",
        "desc": "组织类型（目前固定为1）"
      }
    ],
    "desc": "创建企业组织"
  }
}