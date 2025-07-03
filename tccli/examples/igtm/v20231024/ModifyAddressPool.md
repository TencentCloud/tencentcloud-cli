**Example 1: 编辑地址池**



Input: 

```
tccli igtm ModifyAddressPool --cli-unfold-argument  \
    --PoolId 1 \
    --PoolName testname \
    --TrafficStrategy all \
    --MonitorId 1 \
    --AddressSet.0.AddressId 1 \
    --AddressSet.0.Addr 1.1.1.2 \
    --AddressSet.0.Location 中国上海 \
    --AddressSet.0.Status ok \
    --AddressSet.0.IsEnable ENABLED \
    --AddressSet.0.Weight 1 \
    --AddressSet.0.CreatedOn 2020-09-22T00:00:00+00:00 \
    --AddressSet.0.UpdatedOn 2020-09-22T00:00:00+00:00
```

Output: 
```
{
    "Response": {
        "Msg": "success",
        "RequestId": "9b19115c-873gt2-4940-91339-98952a13f159"
    }
}
```

