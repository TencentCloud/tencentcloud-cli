**Example 1: 释放资源组节点**



Input: 

```
tccli tione DestroyBillingResource --cli-unfold-argument  \
    --ResourceIds eins-12345678 \
    --ResourceGroupId sm-fewf23
```

Output: 
```
{
    "Response": {
        "RequestId": "49f94c76-15c5-45da-8e54-49ebb11ce556",
        "FailResources": [
            {
                "FailMsg": "100",
                "ResourceId": "sm-f23e2re42"
            }
        ]
    }
}
```

