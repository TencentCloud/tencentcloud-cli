**Example 1: DescribeImageRepository**



Input: 

```
tccli tsf DescribeImageRepository --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "RequestId": "9cd915d7-f22e-4bb2-904d-4f5c9b002a30",
        "Result": {
            "Content": [
                {
                    "Reponame": "tsf_100010349923/docker-java-provider",
                    "Repotype": "QCLOUD HUB",
                    "TagCount": 0,
                    "IsPublic": 0,
                    "IsUserFavor": false,
                    "IsQcloudOfficial": false,
                    "FavorCount": 0,
                    "PullCount": 0,
                    "Description": "",
                    "CreationTime": "2019-05-29 15:02:08",
                    "UpdateTime": "2019-05-29 15:02:08"
                },
                {
                    "Reponame": "tsf_100010349923/docker-java-consumer",
                    "Repotype": "QCLOUD HUB",
                    "TagCount": 0,
                    "IsPublic": 0,
                    "IsUserFavor": false,
                    "IsQcloudOfficial": false,
                    "FavorCount": 0,
                    "PullCount": 0,
                    "Description": "",
                    "CreationTime": "2019-05-29 15:00:37",
                    "UpdateTime": "2019-05-29 15:00:37"
                }
            ],
            "TotalCount": 2,
            "Server": "ccr.ccs.tencentyun.com"
        }
    }
}
```

