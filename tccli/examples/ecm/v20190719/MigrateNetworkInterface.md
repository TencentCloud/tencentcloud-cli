**Example 1: 弹性网卡迁移**



Input: 

```
tccli ecm MigrateNetworkInterface --cli-unfold-argument  \
    --NetworkInterfaceId eni-12121212 \
    --SourceInstanceId ins-11221122 \
    --DestinationInstanceId ins-11331133 \
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

