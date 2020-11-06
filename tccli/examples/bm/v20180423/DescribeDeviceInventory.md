**Example 1: 查询设备库存**



Input: 

```
tccli bm DescribeDeviceInventory --cli-unfold-argument  \
    --DeviceClassCode PS100v3 \
    --Zone ap-guangzhou \
    --VpcId vpc-xxx \
    --SubnetId subnet-xxx
```

Output: 
```
{
    "Response": {
        "DeviceCount": 6,
        "RequestId": "3f02fb0c-f782-4cef-9007-d63c68146e39"
    }
}
```

