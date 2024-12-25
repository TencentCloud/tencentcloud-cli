**Example 1: 弹性网卡申请内网 IP**



Input: 

```
tccli ecm AssignPrivateIpAddresses --cli-unfold-argument  \
    --NetworkInterfaceId eni-ms7c7gcr \
    --SecondaryPrivateIpAddressCount 1 \
    --EcmRegion ap-hangzhou-ecm
```

Output: 
```
{
    "Response": {
        "PrivateIpAddressSet": [
            {
                "PrivateIpAddress": "172.16.32.237",
                "AddressId": "",
                "PublicIpAddress": "",
                "Primary": false,
                "IsWanIpBlocked": false,
                "State": "PENDING",
                "Description": "demo"
            }
        ],
        "RequestId": "f23d1450-ed00-4442-98d4-be409e625e6c"
    }
}
```

