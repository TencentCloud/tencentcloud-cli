**Example 1: 查询跨境账单数据**



Input: 

```
tccli ga2 DescribeCrossBorderSettlement --cli-unfold-argument  \
    --GlobalAcceleratorId ga-00000020 \
    --AccelerateRegion ap-beijing \
    --EndpointGroupRegion ap-singapore \
    --SettlementMonth 202512
```

Output: 
```
{
    "Response": {
        "Traffic": 47.024,
        "RequestId": "b2917667-b75c-4959-833a-b8b9d57022c9"
    }
}
```

