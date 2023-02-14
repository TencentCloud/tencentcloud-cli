**Example 1: 修改HAVIP名称**

修改HAVIP名称

Input: 

```
tccli vpc ModifyHaVipAttribute --cli-unfold-argument  \
    --HaVipId havip-9o233uri \
    --HaVipName new+name
```

Output: 
```
{
    "Response": {
        "RequestId": "fcb47621-838b-428e-8c33-6e210d93c451"
    }
}
```

