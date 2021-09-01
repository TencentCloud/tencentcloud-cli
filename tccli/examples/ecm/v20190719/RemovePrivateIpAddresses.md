**Example 1: 弹性网卡退还内网 IP**



Input: 

```
tccli ecm RemovePrivateIpAddresses --cli-unfold-argument  \
    --NetworkInterfaceId eni-12121212 \
    --PrivateIpAddresses.0.PrivateIpAddress 172.16.32.111 \
    --EcmRegion ap-hangzhou-ecm
```

Output: 
```
{
    "Response": {
        "RequestId": "f23d1450-ed00-4442-98d4-be409e625e6c"
    }
}
```

