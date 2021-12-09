**Example 1: 查询镜像实例信息**



Input: 

```
tccli lighthouse DescribeBlueprintInstances --cli-unfold-argument  \
    --InstanceIds lhins-f4s49nap
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "BlueprintInstanceSet": [
            {
                "InstanceId": "lhins-aaaabbbb",
                "Blueprint": {
                    "BlueprintId": "lhbp-5e8807sc",
                    "DisplayTitle": "wordpress",
                    "DisplayVersion": "5.3.2",
                    "Description": "个人blog建站",
                    "OsName": "CentOS-7.6-64bit",
                    "Platform": "CENTOS",
                    "PlatformType": "LINUX_UNIX",
                    "BlueprintName": "my-blueprint",
                    "BlueprintType": "APP_OS",
                    "ImageUrl": "http://www.wordpress.com/image",
                    "RequiredMemorySize": 2,
                    "RequiredSystemDiskSize": 10,
                    "BlueprintState": "NORMAL",
                    "SupportAutomationTools": true,
                    "CreatedTime": "2020-09-22T00:00:00+00:00",
                    "ImageId": "img-f82x5lxe"
                },
                "SoftwareSet": [
                    {
                        "Name": "wordpress",
                        "Version": "5.3.2",
                        "ImageUrl": "",
                        "InstallDir": "/usr/local/lighthouse/softwares/wordpress",
                        "DetailSet": [
                            {
                                "Key": "IndexUrl",
                                "Title": "首页地址",
                                "Value": "http://xxx.xxx.xxx.xxx"
                            }
                        ]
                    }
                ]
            }
        ],
        "RequestId": "989f74ea-567c-4c99-a24e-7bc200cf679b"
    }
}
```

