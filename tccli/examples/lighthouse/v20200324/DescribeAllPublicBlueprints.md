**Example 1: 查询全地域镜像信息**



Input: 

```
tccli lighthouse DescribeAllPublicBlueprints --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "423366c9-c0c2-451d-8e9d-e332eb7d9099",
        "TotalCount": 3,
        "BlueprintInfoSet": [
            {
                "BlueprintId": "lhbp-j9flli0n",
                "DisplayTitle": "CentOS-7.6-m",
                "DisplayVersion": "7.6-m",
                "Description": "CentOS是一款流行的开源Linux发行版，是RHEL（Red Hat Enterprise Linux）源代码经过再编译而成。",
                "OsName": "CentOS 7.6 64bit",
                "Platform": "CENTOS",
                "PlatformType": "",
                "BlueprintType": "APP_OS",
                "ImageUrl": "http://abc.png-m",
                "RequiredSystemDiskSize": 20,
                "BlueprintState": "NORMAL",
                "CreatedTime": "2022-08-31T09:56:40+08:00",
                "BlueprintName": "centos",
                "SupportAutomationTools": true,
                "RequiredMemorySize": 2,
                "SceneIdSet": [],
                "CommunityUrl": "",
                "GuideUrl": "",
                "DockerVersion": "",
                "RegionSet": [
                    "ap-hongkong"
                ]
            }
        ]
    }
}
```

