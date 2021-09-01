**Example 1: 获取满足输入搜索条件的个人版镜像仓库**



Input: 

```
tccli tcr DescribeRepositoryFilterPersonal --cli-unfold-argument  \
    --RepoName dockerhub/test \
    --Public 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "PrivilegeFiltered": false,
            "RepoInfo": [
                {
                    "RepoName": "v3test2/mao",
                    "RepoType": "QCLOUD HUB",
                    "TagCount": 3,
                    "Public": 0,
                    "IsUserFavor": false,
                    "IsQcloudOfficial": false,
                    "FavorCount": 0,
                    "PullCount": 17,
                    "Description": "test",
                    "CreationTime": "2019-12-20 17:15:51",
                    "UpdateTime": "2019-12-26 17:03:11"
                }
            ],
            "Server": "ccr.ccs.tencentyun.com",
            "TotalCount": 1
        },
        "RequestId": "28f2f221-8a92-4b68-8fab-aaf92d4291d5"
    }
}
```

