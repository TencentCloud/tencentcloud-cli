**Example 1: 查询集群**

查询集群

Input: 

```
tccli oceanus DescribeClusters --cli-unfold-argument  \
    --ClusterIds cluster-5c42n3a5 \
    --Limit 1 \
    --WorkSpaceId space-53rqk422
```

Output: 
```
{
    "Response": {
        "ClusterSet": [
            {
                "AppId": 1234567890,
                "ArchGeneration": 2,
                "AutoRenewFlag": 1,
                "CCNs": [
                    {
                        "CcnId": "",
                        "SubnetId": "subnet-abcdefghijklmno",
                        "VpcId": "vpc-pqrstuvwxyz"
                    }
                ],
                "CLSLogName": "",
                "CLSLogSet": "",
                "CLSTopicId": "",
                "CLSTopicName": "",
                "ClusterId": "cluster-abcd1234",
                "ClusterSessions": [
                    {
                        "AppId": 1234567890,
                        "ClusterGroupSerialId": "cluster-abcd1234",
                        "CreateTime": "2023-11-14 18:07:53",
                        "CreatorUin": "100012345678",
                        "CuNum": 3,
                        "FlinkVersion": "Flink-1.13",
                        "JobManagerCuSpec": 1,
                        "OwnerUin": "100098765432",
                        "Properties": [
                            {
                                "Key": "pipeline.max-parallelism",
                                "Value": "2048"
                            }
                        ],
                        "Region": "ap-guangzhou",
                        "Status": 1,
                        "TaskManagerCuSpec": 1,
                        "TaskManagerNum": 2,
                        "UpdateTime": "2023-11-14 18:09:02",
                        "WebUIUrl": "",
                        "Zone": "ap-guangzhou-7"
                    }
                ],
                "ClusterType": 0,
                "Correlations": [
                    {
                        "ClusterGroupId": 1234,
                        "ClusterGroupSerialId": "cluster-abcd1234",
                        "ClusterName": "sample",
                        "ProjectId": 0,
                        "ProjectIdStr": "0",
                        "Status": 2,
                        "WorkSpaceId": "space-1234567890ap-guangzhou",
                        "WorkSpaceName": "Default"
                    }
                ],
                "CreateTime": "2023-08-15 17:18:08",
                "CreatorUin": "100012345678",
                "CuMem": 4,
                "CuNum": 19,
                "CustomizedDNSEnabled": 1,
                "DefaultCOSBucket": "sample-gz-bucket-1234567890",
                "DefaultLogCollectConf": "{\"LogCollectType\":2,\"Conf\":{\"ClsLogsetId\":\"cd9adbb5-6b7d-48d2-9870-77658959c7a4\",\"ClsTopicId\":\"80856bb3-0ef7-4e05-80eb-79ec283bb67d\",\"CosBucket\":\"\"}}",
                "ExpireTime": "2023-12-04 15:10:29",
                "FreeCu": 9,
                "FreeCuNum": 9,
                "IsNeedManageNode": 1,
                "IsolatedTime": "-",
                "Name": "sample",
                "NetEnvironmentType": 1,
                "Orders": [
                    {
                        "AutoRenewFlag": 1,
                        "ComputeCu": 19,
                        "OperateUin": "100098765432",
                        "OrderTime": "2023-11-04 01:57:54",
                        "Type": 2
                    }
                ],
                "OwnerUin": "100098765432",
                "PayMode": 1,
                "Region": "ap-guangzhou",
                "Remark": "sample",
                "RunningCu": 10,
                "SecondsUntilExpiry": "1223380",
                "SqlGateways": [],
                "Status": 2,
                "StatusDesc": "running",
                "Tags": [
                    {
                        "TagKey": "tag1",
                        "TagValue": "value1"
                    },
                    {
                        "TagKey": "tag2",
                        "TagValue": "value2"
                    }
                ],
                "UpdateTime": "-",
                "Version": {
                    "Flink": "Flink-1.13",
                    "SupportedFlink": [
                        "Flink-1.11",
                        "Flink-1.13",
                        "Flink-1.14",
                        "Flink-1.16"
                    ]
                },
                "WebUIType": 0,
                "Zone": "ap-guangzhou-7"
            }
        ],
        "RequestId": "24d0cbe8-9bd4-4356-bb95-74c5c4790877",
        "TotalCount": 1
    }
}
```

