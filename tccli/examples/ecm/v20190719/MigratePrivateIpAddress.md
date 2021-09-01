**Example 1: 弹性网卡内网IP迁移**



Input: 

```
tccli ecm MigratePrivateIpAddress --cli-unfold-argument  \
    --SourceNetworkInterfaceId eni-12121212 \
    --DestinationNetworkInterfaceId eni-13131313 \
    --PrivateIpAddress 172.16.33.109 \
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

