**Example 1: 获取仓库信息**



Input: 

```
tccli tsf DescribeRepository --cli-unfold-argument  \
    --RepositoryId application-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "66e97c87-16d0-4936-b639-fab2c06ab238",
        "Result": {
            "RepositoryId": "application-xxxxxxxx",
            "RepositoryName": "test001",
            "RepositoryType": "private",
            "RepositoryDesc": "",
            "IsUsed": false,
            "CreateTime": "2020-05-26 10:52:20",
            "BucketName": "apple",
            "BucketRegion": "cq",
            "Directory": ""
        }
    }
}
```

