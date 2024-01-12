**Example 1: 查询父目录树**

编排空间 用于定位工作流、任务

Input: 

```
tccli wedata DescribeDsParentFolderTree --cli-unfold-argument  \
    --ProjectId abc \
    --FolderId abc \
    --WorkflowId abc \
    --TaskId abc
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Id": "abc",
                "Title": "abc",
                "Type": "abc",
                "ParentId": "abc",
                "IsLeaf": true,
                "Children": [
                    {
                        "Id": "abc",
                        "Title": "abc",
                        "Type": "abc",
                        "ParentId": "abc",
                        "IsLeaf": true,
                        "Children": [
                            {
                                "Id": "abc",
                                "Title": "abc",
                                "Type": "abc",
                                "ParentId": "abc",
                                "IsLeaf": true,
                                "Params": "abc"
                            }
                        ],
                        "Params": "abc"
                    }
                ],
                "Params": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

