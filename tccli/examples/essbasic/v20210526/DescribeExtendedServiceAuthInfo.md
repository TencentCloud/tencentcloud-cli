**Example 1: 无权限的openid调用此接口**

查询企业扩展服务授权信息，经办人openid不是超管或者法人，会报错返回

Input: 

```
tccli essbasic DescribeExtendedServiceAuthInfo --cli-unfold-argument  \
    --Agent.ProxyOperator.OpenId normal-open-id \
    --Agent.ProxyOrganizationOpenId org-open-id \
    --Agent.AppId APPID12344556667777777
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "OperationDenied",
            "Message": "操作被拒绝。"
        },
        "RequestId": "s1**********72"
    }
}
```

**Example 2: 查询企业扩展服务授权信息**

查询企业扩展服务授权信息

Input: 

```
tccli essbasic DescribeExtendedServiceAuthInfo --cli-unfold-argument  \
    --Agent.ProxyOperator.OpenId admin-open-id \
    --Agent.ProxyOrganizationOpenId org-open-id \
    --Agent.AppId APPID12344556667777777
```

Output: 
```
{
    "Response": {
        "AuthInfo": [
            {
                "Name": "企业与港澳台居民*签署合同",
                "OperateOn": 1671692727,
                "OperatorOpenId": "admin-open-id",
                "Status": "DISABLE",
                "Type": "OVERSEA_SIGN"
            },
            {
                "Name": "使用手机号验证签署方身份",
                "OperateOn": 1673331249,
                "OperatorOpenId": "admin-open-id",
                "Status": "DISABLE",
                "Type": "MOBILE_CHECK_APPROVER"
            },
            {
                "Name": "企业自动签（自动签署）",
                "OperateOn": 1672989237,
                "OperatorOpenId": "admin-open-id",
                "Status": "DISABLE",
                "Type": "AUTO_SIGN"
            },
            {
                "Name": "下载企业合同/文件",
                "OperateOn": 1673331721,
                "OperatorOpenId": "admin-open-id",
                "Status": "ENABLE",
                "Type": "DOWNLOAD_FLOW"
            },
            {
                "Name": "骑缝章",
                "OperateOn": 1673331246,
                "OperatorOpenId": "admin-openid",
                "Status": "DISABLE",
                "Type": "PAGING_SEAL"
            },
            {
                "Name": "拓宽合同签署年龄",
                "OperateOn": 0,
                "OperatorOpenId": "",
                "Status": "ENABLE",
                "Type": "EXPANSION_AGE_LIMIT"
            }
        ],
        "RequestId": "s16733xxx81"
    }
}
```

