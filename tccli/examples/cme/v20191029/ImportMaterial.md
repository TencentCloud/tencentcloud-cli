**Example 1: 导入素材**



Input: 

```
tccli cme ImportMaterial --cli-unfold-argument  \
    --Platform test\
    --VodFileId  123456789\
    --Owner.Id 1111\
    --Owner.Type PERSON\
    --Name material_name
```

Output: 
```
{
    "Response": {
        "RequestId": "requestId",
        "MaterialId": "materialId",
        "PreProcessTaskId": "taskId"
    }
}
```

