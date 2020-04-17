# -*- coding: utf-8 -*-
DESC = "cam-2019-01-16"
INFO = {
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
  "DetectState": {
    "params": [
      {
        "name": "ClientIP",
        "desc": "IP"
      },
      {
        "name": "ClientUA",
        "desc": "浏览器UA"
      },
      {
        "name": "FaceIdToken",
        "desc": "token"
      }
    ],
    "desc": "获取并且更新人联合身状态"
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
  },
  "DescribeMFADeviceColl": {
    "params": [
      {
        "name": "SubUin",
        "desc": "子用户Uin"
      }
    ],
    "desc": "查询mfa设备"
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
  "DescribeMfaCodeStatus": {
    "params": [
      {
        "name": "Tmpcode",
        "desc": "mfaKey"
      },
      {
        "name": "Skey",
        "desc": "登录态skey"
      },
      {
        "name": "ClientUA",
        "desc": "用户浏览器UA"
      },
      {
        "name": "Interface",
        "desc": "接口名"
      },
      {
        "name": "ClientIP",
        "desc": "用户IP"
      },
      {
        "name": "OwnerUin",
        "desc": "主账号"
      }
    ],
    "desc": "查询微信code状态"
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
  "Check": {
    "params": [
      {
        "name": "Skey",
        "desc": "登录态Skey"
      },
      {
        "name": "ClientIP",
        "desc": "IP"
      },
      {
        "name": "ClientUA",
        "desc": "浏览器UA"
      },
      {
        "name": "Interface",
        "desc": "接口名"
      },
      {
        "name": "AuthType",
        "desc": "验证类型"
      },
      {
        "name": "Code",
        "desc": "验证码"
      },
      {
        "name": "OwnerUin",
        "desc": "主账号"
      }
    ],
    "desc": "mfa校验"
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
  "CheckNewMfaCode": {
    "params": [
      {
        "name": "Skey",
        "desc": "登录态Skey"
      },
      {
        "name": "Interface",
        "desc": "接口名"
      },
      {
        "name": "ClientIP",
        "desc": "IP"
      },
      {
        "name": "ClientUA",
        "desc": "浏览器UA"
      },
      {
        "name": "AuthType",
        "desc": "验证类型"
      },
      {
        "name": "OwnerUin",
        "desc": "主账号uin"
      },
      {
        "name": "PhoneCode",
        "desc": "手机验证码"
      },
      {
        "name": "PhoneNumber",
        "desc": "手机号码"
      },
      {
        "name": "MailCode",
        "desc": "邮箱验证码"
      },
      {
        "name": "Mail",
        "desc": "邮箱"
      },
      {
        "name": "CountryCode",
        "desc": "手机国码"
      }
    ],
    "desc": "校验新手机新邮箱接口"
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
  "SetFlag": {
    "params": [
      {
        "name": "OpUin",
        "desc": "设置用户的uin"
      },
      {
        "name": "LoginFlag",
        "desc": "登录设置"
      },
      {
        "name": "ActionFlag",
        "desc": "敏感操作设置"
      },
      {
        "name": "OffsiteFlag",
        "desc": "异地登录设置"
      },
      {
        "name": "NeedResetMfa",
        "desc": "是否需要重置mfa"
      }
    ],
    "desc": "设置用户的登录保护和敏感操作校验方式"
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
  "DetectMaskAuth": {
    "params": [
      {
        "name": "Skey",
        "desc": "登录态Skey"
      },
      {
        "name": "ClientIP",
        "desc": "IP"
      },
      {
        "name": "ClientUA",
        "desc": "浏览器UA"
      },
      {
        "name": "Type",
        "desc": "人脸类型"
      },
      {
        "name": "Name",
        "desc": "用户名称"
      },
      {
        "name": "Idcard",
        "desc": "用户Idcard"
      },
      {
        "name": "OwnerUin",
        "desc": "主账号"
      }
    ],
    "desc": "获取并更新人脸核身校验状态实名传递参数比对"
  },
  "DetectAuth": {
    "params": [
      {
        "name": "Skey",
        "desc": "登录态Skey"
      },
      {
        "name": "ClientIP",
        "desc": "IP"
      },
      {
        "name": "ClientUA",
        "desc": "浏览器UA"
      },
      {
        "name": "Type",
        "desc": "人脸类型"
      },
      {
        "name": "Name",
        "desc": "名称"
      },
      {
        "name": "Idcard",
        "desc": "身份证号"
      },
      {
        "name": "UseAuthInfo",
        "desc": "是否使用用户提交信息"
      },
      {
        "name": "Scene",
        "desc": "场景"
      },
      {
        "name": "OwnerUin",
        "desc": "主账号uin"
      }
    ],
    "desc": "发起人脸核身"
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
  }
}