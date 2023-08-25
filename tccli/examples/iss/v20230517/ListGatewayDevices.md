**Example 1: 成功**

 

Input: 

```
tccli iss ListGatewayDevices --cli-unfold-argument  \
    --GatewayId hijklmno-efgh-5678-ijkl-1234567890abcd
```

Output: 
```
{
    "Response": {
        "Data": {
            "List": [
                {
                    "ChannelNum": 0,
                    "DeviceId": "12345678-abcd-efgh-ijkl-1234567890abcd",
                    "Ip": "192.168.0.1",
                    "Name": "gw121138",
                    "Port": 8090,
                    "ProtocolType": 1,
                    "ProtocolTypeName": "hik",
                    "Status": 0,
                    "Type": 1
                }
            ],
            "TotalCount": 1
        },
        "RequestId": "29b0c8a9-dd64-4ece-a42b-4b03f819c56b"
    }
}
```

