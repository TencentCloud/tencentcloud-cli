**Example 1: 根据存储库名称查询**



Input: 

```
tccli tione DescribeCodeRepositories --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20 \
    --Filters.0.Name instance-name \
    --Filters.0.Values private
```

Output: 
```
{
    "Response": {
        "RequestId": "15837636504347136271",
        "TotalCount": 1,
        "CodeRepoSet": [
            {
                "CreationTime": "2020-03-09 22:01:50",
                "LastModifiedTime": "2020-03-09 22:01:50",
                "CodeRepositoryName": "private",
                "GitConfig": {
                    "Branch": "master",
                    "RepositoryUrl": "https://github.com/example/test.git"
                }
            }
        ]
    }
}
```

