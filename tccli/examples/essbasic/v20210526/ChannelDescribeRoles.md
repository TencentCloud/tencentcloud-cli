**Example 1: 查询角色列表**

IsReturnPermissionGroup设置为0表示不返回角色对应的权限树信息

Input: 

```
tccli essbasic ChannelDescribeRoles --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId  \
    --Limit 10 \
    --Filters.0.Key IsReturnPermissionGroup \
    --Filters.0.Values 0
```

Output: 
```
{
    "Response": {
        "Offset": 1,
        "Limit": 10,
        "TotalCount": 1,
        "ChannelRoles": [
            {
                "RoleId": "abc8jkkjds***121212",
                "RoleName": "业务管理员",
                "RoleStatus": 1
            }
        ],
        "RequestId": " s19ksdjkkds****ldsjfkdfdf"
    }
}
```

**Example 2: 查询角色列表（返回权限树信息）**

1. IsReturnPermissionGroup设置为1表示返回角色对应的权限树信息
2. RoleType设置为2表示只拉取自己创建的角色列表

Input: 

```
tccli essbasic ChannelDescribeRoles --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId  \
    --Limit 10 \
    --Filters.0.Key RoleType \
    --Filters.0.Values 1 \
    --Filters.1.Key IsReturnPermissionGroup \
    --Filters.1.Values 1
```

Output: 
```
{
    "Response": {
        "Offset": 0,
        "Limit": 10,
        "TotalCount": 1,
        "ChannelRoles": [
            {
                "RoleId": "69997f600a7c8e9accc71f4241a8a091",
                "RoleName": "类管理员角色",
                "RoleStatus": 1,
                "PermissionGroups": [
                    {
                        "GroupName": "费用中心",
                        "GroupKey": "bill",
                        "Hide": 0,
                        "Permissions": [
                            {
                                "Name": "费用管理",
                                "Key": "BillManagement",
                                "Type": 1,
                                "Hide": 0,
                                "DataLabel": 0,
                                "DataType": 0,
                                "DataRange": 0,
                                "DataTo": "",
                                "ParentKey": "",
                                "IsChecked": true,
                                "Children": [
                                    {
                                        "Name": "订单管理",
                                        "Key": "BillOrderManagement",
                                        "Type": 2,
                                        "Hide": 1,
                                        "DataLabel": 0,
                                        "DataType": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "ParentKey": "",
                                        "IsChecked": true,
                                        "Children": []
                                    },
                                    {
                                        "Name": "套餐管理",
                                        "Key": "BillSetMealManagement",
                                        "Type": 2,
                                        "Hide": 1,
                                        "DataLabel": 0,
                                        "DataType": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "ParentKey": "",
                                        "IsChecked": true,
                                        "Children": []
                                    },
                                    {
                                        "Name": "发票管理",
                                        "Key": "BillInvoiceManagement",
                                        "Type": 2,
                                        "Hide": 1,
                                        "DataLabel": 0,
                                        "DataType": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "ParentKey": "",
                                        "IsChecked": true,
                                        "Children": []
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "GroupName": "开发者中心",
                        "GroupKey": "channel",
                        "Hide": 0,
                        "Permissions": [
                            {
                                "Name": "渠道模板控件管理",
                                "Key": "WidgetManagement",
                                "Type": 1,
                                "Hide": 0,
                                "DataLabel": 0,
                                "DataType": 0,
                                "DataRange": 0,
                                "DataTo": "",
                                "ParentKey": "",
                                "IsChecked": true,
                                "Children": [
                                    {
                                        "Name": "渠道控件查看",
                                        "Key": "DescribeChannelComponents",
                                        "Type": 2,
                                        "Hide": 1,
                                        "DataLabel": 0,
                                        "DataType": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "ParentKey": "",
                                        "IsChecked": true,
                                        "Children": []
                                    },
                                    {
                                        "Name": "渠道控件编辑",
                                        "Key": "InsertOrModifyChannelComponents",
                                        "Type": 2,
                                        "Hide": 1,
                                        "DataLabel": 0,
                                        "DataType": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "ParentKey": "",
                                        "IsChecked": true,
                                        "Children": []
                                    },
                                    {
                                        "Name": "渠道控件删除",
                                        "Key": "DeleteChannelComponents",
                                        "Type": 2,
                                        "Hide": 1,
                                        "DataLabel": 0,
                                        "DataType": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "ParentKey": "",
                                        "IsChecked": true,
                                        "Children": []
                                    }
                                ]
                            },
                            {
                                "Name": "渠道模板库管理",
                                "Key": "ChannelTemplateManagement",
                                "Type": 1,
                                "Hide": 0,
                                "DataLabel": 0,
                                "DataType": 0,
                                "DataRange": 0,
                                "DataTo": "",
                                "ParentKey": "",
                                "IsChecked": true,
                                "Children": [
                                    {
                                        "Name": "渠道模板库查看",
                                        "Key": "DescribeChannelTemplate",
                                        "Type": 2,
                                        "Hide": 1,
                                        "DataLabel": 0,
                                        "DataType": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "ParentKey": "",
                                        "IsChecked": true,
                                        "Children": []
                                    },
                                    {
                                        "Name": "渠道模板库编辑",
                                        "Key": "InsertOrModifyChannelTemplate",
                                        "Type": 2,
                                        "Hide": 1,
                                        "DataLabel": 0,
                                        "DataType": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "ParentKey": "",
                                        "IsChecked": true,
                                        "Children": []
                                    },
                                    {
                                        "Name": "渠道模板库删除",
                                        "Key": "DeleteChannelTemplate",
                                        "Type": 2,
                                        "Hide": 1,
                                        "DataLabel": 0,
                                        "DataType": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "ParentKey": "",
                                        "IsChecked": true,
                                        "Children": []
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "GroupName": "拓展服务",
                        "GroupKey": "ExpandService",
                        "Hide": 0,
                        "Permissions": [
                            {
                                "Name": "合同相关",
                                "Key": "FlowRelatedManagement",
                                "Type": 1,
                                "Hide": 0,
                                "DataLabel": 0,
                                "DataType": 0,
                                "DataRange": 0,
                                "DataTo": "",
                                "ParentKey": "",
                                "IsChecked": true,
                                "Children": [
                                    {
                                        "Name": "企业自动签署",
                                        "Key": "CompanyAutoSign",
                                        "Type": 1,
                                        "Hide": 0,
                                        "DataLabel": 0,
                                        "DataType": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "ParentKey": "",
                                        "IsChecked": true,
                                        "Children": []
                                    },
                                    {
                                        "Name": "批量签署授权",
                                        "Key": "BatchSignAccredit",
                                        "Type": 1,
                                        "Hide": 0,
                                        "DataLabel": 0,
                                        "DataType": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "ParentKey": "",
                                        "IsChecked": true,
                                        "Children": []
                                    },
                                    {
                                        "Name": "企业与港澳台居民签署合同",
                                        "Key": "OverseasSign",
                                        "Type": 1,
                                        "Hide": 0,
                                        "DataLabel": 0,
                                        "DataType": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "ParentKey": "",
                                        "IsChecked": true,
                                        "Children": []
                                    },
                                    {
                                        "Name": "拓宽签署方年龄限制",
                                        "Key": "ExpandSignAgeLimit",
                                        "Type": 1,
                                        "Hide": 0,
                                        "DataLabel": 0,
                                        "DataType": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "ParentKey": "",
                                        "IsChecked": true,
                                        "Children": []
                                    },
                                    {
                                        "Name": "个人签署方仅校验手机号",
                                        "Key": "SignatoryMobileVerify",
                                        "Type": 1,
                                        "Hide": 0,
                                        "DataLabel": 0,
                                        "DataType": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "ParentKey": "",
                                        "IsChecked": true,
                                        "Children": []
                                    },
                                    {
                                        "Name": "隐藏合同经办人姓名",
                                        "Key": "HideFlowOperatorName",
                                        "Type": 1,
                                        "Hide": 0,
                                        "DataLabel": 0,
                                        "DataType": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "ParentKey": "",
                                        "IsChecked": true,
                                        "Children": []
                                    }
                                ]
                            },
                            {
                                "Name": "印章相关",
                                "Key": "SealRelatedManagement",
                                "Type": 1,
                                "Hide": 0,
                                "DataLabel": 0,
                                "DataType": 0,
                                "DataRange": 0,
                                "DataTo": "",
                                "ParentKey": "",
                                "IsChecked": true,
                                "Children": [
                                    {
                                        "Name": "骑缝章",
                                        "Key": "PagingSeal",
                                        "Type": 1,
                                        "Hide": 0,
                                        "DataLabel": 0,
                                        "DataType": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "ParentKey": "",
                                        "IsChecked": true,
                                        "Children": []
                                    }
                                ]
                            },
                            {
                                "Name": "模板相关",
                                "Key": "TemplateRelatedManagement",
                                "Type": 1,
                                "Hide": 1,
                                "DataLabel": 0,
                                "DataType": 0,
                                "DataRange": 0,
                                "DataTo": "",
                                "ParentKey": "",
                                "IsChecked": true,
                                "Children": []
                            },
                            {
                                "Name": "审批相关",
                                "Key": "ApprovalRelatedManagement",
                                "Type": 1,
                                "Hide": 0,
                                "DataLabel": 0,
                                "DataType": 0,
                                "DataRange": 0,
                                "DataTo": "",
                                "ParentKey": "",
                                "IsChecked": true,
                                "Children": [
                                    {
                                        "Name": "审批流配置",
                                        "Key": "ApprovalFlowConfig",
                                        "Type": 1,
                                        "Hide": 0,
                                        "DataLabel": 0,
                                        "DataType": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "ParentKey": "",
                                        "IsChecked": true,
                                        "Children": []
                                    }
                                ]
                            },
                            {
                                "Name": "其它拓展服务",
                                "Key": "OtherExpandManagement",
                                "Type": 1,
                                "Hide": 0,
                                "DataLabel": 0,
                                "DataType": 0,
                                "DataRange": 0,
                                "DataTo": "",
                                "ParentKey": "",
                                "IsChecked": true,
                                "Children": [
                                    {
                                        "Name": "企业CA证书配置",
                                        "Key": "CompanyCAConfig",
                                        "Type": 1,
                                        "Hide": 0,
                                        "DataLabel": 0,
                                        "DataType": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "ParentKey": "",
                                        "IsChecked": true,
                                        "Children": []
                                    },
                                    {
                                        "Name": "下载企业合同/文件授权",
                                        "Key": "AuthProxyOrgDownLoadFlow",
                                        "Type": 1,
                                        "Hide": 0,
                                        "DataLabel": 0,
                                        "DataType": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "ParentKey": "",
                                        "IsChecked": true,
                                        "Children": []
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "GroupName": "合同中心",
                        "GroupKey": "Flow",
                        "Hide": 0,
                        "Permissions": [
                            {
                                "Name": "查询合同",
                                "Key": "FlowsManagement",
                                "Type": 1,
                                "Hide": 0,
                                "DataLabel": 1,
                                "DataType": 2,
                                "DataRange": 0,
                                "DataTo": "",
                                "ParentKey": "",
                                "IsChecked": true,
                                "Children": [
                                    {
                                        "Name": "企业全部合同",
                                        "Key": "DescribeAllFlows",
                                        "Type": 2,
                                        "Hide": 0,
                                        "DataLabel": 2,
                                        "DataType": 0,
                                        "DataRange": 1,
                                        "DataTo": "",
                                        "ParentKey": "FlowsManagement",
                                        "IsChecked": true,
                                        "Children": []
                                    }
                                ]
                            },
                            {
                                "Name": "合同详情&预览",
                                "Key": "FlowsManagement-Preview",
                                "Type": 1,
                                "Hide": 0,
                                "DataLabel": 1,
                                "DataType": 1,
                                "DataRange": 0,
                                "DataTo": "FlowsManagement",
                                "ParentKey": "",
                                "IsChecked": true,
                                "Children": []
                            },
                            {
                                "Name": "下载合同",
                                "Key": "FlowsManagement-Download",
                                "Type": 1,
                                "Hide": 0,
                                "DataLabel": 1,
                                "DataType": 1,
                                "DataRange": 0,
                                "DataTo": "FlowsManagement",
                                "ParentKey": "",
                                "IsChecked": true,
                                "Children": []
                            },
                            {
                                "Name": "发起合同",
                                "Key": "CreateFlow",
                                "Type": 2,
                                "Hide": 0,
                                "DataLabel": 0,
                                "DataType": 0,
                                "DataRange": 0,
                                "DataTo": "",
                                "ParentKey": "",
                                "IsChecked": true,
                                "Children": [
                                    {
                                        "Name": "上传文件发起",
                                        "Key": "FlowByImportedFile",
                                        "Type": 2,
                                        "Hide": 0,
                                        "DataLabel": 0,
                                        "DataType": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "ParentKey": "",
                                        "IsChecked": true,
                                        "Children": []
                                    },
                                    {
                                        "Name": "企业模版发起",
                                        "Key": "FlowByOrganizationTemplate",
                                        "Type": 1,
                                        "Hide": 0,
                                        "DataLabel": 0,
                                        "DataType": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "ParentKey": "",
                                        "IsChecked": true,
                                        "Children": []
                                    },
                                    {
                                        "Name": "创建签署二维码",
                                        "Key": "CreateMultiFlowSignQRCode",
                                        "Type": 1,
                                        "Hide": 0,
                                        "DataLabel": 0,
                                        "DataType": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "ParentKey": "",
                                        "IsChecked": true,
                                        "Children": []
                                    }
                                ]
                            },
                            {
                                "Name": "领取合同",
                                "Key": "FlowsManagement-Pickup",
                                "Type": 1,
                                "Hide": 1,
                                "DataLabel": 0,
                                "DataType": 0,
                                "DataRange": 0,
                                "DataTo": "",
                                "ParentKey": "",
                                "IsChecked": true,
                                "Children": []
                            },
                            {
                                "Name": "撤销合同",
                                "Key": "CancelFlow",
                                "Type": 2,
                                "Hide": 0,
                                "DataLabel": 0,
                                "DataType": 0,
                                "DataRange": 0,
                                "DataTo": "",
                                "ParentKey": "",
                                "IsChecked": true,
                                "Children": []
                            },
                            {
                                "Name": "申请签署报告",
                                "Key": "ApplyEvidenceReport",
                                "Type": 1,
                                "Hide": 0,
                                "DataLabel": 0,
                                "DataType": 0,
                                "DataRange": 0,
                                "DataTo": "",
                                "ParentKey": "",
                                "IsChecked": true,
                                "Children": []
                            }
                        ]
                    },
                    {
                        "GroupName": "组织员工",
                        "GroupKey": "Organization",
                        "Hide": 0,
                        "Permissions": [
                            {
                                "Name": "组织架构管理",
                                "Key": "OrgManagement",
                                "Type": 1,
                                "Hide": 0,
                                "DataLabel": 0,
                                "DataType": 0,
                                "DataRange": 0,
                                "DataTo": "",
                                "ParentKey": "",
                                "IsChecked": true,
                                "Children": [
                                    {
                                        "Name": "为员工分配角色",
                                        "Key": "CreateUserRoles",
                                        "Type": 2,
                                        "Hide": 1,
                                        "DataLabel": 0,
                                        "DataType": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "ParentKey": "",
                                        "IsChecked": true,
                                        "Children": []
                                    },
                                    {
                                        "Name": "编辑组织架构",
                                        "Key": "ModifyYuFuOrg",
                                        "Type": 1,
                                        "Hide": 1,
                                        "DataLabel": 0,
                                        "DataType": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "ParentKey": "",
                                        "IsChecked": true,
                                        "Children": []
                                    }
                                ]
                            },
                            {
                                "Name": "角色管理",
                                "Key": "RoleManagement",
                                "Type": 1,
                                "Hide": 0,
                                "DataLabel": 0,
                                "DataType": 0,
                                "DataRange": 0,
                                "DataTo": "",
                                "ParentKey": "",
                                "IsChecked": true,
                                "Children": [
                                    {
                                        "Name": "创建角色",
                                        "Key": "CreateRole",
                                        "Type": 2,
                                        "Hide": 1,
                                        "DataLabel": 0,
                                        "DataType": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "ParentKey": "",
                                        "IsChecked": true,
                                        "Children": []
                                    },
                                    {
                                        "Name": "修改角色",
                                        "Key": "ModifyRole",
                                        "Type": 2,
                                        "Hide": 1,
                                        "DataLabel": 0,
                                        "DataType": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "ParentKey": "",
                                        "IsChecked": true,
                                        "Children": []
                                    },
                                    {
                                        "Name": "删除角色",
                                        "Key": "DeleteRole",
                                        "Type": 2,
                                        "Hide": 1,
                                        "DataLabel": 0,
                                        "DataType": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "ParentKey": "",
                                        "IsChecked": true,
                                        "Children": []
                                    },
                                    {
                                        "Name": "启用&禁用角色",
                                        "Key": "ModifyRoleStatus",
                                        "Type": 2,
                                        "Hide": 1,
                                        "DataLabel": 0,
                                        "DataType": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "ParentKey": "",
                                        "IsChecked": true,
                                        "Children": []
                                    },
                                    {
                                        "Name": "添加员工",
                                        "Key": "CreateRoleUsers",
                                        "Type": 2,
                                        "Hide": 1,
                                        "DataLabel": 0,
                                        "DataType": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "ParentKey": "",
                                        "IsChecked": true,
                                        "Children": []
                                    },
                                    {
                                        "Name": "取消关联",
                                        "Key": "DeleteRoleUsers",
                                        "Type": 2,
                                        "Hide": 1,
                                        "DataLabel": 0,
                                        "DataType": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "ParentKey": "",
                                        "IsChecked": true,
                                        "Children": []
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "GroupName": "印章中心",
                        "GroupKey": "Seal",
                        "Hide": 0,
                        "Permissions": [
                            {
                                "Name": "我持有企业印章",
                                "Key": "SealManagement-Hold",
                                "Type": 1,
                                "Hide": 0,
                                "DataLabel": 0,
                                "DataType": 0,
                                "DataRange": 0,
                                "DataTo": "",
                                "ParentKey": "",
                                "IsChecked": true,
                                "Children": [
                                    {
                                        "Name": "查询印章",
                                        "Key": "QueryHoldSeal",
                                        "Type": 2,
                                        "Hide": 1,
                                        "DataLabel": 0,
                                        "DataType": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "ParentKey": "",
                                        "IsChecked": true,
                                        "Children": []
                                    }
                                ]
                            },
                            {
                                "Name": "印章管理",
                                "Key": "SealManagement",
                                "Type": 1,
                                "Hide": 0,
                                "DataLabel": 0,
                                "DataType": 0,
                                "DataRange": 0,
                                "DataTo": "",
                                "ParentKey": "",
                                "IsChecked": true,
                                "Children": [
                                    {
                                        "Name": "查询印章",
                                        "Key": "SealManagement-Manage-Detail",
                                        "Type": 2,
                                        "Hide": 0,
                                        "DataLabel": 0,
                                        "DataType": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "ParentKey": "",
                                        "IsChecked": true,
                                        "Children": [
                                            {
                                                "Name": "授权记录",
                                                "Key": "SealManagement-Manage-Detail-Holder",
                                                "Type": 2,
                                                "Hide": 1,
                                                "DataLabel": 0,
                                                "DataType": 0,
                                                "DataRange": 0,
                                                "DataTo": "",
                                                "ParentKey": "",
                                                "IsChecked": true,
                                                "Children": []
                                            },
                                            {
                                                "Name": "关联模版",
                                                "Key": "SealManagement-Manage-Detail-Holder-Template",
                                                "Type": 2,
                                                "Hide": 1,
                                                "DataLabel": 0,
                                                "DataType": 0,
                                                "DataRange": 0,
                                                "DataTo": "",
                                                "ParentKey": "",
                                                "IsChecked": true,
                                                "Children": []
                                            },
                                            {
                                                "Name": "用印记录",
                                                "Key": "SealManagement-Manage-Detail-Holder-Use-Record",
                                                "Type": 2,
                                                "Hide": 1,
                                                "DataLabel": 0,
                                                "DataType": 0,
                                                "DataRange": 0,
                                                "DataTo": "",
                                                "ParentKey": "",
                                                "IsChecked": true,
                                                "Children": []
                                            },
                                            {
                                                "Name": "变更记录",
                                                "Key": "SealManagement-Manage-Detail-Holder-Change-Record",
                                                "Type": 1,
                                                "Hide": 1,
                                                "DataLabel": 0,
                                                "DataType": 0,
                                                "DataRange": 0,
                                                "DataTo": "",
                                                "ParentKey": "",
                                                "IsChecked": true,
                                                "Children": []
                                            }
                                        ]
                                    },
                                    {
                                        "Name": "创建印章",
                                        "Key": "CreateSeal",
                                        "Type": 2,
                                        "Hide": 0,
                                        "DataLabel": 0,
                                        "DataType": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "ParentKey": "",
                                        "IsChecked": true,
                                        "Children": [
                                            {
                                                "Name": "新建印章-模版印章",
                                                "Key": "SealManagement-Manage-Create-Template",
                                                "Type": 1,
                                                "Hide": 1,
                                                "DataLabel": 0,
                                                "DataType": 0,
                                                "DataRange": 0,
                                                "DataTo": "",
                                                "ParentKey": "",
                                                "IsChecked": true,
                                                "Children": []
                                            },
                                            {
                                                "Name": "新建印章-本地上传",
                                                "Key": "SealManagement-Manage-Create-Upload",
                                                "Type": 1,
                                                "Hide": 1,
                                                "DataLabel": 0,
                                                "DataType": 0,
                                                "DataRange": 0,
                                                "DataTo": "",
                                                "ParentKey": "",
                                                "IsChecked": true,
                                                "Children": []
                                            }
                                        ]
                                    },
                                    {
                                        "Name": "修改印章",
                                        "Key": "ModifySeal",
                                        "Type": 2,
                                        "Hide": 0,
                                        "DataLabel": 0,
                                        "DataType": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "ParentKey": "",
                                        "IsChecked": true,
                                        "Children": []
                                    },
                                    {
                                        "Name": "分配印章管理人",
                                        "Key": "CreateSealPolicy",
                                        "Type": 2,
                                        "Hide": 0,
                                        "DataLabel": 0,
                                        "DataType": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "ParentKey": "",
                                        "IsChecked": true,
                                        "Children": []
                                    },
                                    {
                                        "Name": "删除印章",
                                        "Key": "DeleteSeal",
                                        "Type": 2,
                                        "Hide": 0,
                                        "DataLabel": 0,
                                        "DataType": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "ParentKey": "",
                                        "IsChecked": true,
                                        "Children": []
                                    },
                                    {
                                        "Name": "单次用印审批",
                                        "Key": "ApplySealOnce",
                                        "Type": 2,
                                        "Hide": 0,
                                        "DataLabel": 0,
                                        "DataType": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "ParentKey": "",
                                        "IsChecked": true,
                                        "Children": []
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "GroupName": "模板中心",
                        "GroupKey": "Template",
                        "Hide": 0,
                        "Permissions": [
                            {
                                "Name": "模板管理",
                                "Key": "TemplateManagement",
                                "Type": 1,
                                "Hide": 0,
                                "DataLabel": 0,
                                "DataType": 0,
                                "DataRange": 0,
                                "DataTo": "",
                                "ParentKey": "",
                                "IsChecked": true,
                                "Children": [
                                    {
                                        "Name": "查询模板",
                                        "Key": "TemplateManagement-Query",
                                        "Type": 1,
                                        "Hide": 0,
                                        "DataLabel": 0,
                                        "DataType": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "ParentKey": "",
                                        "IsChecked": true,
                                        "Children": []
                                    },
                                    {
                                        "Name": "官方模板收藏",
                                        "Key": "OfficialFlowTemplateCollection",
                                        "Type": 1,
                                        "Hide": 0,
                                        "DataLabel": 0,
                                        "DataType": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "ParentKey": "",
                                        "IsChecked": true,
                                        "Children": []
                                    },
                                    {
                                        "Name": "下载模板",
                                        "Key": "TemplateManagement-Download",
                                        "Type": 1,
                                        "Hide": 0,
                                        "DataLabel": 0,
                                        "DataType": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "ParentKey": "",
                                        "IsChecked": true,
                                        "Children": []
                                    },
                                    {
                                        "Name": "创建模板",
                                        "Key": "TemplateManagement-Create",
                                        "Type": 1,
                                        "Hide": 0,
                                        "DataLabel": 0,
                                        "DataType": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "ParentKey": "",
                                        "IsChecked": true,
                                        "Children": []
                                    },
                                    {
                                        "Name": "删除模板",
                                        "Key": "DeleteFlowTemplates",
                                        "Type": 2,
                                        "Hide": 0,
                                        "DataLabel": 0,
                                        "DataType": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "ParentKey": "",
                                        "IsChecked": true,
                                        "Children": []
                                    },
                                    {
                                        "Name": "编辑模板",
                                        "Key": "ModifyFlowTemplate",
                                        "Type": 2,
                                        "Hide": 0,
                                        "DataLabel": 0,
                                        "DataType": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "ParentKey": "",
                                        "IsChecked": true,
                                        "Children": []
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ],
        "RequestId": "cb9c33e8-2870-42ea-b798-b9fbd4756827"
    }
}
```

