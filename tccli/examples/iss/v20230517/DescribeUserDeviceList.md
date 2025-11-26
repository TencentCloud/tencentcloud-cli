**Example 1: 成功**



Input: 

```
tccli iss DescribeUserDeviceList --cli-unfold-argument  \
    --DeviceIds da238a8c-****-4a5b-****-************
```

Output: 
```
{
    "Response": {
        "RequestId": "423da921-fd90-4b07-a1a4-a17b8df24e37",
        "Data": {
            "List": [
                {
                    "DeviceId": "da238a8c-****-4a5b-****-************",
                    "Name": "rxxxxx2710",
                    "Code": "AE7YT98IOP",
                    "Status": 0,
                    "Region": "ap-shanghai",
                    "Type": 1,
                    "TransportProtocol": 0,
                    "AccessProtocol": 1,
                    "OrganizationId": "1",
                    "Manufacturer": "",
                    "Description": "",
                    "ClusterId": "41xxxxxxxad-4c16-xxx-dxxx3axxxxx90",
                    "ClusterName": "xxxx区",
                    "SipId": "",
                    "SipDomain": "",
                    "SipIp": "",
                    "SipPort": 0,
                    "Password": "",
                    "PushStreamUrl": "",
                    "GatewayId": "",
                    "GatewayName": "",
                    "ProtocolType": 0,
                    "ProtocolTypeName": "",
                    "Ip": "",
                    "Port": 0,
                    "Username": "",
                    "AudioSwitch": 1,
                    "SubscribeSwitch": 0,
                    "AppName": "tesxxxxxx",
                    "StreamName": "testsxxxxx",
                    "SilentFrameSwitch": 0
                }
            ]
        }
    }
}
```

