**Example 1: 成功**

 

Input: 

```
tccli iss DescribeGatewayMonitor --cli-unfold-argument  \
    --GatewayId hijklmno-efgh-5678-ijkl-1234567890ab
```

Output: 
```
{
    "Response": {
        "Data": {
            "ChannelOffline": 0,
            "ChannelOnline": 0,
            "ChannelPull": 0,
            "ChannelTotal": 0,
            "ChannelUnPull": 0,
            "DeviceOffline": 0,
            "DeviceOnline": 0,
            "DeviceTotal": 0,
            "UpFlow": 0
        },
        "RequestId": "58208bdd-38de-41c3-8671-3e662eea86c6"
    }
}
```

