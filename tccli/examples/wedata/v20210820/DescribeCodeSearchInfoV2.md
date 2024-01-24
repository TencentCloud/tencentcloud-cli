**Example 1: 全局搜索根据条件搜索代码**

全局搜索根据条件搜索代码

Input: 

```
tccli wedata DescribeCodeSearchInfoV2 --cli-unfold-argument  \
    --Keyword abc \
    --SearchScope abc \
    --SearchScopes abc \
    --OwnerIds abc \
    --FileTypes abc \
    --TaskTypes abc \
    --StartTime abc \
    --EndTime abc \
    --Status abc \
    --PageNumber 1 \
    --PageSize 1 \
    --ProjectId abc \
    --WorkflowIds abc \
    --FolderIds abc \
    --DatasourceIds abc \
    --FolderPaths abc \
    --TaskStatus abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "CodeSearchInfoList": {
                "Rows": [
                    {
                        "Id": "abc",
                        "Name": "abc",
                        "Type": "abc",
                        "Content": [
                            {
                                "Number": 1,
                                "Line": "abc",
                                "NodeType": "abc"
                            }
                        ],
                        "OwnerName": "abc",
                        "UpdateTime": "abc",
                        "CreateTime": "abc",
                        "MatchRows": 1,
                        "SubmitTime": "abc",
                        "DisplayType": "abc",
                        "CosPath": "abc"
                    }
                ],
                "TotalCount": 1
            },
            "DevCount": 1,
            "ScheduleCount": 1,
            "RecycleCount": 1
        },
        "RequestId": "abc"
    }
}
```

