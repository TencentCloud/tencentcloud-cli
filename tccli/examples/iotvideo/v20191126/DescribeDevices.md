**Example 1: 获取设备信息列表**



Input: 

```
tccli iotvideo DescribeDevices --cli-unfold-argument  \
    --ProductId 123456789000 \
    --ReturnModel true \
    --Limit 10 \
    --Offset 0 \
    --OtaVersion test \
    --DeviceName test
```

Output: 
```
{
    "Response": {
        "TotalCount": 3,
        "Data": [
            {
                "Tid": "xxx0",
                "DeviceName": "xxxx0",
                "ActiveTime": 0,
                "Disabled": false,
                "StreamStatus": true,
                "OtaVersion": "test",
                "Online": 0,
                "LastOnlineTime": 0,
                "IotModel": "xxx"
            },
            {
                "Tid": "xxx1",
                "DeviceName": "xxxx1",
                "ActiveTime": 1546275361,
                "Disabled": false,
                "StreamStatus": true,
                "OtaVersion": "test",
                "Online": 1,
                "LastOnlineTime": 1546275661,
                "IotModel": "xxx"
            },
            {
                "Tid": "xxx2",
                "DeviceName": "xxxx2",
                "ActiveTime": 0,
                "Disabled": false,
                "StreamStatus": true,
                "OtaVersion": "",
                "Online": 0,
                "LastOnlineTime": 0,
                "IotModel": ""
            }
        ],
        "RequestId": "749c3503-4181-417c-968f-37c39c140274"
    }
}
```

