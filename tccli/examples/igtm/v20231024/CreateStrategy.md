**Example 1: 创建策略**



Input: 

```
tccli igtm CreateStrategy --cli-unfold-argument  \
    --InstanceId gtm-sdsderd12e \
    --StrategyName testname \
    --Source.0.DnsLineId 1 \
    --Source.0.Name line1 \
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
    --KeepDomainRecords DISABLED
```

Output: 
```
{
    "Response": {
        "StrategyId": 0,
        "RequestId": "abcasd232dsad1dsadasd"
    }
}
```

