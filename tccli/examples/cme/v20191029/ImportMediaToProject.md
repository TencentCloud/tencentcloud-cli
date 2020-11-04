**Example 1: 导入项目素材**



Input: 

```
tccli cme ImportMediaToProject --cli-unfold-argument  \
    --Platform test\
    --ProjectId user_111\
    --VodFileId 111122\
    --Name test\
    --PreProcessDefinition 10
```

Output: 
```
{
    "Response": {
        "MaterialId": "248208104522663991",
        "TaskId": "125xxx65-procedurev2-bffb15f07530b57bc1aabb01fac74bca",
        "RequestId": "requestid"
    }
}
```

