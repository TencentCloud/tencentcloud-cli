**Example 1: 弹性网卡内网IP迁移**

弹性网卡内网IP迁移

Input: 

```
tccli vpc MigratePrivateIpAddress --cli-unfold-argument  \
    --SourceNetworkInterfaceId eni-afo43z61 \
    --DestinationNetworkInterfaceId eni-g0n2axhd \
    --PrivateIpAddress 172.16.33.109
```

Output: 
```
{
    "Response": {
        "RequestId": "f23d1450-ed00-4442-98d4-be409e625e6c"
    }
}
```

