**Example 1: 批量查询控制台检索页/仪表盘免登录分享站点示例**



Input: 

```
tccli cls DescribeConsoleSharingList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ConsoleSharingInfos": [
            {
                "SharingId": "13cez28h",
                "SharingUrl": "https://clsshare.tencent-cloud.com/s/13cez28h",
                "SharingConfig": {
                    "Name": "my-sharing",
                    "Type": 1,
                    "VerifyCode": "lEC0V0",
                    "DurationMilliseconds": 18000,
                    "NowTime": 1706787306086,
                    "IsLockTimeRange": true,
                    "IsLockQuery": true,
                    "Params": [],
                    "Resources": [
                        "qcs::cls:ap-guangzhou:uin/10000000001:topic/c1306921-2180-3e45-9azb-31d12217871e6"
                    ]
                },
                "ExpiredTime": 1706789065000,
                "CreateTime": 1706787264000,
                "UpdateTime": 1706787264000
            }
        ],
        "RequestId": "714cf720-43e9-460b-bd9a-42a193ca3d94"
    }
}
```

