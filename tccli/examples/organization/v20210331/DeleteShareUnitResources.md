**Example 1: 删除共享单元资源**



Input: 

```
tccli organization DeleteShareUnitResources --cli-unfold-argument  \
    --UnitId shareUnit-xhre**ra2p \
    --Area ap-guangzhou \
    --Type secret \
    --Resources.0.ResourceId shareResource-12**erte
```

Output: 
```
{
    "Response": {
        "RequestId": "5ef007aa-2dc5-4729-a880-b7ac69d94714"
    }
}
```

