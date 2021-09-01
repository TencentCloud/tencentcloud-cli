**Example 1: 查询个人收藏仓库**



Input: 

```
tccli tcr DescribeFavorRepositoryPersonal --cli-unfold-argument  \
    --RepoName mytest/test1234 \
    --Limit 10 \
    --Offset 20
```

Output: 
```
{
    "Response": {
        "Data": {
            "RepoInfo": [
                {
                    "RepoName": "v3test2/mao",
                    "RepoType": "QCLOUD HUB",
                    "PullCount": 0,
                    "FavorCount": 1,
                    "Public": 0,
                    "IsQcloudOfficial": false,
                    "TagCount": 3,
                    "Logo": "",
                    "Region": "gz",
                    "RegionId": 1
                }
            ],
            "TotalCount": 1
        },
        "RequestId": "444332c8-056a-4f8a-899b-16ba6e2d0be5"
    }
}
```

