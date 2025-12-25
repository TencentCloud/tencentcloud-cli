**Example 1: 代码仓库列表**



Input: 

```
tccli tione DescribeCodeRepos --cli-unfold-argument  \
    --Filters.0.Fuzzy True \
    --Filters.0.Values  \
    --Filters.0.Name cr-ewqnewq \
    --Filters.0.Negative True \
    --Limit 0 \
    --Order  \
    --OrderField  \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "CodeRepoSet": [
            {
                "UpdateTime": "",
                "Name": "",
                "Id": "",
                "GitConfig": {
                    "RepositoryUrl": "",
                    "Branch": ""
                },
                "NoSecret": true,
                "CreateTime": ""
            }
        ],
        "RequestId": ""
    }
}
```

