**Example 1: 查询角色列表**

查询角色列表，默认不返回角色对应的权限树信息

Input: 

```
tccli essbasic ChannelDescribeRoles --cli-unfold-argument  \
    --Agent.AppId  jsdk812kxkdfjks***k88123123 \
    --Agent.ProxyOrganizationOpenId test_org_openid \
    --Agent.ProxyOperator.OpenId test_openid \
    --Filters.0.Key  \
    --Filters.0.Values  \
    --Offset 1 \
    --Limit abc
```

Output: 
```
{
    "Response": {
        "Offset": 1,
        "Limit": 1,
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

查询角色列表，增加查询筛选条件“IsReturnPermissionGroup”，将返回角色对应的权限树信息

Input: 

```
tccli essbasic ChannelDescribeRoles --cli-unfold-argument  \
    --Agent.AppId  jsdk812kxkdfjks***k88123123 \
    --Agent.ProxyOrganizationOpenId test_org_openid \
    --Agent.ProxyOperator.OpenId test_openid \
    --Filters.0.Key IsReturnPermissionGroup \
    --Filters.0.Values 1 \
    --Offset 1 \
    --Limit abc
```

Output: 
```
{
    "Response": {
        "Offset": 1,
        "Limit": 1,
        "TotalCount": 1,
        "ChannelRoles": [
            {
                "RoleId": "abc8jkkjds***121212",
                "RoleName": "业务管理员",
                "RoleStatus": 1,
                "PermissionGroups": [
                    {
                        "GroupKey": "bill",
                        "GroupName": "费用中心",
                        "Hide": 0,
                        "Permissions": [
                            {
                                "Children": [
                                    {
                                        "Children": [],
                                        "DataLabel": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "DataType": 0,
                                        "Hide": 1,
                                        "IsChecked": false,
                                        "Key": "BillOrderManagement",
                                        "Name": "订单管理",
                                        "ParentKey": "",
                                        "Type": 2
                                    },
                                    {
                                        "Children": [],
                                        "DataLabel": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "DataType": 0,
                                        "Hide": 1,
                                        "IsChecked": false,
                                        "Key": "BillSetMealManagement",
                                        "Name": "套餐管理",
                                        "ParentKey": "",
                                        "Type": 2
                                    },
                                    {
                                        "Children": [],
                                        "DataLabel": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "DataType": 0,
                                        "Hide": 1,
                                        "IsChecked": false,
                                        "Key": "BillInvoiceManagement",
                                        "Name": "发票管理",
                                        "ParentKey": "",
                                        "Type": 2
                                    }
                                ],
                                "DataLabel": 0,
                                "DataRange": 0,
                                "DataTo": "",
                                "DataType": 0,
                                "Hide": 0,
                                "IsChecked": false,
                                "Key": "BillManagement",
                                "Name": "费用管理",
                                "ParentKey": "",
                                "Type": 1
                            }
                        ]
                    },
                    {
                        "GroupKey": "channel",
                        "GroupName": "开发者中心",
                        "Hide": 0,
                        "Permissions": [
                            {
                                "Children": [
                                    {
                                        "Children": [],
                                        "DataLabel": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "DataType": 0,
                                        "Hide": 1,
                                        "IsChecked": false,
                                        "Key": "DescribeChannelComponents",
                                        "Name": "渠道控件查看",
                                        "ParentKey": "",
                                        "Type": 2
                                    },
                                    {
                                        "Children": [],
                                        "DataLabel": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "DataType": 0,
                                        "Hide": 1,
                                        "IsChecked": false,
                                        "Key": "InsertOrModifyChannelComponents",
                                        "Name": "渠道控件编辑",
                                        "ParentKey": "",
                                        "Type": 2
                                    },
                                    {
                                        "Children": [],
                                        "DataLabel": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "DataType": 0,
                                        "Hide": 1,
                                        "IsChecked": false,
                                        "Key": "DeleteChannelComponents",
                                        "Name": "渠道控件删除",
                                        "ParentKey": "",
                                        "Type": 2
                                    }
                                ],
                                "DataLabel": 0,
                                "DataRange": 0,
                                "DataTo": "",
                                "DataType": 0,
                                "Hide": 0,
                                "IsChecked": false,
                                "Key": "WidgetManagement",
                                "Name": "渠道模板控件管理",
                                "ParentKey": "",
                                "Type": 1
                            },
                            {
                                "Children": [
                                    {
                                        "Children": [],
                                        "DataLabel": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "DataType": 0,
                                        "Hide": 1,
                                        "IsChecked": false,
                                        "Key": "DescribeChannelTemplate",
                                        "Name": "渠道模板库查看",
                                        "ParentKey": "",
                                        "Type": 2
                                    },
                                    {
                                        "Children": [],
                                        "DataLabel": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "DataType": 0,
                                        "Hide": 1,
                                        "IsChecked": false,
                                        "Key": "InsertOrModifyChannelTemplate",
                                        "Name": "渠道模板库编辑",
                                        "ParentKey": "",
                                        "Type": 2
                                    },
                                    {
                                        "Children": [],
                                        "DataLabel": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "DataType": 0,
                                        "Hide": 1,
                                        "IsChecked": false,
                                        "Key": "DeleteChannelTemplate",
                                        "Name": "渠道模板库删除",
                                        "ParentKey": "",
                                        "Type": 2
                                    }
                                ],
                                "DataLabel": 0,
                                "DataRange": 0,
                                "DataTo": "",
                                "DataType": 0,
                                "Hide": 0,
                                "IsChecked": false,
                                "Key": "ChannelTemplateManagement",
                                "Name": "渠道模板库管理",
                                "ParentKey": "",
                                "Type": 1
                            }
                        ]
                    },
                    {
                        "GroupKey": "Flow",
                        "GroupName": "合同中心",
                        "Hide": 0,
                        "Permissions": [
                            {
                                "Children": [
                                    {
                                        "Children": [],
                                        "DataLabel": 2,
                                        "DataRange": 1,
                                        "DataTo": "",
                                        "DataType": 0,
                                        "Hide": 0,
                                        "IsChecked": true,
                                        "Key": "DescribeAllFlows",
                                        "Name": "企业全部合同",
                                        "ParentKey": "FlowsManagement",
                                        "Type": 2
                                    }
                                ],
                                "DataLabel": 1,
                                "DataRange": 0,
                                "DataTo": "",
                                "DataType": 2,
                                "Hide": 0,
                                "IsChecked": true,
                                "Key": "FlowsManagement",
                                "Name": "查询合同",
                                "ParentKey": "",
                                "Type": 1
                            },
                            {
                                "Children": [],
                                "DataLabel": 1,
                                "DataRange": 0,
                                "DataTo": "FlowsManagement",
                                "DataType": 1,
                                "Hide": 0,
                                "IsChecked": true,
                                "Key": "FlowsManagement-Preview",
                                "Name": "合同详情&预览",
                                "ParentKey": "",
                                "Type": 1
                            },
                            {
                                "Children": [],
                                "DataLabel": 1,
                                "DataRange": 0,
                                "DataTo": "FlowsManagement",
                                "DataType": 1,
                                "Hide": 0,
                                "IsChecked": true,
                                "Key": "FlowsManagement-Download",
                                "Name": "下载合同",
                                "ParentKey": "",
                                "Type": 1
                            },
                            {
                                "Children": [
                                    {
                                        "Children": [],
                                        "DataLabel": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "DataType": 0,
                                        "Hide": 0,
                                        "IsChecked": true,
                                        "Key": "FlowByImportedFile",
                                        "Name": "上传文件发起",
                                        "ParentKey": "",
                                        "Type": 2
                                    },
                                    {
                                        "Children": [],
                                        "DataLabel": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "DataType": 0,
                                        "Hide": 0,
                                        "IsChecked": true,
                                        "Key": "FlowByOrganizationTemplate",
                                        "Name": "企业模版发起",
                                        "ParentKey": "",
                                        "Type": 1
                                    },
                                    {
                                        "Children": [],
                                        "DataLabel": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "DataType": 0,
                                        "Hide": 0,
                                        "IsChecked": true,
                                        "Key": "CreateMultiFlowSignQRCode",
                                        "Name": "创建签署二维码",
                                        "ParentKey": "",
                                        "Type": 1
                                    }
                                ],
                                "DataLabel": 0,
                                "DataRange": 0,
                                "DataTo": "",
                                "DataType": 0,
                                "Hide": 0,
                                "IsChecked": true,
                                "Key": "CreateFlow",
                                "Name": "发起合同",
                                "ParentKey": "",
                                "Type": 2
                            },
                            {
                                "Children": [],
                                "DataLabel": 0,
                                "DataRange": 0,
                                "DataTo": "",
                                "DataType": 0,
                                "Hide": 1,
                                "IsChecked": true,
                                "Key": "FlowsManagement-Pickup",
                                "Name": "领取合同",
                                "ParentKey": "",
                                "Type": 1
                            },
                            {
                                "Children": [],
                                "DataLabel": 0,
                                "DataRange": 0,
                                "DataTo": "",
                                "DataType": 0,
                                "Hide": 0,
                                "IsChecked": true,
                                "Key": "CancelFlow",
                                "Name": "撤销合同",
                                "ParentKey": "",
                                "Type": 2
                            }
                        ]
                    },
                    {
                        "GroupKey": "Organization",
                        "GroupName": "组织员工",
                        "Hide": 0,
                        "Permissions": [
                            {
                                "Children": [
                                    {
                                        "Children": [],
                                        "DataLabel": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "DataType": 0,
                                        "Hide": 1,
                                        "IsChecked": true,
                                        "Key": "CreateUserRoles",
                                        "Name": "为员工分配角色",
                                        "ParentKey": "",
                                        "Type": 2
                                    },
                                    {
                                        "Children": [],
                                        "DataLabel": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "DataType": 0,
                                        "Hide": 1,
                                        "IsChecked": true,
                                        "Key": "ModifyYuFuOrg",
                                        "Name": "编辑组织架构",
                                        "ParentKey": "",
                                        "Type": 1
                                    }
                                ],
                                "DataLabel": 0,
                                "DataRange": 0,
                                "DataTo": "",
                                "DataType": 0,
                                "Hide": 0,
                                "IsChecked": true,
                                "Key": "OrgManagement",
                                "Name": "组织架构管理",
                                "ParentKey": "",
                                "Type": 1
                            },
                            {
                                "Children": [
                                    {
                                        "Children": [],
                                        "DataLabel": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "DataType": 0,
                                        "Hide": 1,
                                        "IsChecked": false,
                                        "Key": "CreateRole",
                                        "Name": "创建角色",
                                        "ParentKey": "",
                                        "Type": 2
                                    },
                                    {
                                        "Children": [],
                                        "DataLabel": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "DataType": 0,
                                        "Hide": 1,
                                        "IsChecked": false,
                                        "Key": "ModifyRole",
                                        "Name": "修改角色",
                                        "ParentKey": "",
                                        "Type": 2
                                    },
                                    {
                                        "Children": [],
                                        "DataLabel": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "DataType": 0,
                                        "Hide": 1,
                                        "IsChecked": false,
                                        "Key": "DeleteRole",
                                        "Name": "删除角色",
                                        "ParentKey": "",
                                        "Type": 2
                                    },
                                    {
                                        "Children": [],
                                        "DataLabel": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "DataType": 0,
                                        "Hide": 1,
                                        "IsChecked": false,
                                        "Key": "ModifyRoleStatus",
                                        "Name": "启用&禁用角色",
                                        "ParentKey": "",
                                        "Type": 2
                                    },
                                    {
                                        "Children": [],
                                        "DataLabel": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "DataType": 0,
                                        "Hide": 1,
                                        "IsChecked": false,
                                        "Key": "CreateRoleUsers",
                                        "Name": "添加员工",
                                        "ParentKey": "",
                                        "Type": 2
                                    },
                                    {
                                        "Children": [],
                                        "DataLabel": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "DataType": 0,
                                        "Hide": 1,
                                        "IsChecked": false,
                                        "Key": "DeleteRoleUsers",
                                        "Name": "取消关联",
                                        "ParentKey": "",
                                        "Type": 2
                                    }
                                ],
                                "DataLabel": 0,
                                "DataRange": 0,
                                "DataTo": "",
                                "DataType": 0,
                                "Hide": 0,
                                "IsChecked": false,
                                "Key": "RoleManagement",
                                "Name": "角色管理",
                                "ParentKey": "",
                                "Type": 1
                            }
                        ]
                    },
                    {
                        "GroupKey": "Seal",
                        "GroupName": "印章中心",
                        "Hide": 0,
                        "Permissions": [
                            {
                                "Children": [
                                    {
                                        "Children": [],
                                        "DataLabel": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "DataType": 0,
                                        "Hide": 1,
                                        "IsChecked": true,
                                        "Key": "QueryHoldSeal",
                                        "Name": "查询印章",
                                        "ParentKey": "",
                                        "Type": 2
                                    }
                                ],
                                "DataLabel": 0,
                                "DataRange": 0,
                                "DataTo": "",
                                "DataType": 0,
                                "Hide": 0,
                                "IsChecked": true,
                                "Key": "SealManagement-Hold",
                                "Name": "我持有企业印章",
                                "ParentKey": "",
                                "Type": 1
                            },
                            {
                                "Children": [
                                    {
                                        "Children": [
                                            {
                                                "Children": [],
                                                "DataLabel": 0,
                                                "DataRange": 0,
                                                "DataTo": "",
                                                "DataType": 0,
                                                "Hide": 1,
                                                "IsChecked": true,
                                                "Key": "SealManagement-Manage-Detail-Holder",
                                                "Name": "授权记录",
                                                "ParentKey": "",
                                                "Type": 2
                                            },
                                            {
                                                "Children": [],
                                                "DataLabel": 0,
                                                "DataRange": 0,
                                                "DataTo": "",
                                                "DataType": 0,
                                                "Hide": 1,
                                                "IsChecked": true,
                                                "Key": "SealManagement-Manage-Detail-Holder-Template",
                                                "Name": "关联模版",
                                                "ParentKey": "",
                                                "Type": 2
                                            },
                                            {
                                                "Children": [],
                                                "DataLabel": 0,
                                                "DataRange": 0,
                                                "DataTo": "",
                                                "DataType": 0,
                                                "Hide": 1,
                                                "IsChecked": true,
                                                "Key": "SealManagement-Manage-Detail-Holder-Use-Record",
                                                "Name": "用印记录",
                                                "ParentKey": "",
                                                "Type": 2
                                            },
                                            {
                                                "Children": [],
                                                "DataLabel": 0,
                                                "DataRange": 0,
                                                "DataTo": "",
                                                "DataType": 0,
                                                "Hide": 1,
                                                "IsChecked": true,
                                                "Key": "SealManagement-Manage-Detail-Holder-Change-Record",
                                                "Name": "变更记录",
                                                "ParentKey": "",
                                                "Type": 1
                                            }
                                        ],
                                        "DataLabel": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "DataType": 0,
                                        "Hide": 0,
                                        "IsChecked": true,
                                        "Key": "SealManagement-Manage-Detail",
                                        "Name": "查询印章",
                                        "ParentKey": "",
                                        "Type": 2
                                    },
                                    {
                                        "Children": [
                                            {
                                                "Children": [],
                                                "DataLabel": 0,
                                                "DataRange": 0,
                                                "DataTo": "",
                                                "DataType": 0,
                                                "Hide": 1,
                                                "IsChecked": true,
                                                "Key": "SealManagement-Manage-Create-Template",
                                                "Name": "新建印章-模版印章",
                                                "ParentKey": "",
                                                "Type": 1
                                            },
                                            {
                                                "Children": [],
                                                "DataLabel": 0,
                                                "DataRange": 0,
                                                "DataTo": "",
                                                "DataType": 0,
                                                "Hide": 1,
                                                "IsChecked": true,
                                                "Key": "SealManagement-Manage-Create-Upload",
                                                "Name": "新建印章-本地上传",
                                                "ParentKey": "",
                                                "Type": 1
                                            }
                                        ],
                                        "DataLabel": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "DataType": 0,
                                        "Hide": 0,
                                        "IsChecked": true,
                                        "Key": "CreateSeal",
                                        "Name": "创建印章",
                                        "ParentKey": "",
                                        "Type": 2
                                    },
                                    {
                                        "Children": [],
                                        "DataLabel": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "DataType": 0,
                                        "Hide": 0,
                                        "IsChecked": true,
                                        "Key": "ModifySeal",
                                        "Name": "修改印章",
                                        "ParentKey": "",
                                        "Type": 2
                                    },
                                    {
                                        "Children": [],
                                        "DataLabel": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "DataType": 0,
                                        "Hide": 0,
                                        "IsChecked": true,
                                        "Key": "CreateSealPolicy",
                                        "Name": "分配印章管理人",
                                        "ParentKey": "",
                                        "Type": 2
                                    },
                                    {
                                        "Children": [],
                                        "DataLabel": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "DataType": 0,
                                        "Hide": 0,
                                        "IsChecked": true,
                                        "Key": "DeleteSeal",
                                        "Name": "删除印章",
                                        "ParentKey": "",
                                        "Type": 2
                                    },
                                    {
                                        "Children": [],
                                        "DataLabel": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "DataType": 0,
                                        "Hide": 0,
                                        "IsChecked": true,
                                        "Key": "ApplySealOnce",
                                        "Name": "单次用印审批",
                                        "ParentKey": "",
                                        "Type": 2
                                    }
                                ],
                                "DataLabel": 0,
                                "DataRange": 0,
                                "DataTo": "",
                                "DataType": 0,
                                "Hide": 0,
                                "IsChecked": true,
                                "Key": "SealManagement",
                                "Name": "印章管理",
                                "ParentKey": "",
                                "Type": 1
                            }
                        ]
                    },
                    {
                        "GroupKey": "Template",
                        "GroupName": "模板中心",
                        "Hide": 0,
                        "Permissions": [
                            {
                                "Children": [
                                    {
                                        "Children": [],
                                        "DataLabel": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "DataType": 0,
                                        "Hide": 0,
                                        "IsChecked": true,
                                        "Key": "TemplateManagement-Query",
                                        "Name": "查询模板",
                                        "ParentKey": "",
                                        "Type": 1
                                    },
                                    {
                                        "Children": [],
                                        "DataLabel": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "DataType": 0,
                                        "Hide": 0,
                                        "IsChecked": true,
                                        "Key": "OfficialFlowTemplateCollection",
                                        "Name": "官方模板收藏",
                                        "ParentKey": "",
                                        "Type": 1
                                    },
                                    {
                                        "Children": [],
                                        "DataLabel": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "DataType": 0,
                                        "Hide": 0,
                                        "IsChecked": true,
                                        "Key": "TemplateManagement-Download",
                                        "Name": "下载模板",
                                        "ParentKey": "",
                                        "Type": 1
                                    },
                                    {
                                        "Children": [],
                                        "DataLabel": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "DataType": 0,
                                        "Hide": 0,
                                        "IsChecked": true,
                                        "Key": "TemplateManagement-Create",
                                        "Name": "创建模板",
                                        "ParentKey": "",
                                        "Type": 1
                                    },
                                    {
                                        "Children": [],
                                        "DataLabel": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "DataType": 0,
                                        "Hide": 0,
                                        "IsChecked": true,
                                        "Key": "DeleteFlowTemplates",
                                        "Name": "删除模板",
                                        "ParentKey": "",
                                        "Type": 2
                                    },
                                    {
                                        "Children": [],
                                        "DataLabel": 0,
                                        "DataRange": 0,
                                        "DataTo": "",
                                        "DataType": 0,
                                        "Hide": 0,
                                        "IsChecked": true,
                                        "Key": "ModifyFlowTemplate",
                                        "Name": "编辑模板",
                                        "ParentKey": "",
                                        "Type": 2
                                    }
                                ],
                                "DataLabel": 0,
                                "DataRange": 0,
                                "DataTo": "",
                                "DataType": 0,
                                "Hide": 0,
                                "IsChecked": true,
                                "Key": "TemplateManagement",
                                "Name": "模板管理",
                                "ParentKey": "",
                                "Type": 1
                            }
                        ]
                    }
                ]
            }
        ],
        "RequestId": " s19ksdjkkds****ldsjfkdfdf"
    }
}
```

