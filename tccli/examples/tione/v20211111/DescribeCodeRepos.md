**Example 1: 代码仓库列表**



Input: 

```
tccli tione DescribeCodeRepos --cli-unfold-argument  \
    --Filters.0.Fuzzy True \
    --Filters.0.Values abcd \
    --Filters.0.Name cr-ewqnewq \
    --Filters.0.Negative True \
    --Limit 0 \
    --Order test \
    --OrderField test \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "CodeRepoSet": [
            {
                "UpdateTime": "test",
                "Name": "test",
                "Id": "test",
                "GitConfig": {
                    "RepositoryUrl": "test",
                    "Branch": "test"
                },
                "NoSecret": true,
                "CreateTime": "test"
            }
        ],
        "RequestId": "test"
    }
}
```

