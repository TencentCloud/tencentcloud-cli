**Example 1: 导入媒体到个人**



Input: 

```
tccli cme ImportMaterial --cli-unfold-argument  \
    --Platform test \
    --VodFileId 5285890796182734267 \
    --Owner.Id 1111 \
    --Owner.Type PERSON \
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

**Example 2: 导入媒体到团队**



Input: 

```
tccli cme ImportMaterial --cli-unfold-argument  \
    --Platform test \
    --VodFileId 5285890796182734267 \
    --Owner.Id cmetid_37b1bb3bf8fb2eb3ba00e41dcca0ce \
    --Owner.Type TEAM \
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

