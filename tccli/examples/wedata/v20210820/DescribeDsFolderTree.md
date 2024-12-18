**Example 1: 查询目录树**

查询目录树，展开目录树

Input: 

```
tccli wedata DescribeDsFolderTree --cli-unfold-argument  \
    --ProjectId 1485413914375667733 \
    --FirstLevelPull True \
    --FolderId 11265328-2c7d-11ee-8d13-a4ae120f8272 \
    --WorkflowId 11265328-2c7d-11ee-8d13-a4ae120f8273 \
    --Keyword demoKey \
    --IncludeWorkflow True \
    --IncludeTask True
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Children": [
                    {
                        "Children": [],
                        "Id": "156b3b03-2c7d-11ee-8d13-a4ae120f8272",
                        "IsLeaf": false,
                        "Params": "eyJzdWJtaXRGbGFnIjp0cnVlLCJvd25lcklkIjoiMTAwMDI5NDExMDU2Iiwid29ya2Zsb3dEZXNjIjoiIn0=",
                        "ParentId": "11265328-2c7d-11ee-8d13-a4ae120f8272",
                        "Title": "f1332",
                        "Type": "workflow"
                    },
                    {
                        "Children": [],
                        "Id": "2f03778a-2c7d-11ee-8d13-a4ae120f8272",
                        "IsLeaf": false,
                        "Params": "eyJzdWJtaXRGbGFnIjp0cnVlLCJvd25lcklkIjoiMTAwMDI5NDExMDU2Iiwid29ya2Zsb3dEZXNjIjoiIn0=",
                        "ParentId": "11265328-2c7d-11ee-8d13-a4ae120f8272",
                        "Title": "f2",
                        "Type": "workflow"
                    }
                ],
                "Id": "11265328-2c7d-11ee-8d13-a4ae120f8272",
                "IsLeaf": false,
                "Params": null,
                "ParentId": "",
                "Title": "0_dengboxu",
                "Type": "folder"
            }
        ],
        "RequestId": "de4d6055-1501-46e4-86d3-7b6e47c5b8d5"
    }
}
```

**Example 2: 错误示例**

错误示例

Input: 

```
tccli wedata DescribeDsFolderTree --cli-unfold-argument  \
    --ProjectId 1111
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "UnauthorizedOperation",
            "Message": "当前用户角色或WeData版本没有权限，请进行角色授权或者升级WeData版本"
        },
        "RequestId": "78deafe3-7320-448e-a6a5-2fcb38a4e4a5"
    }
}
```

