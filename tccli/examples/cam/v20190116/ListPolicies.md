**Example 1: 查看策略列表**



Input: 

```
tccli cam ListPolicies --cli-unfold-argument  \
    --Rp 1 \
    --Page 10
```

Output: 
```
{
    "Response": {
        "ServiceTypeList": [
            "xx"
        ],
        "List": [
            {
                "PolicyId": 16313162,
                "PolicyName": "QcloudAccessForCDNRole",
                "AddTime": "2019-04-19 10:55:31",
                "Type": 2,
                "Description": "腾讯云内容分发网络(CDN)操作权限含日志服务(CLS)的增删改查日志集，增删改查日志主题，搜索下载上传日志。",
                "CreateMode": 2,
                "Attachments": 0,
                "ServiceType": "cooperator",
                "IsAttached": 1,
                "Deactived": 1,
                "DeactivedDetail": [
                    "cvm"
                ],
                "IsServiceLinkedPolicy": 1,
                "UpdateTime": "2019-04-19 10:55:31",
                "AttachEntityCount": 0,
                "AttachEntityBoundaryCount": 0
            }
        ],
        "TotalNum": 239,
        "RequestId": "ae2bd2b7-1d55-4b0a-8154-e02407a2b390"
    }
}
```

