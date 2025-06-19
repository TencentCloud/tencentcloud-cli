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
        "Result": {
            "TotalCount": 0,
            "Server": "ccr.tencent.com",
            "Content": [
                {
                    "Reponame": "tsf_100010349923/docker-java-provider",
                    "Repotype": "tcr",
                    "TagCount": 0,
                    "IsPublic": 0,
                    "IsUserFavor": true,
                    "IsQcloudOfficial": true,
                    "FavorCount": 0,
                    "PullCount": 0,
                    "Description": "this is a desc",
                    "CreationTime": "2019-05-29 15:02:08",
                    "UpdateTime": "2019-05-29 15:02:08",
                    "TcrRepoInfo": {
                        "RepoName": "name",
                        "Region": "ap-guangzhou",
                        "RegistryId": "reg-6a79x94v",
                        "RegistryName": "reg-mock",
                        "Namespace": "default"
                    },
                    "TcrBindingId": 0,
                    "ApplicationId": "application-6a79x94v",
                    "ApplicationName": {
                        "RuleId": "rule-6a79x94v",
                        "Name": "app-mock",
                        "ExpandVmCountLimit": 0,
                        "ShrinkVmCountLimit": 0,
                        "GroupCount": 0,
                        "Desc": "this is a desc",
                        "Description": "this is a desc",
                        "DisableMetricAS": 1,
                        "EnableCronAS": 1
                    },
                    "ApplicationNameReal": "app-mock",
                    "Public": 0,
                    "CreateMode": "manual"
                }
            ]
        },
        "RequestId": "96561cf1-738a-47d6-943b-dec7ebbccabe"
    }
}
```

