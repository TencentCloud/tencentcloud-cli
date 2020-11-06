**Example 1: 查询拨测任务的返回码统计信息 示例**



Input: 

```
tccli cat GetReturnCodeInfo --cli-unfold-argument  \
    --TaskId 260228 \
    --BeginTime '2019-12-11 10:00:00' \
    --EndTime '2019-12-11 20:30:00'
```

Output: 
```
{
    "Response": {
        "Details": [
            {
                "IspName": "移动",
                "Province": "beijing-1",
                "ProvinceName": "北京(一区)",
                "MapKey": "beijing-1",
                "ServerIp": "119.29.5.164",
                "ResultCount": 1568,
                "ResultCode": 10016,
                "ErrorReason": "Ping超时"
            },
            {
                "IspName": "电信",
                "Province": "beijing-1",
                "ProvinceName": "北京(一区)",
                "MapKey": "beijing-1",
                "ServerIp": "119.29.5.164",
                "ResultCount": 1609,
                "ResultCode": 10016,
                "ErrorReason": "Ping超时"
            },
            {
                "IspName": "联通",
                "Province": "beijing-1",
                "ProvinceName": "北京(一区)",
                "MapKey": "beijing-1",
                "ServerIp": "119.29.5.164",
                "ResultCount": 1581,
                "ResultCode": 10016,
                "ErrorReason": "Ping超时"
            },
            {
                "IspName": "腾讯云",
                "Province": "bangkok-1",
                "ProvinceName": "曼谷(一区)",
                "MapKey": "bangkok-1",
                "ServerIp": "119.29.5.164",
                "ResultCount": 3918,
                "ResultCode": 10016,
                "ErrorReason": "Ping超时"
            }
        ],
        "Summary": [
            {
                "ResultCode": 10016,
                "ResultCount": 8676,
                "ErrorReason": "Ping超时"
            }
        ],
        "BeginTime": "2019-12-11 10:00:00",
        "EndTime": "2019-12-11 20:30:00",
        "RequestId": "37bebabf-7868-46e7-a968-9054de07b978"
    }
}
```

