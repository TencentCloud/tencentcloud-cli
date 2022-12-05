**Example 1: 查询镜像信息**

查询镜像信息

Input: 

```
tccli lighthouse DescribeBlueprints --cli-unfold-argument  \
    --BlueprintIds lhbp-5e8807sc
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "BlueprintSet": [
            {
                "BlueprintId": "lhbp-5e8807sc",
                "DisplayTitle": "wordpress",
                "DisplayVersion": "5.3.2",
                "Description": "个人blog建站",
                "OsName": "CentOS-7.6-64bit",
                "Platform": "CENTOS",
                "PlatformType": "LINUX_UNIX",
                "BlueprintType": "APP_OS",
                "ImageUrl": "http://www.wordpress.com/image",
                "RequiredSystemDiskSize": 50,
                "BlueprintState": "NORMAL",
                "CreatedTime": "2020-04-28T03:46:09Z",
                "BlueprintName": "Wordpress",
                "SupportAutomationTools": true,
                "RequiredMemorySize": 1,
                "ImageId": "",
                "SceneIdSet": [],
                "CommunityUrl": "CommunityUrl_test",
                "GuideUrl": "GuideUrl_test"
            }
        ],
        "RequestId": "3df9cd92-cec1-4864-a2a1-358084f41551"
    }
}
```

