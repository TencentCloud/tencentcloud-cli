**Example 1: 查询目录树**

查询目录树，展开目录树

Input: 

```
tccli wedata DescribeDsFolderTree --cli-unfold-argument  \
    --ProjectId abc \
    --FirstLevelPull True \
    --FolderId abc \
    --WorkflowId abc \
    --Keyword abc \
    --IncludeWorkflow True \
    --IncludeTask True
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

