**Example 1: 代码仓库详情**



Input: 

```
tccli tione DescribeCodeRepo --cli-unfold-argument  \
    --Id cr-213214124142
```

Output: 
```
{
    "Response": {
        "CodeRepoDetail": {
            "UpdateTime": "2024-09-08 18:00:00",
            "Name": "git_test",
            "Id": "cr-213214124142",
            "GitConfig": {
                "RepositoryUrl": "https://test.git",
                "Branch": "master"
            },
            "NoSecret": true,
            "CreateTime": "2024-09-24 11:00:00"
        },
        "RequestId": "2313123123yt321y3y2312y"
    }
}
```

