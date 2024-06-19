**Example 1: 获取所有仓库列表**



Input: 

```
tccli tsf DescribeRepositories --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20 \
    --SearchWord demo \
    --RepositoryType default
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 0,
            "Content": [
                {
                    "RepositoryId": "abc",
                    "RepositoryName": "abc",
                    "RepositoryType": "abc",
                    "RepositoryDesc": "abc",
                    "IsUsed": true,
                    "CreateTime": "abc",
                    "BucketName": "abc",
                    "BucketRegion": "abc",
                    "Directory": "abc"
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

