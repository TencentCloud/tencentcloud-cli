**Example 1: DescribeWxCloudBaseRunEnvs**



Input: 

```
tccli tcb DescribeWxCloudBaseRunEnvs --cli-unfold-argument  \
    --WxAppId xx
```

Output: 
```
{
    "Response": {
        "EnvList": [
            {
                "Status": "xx",
                "PayMode": "xx",
                "UpdateTime": "2020-09-22 00:00:00",
                "EnvId": "xx",
                "Tags": [
                    {
                        "Value": "xx",
                        "Key": "xx"
                    }
                ],
                "PackageName": "xx",
                "IsAutoDegrade": true,
                "Functions": [
                    {
                        "Region": "xx",
                        "Namespace": "xx"
                    }
                ],
                "EnvChannel": "xx",
                "Source": "xx",
                "Alias": "xx",
                "Region": "xx",
                "IsDefault": true,
                "PackageId": "xx",
                "Databases": [
                    {
                        "InstanceId": "xx",
                        "Status": "xx",
                        "Region": "xx"
                    }
                ],
                "Storages": [
                    {
                        "CdnDomain": "xx",
                        "Region": "xx",
                        "Bucket": "xx",
                        "AppId": "xx"
                    }
                ],
                "LogServices": [
                    {
                        "TopicId": "xx",
                        "Region": "xx",
                        "TopicName": "xx",
                        "LogsetName": "xx",
                        "LogsetId": "xx"
                    }
                ],
                "CreateTime": "2020-09-22 00:00:00",
                "StaticStorages": [
                    {
                        "Status": "xx",
                        "StaticDomain": "xx",
                        "DefaultDirName": "xx",
                        "Bucket": "xx",
                        "Region": "xx"
                    }
                ]
            }
        ],
        "RequestId": "xx"
    }
}
```

