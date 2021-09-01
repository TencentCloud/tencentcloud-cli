**Example 1: 修改项目**



Input: 

```
tccli iotexplorer ModifyProject --cli-unfold-argument  \
    --ProjectId prj-4r2kajtp \
    --ProjectName name \
    --ProjectDesc desc
```

Output: 
```
{
    "Response": {
        "Project": {
            "ProjectId": "prj-4r2kajtp",
            "ProjectName": "name",
            "ProjectDesc": "desc",
            "CreateTime": 1544146149,
            "UpdateTime": 1556160627
        },
        "RequestId": "77f57c79-8288-4899-9b40-9254c860b053"
    }
}
```

