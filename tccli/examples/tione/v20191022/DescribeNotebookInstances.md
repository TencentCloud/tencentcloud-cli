**Example 1: 查询Notebook实例列表**



Input: 

```
tccli tione DescribeNotebookInstances --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --SortOrder Descending \
    --Filters.0.Name instance-name \
    --Filters.0.Values aaaafixa1
```

Output: 
```
{
    "Response": {
        "RequestId": "15838635149573473305",
        "TotalCount": 1,
        "NotebookInstanceSet": [
            {
                "CreationTime": "2020-03-06 12:40:35",
                "LastModifiedTime": "2020-03-06 12:43:39",
                "NotebookInstanceName": "aaaafixa1",
                "NotebookInstanceStatus": "Inservice",
                "InstanceType": "MEDIUM4",
                "InstanceId": "notebook-jq5r1whsjl"
            }
        ]
    }
}
```

