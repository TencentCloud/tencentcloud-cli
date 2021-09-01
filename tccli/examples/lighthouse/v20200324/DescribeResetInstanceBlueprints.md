**Example 1: 查询重置实例的镜像信息**



Input: 

```
tccli lighthouse DescribeResetInstanceBlueprints --cli-unfold-argument  \
    --InstanceId lhins-383nzmm1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ResetInstanceBlueprintSet": [
            {
                "BlueprintInfo": {
                    "BlueprintId": "lhbp-kyfeje6z",
                    "BlueprintName": "my-blueprint2",
                    "DisplayTitle": "wordpress2",
                    "DisplayVersion": "5.3.2",
                    "Description": "个人blog建站",
                    "OsName": "CentOS 7.4 64bit",
                    "Platform": "CENTOS",
                    "PlatformType": "LINUX_UNIX",
                    "BlueprintType": "APP_OS",
                    "ImageUrl": "http://www.wordpress.com/image",
                    "RequiredSystemDiskSize": 10,
                    "RequiredMemorySize": 2,
                    "SupportAutomationTools": true,
                    "BlueprintState": "NORMAL",
                    "CreatedTime": "2020-09-22T00:00:00+00:00",
                    "ImageId": ""
                },
                "IsResettable": false,
                "NonResettableMessage": "The current system disk size of instance does not match the system disk size requirements of the blueprint."
            }
        ],
        "RequestId": "a1768b80-f8f1-47c0-ad60-bb7e3318610b"
    }
}
```

