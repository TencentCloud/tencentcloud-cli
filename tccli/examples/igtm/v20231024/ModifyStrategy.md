**Example 1: 修改策略**



Input: 

```
tccli igtm ModifyStrategy --cli-unfold-argument  \
    --InstanceId gtm-sdsdrdasd \
    --StrategyId 1 \
    --StrategyName test_strategy \
    --Source.0.DnsLineId 1 \
    --Source.0.Name 默认 \
    --MainAddressPoolSet.0.MainAddressPoolId 1 \
    --MainAddressPoolSet.0.AddressPools.0.PoolId 1 \
    --MainAddressPoolSet.0.AddressPools.0.Weight 1 \
    --MainAddressPoolSet.0.MinSurviveNum 1 \
    --MainAddressPoolSet.0.TrafficStrategy all \
    --FallbackAddressPoolSet.0.MainAddressPoolId 1 \
    --FallbackAddressPoolSet.0.AddressPools.0.PoolId 1 \
    --FallbackAddressPoolSet.0.AddressPools.0.Weight 1 \
    --FallbackAddressPoolSet.0.MinSurviveNum 1 \
    --FallbackAddressPoolSet.0.TrafficStrategy all \
    --IsEnabled ENABLED \
    --KeepDomainRecords DISABLED
```

Output: 
```
{
    "Response": {
        "Msg": "success",
        "RequestId": "abdsadasddc12312jhjyg"
    }
}
```

