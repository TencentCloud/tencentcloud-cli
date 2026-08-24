**Example 1: 获取会话列表**



Input: 

```
tccli csip DescribeDspmSessionList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0 \
    --EndTime 1782489599 \
    --StartTime 946656000 \
    --DbTypes cdb
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "AppId": 260085118,
                "AssetName": "cdb-l8hhoqwd",
                "AssetType": "cdb",
                "ClientIp": "169.254.128.1",
                "ClientPort": 58008,
                "DbIp": "10.0.0.5",
                "DbName": "",
                "DbPort": 3306,
                "DbType": "MYSQL",
                "DbUser": "dspmsc_seybalbp",
                "InstanceId": 259954,
                "InstanceName": "自动化测试实例-勿动",
                "LoginTime": 1782181126,
                "LogoutTime": 1782181126,
                "OpTime": 1782181126,
                "RetNo": 1,
                "SessionId": "0_0_1462470",
                "SourceType": "云数据库",
                "SourceTypeEn": "cdb",
                "SourceTypeEnDisplayName": "cdb",
                "SqlCount": 2
            }
        ],
        "TotalCount": 10000,
        "RequestId": "e34db94f-6139-4310-9f71-48b0f973f730"
    }
}
```

