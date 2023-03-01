**Example 1: 查询企业扩展服务授权信息**

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
                "Name": "企业静默签（自动签署）",
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
            }
        ],
        "RequestId": "s16733xxx81"
    }
}
```

