# -*- coding: utf-8 -*-
DESC = "cam-2019-01-16"
INFO = {
  "SetMfaFlag": {
    "params": [
      {
        "name": "OpUin",
        "desc": "设置用户的uin"
      },
      {
        "name": "LoginFlag",
        "desc": "登录保护设置"
      },
      {
        "name": "ActionFlag",
        "desc": "操作保护设置"
      }
    ],
    "desc": "设置子用户的登录保护和敏感操作校验方式"
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
  "DeleteServiceLinkedRole": {
    "params": [
      {
        "name": "RoleName",
        "desc": "要删除的服务相关角色的名称。"
      }
    ],
    "desc": "删除服务相关角色"
  },
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
        "desc": "子用户控制台登录密码，若未进行密码规则设置则默认密码规则为8位以上同时包含大小写字母、数字和特殊字符。只有可以登录控制台时才有效，如果传空并且上面指定允许登录控制台，则自动生成随机密码，随机密码规则为32位包含大小写字母、数字和特殊字符。"
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
  "CreateServiceLinkedRole": {
    "params": [
      {
        "name": "QCSServiceName",
        "desc": "授权服务，附加了此角色的腾讯云服务主体。"
      },
      {
        "name": "CustomSuffix",
        "desc": "自定义后缀，根据您提供的字符串，与服务提供的前缀组合在一起以形成完整的角色名称。"
      },
      {
        "name": "Description",
        "desc": "角色说明。"
      }
    ],
    "desc": "创建服务相关角色"
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
  "CreateRole": {
    "params": [
      {
        "name": "RoleName",
        "desc": "角色名称"
      },
      {
        "name": "PolicyDocument",
        "desc": "策略文档，示例：{\"version\":\"2.0\",\"statement\":[{\"action\":\"name/sts:AssumeRole\",\"effect\":\"allow\",\"principal\":{\"service\":[\"cloudaudit.cloud.tencent.com\",\"cls.cloud.tencent.com\"]}}]}，principal用于指定角色的授权对象。获取该参数可参阅 获取角色详情（https://cloud.tencent.com/document/product/598/36221） 输出参数RoleInfo"
      },
      {
        "name": "Description",
        "desc": "角色描述"
      },
      {
        "name": "ConsoleLogin",
        "desc": "是否允许登录 1 为允许 0 为不允许"
      },
      {
        "name": "SessionDuration",
        "desc": "申请角色临时密钥的最长有效期限制(范围：0~43200)"
      }
    ],
    "desc": "本接口（CreateRole）用于创建角色。"
  },
  "ListUsers": {
    "params": [],
    "desc": "拉取子用户"
  },
  "ListAttachedRolePolicies": {
    "params": [
      {
        "name": "Page",
        "desc": "页码，从 1 开始"
      },
      {
        "name": "Rp",
        "desc": "每页行数，不能大于200"
      },
      {
        "name": "RoleId",
        "desc": "角色 ID。用于指定角色，入参 RoleId 与 RoleName 二选一"
      },
      {
        "name": "RoleName",
        "desc": "角色名。用于指定角色，入参 RoleId 与 RoleName 二选一"
      },
      {
        "name": "PolicyType",
        "desc": "按策略类型过滤，User表示仅查询自定义策略，QCS表示仅查询预设策略"
      }
    ],
    "desc": "本接口（ListAttachedRolePolicies）用于获取角色绑定的策略列表。"
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
  "DeletePolicyVersion": {
    "params": [
      {
        "name": "PolicyId",
        "desc": "策略ID"
      },
      {
        "name": "VersionId",
        "desc": "策略版本号"
      }
    ],
    "desc": "本接口（DeletePolicyVersion）可用于删除一个策略的策略版本。"
  },
  "DetachRolePolicy": {
    "params": [
      {
        "name": "PolicyId",
        "desc": "策略ID，入参PolicyId与PolicyName二选一"
      },
      {
        "name": "DetachRoleId",
        "desc": "角色ID，用于指定角色，入参 AttachRoleId 与 AttachRoleName 二选一"
      },
      {
        "name": "DetachRoleName",
        "desc": "角色名称，用于指定角色，入参 AttachRoleId 与 AttachRoleName 二选一"
      },
      {
        "name": "PolicyName",
        "desc": "策略名，入参PolicyId与PolicyName二选一"
      }
    ],
    "desc": "本接口（DetachRolePolicy）用于解除绑定角色的策略。"
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
        "desc": "子用户控制台登录密码，若未进行密码规则设置则默认密码规则为8位以上同时包含大小写字母、数字和特殊字符。只有可以登录控制台时才有效，如果传空并且上面指定允许登录控制台，则自动生成随机密码，随机密码规则为32位包含大小写字母、数字和特殊字符。"
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
  "DescribeRoleList": {
    "params": [
      {
        "name": "Page",
        "desc": "页码，从1开始"
      },
      {
        "name": "Rp",
        "desc": "每页行数，不能大于200"
      }
    ],
    "desc": "本接口（DescribeRoleList）用于获取账号下的角色列表。"
  },
  "GetCustomMFATokenInfo": {
    "params": [
      {
        "name": "MFAToken",
        "desc": "自定义多因子验证Token"
      }
    ],
    "desc": "获取自定义多因子Token关联信息"
  },
  "ListAccessKeys": {
    "params": [
      {
        "name": "TargetUin",
        "desc": "指定用户Uin，不填默认列出当前用户访问密钥"
      }
    ],
    "desc": "列出指定CAM用户的访问密钥"
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
  "DeleteRole": {
    "params": [
      {
        "name": "RoleId",
        "desc": "角色ID，用于指定角色，入参 RoleId 与 RoleName 二选一"
      },
      {
        "name": "RoleName",
        "desc": "角色名称，用于指定角色，入参 RoleId 与 RoleName 二选一"
      }
    ],
    "desc": "本接口（DeleteRole）用于删除指定角色。"
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
        "desc": "用户组ID"
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
      },
      {
        "name": "SubUin",
        "desc": "子账号UIN"
      }
    ],
    "desc": "列出用户关联的用户组"
  },
  "GetServiceLinkedRoleDeletionStatus": {
    "params": [
      {
        "name": "DeletionTaskId",
        "desc": "删除任务ID"
      }
    ],
    "desc": "根据删除TaskId获取服务相关角色删除状态"
  },
  "ConsumeCustomMFAToken": {
    "params": [
      {
        "name": "MFAToken",
        "desc": "自定义多因子验证Token"
      }
    ],
    "desc": "验证自定义多因子Token"
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
  "GetPolicyVersion": {
    "params": [
      {
        "name": "PolicyId",
        "desc": "策略ID"
      },
      {
        "name": "VersionId",
        "desc": "策略版本号"
      }
    ],
    "desc": "该接口（GetPolicyVersion）用于查询策略版本详情"
  },
  "SetDefaultPolicyVersion": {
    "params": [
      {
        "name": "PolicyId",
        "desc": "策略ID"
      },
      {
        "name": "VersionId",
        "desc": "策略版本号"
      }
    ],
    "desc": "本接口（SetDefaultPolicyVersion）可用于设置生效的策略版本。"
  },
  "DeleteUser": {
    "params": [
      {
        "name": "Name",
        "desc": "子用户用户名"
      },
      {
        "name": "Force",
        "desc": "是否强制删除该子用户，默认入参为0。0：若该用户存在未删除API密钥，则不删除用户；1：若该用户存在未删除API密钥，则先删除密钥后删除用户。删除密钥需要您拥有cam:DeleteApiKey权限，您将可以删除该用户下启用或禁用状态的所有密钥，无权限则删除密钥和用户失败"
      }
    ],
    "desc": "删除子用户"
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
        "desc": "策略ID"
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
        "desc": "策略文档，示例：{\"version\":\"2.0\",\"statement\":[{\"action\":\"name/sts:AssumeRole\",\"effect\":\"allow\",\"principal\":{\"service\":[\"cloudaudit.cloud.tencent.com\",\"cls.cloud.tencent.com\"]}}]}，principal用于指定角色的授权对象。获取该参数可参阅 获取角色详情（https://cloud.tencent.com/document/product/598/36221） 输出参数RoleInfo"
      },
      {
        "name": "Alias",
        "desc": "预设策略备注"
      }
    ],
    "desc": "本接口（UpdatePolicy ）可用于更新策略。\n如果已存在策略版本，本接口会直接更新策略的默认版本，不会创建新版本，如果不存在任何策略版本，则直接创建一个默认版本。"
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
  "GetRole": {
    "params": [
      {
        "name": "RoleId",
        "desc": "角色 ID，用于指定角色，入参 RoleId 与 RoleName 二选一"
      },
      {
        "name": "RoleName",
        "desc": "角色名，用于指定角色，入参 RoleId 与 RoleName 二选一"
      }
    ],
    "desc": "本接口（GetRole）用于获取指定角色的详细信息。"
  },
  "UpdateRoleDescription": {
    "params": [
      {
        "name": "Description",
        "desc": "角色描述"
      },
      {
        "name": "RoleId",
        "desc": "角色ID，用于指定角色，入参 RoleId 与 RoleName 二选一"
      },
      {
        "name": "RoleName",
        "desc": "角色名称，用于指定角色，入参 RoleId 与 RoleName 二选一"
      }
    ],
    "desc": "本接口（UpdateRoleDescription）用于修改角色的描述信息。"
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
  "CreatePolicyVersion": {
    "params": [
      {
        "name": "PolicyId",
        "desc": "策略ID"
      },
      {
        "name": "PolicyDocument",
        "desc": "策略文本信息"
      },
      {
        "name": "SetAsDefault",
        "desc": "是否设置为当前策略的版本"
      }
    ],
    "desc": "该接口（CreatePolicyVersion）用于新增策略版本，用户创建了一个策略版本之后可以方便的通过变更策略版本的方式来变更策略。"
  },
  "ListCollaborators": {
    "params": [
      {
        "name": "Limit",
        "desc": "分页条数，缺省为20"
      },
      {
        "name": "Offset",
        "desc": "分页起始值，缺省为0"
      }
    ],
    "desc": "获取协作者列表"
  },
  "AttachRolePolicy": {
    "params": [
      {
        "name": "PolicyId",
        "desc": "策略ID，入参PolicyId与PolicyName二选一"
      },
      {
        "name": "AttachRoleId",
        "desc": "角色ID，用于指定角色，入参 AttachRoleId 与 AttachRoleName 二选一"
      },
      {
        "name": "AttachRoleName",
        "desc": "角色名称，用于指定角色，入参 AttachRoleId 与 AttachRoleName 二选一"
      },
      {
        "name": "PolicyName",
        "desc": "策略名，入参PolicyId与PolicyName二选一"
      }
    ],
    "desc": "本接口（AttachRolePolicy）用于绑定策略到角色。"
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
  "UpdateRoleConsoleLogin": {
    "params": [
      {
        "name": "ConsoleLogin",
        "desc": "是否可登录，可登录：1，不可登录：0"
      },
      {
        "name": "RoleId",
        "desc": "角色ID"
      },
      {
        "name": "RoleName",
        "desc": "角色名"
      }
    ],
    "desc": "本接口（UpdateRoleConsoleLogin）用于修改角色是否可登录。"
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
  "ListPolicyVersions": {
    "params": [
      {
        "name": "PolicyId",
        "desc": "策略ID"
      }
    ],
    "desc": "该接口（ListPolicyVersions）用于获取策略版本列表"
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
  "UpdateAssumeRolePolicy": {
    "params": [
      {
        "name": "PolicyDocument",
        "desc": "策略文档，示例：{\"version\":\"2.0\",\"statement\":[{\"action\":\"name/sts:AssumeRole\",\"effect\":\"allow\",\"principal\":{\"service\":[\"cloudaudit.cloud.tencent.com\",\"cls.cloud.tencent.com\"]}}]}，principal用于指定角色的授权对象。获取该参数可参阅 获取角色详情（https://cloud.tencent.com/document/product/598/36221） 输出参数RoleInfo"
      },
      {
        "name": "RoleId",
        "desc": "角色ID，用于指定角色，入参 RoleId 与 RoleName 二选一"
      },
      {
        "name": "RoleName",
        "desc": "角色名称，用于指定角色，入参 RoleId 与 RoleName 二选一"
      }
    ],
    "desc": "本接口（UpdateAssumeRolePolicy）用于修改角色信任策略的策略文档。"
  },
  "CreatePolicy": {
    "params": [
      {
        "name": "PolicyName",
        "desc": "策略名"
      },
      {
        "name": "PolicyDocument",
        "desc": "策略文档，示例：{\"version\":\"2.0\",\"statement\":[{\"action\":\"name/sts:AssumeRole\",\"effect\":\"allow\",\"principal\":{\"service\":[\"cloudaudit.cloud.tencent.com\",\"cls.cloud.tencent.com\"]}}]}，principal用于指定角色的授权对象。获取该参数可参阅 获取角色详情（https://cloud.tencent.com/document/product/598/36221） 输出参数RoleInfo"
      },
      {
        "name": "Description",
        "desc": "策略描述"
      }
    ],
    "desc": "本接口（CreatePolicy）可用于创建策略。"
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
    "desc": "本接口（ListPolicies）可用于查询策略列表。"
  }
}