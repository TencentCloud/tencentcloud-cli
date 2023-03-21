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
        "OperateResult": 0,
        "ReferenceId": "60ad167d-9856-4681-b858-7a8dadca8859",
        "RequestId": "gwergwerg3432",
        "ResourceSet": [
            {
                "ResourceId": "ins-abcdefg",
                "OperateResult": 0,
                "Message": "fdasf",
                "OperateEndTime": "2022-10-10 10:10:00"
            }
        ],
        "DealNames": [
            "sdfasdfa"
        ]
    }
}
```

