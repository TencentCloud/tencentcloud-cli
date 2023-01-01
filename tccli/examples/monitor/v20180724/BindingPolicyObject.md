**Example 1: 绑定策略对象**



Input: 

```
tccli monitor BindingPolicyObject --cli-unfold-argument  \
    --GroupId 111111 \
    --Module monitor \
    --Dimensions.0.EventDimensions {"uuid":"9d51a69e-0e4a-4120-ae58-9c073c851e24"} \
    --Dimensions.0.Region gz \
    --Dimensions.0.RegionId 1 \
    --Dimensions.0.Dimensions {"unInstanceId":"ins-ot3cq4bi"}
```

Output: 
```
{
    "Response": {
        "RequestId": "78345016-ff97-4360-839a-82f3d96430e8"
    }
}
```

