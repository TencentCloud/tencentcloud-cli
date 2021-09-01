**Example 1: 弹性网卡申请内网 IP**



Input: 

```
tccli ecm AssignPrivateIpAddresses --cli-unfold-argument  \
    --NetworkInterfaceId eni-12121212 \
    --SecondaryPrivateIpAddressCount 2 \
    --EcmRegion ap-hangzhou-ecm
```

Output: 
```
{
    "Response": {
        "PrivateIpAddressSet": [
            {
                "PrivateIpAddress": "172.16.32.237"
            },
            {
                "PrivateIpAddress": "172.16.32.84"
            }
        ],
        "RequestId": "f23d1450-ed00-4442-98d4-be409e625e6c"
    }
}
```

