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
                    "RepositoryId": "repo-6a79x94v",
                    "RepositoryName": "repo-mock",
                    "RepositoryType": "cos",
                    "RepositoryDesc": "this is a desc",
                    "IsUsed": true,
                    "CreateTime": "2019-12-20 09:33:22",
                    "BucketName": "testBucket",
                    "BucketRegion": "ap-guangzhou",
                    "Directory": "/app"
                }
            ]
        },
        "RequestId": "96561cf1-738a-47d6-943b-dec7ebbccabe"
    }
}
```

