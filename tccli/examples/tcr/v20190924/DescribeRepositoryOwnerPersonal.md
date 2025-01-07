**Example 1: 查询个人版所有仓库**



Input: 

```
tccli tcr DescribeRepositoryOwnerPersonal --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --RepoName richardgu/hyperkube
```

Output: 
```
{
    "Response": {
        "Data": {
            "RepoInfo": [
                {
                    "CreationTime": "2023-06-20 15:27:03",
                    "Description": "",
                    "FavorCount": 0,
                    "IsQcloudOfficial": false,
                    "IsUserFavor": false,
                    "Public": 1,
                    "PullCount": 0,
                    "RepoName": "richardgu/hyperkube",
                    "RepoType": "QCLOUD HUB",
                    "TagCount": 423,
                    "UpdateTime": "2024-12-30 11:47:17"
                }
            ],
            "Server": "ccr.ccs.tencentyun.com",
            "TotalCount": 1
        },
        "RequestId": "c88a0f09-134d-4422-89bc-a4c7a93b106b"
    }
}
```

