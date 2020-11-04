**Example 1: 获取所有仓库列表**



Input: 

```
tccli tsf DescribeRepositories --cli-unfold-argument  \
    --Offset 0\
    --Limit 20
```

Output: 
```
{
    "Response": {
        "RequestId": "58998bc6-b283-4242-94e9-4d1b75e47a01",
        "Result": {
            "Result": {
                "TotalCount": 2,
                "Content": [
                    {
                        "RepositoryId": "application-j4y4eqvk",
                        "RepositoryName": "consumer",
                        "RepositoryType": "default",
                        "RepositoryDesc": "",
                        "IsUsed": false,
                        "CreateTime": "2020-07-20 15:08:56",
                        "BucketName": "",
                        "BucketRegion": "",
                        "Directory": ""
                    },
                    {
                        "RepositoryId": "application-l6ymbvgd",
                        "RepositoryName": "mesh-vm",
                        "RepositoryType": "default",
                        "RepositoryDesc": "",
                        "IsUsed": false,
                        "CreateTime": "",
                        "BucketName": "",
                        "BucketRegion": "",
                        "Directory": ""
                    }
                ]
            }
        }
    }
}
```

