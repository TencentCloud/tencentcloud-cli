**Example 1: 编辑地址池**



Input: 

```
tccli igtm ModifyAddressPool --cli-unfold-argument  \
    --PoolId 1 \
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
        "Msg": "abc",
        "RequestId": "abc"
    }
}
```

