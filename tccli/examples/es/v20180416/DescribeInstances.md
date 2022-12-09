**Example 1: 查询ES集群实例**



Input: 

```
tccli es DescribeInstances --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "InstanceList": [
            {
                "InstanceId": "es-7sy7efoi",
                "InstanceName": "_some_name_",
                "InstanceType": 2,
                "Region": "ap-guangzhou",
                "Zone": "ap-guangzhou-3",
                "AppId": 130000000,
                "Uin": "100000000",
                "VpcUid": "vpc-xxxxxx",
                "SubnetUid": "subnet-xxxxxx",
                "Status": 1,
                "ChargeType": "POSTPAID_BY_HOUR",
                "ChargePeriod": 0,
                "RenewFlag": "",
                "NodeInfoList": [
                    {
                        "Type": "hotData",
                        "NodeNum": 3,
                        "NodeType": "ES.SA2.MEDIUM4",
                        "DiskType": "CLOUD_SSD",
                        "DiskSize": 20,
                        "DiskEncrypt": 0,
                        "DiskCount": 1,
                        "LocalDiskInfo": null
                    }
                ],
                "NodeType": "ES.SA2.MEDIUM4",
                "NodeNum": 3,
                "CpuNum": 2,
                "MemSize": 4,
                "DiskType": "CLOUD_SSD",
                "AutoIndexEnabled": true,
                "DiskSize": 20,
                "EnableHotWarmMode": false,
                "WarmNodeType": "",
                "WarmNodeNum": 0,
                "WarmCpuNum": 0,
                "WarmMemSize": 0,
                "WarmDiskType": "",
                "WarmDiskSize": 0,
                "ColdNodeType": "",
                "ColdNodeNum": 0,
                "ColdCpuNum": 0,
                "ColdMemSize": 0,
                "ColdDiskType": "",
                "ColdDiskSize": 0,
                "FrozenNodeType": "",
                "FrozenNodeNum": 0,
                "FrozenCpuNum": 0,
                "FrozenMemSize": 0,
                "FrozenDiskType": "",
                "FrozenDiskSize": 0,
                "MasterNodeInfo": {
                    "EnableDedicatedMaster": false,
                    "MasterNodeType": "",
                    "MasterNodeNum": 0,
                    "MasterNodeCpuNum": 0,
                    "MasterNodeMemSize": 0,
                    "MasterNodeDiskType": "",
                    "MasterNodeDiskSize": 0
                },
                "KibanaNodeInfo": {
                    "KibanaNodeType": "ES.SA2.SMALL2",
                    "KibanaNodeNum": 1,
                    "KibanaNodeCpuNum": 1,
                    "KibanaNodeMemSize": 2,
                    "KibanaNodeDiskType": "CLOUD_PREMIUM",
                    "KibanaNodeDiskSize": 50
                },
                "EsDomain": "es-7sy7efoi.myelasticsearch.com",
                "EsPrivateDomain": "es-7sy7efoi-esinternal.kibana.myelasticsearch.com",
                "EsVip": "{vip}",
                "EsPort": 9200,
                "KibanaUrl": "https://es-7sy7efoi.kibana.myelasticsearch.com:5601",
                "KibanaPrivateUrl": "",
                "PublicAccess": "CLOSE",
                "KibanaPublicAccess": "OPEN",
                "KibanaPrivateAccess": "CLOSE",
                "KibanaAlteringPublicAccess": "CLOSE",
                "Protocol": "",
                "SecurityGroups": [],
                "EsPublicUrl": "",
                "EsPrivateUrl": "https://es-7sy7efoi-esinternal.kibana.myelasticsearch.com:9200",
                "EsVersion": "7.14.2",
                "EsConfig": "{}",
                "EsConfigSets": [],
                "KibanaConfig": "",
                "EsAcl": {
                    "WhiteIpList": [
                        "127.0.0.1"
                    ],
                    "BlackIpList": []
                },
                "EsPublicAcl": {
                    "WhiteIpList": [],
                    "BlackIpList": []
                },
                "IkConfig": {
                    "UpdateType": "",
                    "MainDict": [],
                    "Stopwords": [],
                    "Synonym": [],
                    "QQDict": []
                },
                "AllowCosBackup": true,
                "CosBackup": {
                    "IsAutoBackup": false,
                    "BackupTime": ""
                },
                "DeployMode": 0,
                "MultiZoneInfo": [
                    {
                        "Zone": "ap-guangzhou-3",
                        "SubnetId": "subnet-q29llw8g"
                    }
                ],
                "TagList": [],
                "HealthStatus": 0,
                "SecurityType": 2,
                "LicenseType": "platinum",
                "SceneType": 1,
                "Jdk": "kona",
                "WebNodeTypeInfo": {
                    "NodeNum": 1,
                    "NodeType": "ES.SA2.SMALL2"
                },
                "CreateTime": "2022-07-06 20:52:48",
                "UpdateTime": "2022-07-07 17:35:29",
                "Deadline": "2017-12-04 00:00:00",
                "OperationDuration": null,
                "OptionalWebServiceInfos": [
                    {
                        "Status": 0,
                        "PrivateAccess": "xx",
                        "PublicAccess": "xx",
                        "PrivateUrl": "xx",
                        "Version": "xx",
                        "Type": "xx",
                        "PublicUrl": "xx"
                    }
                ],
                "ProcessPercent": 0.5,
                "EnableHybridStorage": true
            }
        ],
        "RequestId": "xxxx"
    }
}
```

