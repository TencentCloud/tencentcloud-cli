**Example 1: 获取管理员同步配置**

获取管理员同步配置

Input: 

```
tccli csip DescribeBaselineSyncConf --cli-unfold-argument  \
    --MemberId mem-tencent-6*************29
```

Output: 
```
{
    "Response": {
        "SyncConf": {
            "AutoSync": true,
            "TargetAppidList": [
                200000000
            ],
            "UserConfList": [
                {
                    "AllowSync": true,
                    "AppID": 200000000,
                    "InConf": true,
                    "ManagedByOther": false
                }
            ]
        },
        "RequestId": "e61baf5c-ab92-4f36-b109-740196e4859b"
    }
}
```

