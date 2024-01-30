**Example 1: 修改策略**



Input: 

```
tccli igtm ModifyStrategy --cli-unfold-argument  \
    --InstanceId abc \
    --StrategyId 1 \
    --StrategyName abc \
    --Source.0.DnsLineId 1 \
    --Source.0.Name abc \
    --MainAddressPoolSet.0.MainAddressPoolId 1 \
    --MainAddressPoolSet.0.AddressPools.0.PoolId 1 \
    --MainAddressPoolSet.0.AddressPools.0.Weight 1 \
    --MainAddressPoolSet.0.MinSurviveNum 1 \
    --MainAddressPoolSet.0.TrafficStrategy abc \
    --FallbackAddressPoolSet.0.MainAddressPoolId 1 \
    --FallbackAddressPoolSet.0.AddressPools.0.PoolId 1 \
    --FallbackAddressPoolSet.0.AddressPools.0.Weight 1 \
    --FallbackAddressPoolSet.0.MinSurviveNum 1 \
    --FallbackAddressPoolSet.0.TrafficStrategy abc \
    --IsEnabled abc \
    --KeepDomainRecords abc
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

