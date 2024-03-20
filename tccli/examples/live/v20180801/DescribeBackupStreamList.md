**Example 1: 请求示例**

查询在推的主备流。

Input: 

```
tccli live DescribeBackupStreamList --cli-unfold-argument  \
    --StreamName stream1
```

Output: 
```
{
    "Response": {
        "RequestId": "4b3d1d04-6f79-4f56-a8e7-46de97de1713",
        "StreamInfoList": [
            {
                "OptimalEnable": 0,
                "HostGroupName": "",
                "StreamName": "stream1",
                "BackupList": [
                    {
                        "DomainName": "5000.livepush.com",
                        "AppName": "live",
                        "PublishTime": "2018-06-29T19:00:00Z",
                        "UpstreamSequence": "710313341080024595",
                        "SourceFrom": "直推流",
                        "MasterFlag": 0
                    },
                    {
                        "DomainName": "5000.livepush.com",
                        "AppName": "gifshow",
                        "PublishTime": "2018-06-29T19:00:00Z",
                        "UpstreamSequence": "710313341080024599",
                        "SourceFrom": "拉流转推(123)",
                        "MasterFlag": 1
                    }
                ]
            }
        ]
    }
}
```

