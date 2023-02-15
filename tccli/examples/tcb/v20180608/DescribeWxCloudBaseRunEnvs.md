**Example 1: DescribeWxCloudBaseRunEnvs**

查询环境列表

Input: 

```
tccli tcb DescribeWxCloudBaseRunEnvs --cli-unfold-argument  \
    --WxAppId xx \
    --AllRegions False
```

Output: 
```
{
    "Response": {
        "EnvList": [
            {
                "Functions": [
                    {
                        "Region": "xx",
                        "Namespace": "xx"
                    }
                ],
                "IsAutoDegrade": true,
                "PackageName": "xx",
                "EnvChannel": "xx",
                "Source": "xx",
                "Storages": [
                    {
                        "CdnDomain": "xx",
                        "Region": "xx",
                        "Bucket": "xx",
                        "AppId": "xx"
                    }
                ],
                "Status": "xx",
                "UpdateTime": "2020-09-22 00:00:00",
                "Tags": [
                    {
                        "Value": "xx",
                        "Key": "xx"
                    }
                ],
                "CustomLogServices": [
                    {
                        "ClsTopicId": "xx",
                        "ClsRegion": "xx",
                        "ClsLogsetId": "xx",
                        "CreateTime": "2020-09-22 00:00:00"
                    }
                ],
                "StaticStorages": [
                    {
                        "Status": "xx",
                        "StaticDomain": "xx",
                        "DefaultDirName": "xx",
                        "Bucket": "xx",
                        "Region": "xx"
                    }
                ],
                "PackageId": "xx",
                "EnvId": "xx",
                "Region": "xx",
                "PayMode": "xx",
                "Alias": "xx",
                "PackageType": "xx",
                "IsDauPackage": true,
                "Databases": [
                    {
                        "InstanceId": "xx",
                        "Status": "xx",
                        "Region": "xx",
                        "UpdateTime": "2020-09-22T00:00:00+00:00"
                    }
                ],
                "IsDefault": true,
                "LogServices": [
                    {
                        "TopicId": "xx",
                        "Region": "xx",
                        "Period": 0,
                        "TopicName": "xx",
                        "LogsetName": "xx",
                        "LogsetId": "xx"
                    }
                ],
                "EnvType": "xx",
                "CreateTime": "2020-09-22 00:00:00"
            }
        ],
        "RequestId": "xx"
    }
}
```

