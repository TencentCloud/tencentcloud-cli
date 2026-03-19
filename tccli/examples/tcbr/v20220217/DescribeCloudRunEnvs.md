**Example 1: 查询环境信息**



Input: 

```
tccli tcbr DescribeCloudRunEnvs --cli-unfold-argument  \
    --EnvId lowcode-xxxxxx
```

Output: 
```
{
    "Response": {
        "EnvList": [
            {
                "Alias": "lowcode",
                "CreateTime": "2022-04-11 14:00:28",
                "CustomLogServices": [],
                "Databases": [],
                "EnvChannel": "low_code",
                "EnvId": "lowcode-xxxxxx",
                "EnvType": "baas",
                "Functions": [],
                "IsAutoDegrade": false,
                "IsDefault": false,
                "LogServices": [],
                "PackageId": "",
                "PackageName": "",
                "PayMode": "",
                "Region": "ap-shanghai",
                "Source": "qcloud",
                "StaticStorages": [
                    {
                        "Bucket": "8738-static-lowcode-xxxxxx",
                        "DefaultDirName": "",
                        "Region": "ap-shanghai",
                        "StaticDomain": "lowcode-xxxxxx-xxxxxx.tcloudbaseapp.com",
                        "Status": "create_fail"
                    }
                ],
                "Status": "UNAVAILABLE",
                "Storages": [],
                "Tags": [],
                "UpdateTime": "2022-04-11 14:00:28"
            }
        ],
        "RequestId": "ab5ecfa4-9d05-xxxxxx"
    }
}
```

