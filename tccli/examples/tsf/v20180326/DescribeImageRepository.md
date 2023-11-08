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
                    "Repotype": "tcr",
                    "TagCount": 0,
                    "IsPublic": 0,
                    "IsUserFavor": false,
                    "IsQcloudOfficial": false,
                    "FavorCount": 0,
                    "PullCount": 0,
                    "Description": "",
                    "CreationTime": "2019-05-29 15:02:08",
                    "UpdateTime": "2019-05-29 15:02:08",
                    "TcrRepoInfo": {
                        "Region": "1",
                        "RegistryId": "id",
                        "RegistryName": "tsf/nginx",
                        "Namespace": "tsf",
                        "RepoName": "nginx"
                    },
                    "TcrBindingId": null,
                    "ApplicationId": "abc",
                    "ApplicationName": null,
                    "ApplicationNameReal": "abc",
                    "Public": 0
                }
            ],
            "TotalCount": 2,
            "Server": "ccr.ccs.tencentyun.com"
        }
    }
}
```

