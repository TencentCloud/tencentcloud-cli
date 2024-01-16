**Example 1: 退资源**

执行资源退还

Input: 

```
tccli billing OperateResourcesInner --cli-unfold-argument  \
    --ActionType return \
    --ReferenceId 60ad167d-9856-4681-b858-7a8dadca8859 \
    --OwnerUin 909619400 \
    --OperateUin 909619400 \
    --ResultNotified 1 \
    --ResourceSet.0.ResourceId ins-abcdefg \
    --ResourceSet.0.ProductCode p_cvm \
    --ResourceSet.0.RegionApCode ap-guanzhou
```

Output: 
```
{
    "Response": {
        "ReferenceId": "abc",
        "OperateResult": 0,
        "DealNames": [
            "abc"
        ],
        "ResourceSet": [
            {
                "ResourceId": "abc",
                "OperateResult": 0,
                "OperateEndTime": "abc",
                "Message": "abc",
                "FailureReason": "abc",
                "FlowId": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

