**Example 1: 查询实例可重装镜像**

查询实例可重装镜像

Input: 

```
tccli lighthouse DescribeResetInstanceBlueprints --cli-unfold-argument  \
    --InstanceId lhins-euqk4yut
```

Output: 
```
{
    "Response": {
        "RequestId": "d085dd6e-fd50-426f-bb29-b0ed899ccdf7",
        "ResetInstanceBlueprintSet": [
            {
                "BlueprintInfo": {
                    "BlueprintId": "lhbp-m1g6ap11",
                    "BlueprintName": "docker-debian12",
                    "BlueprintShared": false,
                    "BlueprintState": "NORMAL",
                    "BlueprintType": "DOCKER",
                    "CommunityUrl": "",
                    "CreatedTime": "2024-06-12T23:30:03Z",
                    "Description": "test",
                    "DisplayTitle": "7日杀Windows",
                    "DisplayVersion": " ",
                    "DockerVersion": "24.0.7",
                    "GuideUrl": "",
                    "ImageId": "",
                    "ImageUrl": "https://cloudcache.tencent-cloud.com/qcloud/ui/static/static_source_business/f1afb130-22a7-479d-a5a3-013e8f633b5a.svg",
                    "OsName": "Windows Server 2022 DataCenter 64bit CN",
                    "Platform": "WINDOWS",
                    "PlatformType": "WINDOWS",
                    "RequiredMemorySize": 2,
                    "RequiredSystemDiskSize": 50,
                    "SceneIdSet": [],
                    "SupportAutomationTools": true
                },
                "IsResettable": false,
                "NonResettableMessage": "非中国大陆地域不支持Linux系统和Windows系统之间互转。"
            }
        ],
        "TotalCount": 1
    }
}
```

