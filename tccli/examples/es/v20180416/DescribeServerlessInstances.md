**Example 1: Serverless获取索引列表**

Serverless获取索引列表

Input: 

```
tccli es DescribeServerlessInstances --cli-unfold-argument  \
    --IndexNames test \
    --InstanceIds index-abcdefgh \
    --Limit 0 \
    --Offset 10
```

Output: 
```
{
    "Response": {
        "IndexMetaFields": [
            {
                "AppId": 1,
                "IndexName": "abc",
                "IndexDocs": 0,
                "IndexStorage": 0,
                "IndexCreateTime": "abc",
                "InstanceId": "abc",
                "IndexOptionsField": {
                    "ExpireMaxAge": "abc",
                    "TimestampField": "abc"
                },
                "IndexSettingsField": {
                    "NumberOfShards": "abc",
                    "RefreshInterval": "abc"
                },
                "IndexNetworkField": {
                    "Region": "abc",
                    "Zone": "abc",
                    "VpcUid": "abc",
                    "SubnetUid": "abc",
                    "Username": "abc",
                    "Password": "abc"
                },
                "KibanaUrl": "abc",
                "KibanaPrivateUrl": "abc",
                "IndexAccessUrl": "abc",
                "KibanaPublicAcl": {
                    "BlackIpList": [
                        "abc"
                    ],
                    "WhiteIpList": [
                        "abc"
                    ]
                },
                "Status": 0,
                "SpaceId": "abc",
                "SpaceName": "abc",
                "DiDataList": [
                    {
                        "DiId": "abc",
                        "CreateTime": "abc",
                        "Status": 0,
                        "DiDataSourceCvm": {
                            "VpcId": "abc",
                            "LogPaths": [
                                "abc"
                            ],
                            "CvmInstances": [
                                {
                                    "InstanceId": "abc",
                                    "VpcId": "abc",
                                    "SubnetId": "abc",
                                    "ErrMsg": "abc"
                                }
                            ],
                            "CollectorId": "abc"
                        },
                        "DiDataSourceTke": {
                            "VpcId": "abc",
                            "TkeId": "abc",
                            "CollectorName": "abc",
                            "CollectorVersion": "abc",
                            "CollectorType": "abc",
                            "IncludeNamespaces": [
                                "abc"
                            ],
                            "ExcludeNamespaces": [
                                "abc"
                            ],
                            "PodLabelKeys": [
                                "abc"
                            ],
                            "PodLabelValues": [
                                "abc"
                            ],
                            "ContainerName": "abc",
                            "ConfigContent": "abc",
                            "CollectorId": "abc"
                        },
                        "DiDataSinkServerless": {
                            "ServerlessId": "abc"
                        }
                    }
                ],
                "Username": "abc",
                "StorageType": 0
            }
        ],
        "TotalCount": 0,
        "RequestId": "abc"
    }
}
```

