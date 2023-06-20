**Example 1: 查询全部授权服务信息**

查询全部授权服务信息

Input: 

```
tccli ess DescribeExtendedServiceAuthInfos --cli-unfold-argument  \
    --Operator.UserId abc \
    --ExtendServiceType 
```

Output: 
```
{
    "Response": {
        "AuthInfoList": [
            {
                "HasAuthUserList": [
                    {
                        "BelongTo": "CurrentOrg",
                        "UserId": "userId1"
                    },
                    {
                        "BelongTo": "CurrentOrg",
                        "UserId": "userId2"
                    },
                    {
                        "BelongTo": "CurrentOrg",
                        "UserId": "userId3"
                    }
                ],
                "Name": "企业静默签（自动签署）",
                "OperateOn": 1681289048,
                "OperatorUserId": "OperatorUserId",
                "Status": "ENABLE",
                "Type": "OPEN_SERVER_SIGN"
            },
            {
                "Name": "企业与港澳台居民*签署合同",
                "OperateOn": 1667458840,
                "OperatorUserId": "OperatorUserId",
                "Status": "ENABLE",
                "Type": "OVERSEA_SIGN"
            },
            {
                "Name": "使用手机号验证签署方身份",
                "OperateOn": 0,
                "OperatorUserId": "",
                "Status": "ENABLE",
                "Type": "MOBILE_CHECK_APPROVER"
            },
            {
                "Name": "骑缝章",
                "OperateOn": 0,
                "OperatorUserId": "",
                "Status": "ENABLE",
                "Type": "PAGING_SEAL"
            },
            {
                "HasAuthUserList": [
                    {
                        "BelongTo": "CurrentOrg",
                        "UserId": "userId1"
                    },
                    {
                        "BelongTo": "CurrentOrg",
                        "UserId": "userId2"
                    },
                    {
                        "BelongTo": "CurrentOrg",
                        "UserId": "userId3"
                    }
                ],
                "Name": "批量签署",
                "OperateOn": 1667460697,
                "OperatorUserId": "OperatorUserId",
                "Status": "ENABLE",
                "Type": "BATCH_SIGN"
            }
        ],
        "RequestId": "abc"
    }
}
```

**Example 2: 查询单个授权服务信息**

查询单个授权服务信息

Input: 

```
tccli ess DescribeExtendedServiceAuthInfos --cli-unfold-argument  \
    --Operator.UserId abc \
    --ExtendServiceType OPEN_SERVER_SIGN
```

Output: 
```
{
    "Response": {
        "AuthInfoList": [
            {
                "HasAuthUserList": [
                    {
                        "BelongTo": "CurrentOrg",
                        "UserId": "userId1"
                    },
                    {
                        "BelongTo": "CurrentOrg",
                        "UserId": "userId2"
                    },
                    {
                        "BelongTo": "CurrentOrg",
                        "UserId": "userId3"
                    }
                ],
                "Name": "企业静默签（自动签署）",
                "OperateOn": 1681289048,
                "OperatorUserId": "OperatorUserId",
                "Status": "ENABLE",
                "Type": "OPEN_SERVER_SIGN"
            }
        ],
        "RequestId": "abc"
    }
}
```

