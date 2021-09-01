**Example 1: 查询环境信息**



Input: 

```
tccli tcb DescribeEnvs --cli-unfold-argument  \
    --EnvId yourenvid-2fb346
```

Output: 
```
{
    "Response": {
        "EnvList": [
            {
                "EnvId": "yourenvid-2fb346",
                "Source": "miniapp",
                "Alias": "默认环境",
                "Status": "NORMAL",
                "PayMode": "postpaid",
                "Tags": [],
                "PackageName": "free",
                "IsAutoDegrade": true,
                "EnvChannel": "xx",
                "Region": "xx",
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
                        "Status": "RUNNING"
                    }
                ],
                "Storages": [
                    {
                        "Region": "ap-shanghai",
                        "Bucket": "yourenvid-2fb346-12532284",
                        "CdnDomain": "yourenvid-2fb346.tcb.qcloud.la",
                        "AppId": "xx"
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

