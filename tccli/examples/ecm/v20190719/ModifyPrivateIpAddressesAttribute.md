**Example 1: 修改弹性网卡内网IP属性**



Input: 

```
tccli ecm ModifyPrivateIpAddressesAttribute --cli-unfold-argument  \
    --NetworkInterfaceId eni-pwbqma5d \
    --PrivateIpAddresses.0.PrivateIpAddress 192.168.2.7 \
    --PrivateIpAddresses.0.Description new-name \
    --EcmRegion "ap-guangzhou-ecm"
```

Output: 
```
{
    "Response": {
        "RequestId": "f23d1450-ed00-4442-98d4-be409e625e6c"
    }
}
```

