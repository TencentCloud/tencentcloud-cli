**Example 1: 创建地址池**



Input: 

```
tccli igtm CreateAddressPool --cli-unfold-argument  \
    --PoolName abc \
    --TrafficStrategy abc \
    --MonitorId 1 \
    --AddressSet.0.AddressId 1 \
    --AddressSet.0.Addr abc \
    --AddressSet.0.Location abc \
    --AddressSet.0.Status abc \
    --AddressSet.0.IsEnable abc \
    --AddressSet.0.Weight 1 \
    --AddressSet.0.CreatedOn 2020-09-22T00:00:00+00:00 \
    --AddressSet.0.UpdatedOn 2020-09-22T00:00:00+00:00
```

Output: 
```
{
    "Response": {
        "AddressPoolId": 1,
        "RequestId": "abc"
    }
}
```

