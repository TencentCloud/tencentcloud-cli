**Example 1: 查询全部扩展服务信息**

查询全部支持的扩展服务开通和授权信息

Input: 

```
tccli ess DescribeExtendedServiceAuthInfos --cli-unfold-argument  \
    --Operator.UserId yDRC*********g0vjoimj \
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
                        "UserId": "yDRC*********g0vjoimj"
                    },
                    {
                        "BelongTo": "CurrentOrg",
                        "UserId": "yDRC*********g0vjoimj"
                    },
                    {
                        "BelongTo": "CurrentOrg",
                        "UserId": "yDRC*********g0vjoimj"
                    }
                ],
                "Name": "企业自动签（自动签署）",
                "OperateOn": 1681289048,
                "OperatorUserId": "yDRC*********g0vjoimj",
                "Status": "ENABLE",
                "Type": "OPEN_SERVER_SIGN"
            },
            {
                "Name": "企业与港澳台居民*签署合同",
                "OperateOn": 1667458840,
                "OperatorUserId": "yDRC*********g0vjoimj",
                "Status": "ENABLE",
                "Type": "OVERSEA_SIGN",
                "HasAuthUserList": []
            },
            {
                "Name": "使用手机号验证签署方身份",
                "OperateOn": 0,
                "OperatorUserId": "yDRC*********g0vjoimj",
                "Status": "DISABLE",
                "Type": "MOBILE_CHECK_APPROVER",
                "HasAuthUserList": []
            },
            {
                "Name": "骑缝章",
                "OperateOn": 0,
                "OperatorUserId": "yDRC*********g0vjoimj",
                "Status": "ENABLE",
                "Type": "PAGING_SEAL",
                "HasAuthUserList": []
            },
            {
                "HasAuthUserList": [
                    {
                        "BelongTo": "CurrentOrg",
                        "UserId": "yDRC*********g0vjoimj"
                    },
                    {
                        "BelongTo": "CurrentOrg",
                        "UserId": "yDRC*********g0vjoimj"
                    },
                    {
                        "BelongTo": "CurrentOrg",
                        "UserId": "yDRC*********g0vjoimj"
                    }
                ],
                "Name": "批量签署",
                "OperateOn": 1667460697,
                "OperatorUserId": "yDRC*********g0vjoimj",
                "Status": "ENABLE",
                "Type": "BATCH_SIGN"
            }
        ],
        "RequestId": "s1******80"
    }
}
```

**Example 2: 查询特定的扩展服务信息**

查询特定的扩展服务开通和授权信息

Input: 

```
tccli ess DescribeExtendedServiceAuthInfos --cli-unfold-argument  \
    --Operator.UserId yDR*****oimj \
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
                        "UserId": "yDR*****oimj"
                    },
                    {
                        "BelongTo": "CurrentOrg",
                        "UserId": "yDR*****oimj"
                    },
                    {
                        "BelongTo": "CurrentOrg",
                        "UserId": "yDR*****oimj"
                    }
                ],
                "Name": "企业自动签（自动签署）",
                "OperateOn": 1681289048,
                "OperatorUserId": "yDR*****oimj",
                "Status": "ENABLE",
                "Type": "OPEN_SERVER_SIGN"
            }
        ],
        "RequestId": "s1*****90"
    }
}
```

**Example 3: 查询不支持的特定扩展服务**

传入了不支持的特定扩展服务，返回错误

Input: 

```
tccli ess DescribeExtendedServiceAuthInfos --cli-unfold-argument  \
    --Operator.UserId yDR*****oimj \
    --ExtendServiceType TEST
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "OperationDenied",
            "Message": "不支持的扩展类型"
        },
        "RequestId": "s1**********72"
    }
}
```

