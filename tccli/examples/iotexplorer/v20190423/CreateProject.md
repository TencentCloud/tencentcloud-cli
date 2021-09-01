**Example 1: 新建项目**

新建项目

Input: 

```
tccli iotexplorer CreateProject --cli-unfold-argument  \
    --ProjectName TestProjectName \
    --ProjectDesc projcet_desc
```

Output: 
```
{
    "Response": {
        "Project": {
            "ProjectId": "prj-z6j2tyr0",
            "ProjectName": "TestProjectName",
            "ProjectDesc": "projcet_desc",
            "CreateTime": 1560328276,
            "UpdateTime": 1560328276
        },
        "RequestId": "17a769e5-b355-4e32-8828-404d596f9b2c"
    }
}
```

