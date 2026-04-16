**Example 1: 查询指定环境信息**



Input: 

```
tccli tcb DescribeEnvInfoInner --cli-unfold-argument  \
    --EnvId goreliu-1-0gvmsp6sd8c22011
```

Output: 
```
{
    "Response": {
        "EnvInfo": {
            "BillingInfo": {
                "CreateTime": "2026-04-10 00:31:31",
                "EnableOverrun": false,
                "EnvActivated": "no",
                "EnvCharged": "yes",
                "EnvId": "goreliu-1-0gvmsp6sd8c22011",
                "ExpireTime": "2026-05-10 23:59:59",
                "ExtPackageType": "baas",
                "FreeQuota": "",
                "IsAlwaysFree": false,
                "IsAutoRenew": false,
                "IsolatedTime": "",
                "OrderInfo": {
                    "CreateTime": "",
                    "ExtensionId": "",
                    "Flag": "",
                    "PackageId": "",
                    "PayMode": "",
                    "ReqBody": "",
                    "ResourceReady": "",
                    "TranId": "",
                    "TranStatus": "",
                    "TranType": "",
                    "UpdateTime": ""
                },
                "PackageId": "baas_personal",
                "PayMode": "PREPAYMENT",
                "PaymentChannel": "",
                "Status": "NORMAL",
                "UpdateTime": ""
            },
            "CircleEndTime": "2026-05-10 23:59:59",
            "CircleStartTime": "2026-04-10 00:31:31",
            "Eid": 3772064,
            "EnvBaseInfo": {
                "Alias": "goreliu-1",
                "CreateTime": "2026-04-10 00:31:22",
                "CustomLogServices": [],
                "Databases": [
                    {
                        "InstanceId": "tnt-9nliy625w",
                        "Region": "ap-shanghai",
                        "Status": "RUNNING",
                        "UpdateTime": "2026-04-10 00:31:31"
                    }
                ],
                "EnvChannel": "qc_console",
                "EnvId": "goreliu-1-0gvmsp6sd8c22011",
                "EnvPreferences": [
                    {
                        "Key": "Staging",
                        "Value": "off"
                    }
                ],
                "EnvStatus": "NORMAL",
                "EnvType": "baas",
                "Functions": [
                    {
                        "Namespace": "goreliu-1-0gvmsp6sd8c22011",
                        "Region": "ap-shanghai"
                    }
                ],
                "IsAutoDegrade": false,
                "IsDauPackage": false,
                "IsDefault": false,
                "LogServices": [],
                "Meta": [],
                "PackageId": "baas_personal",
                "PackageName": "个人版",
                "PackageType": "baas",
                "PayMode": "prepayment",
                "PostgreSQL": [],
                "Region": "ap-shanghai",
                "Source": "qcloud",
                "StaticStorages": [
                    {
                        "Bucket": "5512-static-goreliu-1-0gvmsp6sd8c22011-1259548930",
                        "DefaultDirName": "",
                        "ExternalStorage": {
                            "BasePath": "",
                            "BucketName": "",
                            "Enabled": false,
                            "Region": ""
                        },
                        "Region": "ap-shanghai",
                        "StaticDomain": "goreliu-1-0gvmsp6sd8c22011-1259548930.tcloudbaseapp.com",
                        "Status": "online"
                    }
                ],
                "Status": "NORMAL",
                "Storages": [
                    {
                        "AppId": "",
                        "Bucket": "676f-goreliu-1-0gvmsp6sd8c22011-1259548930",
                        "CdnDomain": "676f-goreliu-1-0gvmsp6sd8c22011-1259548930.tcb.qcloud.la",
                        "ExternalStorage": {
                            "BasePath": "",
                            "BucketName": "",
                            "Enabled": false,
                            "Region": ""
                        },
                        "Region": "ap-shanghai"
                    }
                ],
                "Tags": [],
                "UpdateTime": "2026-04-10 00:31:31"
            },
            "SiteFlag": "cn",
            "UserInfo": {
                "AppId": 1259548930,
                "CreateTime": "",
                "OpenAppId": "",
                "Uin": 100010683263,
                "UpdateTime": "",
                "WxAppId": "wx54b29eb8f62a4731"
            }
        },
        "RequestId": "2f8da793-126a-4ad5-b07b-437dcb7d5aef"
    }
}
```

