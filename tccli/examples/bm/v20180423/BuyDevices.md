**Example 1: 购买物理机**



Input: 

```
tccli bm BuyDevices --cli-unfold-argument  \
    --Zone ap-guangzhou \
    --OsTypeId 1 \
    --RaidId 1 \
    --GoodsCount 100 \
    --VpcId vpc-xxx \
    --SubnetId subnet-xxx \
    --DeviceClassCode PS100v3 \
    --TimeUnit M \
    --TimeSpan 12
```

Output: 
```
{
    "Response": {
        "InstanceIds": [
            "cpm-xxx"
        ],
        "RequestId": "3f02fb0c-f782-4cef-9007-d63c68146e39"
    }
}
```

