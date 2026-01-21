**Example 1: 测试**



Input: 

```
tccli tione ModifyServiceGroupWeights --cli-unfold-argument  \
    --ServiceGroupId ms-fdsfsd \
    --Weights.0.ServiceId ms-j7jlxfwk-2 \
    --Weights.0.Weight 0 \
    --Weights.1.ServiceId ms-j7jlxfwk-1 \
    --Weights.1.Weight 100
```

Output: 
```
{
    "Response": {
        "ServiceGroup": null,
        "RequestId": "cccc13d6-b255-48cd-b189-2a17d4b236af"
    }
}
```

