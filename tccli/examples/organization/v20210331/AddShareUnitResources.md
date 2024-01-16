**Example 1: 添加共享单元资源**



Input: 

```
tccli organization AddShareUnitResources --cli-unfold-argument  \
    --Area ap-guangzhou \
    --Type secret \
    --Resources.0.ProductResourceId sec***002 \
    --UnitId shareUnit-xhre**ra2p
```

Output: 
```
{
    "Response": {
        "RequestId": "5ef007aa-2dc5-4729-a880-b7ac69d94714"
    }
}
```

