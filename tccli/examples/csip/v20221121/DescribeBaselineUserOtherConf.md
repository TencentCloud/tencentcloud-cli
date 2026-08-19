**Example 1: 获取其他配置**

获取其他配置

Input: 

```
tccli csip DescribeBaselineUserOtherConf --cli-unfold-argument  \
    --MemberId mem-tencent-6*************29
```

Output: 
```
{
    "Response": {
        "AdminInfo": {
            "AppID": 260000006,
            "Nick": "多账号-管理员",
            "Uin": "7**********9"
        },
        "IsSync": false,
        "UserConf": {
            "AgentScanTimeout": 1800,
            "AllowSync": true,
            "CleanRiskWhenOffline": true
        },
        "RequestId": "c9048437-9575-4a66-8ed4-6f34be82b2b5"
    }
}
```

