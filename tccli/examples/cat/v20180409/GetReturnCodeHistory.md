**Example 1: 查询拨测任务的历史返回码信息示例**



Input: 

```
tccli cat GetReturnCodeHistory --cli-unfold-argument  \
    --TaskId 260228 \
    --BeginTime '2019-12-11 10:00:00' \
    --EndTime '2019-12-11 20:30:00' \
    --Province beijing-1
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
                "ResultCount": 196,
                "ResultCode": 10016,
                "ErrorReason": "Ping超时"
            },
            {
                "IspName": "电信",
                "Province": "beijing-1",
                "ProvinceName": "北京(一区)",
                "MapKey": "beijing-1",
                "ServerIp": "119.29.5.164",
                "ResultCount": 196,
                "ResultCode": 10016,
                "ErrorReason": "Ping超时"
            },
            {
                "IspName": "联通",
                "Province": "beijing-1",
                "ProvinceName": "北京(一区)",
                "MapKey": "beijing-1",
                "ServerIp": "119.29.5.164",
                "ResultCount": 196,
                "ResultCode": 10016,
                "ErrorReason": "Ping超时"
            },
            {
                "IspName": "腾讯云",
                "Province": "beijing-1",
                "ProvinceName": "北京(一区)",
                "MapKey": "beijing-1",
                "ServerIp": "119.29.5.164",
                "ResultCount": 196,
                "ResultCode": 10016,
                "ErrorReason": "Ping超时"
            }
        ],
        "Summary": [
            {
                "ResultCode": 10016,
                "ResultCount": 784,
                "ErrorReason": "Ping超时"
            }
        ],
        "BeginTime": "2019-12-11 10:00:00",
        "EndTime": "2019-12-11 20:30:00",
        "RequestId": "87869edf-ca3e-4c2c-8a5a-52eee8396e20"
    }
}
```

