**Example 1: 查询个人版所有仓库**



Input: 

```
tccli tcr DescribeRepositoryOwnerPersonal --cli-unfold-argument  \
    --RepoName dockerhub/test \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "RepoInfo": [
                {
                    "RepoName": "dockerhub/test",
                    "RepoType": "QCLOUD HUB",
                    "TagCount": 49,
                    "Public": 1,
                    "IsUserFavor": false,
                    "IsQcloudOfficial": false,
                    "FavorCount": 0,
                    "PullCount": 3727,
                    "Description": "",
                    "CreationTime": "2019-04-26 18:21:48",
                    "UpdateTime": "2020-02-20 16:43:47"
                }
            ],
            "Server": "ccr.ccs.tencentyun.com",
            "TotalCount": 1
        },
        "RequestId": "8e76ee07-c67d-478e-ba2d-b68c17c059f4"
    }
}
```

