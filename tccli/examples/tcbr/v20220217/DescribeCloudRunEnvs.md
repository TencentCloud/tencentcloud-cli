**Example 1: DescribeCloudRunEnvs**



Input: 

```
tccli tcbr DescribeCloudRunEnvs --cli-unfold-argument  \
    --EnvId prod-6gvwy9lua50e9504
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
                "PackageId": "basic1",
                "PackageName": "基础版1",
                "IsAutoDegrade": true,
                "EnvChannel": "xx",
                "Region": "xx",
                "IsDefault": true,
                "CreateTime": "2020-09-22T00:00:00+00:00",
                "UpdateTime": "2020-09-22T00:00:00+00:00",
                "EnvType": "tcbr",
                "LogServices": [],
                "StaticStorages": [
                    {
                        "Status": "xx",
                        "StaticDomain": "xx",
                        "DefaultDirName": "xx",
                        "Bucket": "xx",
                        "Region": "xx"
                    }
                ],
                "Databases": [
                    {
                        "InstanceId": "default",
                        "Region": "ap-shanghai",
                        "Status": "RUNNING"
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

**Example 2: success**



Input: 

```
tccli tcbr DescribeCloudRunEnvs --cli-unfold-argument  \
    --Channels 字符串 \
    --EnvId 字符串 \
    --IsVisible true
```

Output: 
```
{
    "Response": {
        "EnvList": [],
        "RequestId": "bf7eb6ec-1ae5-475c-99aa-81c1bd906152"
    }
}
```

