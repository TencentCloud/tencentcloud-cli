**Example 1: 查询企业扩展服务授权详情-自动签**



Input: 

```
tccli ess DescribeExtendedServiceAuthDetail --cli-unfold-argument  \
    --Operator.UserId yDwf3UUckps8dvveUEfH3DjvMmg3ZkjQ \
    --ExtendServiceType OPEN_SERVER_SIGN \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "AuthInfoDetail": {
            "AuthOrganizationTotal": 1,
            "AuthUserTotal": 1,
            "HasAuthOrganizationList": [
                {
                    "AuthorizeTime": 1689129513,
                    "AuthorizedOrganizationId": "yDwf3xxxxxxxxxxxFOE0qLixm",
                    "AuthorizedOrganizationName": "xxxxx有限责任公司",
                    "OrganizationId": "yDR0MUxxxxxxxxxxxxxxJAuJ4xN",
                    "OrganizationName": "xxx公司",
                    "TemplateId": "yDwxxxxxxxxtSqKhFvy",
                    "TemplateName": "B2B 双方静默签署"
                }
            ],
            "HasAuthUserList": [
                {
                    "BelongTo": "CurrentOrg",
                    "MainOrganizationId": "",
                    "UserId": "yDxjKxxxxxxxx4zjESzn1dvkm5"
                }
            ],
            "Name": "企业静默签（自动签署）",
            "Type": "OPEN_SERVER_SIGN"
        },
        "RequestId": "d03c95cb-82f4-488a-a832-4ced6e367a54"
    }
}
```

**Example 2: 查询企业扩展服务授权详情-批量签署**



Input: 

```
tccli ess DescribeExtendedServiceAuthDetail --cli-unfold-argument  \
    --Operator.UserId yDwf3UUckps8dvveUEfH3DjvMmg3ZkjQ \
    --ExtendServiceType OPEN_SERVER_SIGN \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "AuthInfoDetail": {
            "AuthOrganizationTotal": 0,
            "AuthUserTotal": 1,
            "HasAuthOrganizationList": [],
            "HasAuthUserList": [
                {
                    "BelongTo": "CurrentOrg",
                    "MainOrganizationId": "",
                    "UserId": "yDxjKxxxxxxxx4zjESzn1dvkm5"
                }
            ],
            "Name": "批量签署",
            "Type": "BATCH_SIGN"
        },
        "RequestId": "d03c95cb-82f4-488a-a832-4ced6e367a54"
    }
}
```

