**Example 1: 查询个人版仓库信息**



Input: 

```
tccli tcr DescribeRepositoryPersonal --cli-unfold-argument  \
    --RepoName test/kube_test
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "Data": {
            "CreationTime": "2017-12-28 11:00:10",
            "Description": "",
            "FavorCount": 0,
            "IsQcloudOfficial": false,
            "IsUserFavor": false,
            "Public": 0,
            "PullCount": 0,
            "RepoName": "test/kube_test",
            "RepoType": "QCLOUD HUB"
        }
    }
}
```

