**Example 1: 查看存储库详情**

查看存储库详情

Input: 

```
tccli tione DescribeCodeRepository --cli-unfold-argument  \
    --CodeRepositoryName private
```

Output: 
```
{
    "Response": {
        "RequestId": "15837634774603167083",
        "CreationTime": "2020-03-09 17:59:15",
        "LastModifiedTime": "2020-03-09 17:59:15",
        "CodeRepositoryName": "private",
        "GitConfig": {
            "Branch": "master",
            "RepositoryUrl": "https://github.com/example/test.git"
        },
        "NoSecret": true
    }
}
```

