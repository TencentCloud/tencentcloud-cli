**Example 1: DescribeWxCloudBaseRunEnvs**

查询环境列表

Input: 

```
tccli tcb DescribeWxCloudBaseRunEnvs --cli-unfold-argument  \
    --WxAppId wxappid \
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
                        "Region": "ap-shanghai",
                        "Namespace": "ns"
                    }
                ],
                "IsAutoDegrade": true,
                "PackageName": "package",
                "EnvChannel": "",
                "Source": "",
                "Storages": [
                    {
                        "CdnDomain": "",
                        "Region": "ap-shanghai",
                        "Bucket": "",
                        "AppId": ""
                    }
                ],
                "Status": "",
                "UpdateTime": "2020-09-22 00:00:00",
                "Tags": [
                    {
                        "Value": "",
                        "Key": ""
                    }
                ],
                "CustomLogServices": [
                    {
                        "ClsTopicId": "",
                        "ClsRegion": "",
                        "ClsLogsetId": "",
                        "CreateTime": "2020-09-22 00:00:00"
                    }
                ],
                "StaticStorages": [
                    {
                        "Status": "",
                        "StaticDomain": "",
                        "DefaultDirName": "",
                        "Bucket": "",
                        "Region": "ap-shanghai"
                    }
                ],
                "PackageId": "",
                "EnvId": "",
                "Region": "",
                "PayMode": "",
                "Alias": "",
                "PackageType": "",
                "IsDauPackage": true,
                "Databases": [
                    {
                        "InstanceId": "",
                        "Status": "",
                        "Region": "",
                        "UpdateTime": "2020-09-22T00:00:00+00:00"
                    }
                ],
                "IsDefault": true,
                "LogServices": [
                    {
                        "TopicId": "",
                        "Region": "",
                        "Period": 0,
                        "TopicName": "",
                        "LogsetName": "",
                        "LogsetId": ""
                    }
                ],
                "EnvType": "tcbr",
                "CreateTime": "2020-09-22 00:00:00"
            }
        ],
        "RequestId": "sdfsdf"
    }
}
```

