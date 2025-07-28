**Example 1: 批量添加共享单元资源**



Input: 

```
tccli organization AddShareUnitsResources --cli-unfold-argument  \
    --ShareUnits.0.UnitId shareUnit-2lc***zor \
    --ShareUnits.0.Area ap-guangzhou \
    --Type subnet \
    --Resources.0.ProductResourceId sub-eeu***
```

Output: 
```
{
    "Response": {
        "RequestId": "f82ba7fa-5d8a-4ad0-bc5c-96c015b79fe7"
    }
}
```

