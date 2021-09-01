**Example 1: 创建黑石竞价实例**



Input: 

```
tccli bm CreateSpotDevice --cli-unfold-argument  \
    --ComputeType v1.c2.medium \
    --GoodsNum 37 \
    --VpcId vpc-3c7b2102 \
    --OsTypeId 12 \
    --SubnetId subnet-34ts34da \
    --SpotStrategy SpotWithPriceLimit \
    --SpotPriceLimit 1000 \
    --Zone ap-guangzhoutest-blshw-1
```

Output: 
```
{
    "Response": {
        "ResourceIds": [
            "tcpm-i470dvkz"
        ],
        "FlowId": 902723,
        "RequestId": "f914265c-a5ba-4460-aec4-2e945df894cf"
    }
}
```

