**Example 1: 弹性网卡绑定云主机**



Input: 

```
tccli ecm AttachNetworkInterface --cli-unfold-argument  \
    --NetworkInterfaceId eni-12121212 \
    --InstanceId ins-ins-11221122 \
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

