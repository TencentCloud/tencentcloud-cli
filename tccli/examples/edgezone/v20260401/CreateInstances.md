**Example 1: 创建单台物理机实例**



Input: 

```
tccli edgezone CreateInstances --cli-unfold-argument  \
    --Zone ap-guangzhou-1 \
    --InstanceType BMS5.MEDIUM8 \
    --ImageId img-hmk3il0q \
    --InstanceName my-epm-instance \
    --InstanceCount 1 \
    --PrivateNetworkId net-private-001 \
    --PublicNetworkId net-public-001
```

Output: 
```
{
    "Response": {
        "InstanceIdSet": [
            "epm-abcd1234"
        ],
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

