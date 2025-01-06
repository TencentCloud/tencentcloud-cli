**Example 1: 获取满足输入搜索条件的个人版镜像仓库**



Input: 

```
tccli tcr DescribeRepositoryFilterPersonal --cli-unfold-argument  \
    --RepoName golang-test \
    --Offset 0 \
    --Limit 10 \
    --Public 0 \
    --Namespace nicokang
```

Output: 
```
{
    "Response": {
        "Data": {
            "PrivilegeFiltered": false,
            "RepoInfo": [
                {
                    "CreationTime": "2024-11-09 16:11:32",
                    "Description": "",
                    "FavorCount": 0,
                    "IsQcloudOfficial": false,
                    "IsUserFavor": false,
                    "Public": 0,
                    "PullCount": 0,
                    "RepoName": "nicokang/golang-test",
                    "RepoType": "QCLOUD HUB",
                    "TagCount": 1,
                    "UpdateTime": "2024-11-12 17:29:20"
                }
            ],
            "Server": "ccr.ccs.tencentyun.com",
            "TotalCount": 1
        },
        "RequestId": "86ad9298-a532-4102-ba2a-b87b55e589fa"
    }
}
```

