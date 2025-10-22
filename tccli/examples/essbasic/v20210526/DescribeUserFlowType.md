**Example 1: 查询用户合同类型（不指定filter）**

查询用户合同类型（不指定filter）

Input: 

```
tccli essbasic DescribeUserFlowType --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId 
```

Output: 
```
{
    "Response": {
        "AllUserFlowTypes": [
            {
                "Description": "",
                "Name": "单方合同",
                "TemplateNum": 0,
                "UserFlowTypeId": "yDwXXUUckp19hvn8URxp4X6wVwCLodxJ"
            }
        ],
        "RequestId": "s1741681654595707818"
    }
}
```

**Example 2: 查询用户合同类型（不指定查询绑定模板的合同类型）**

查询用户合同类型（不指定查询绑定模板的合同类型）

Input: 

```
tccli essbasic DescribeUserFlowType --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId  \
    --QueryBindTemplate False
```

Output: 
```
{
    "Response": {
        "AllUserFlowTypes": [
            {
                "Description": "",
                "Name": "单方合同",
                "TemplateNum": 0,
                "UserFlowTypeId": "yDwXXUUckp19hvn8URxp4X6wVwCLodxJ"
            }
        ],
        "RequestId": "s1741681654595707818"
    }
}
```

**Example 3: 查询用户合同类型（指定查询绑定模板的合同类型）**

查询用户合同类型（指定查询绑定模板的合同类型）

Input: 

```
tccli essbasic DescribeUserFlowType --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId  \
    --QueryBindTemplate True
```

Output: 
```
{
    "Response": {
        "AllUserFlowTypes": [
            {
                "Description": "",
                "Name": "单方合同",
                "TemplateNum": 10,
                "UserFlowTypeId": "yDwXXUUckp19hvn8URxp4X6wVwCLodxJ"
            }
        ],
        "RequestId": "s1741681654595707818"
    }
}
```

**Example 4: 查询用户合同类型（指定用户模板id）**

查询用户合同类型（指定用户模板id）

Input: 

```
tccli essbasic DescribeUserFlowType --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId  \
    --Filters.0.Key user-flow-type-id \
    --Filters.0.Values yDwXXUUckp19hvn8URxp4X6wVwCLodxJ \
    --QueryBindTemplate True
```

Output: 
```
{
    "Response": {
        "AllUserFlowTypes": [
            {
                "Description": "",
                "Name": "单方合同",
                "TemplateNum": 10,
                "UserFlowTypeId": "yDwXXUUckp19hvn8URxp4X6wVwCLodxJ"
            }
        ],
        "RequestId": "s1741681654595707818"
    }
}
```

