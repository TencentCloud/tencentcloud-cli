**Example 1: 查询环境信息**

查询环境信息 

Input: 

```
tccli tcb DescribeEnvs --cli-unfold-argument  \
    --EnvId yourenvid-2fb346
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "EnvList": [
            {
                "EnvId": "yourenvid-2fb346",
                "PackageType": "",
                "EnvType": "baas",
                "IsDauPackage": false,
                "Source": "miniapp",
                "Alias": "默认环境",
                "Status": "NORMAL",
                "PayMode": "postpaid",
                "Tags": [],
                "PackageName": "free",
                "IsAutoDegrade": true,
                "EnvChannel": "web",
                "Region": "ap-shanghai",
                "IsDefault": true,
                "PackageId": "free",
                "CreateTime": "2018-08-13 10:52:09",
                "UpdateTime": "2018-08-13 10:52:40",
                "LogServices": [],
                "StaticStorages": [],
                "Databases": [
                    {
                        "InstanceId": "default",
                        "Region": "ap-shanghai",
                        "Status": "RUNNING",
                        "UpdateTime": "2023-10-05T14:48:00Z"
                    }
                ],
                "CustomLogServices": [
                    {
                        "ClsTopicId": "topicId",
                        "ClsRegion": "ap-shanghai",
                        "ClsLogsetId": "logset",
                        "CreateTime": "2020-09-22 00:00:00"
                    }
                ],
                "Storages": [
                    {
                        "Region": "ap-shanghai",
                        "Bucket": "yourenvid-2fb346-12532284",
                        "CdnDomain": "yourenvid-2fb346.tcb.qcloud.la",
                        "AppId": "1234567890"
                    }
                ],
                "Functions": [
                    {
                        "Namespace": "yourenvid-2fb346",
                        "Region": "ap-shanghai"
                    }
                ]
            }
        ],
        "RequestId": "75ec26f6-b624-40f1-a3f4-e724843f483e"
    }
}
```

