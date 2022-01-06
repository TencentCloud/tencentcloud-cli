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
                "ChannelId": "",
                "EventLog": ""
            },
            {
                "EventTime": 1629285654,
                "EventType": 2,
                "EventDesc": "succ",
                "DeviceType": 2,
                "DeviceAddress": "10.0.16.80:3445",
                "DeviceId": "99933020581320000255",
                "ChannelId": "",
                "EventLog": ""
            },
            {
                "EventTime": 1629285652,
                "EventType": 2,
                "EventDesc": "succ",
                "DeviceType": 2,
                "DeviceAddress": "10.0.16.80:18583",
                "DeviceId": "44020000001320623122",
                "ChannelId": "",
                "EventLog": ""
            },
            {
                "EventTime": 1629285650,
                "EventType": 2,
                "EventDesc": "succ",
                "DeviceType": 2,
                "DeviceAddress": "10.0.16.80:18582",
                "DeviceId": "99933020581320000095",
                "ChannelId": "",
                "EventLog": ""
            },
            {
                "EventTime": 1629285638,
                "EventType": 2,
                "EventDesc": "succ",
                "DeviceType": 2,
                "DeviceAddress": "10.0.16.80:9454",
                "DeviceId": "99933020581320000251",
                "ChannelId": "",
                "EventLog": ""
            },
            {
                "EventTime": 1629285618,
                "EventType": 2,
                "EventDesc": "succ",
                "DeviceType": 2,
                "DeviceAddress": "10.0.16.80:3487",
                "DeviceId": "44020000001320443631",
                "ChannelId": "",
                "EventLog": ""
            },
            {
                "EventTime": 1629285609,
                "EventType": 2,
                "EventDesc": "succ",
                "DeviceType": 2,
                "DeviceAddress": "10.0.16.80:3446",
                "DeviceId": "99933020581320000278",
                "ChannelId": "",
                "EventLog": ""
            },
            {
                "EventTime": 1629285608,
                "EventType": 2,
                "EventDesc": "succ",
                "DeviceType": 2,
                "DeviceAddress": "10.0.16.80:8183",
                "DeviceId": "99933020581320000274",
                "ChannelId": "",
                "EventLog": ""
            },
            {
                "EventTime": 1629285604,
                "EventType": 1,
                "EventDesc": "fail",
                "DeviceType": 2,
                "DeviceAddress": "10.0.16.80:5060",
                "DeviceId": "99933020581320000255",
                "ChannelId": "",
                "EventLog": "设备注册签名错误"
            },
            {
                "EventTime": 1629285594,
                "EventType": 2,
                "EventDesc": "succ",
                "DeviceType": 2,
                "DeviceAddress": "10.0.16.80:3445",
                "DeviceId": "99933020581320000255",
                "ChannelId": "",
                "EventLog": ""
            }
        ],
        "RequestId": "c5a0a4e9-91f3-48f1-87e2-2c003cbdc3ed",
        "TotalCount": 9284
    }
}
```

