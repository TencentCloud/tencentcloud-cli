**Example 1: 查询企业扩展服务授权详情-批量签署**



Input: 

```
tccli essbasic DescribeExtendedServiceAuthDetail --cli-unfold-argument  \
    --Agent.AppId yDxjsxxxxxxxxxxxxxxMOX9y \
    --Agent.ProxyOrganizationOpenId open_id_test \
    --Agent.ProxyOperator.OpenId user_open_id \
    --ExtendServiceType BATCH_SIGN \
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
                    "OpenId": "us-user_open_id"
                }
            ],
            "Name": "批量签署",
            "Type": "BATCH_SIGN"
        },
        "RequestId": "s1699xxxxxxx898950"
    }
}
```

**Example 2: 查询企业扩展服务授权详情- 企业自动签**



Input: 

```
tccli essbasic DescribeExtendedServiceAuthDetail --cli-unfold-argument  \
    --Agent.AppId yDxjsxxxxxxxxxxxxxxMOX9y \
    --Agent.ProxyOrganizationOpenId open_id_test \
    --Agent.ProxyOperator.OpenId user_open_id \
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
                    "AuthorizeTime": 1682521720,
                    "AuthorizedOrganizationName": "xxxx有限公司",
                    "AuthorizedOrganizationOpenId": "org_open_id",
                    "OrganizationName": "xxxxxx有限公司",
                    "OrganizationOpenId": "org_open_id"
                }
            ],
            "HasAuthUserList": [
                {
                    "OpenId": "us-user_open_id"
                }
            ],
            "Name": "企业静默签（自动签署）",
            "Type": "OPEN_SERVER_SIGN"
        },
        "RequestId": "s1699xxxxxxx898950"
    }
}
```

