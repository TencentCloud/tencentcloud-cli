**Example 1: 查看notebook生命周期脚本列表**



Input: 

```
tccli tione DescribeNotebookLifecycleScripts --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --SortBy created \
    --SortOrder Descending \
    --Filters.0.Name search-by-name \
    --Filters.0.Values s
```

Output: 
```
{
    "Response": {
        "RequestId": "15838617732076459472",
        "TotalCount": 3,
        "NotebookLifecycleScriptsSet": [
            {
                "CreationTime": "2020-03-08 15:02:34",
                "LastModifiedTime": "2020-03-08 16:35:14",
                "NotebookLifecycleScriptsName": "bashsss"
            },
            {
                "CreationTime": "2020-03-08 14:45:28",
                "LastModifiedTime": "2020-03-08 14:45:28",
                "NotebookLifecycleScriptsName": "bashSs"
            },
            {
                "CreationTime": "2020-03-08 14:44:03",
                "LastModifiedTime": "2020-03-08 14:44:03",
                "NotebookLifecycleScriptsName": "bashShell"
            }
        ]
    }
}
```

