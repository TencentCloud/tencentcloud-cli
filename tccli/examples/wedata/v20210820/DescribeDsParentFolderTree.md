**Example 1: 查询父目录树**

编排空间 用于定位工作流、任务

Input: 

```
tccli wedata DescribeDsParentFolderTree --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --FolderId 37ae6016-1ea0-4aad-a070-48ecbf660588 \
    --WorkflowId ed7ea1ca-be5c-11ed-b7fc-043f72e73c62 \
    --TaskId 20230504163927698
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Id": "100028578885",
                "Title": "wedata",
                "Type": "select-option",
                "ParentId": "e345e27f-be5c-11ed-b7fc-043f72e73c62",
                "IsLeaf": true,
                "Children": [
                    {
                        "Id": "100028578886",
                        "Title": "tbds",
                        "Type": "select-option",
                        "ParentId": "e345e27f-be5c-11ed-b7fc-043f72e73c7",
                        "IsLeaf": true,
                        "Children": [
                            {
                                "Id": "100028578887",
                                "Title": "tenc",
                                "Type": "select-option",
                                "ParentId": "e345e27f-be5c-11ed-b7fc-043f72e73c8",
                                "IsLeaf": true,
                                "Params": "json"
                            }
                        ],
                        "Params": "code1"
                    }
                ],
                "Params": "code2"
            }
        ],
        "RequestId": "2ff1f873-90fb-438d-a948-50f90bc9c686"
    }
}
```

