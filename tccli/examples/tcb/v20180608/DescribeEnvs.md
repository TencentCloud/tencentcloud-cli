**Example 1: 分批查询环境信息**



Input: 

```
tccli tcb DescribeEnvs --cli-unfold-argument  \
    --Limit 50 \
    --Offset 100
```

Output: 
```
{
    "Response": {
        "EnvList": [
            {
                "Alias": "env-alias",
                "CreateTime": "2026-04-16 10:32:21",
                "CustomLogServices": [],
                "Databases": [],
                "EnvChannel": "wxrun",
                "EnvId": "env-alias-3gf2x8bcb714facd",
                "EnvType": "run",
                "Functions": [],
                "IsAutoDegrade": false,
                "IsDauPackage": false,
                "IsDefault": false,
                "LogServices": [],
                "Meta": [],
                "PackageId": "",
                "PackageName": "",
                "PackageType": "normal",
                "PayMode": "postpaid",
                "PostgreSQL": [],
                "Region": "ap-shanghai",
                "Source": "miniapp",
                "StaticStorages": [],
                "Status": "NORMAL",
                "Storages": [
                    {
                        "AppId": "",
                        "Bucket": "656e-env-alias",
                        "CdnDomain": "656e-env-alias.tcb.qcloud.la",
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
                "UpdateTime": "2026-04-16 10:32:35"
            }
        ],
        "Total": 10000,
        "RequestId": "3c628980-0441-48d7-a9ca-850209a646c2"
    }
}
```

**Example 2: 查询某个环境的信息**



Input: 

```
tccli tcb DescribeEnvs --cli-unfold-argument  \
    --EnvId pg-cassieluliu-d5gmvd3id25eb60d6
```

Output: 
```
{
    "Response": {
        "EnvList": [
            {
                "Alias": "alias",
                "CreateTime": "2026-05-08 16:31:20",
                "CustomLogServices": [],
                "Databases": [],
                "EnvChannel": "qc_console",
                "EnvId": "alis-d5gmvd3id25eb60d6",
                "EnvType": "baas",
                "Functions": [
                    {
                        "Namespace": "palis-d5gmvd3id25eb60d6",
                        "Region": "ap-shanghai"
                    }
                ],
                "IsAutoDegrade": false,
                "IsDauPackage": false,
                "IsDefault": false,
                "LogServices": [],
                "Meta": [
                    {
                        "Key": "postgresql",
                        "Value": "enable"
                    }
                ],
                "PackageId": "baas_personal",
                "PackageName": "个人版",
                "PackageType": "baas",
                "PayMode": "prepayment",
                "PostgreSQL": [
                    {
                        "InstanceName": "postgres-4**0*5*g",
                        "Name": "postgres",
                        "Region": "ap-shanghai",
                        "Status": 1
                    }
                ],
                "Region": "ap-shanghai",
                "Source": "qcloud",
                "StaticStorages": [
                    {
                        "Bucket": "14c1-st*tic-**-***********-d5g*******5**6**6****9***930",
                        "DefaultDirName": "",
                        "ExternalStorage": {
                            "BasePath": "",
                            "BucketName": "",
                            "Enabled": false,
                            "Region": ""
                        },
                        "Region": "ap-shanghai",
                        "StaticDomain": "asdas-1259548930.tcloudbaseapp.com",
                        "Status": "online"
                    }
                ],
                "Status": "NORMAL",
                "Storages": [
                    {
                        "AppId": "",
                        "Bucket": "7067-asasff-121412430",
                        "CdnDomain": "7067-asafsfafasf-id25eb60d6-112131430.tcb.qcloud.la",
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
                "UpdateTime": "2026-05-08 16:33:26"
            }
        ],
        "Total": 1,
        "RequestId": "332159dc-278e-45b9-ba47-1444e3f35002"
    }
}
```

