**Example 1: 获取设备事件**



Input: 

```
tccli iotvideoindustry DescribeDeviceEvent --cli-unfold-argument  \
    --EventTypes 1 \
    --EndTime 0 \
    --DeviceId  \
    --StartTime 0
```

Output: 
```
{
    "Response": {
        "Events": [
            {
                "EventTime": 1629285654,
                "EventType": 2,
                "EventDesc": "succ",
                "DeviceType": 2,
                "DeviceAddress": "10.0.16.80:9455",
                "DeviceId": "99933020581320000262",
                "ChannelId": "99933020581320000262",
                "EventLog": "log",
                "DeviceName": "事件测试1"
            }
        ],
        "RequestId": "c5a0a4e9-91f3-48f1-87e2-2c003cbdc3ed",
        "TotalCount": 1
    }
}
```

