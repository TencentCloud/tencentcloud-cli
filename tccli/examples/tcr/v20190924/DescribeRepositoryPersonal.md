**Example 1: 查询个人版仓库信息**



Input: 

```
tccli tcr DescribeRepositoryPersonal --cli-unfold-argument  \
    --RepoName richardgu/hyperkube
```

Output: 
```
{
    "Response": {
        "Data": {
            "CreationTime": "2023-06-20 15:27:03",
            "Description": "",
            "FavorCount": 0,
            "IsQcloudOfficial": false,
            "IsUserFavor": false,
            "Public": 1,
            "PullCount": 0,
            "RepoName": "richardgu/hyperkube",
            "RepoType": "QCLOUD HUB",
            "Server": "ccr.ccs.tencentyun.com"
        },
        "RequestId": "8ce48e45-dd95-48c9-ba00-801ab1054323"
    }
}
```

