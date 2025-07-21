**Example 1: 创建地址池**



Input: 

```
tccli igtm CreateAddressPool --cli-unfold-argument  \
    --PoolName 测试地址池 \
    --TrafficStrategy ALL \
    --MonitorId 1 \
    --AddressSet.0.AddressId 1 \
    --AddressSet.0.Addr 1.1.1.2 \
    --AddressSet.0.Location 上海电信 \
    --AddressSet.0.Status  \
    --AddressSet.0.IsEnable ENABLED
```

Output: 
```
{
    "Response": {
        "AddressPoolId": 1,
        "RequestId": "8f0325a8-4dd6-4fcb-8f6b-c45e587e51b0"
    }
}
```

