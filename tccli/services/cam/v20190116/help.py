# -*- coding: utf-8 -*-
DESC = "cam-2019-01-16"
INFO = {
  "AddUser": {
    "params": [
      {
        "name": "Name",
        "desc": "子用户用户名"
      },
      {
        "name": "Remark",
        "desc": "子用户备注"
      },
      {
        "name": "ConsoleLogin",
        "desc": "子用户是否可以登录控制台。传0子用户无法登录控制台，传1子用户可以登录控制台。"
      },
      {
        "name": "UseApi",
        "desc": "是否生成子用户密钥。传0不生成子用户密钥，传1生成子用户密钥。"
      },
      {
        "name": "Password",
        "desc": "子用户控制台登录密码，若未进行密码规则设置则默认密码规则为8位以上同时包含大写小字母、数字和特殊字符。只有可以登录控制台时才有效，如果传空并且上面指定允许登录控制台，则自动生成随机密码，随机密码规则为32位包含大写小字母、数字和特殊字符。"
      },
      {
        "name": "NeedResetPassword",
        "desc": "子用户是否要在下次登录时重置密码。传0子用户下次登录控制台不需重置密码，传1子用户下次登录控制台需要重置密码。"
      },
      {
        "name": "PhoneNum",
        "desc": "手机号"
      },
      {
        "name": "CountryCode",
        "desc": "区号"
      },
      {
        "name": "Email",
        "desc": "邮箱"
      }
    ],
    "desc": "添加子用户"
  },
  "GetSAMLProvider": {
    "params": [
      {
        "name": "Name",
        "desc": "SAML身份提供商名称"
      }
    ],
    "desc": "查询SAML身份提供商详情"
  },
  "ListUsers": {
    "params": [],
    "desc": "拉取子用户"
  },
  "DeletePolicy": {
    "params": [
      {
        "name": "PolicyId",
        "desc": "数组，数组成员是策略 id，支持批量删除策略"
      }
    ],
    "desc": "本接口（DeletePolicy）可用于删除策略。"
  },
  "CreateGroup": {
    "params": [
      {
        "name": "GroupName",
        "desc": "用户组名"
      },
      {
        "name": "Remark",
        "desc": "用户组描述"
      }
    ],
    "desc": "创建用户组"
  },
  "GetPolicy": {
    "params": [
      {
        "name": "PolicyId",
        "desc": "策略Id"
      }
    ],
    "desc": "本接口（GetPolicy）可用于查询查看策略详情。"
  },
  "CreateSAMLProvider": {
    "params": [
      {
        "name": "Name",
        "desc": "SAML身份提供商名称"
      },
      {
        "name": "Description",
        "desc": "SAML身份提供商描述"
      },
      {
        "name": "SAMLMetadataDocument",
        "desc": "SAML身份提供商Base64编码的元数据文档"
      }
    ],
    "desc": "创建SAML身份提供商"
  },
  "DeleteSAMLProvider": {
    "params": [
      {
        "name": "Name",
        "desc": "SAML身份提供商名称"
      }
    ],
    "desc": "删除SAML身份提供商"
  },
  "UpdateUser": {
    "params": [
      {
        "name": "Name",
        "desc": "子用户用户名"
      },
      {
        "name": "Remark",
        "desc": "子用户备注"
      },
      {
        "name": "ConsoleLogin",
        "desc": "子用户是否可以登录控制台。传0子用户无法登录控制台，传1子用户可以登录控制台。"
      },
      {
        "name": "Password",
        "desc": "子用户控制台登录密码，若未进行密码规则设置则默认密码规则为8位以上同时包含大写小字母、数字和特殊字符。只有可以登录控制台时才有效，如果传空并且上面指定允许登录控制台，则自动生成随机密码，随机密码规则为32位包含大写小字母、数字和特殊字符。"
      },
      {
        "name": "NeedResetPassword",
        "desc": "子用户是否要在下次登录时重置密码。传0子用户下次登录控制台不需重置密码，传1子用户下次登录控制台需要重置密码。"
      },
      {
        "name": "PhoneNum",
        "desc": "手机号"
      },
      {
        "name": "CountryCode",
        "desc": "区号"
      },
      {
        "name": "Email",
        "desc": "邮箱"
      }
    ],
    "desc": "更新子用户"
  },
  "DeleteGroup": {
    "params": [
      {
        "name": "GroupId",
        "desc": "用户组 ID"
      }
    ],
    "desc": "删除用户组"
  },
  "GetUser": {
    "params": [
      {
        "name": "Name",
        "desc": "子用户用户名"
      }
    ],
    "desc": "查询子用户"
  },
  "AttachGroupPolicy": {
    "params": [
      {
        "name": "PolicyId",
        "desc": "策略 id"
      },
      {
        "name": "AttachGroupId",
        "desc": "用户组 id"
      }
    ],
    "desc": "本接口（AttachGroupPolicy）可用于绑定策略到用户组。"
  },
  "ListAttachedGroupPolicies": {
    "params": [
      {
        "name": "TargetGroupId",
        "desc": "用户组 id"
      },
      {
        "name": "Page",
        "desc": "页码，默认值是 1，从 1 开始"
      },
      {
        "name": "Rp",
        "desc": "每页大小，默认值是 20"
      }
    ],
    "desc": "本接口（ListAttachedGroupPolicies）可用于查询用户组关联的策略列表。"
  },
  "ListGroupsForUser": {
    "params": [
      {
        "name": "Uid",
        "desc": "子用户 UID"
      },
      {
        "name": "Rp",
        "desc": "每页数量。默认为20。"
      },
      {
        "name": "Page",
        "desc": "页码。默认为1。"
      }
    ],
    "desc": "列出用户关联的用户组"
  },
  "ListEntitiesForPolicy": {
    "params": [
      {
        "name": "PolicyId",
        "desc": "策略 id"
      },
      {
        "name": "Page",
        "desc": "页码，默认值是 1，从 1 开始"
      },
      {
        "name": "Rp",
        "desc": "每页大小，默认值是 20"
      },
      {
        "name": "EntityFilter",
        "desc": "可取值 'All'、'User'、'Group' 和 'Role'，'All' 表示获取所有实体类型，'User' 表示只获取子账号，'Group' 表示只获取用户组，'Role' 表示只获取角色，默认取 'All'"
      }
    ],
    "desc": "本接口（ListEntitiesForPolicy）可用于查询策略关联的实体列表。"
  },
  "ListGroups": {
    "params": [
      {
        "name": "Page",
        "desc": "页码。默认为1。"
      },
      {
        "name": "Rp",
        "desc": "每页数量。默认为20。"
      },
      {
        "name": "Keyword",
        "desc": "按用户组名称匹配。"
      }
    ],
    "desc": "查询用户组列表"
  },
  "AddUserToGroup": {
    "params": [
      {
        "name": "Info",
        "desc": "添加的子用户 UID 和用户组 ID 关联关系"
      }
    ],
    "desc": "用户加入到用户组"
  },
  "UpdateSAMLProvider": {
    "params": [
      {
        "name": "Name",
        "desc": "SAML身份提供商名称"
      },
      {
        "name": "Description",
        "desc": "SAML身份提供商描述"
      },
      {
        "name": "SAMLMetadataDocument",
        "desc": "SAML身份提供商Base64编码的元数据文档"
      }
    ],
    "desc": "更新SAML身份提供商信息"
  },
  "UpdatePolicy": {
    "params": [
      {
        "name": "PolicyId",
        "desc": "策略 id"
      },
      {
        "name": "PolicyName",
        "desc": "策略名"
      },
      {
        "name": "Description",
        "desc": "策略描述"
      },
      {
        "name": "PolicyDocument",
        "desc": "策略文档"
      }
    ],
    "desc": "本接口（UpdatePolicy ）可用于更新策略。"
  },
  "ListAttachedUserPolicies": {
    "params": [
      {
        "name": "TargetUin",
        "desc": "子账号 uin"
      },
      {
        "name": "Page",
        "desc": "页码，默认值是 1，从 1 开始"
      },
      {
        "name": "Rp",
        "desc": "每页大小，默认值是 20"
      }
    ],
    "desc": "本接口（ListAttachedUserPolicies）可用于查询子账号关联的策略列表。"
  },
  "DeleteUser": {
    "params": [
      {
        "name": "Name",
        "desc": "子用户用户名"
      }
    ],
    "desc": "删除子用户"
  },
  "DetachGroupPolicy": {
    "params": [
      {
        "name": "PolicyId",
        "desc": "策略 id"
      },
      {
        "name": "DetachGroupId",
        "desc": "用户组 id"
      }
    ],
    "desc": "本接口（DetachGroupPolicy）可用于解除绑定到用户组的策略。"
  },
  "RemoveUserFromGroup": {
    "params": [
      {
        "name": "Info",
        "desc": "要删除的用户 UID和用户组 ID对应数组"
      }
    ],
    "desc": "从用户组删除用户"
  },
  "ListSAMLProviders": {
    "params": [],
    "desc": "查询SAML身份提供商列表"
  },
  "ListUsersForGroup": {
    "params": [
      {
        "name": "GroupId",
        "desc": "用户组 ID。"
      },
      {
        "name": "Page",
        "desc": "页码。默认为1。"
      },
      {
        "name": "Rp",
        "desc": "每页数量。默认为20。"
      }
    ],
    "desc": "查询用户组关联的用户列表"
  },
  "AttachUserPolicy": {
    "params": [
      {
        "name": "PolicyId",
        "desc": "策略 id"
      },
      {
        "name": "AttachUin",
        "desc": "子账号 uin"
      }
    ],
    "desc": "本接口（AttachUserPolicy）可用于绑定到用户的策略。"
  },
  "GetGroup": {
    "params": [
      {
        "name": "GroupId",
        "desc": "用户组 ID"
      }
    ],
    "desc": "查询用户组详情"
  },
  "UpdateGroup": {
    "params": [
      {
        "name": "GroupId",
        "desc": "用户组 ID"
      },
      {
        "name": "GroupName",
        "desc": "用户组名"
      },
      {
        "name": "Remark",
        "desc": "用户组描述"
      }
    ],
    "desc": "更新用户组"
  },
  "CreatePolicy": {
    "params": [
      {
        "name": "PolicyName",
        "desc": "策略名"
      },
      {
        "name": "PolicyDocument",
        "desc": "策略文档"
      },
      {
        "name": "Description",
        "desc": "策略描述"
      }
    ],
    "desc": "本接口（CreatePolicy）可用于创建策略。"
  },
  "DetachUserPolicy": {
    "params": [
      {
        "name": "PolicyId",
        "desc": "策略 id"
      },
      {
        "name": "DetachUin",
        "desc": "子账号 uin"
      }
    ],
    "desc": "本接口（DetachUserPolicy）可用于解除绑定到用户的策略。"
  },
  "ListPolicies": {
    "params": [
      {
        "name": "Rp",
        "desc": "每页数量，默认值是 20，必须大于 0 且小于或等于 200"
      },
      {
        "name": "Page",
        "desc": "页码，默认值是 1，从 1开始，不能大于 200"
      },
      {
        "name": "Scope",
        "desc": "可取值 'All'、'QCS' 和 'Local'，'All' 获取所有策略，'QCS' 只获取预设策略，'Local' 只获取自定义策略，默认取 'All'"
      },
      {
        "name": "Keyword",
        "desc": "按策略名匹配"
      }
    ],
    "desc": "本接口（ListPolicies）可用于查询策略列表"
  }
}