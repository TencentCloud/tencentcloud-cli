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
                "AppId": 1257780094,
                "InstanceId": "index-2v3kt0yr",
                "SpaceId": "space-mdo5a8bf",
                "SpaceName": "tom-test",
                "IndexName": "curl-datalink-mdo5a8bf",
                "IndexStorage": 0,
                "IndexCreateTime": "2023-11-23 14:34:55",
                "IndexDocs": 0,
                "Status": 1,
                "IndexSettingsField": {
                    "NumberOfShards": "",
                    "RefreshInterval": "30s"
                },
                "IndexOptionsField": {
                    "ExpireMaxAge": "30d",
                    "TimestampField": "@timestamp"
                },
                "IndexNetworkField": {
                    "Region": "ap-guangzhou",
                    "Zone": "ap-guangzhou-7",
                    "VpcUid": "vpc-444yjczv",
                    "SubnetUid": "subnet-mrezecu2",
                    "Username": "",
                    "Password": ""
                },
                "KibanaUrl": "https://index-2v3kt0yr.kibana.myserverlessindex.com:5601",
                "KibanaPrivateUrl": "",
                "IndexAccessUrl": "index-2v3kt0yr.ap-guangzhou.myserverlessindex.com",
                "StorageType": 0,
                "TagList": []
            },
            {
                "AppId": 1257780094,
                "InstanceId": "index-2s8pkoa7",
                "SpaceId": "space-mdo5a8bf",
                "SpaceName": "tom-test",
                "IndexName": "beats-tke-datalink-mdo5a8bf",
                "IndexStorage": 0,
                "IndexCreateTime": "2023-11-23 14:34:20",
                "IndexDocs": 0,
                "Status": 1,
                "IndexSettingsField": {
                    "NumberOfShards": "",
                    "RefreshInterval": "30s"
                },
                "IndexOptionsField": {
                    "ExpireMaxAge": "30d",
                    "TimestampField": "@timestamp"
                },
                "IndexNetworkField": {
                    "Region": "ap-guangzhou",
                    "Zone": "ap-guangzhou-7",
                    "VpcUid": "vpc-444yjczv",
                    "SubnetUid": "subnet-mrezecu2",
                    "Username": "",
                    "Password": ""
                },
                "KibanaUrl": "https://index-2s8pkoa7.kibana.myserverlessindex.com:5601",
                "KibanaPrivateUrl": "",
                "IndexAccessUrl": "index-2s8pkoa7.ap-guangzhou.myserverlessindex.com",
                "StorageType": 0,
                "TagList": []
            },
            {
                "AppId": 1257780094,
                "InstanceId": "index-7th48x7l",
                "SpaceId": "space-mdo5a8bf",
                "SpaceName": "tom-test",
                "IndexName": "beats-cvm-datalink-mdo5a8bf",
                "IndexStorage": 0,
                "IndexCreateTime": "2023-11-23 14:33:48",
                "IndexDocs": 0,
                "Status": 1,
                "IndexSettingsField": {
                    "NumberOfShards": "",
                    "RefreshInterval": "30s"
                },
                "IndexOptionsField": {
                    "ExpireMaxAge": "30d",
                    "TimestampField": "@timestamp"
                },
                "IndexNetworkField": {
                    "Region": "ap-guangzhou",
                    "Zone": "ap-guangzhou-7",
                    "VpcUid": "vpc-444yjczv",
                    "SubnetUid": "subnet-mrezecu2",
                    "Username": "",
                    "Password": ""
                },
                "KibanaUrl": "https://index-7th48x7l.kibana.myserverlessindex.com:5601",
                "KibanaPrivateUrl": "",
                "IndexAccessUrl": "index-7th48x7l.ap-guangzhou.myserverlessindex.com",
                "StorageType": 0,
                "TagList": []
            },
            {
                "AppId": 1257780094,
                "InstanceId": "index-brjddwvb",
                "SpaceId": "space-mdo5a8bf",
                "SpaceName": "tom-test",
                "IndexName": "tke-data-link-mdo5a8bf",
                "IndexStorage": 0,
                "IndexCreateTime": "2023-11-23 14:30:26",
                "IndexDocs": 0,
                "Status": 1,
                "IndexSettingsField": {
                    "NumberOfShards": "",
                    "RefreshInterval": "30s"
                },
                "IndexOptionsField": {
                    "ExpireMaxAge": "30d",
                    "TimestampField": "@timestamp"
                },
                "IndexNetworkField": {
                    "Region": "ap-guangzhou",
                    "Zone": "ap-guangzhou-7",
                    "VpcUid": "vpc-444yjczv",
                    "SubnetUid": "subnet-mrezecu2",
                    "Username": "",
                    "Password": ""
                },
                "KibanaUrl": "https://index-brjddwvb.kibana.myserverlessindex.com:5601",
                "KibanaPrivateUrl": "",
                "IndexAccessUrl": "index-brjddwvb.ap-guangzhou.myserverlessindex.com",
                "StorageType": 0,
                "TagList": []
            },
            {
                "AppId": 1257780094,
                "InstanceId": "index-k75a66tp",
                "SpaceId": "space-0gyg87rx",
                "SpaceName": "price-test",
                "IndexName": "ychenjiang-test2-0gyg87rx",
                "IndexStorage": 0,
                "IndexCreateTime": "2023-11-23 14:29:47",
                "IndexDocs": 0,
                "Status": 1,
                "IndexSettingsField": {
                    "NumberOfShards": "",
                    "RefreshInterval": "30s"
                },
                "IndexOptionsField": {
                    "ExpireMaxAge": "30d",
                    "TimestampField": "@timestamp"
                },
                "IndexNetworkField": {
                    "Region": "ap-guangzhou",
                    "Zone": "ap-guangzhou-7",
                    "VpcUid": "vpc-ld5dkwwx",
                    "SubnetUid": "subnet-267c2gvq",
                    "Username": "",
                    "Password": ""
                },
                "KibanaUrl": "https://index-k75a66tp.kibana.myserverlessindex.com:5601",
                "KibanaPrivateUrl": "",
                "IndexAccessUrl": "index-k75a66tp.ap-guangzhou.myserverlessindex.com",
                "StorageType": 0,
                "TagList": []
            },
            {
                "AppId": 1257780094,
                "InstanceId": "index-o8otig09",
                "SpaceId": "space-mdo5a8bf",
                "SpaceName": "tom-test",
                "IndexName": "cvm-datalink-mdo5a8bf",
                "IndexStorage": 0,
                "IndexCreateTime": "2023-11-23 14:23:02",
                "IndexDocs": 0,
                "Status": 1,
                "IndexSettingsField": {
                    "NumberOfShards": "",
                    "RefreshInterval": "30s"
                },
                "IndexOptionsField": {
                    "ExpireMaxAge": "30d",
                    "TimestampField": "@timestamp"
                },
                "IndexNetworkField": {
                    "Region": "ap-guangzhou",
                    "Zone": "ap-guangzhou-7",
                    "VpcUid": "vpc-444yjczv",
                    "SubnetUid": "subnet-mrezecu2",
                    "Username": "",
                    "Password": ""
                },
                "KibanaUrl": "https://index-o8otig09.kibana.myserverlessindex.com:5601",
                "KibanaPrivateUrl": "",
                "IndexAccessUrl": "index-o8otig09.ap-guangzhou.myserverlessindex.com",
                "StorageType": 0,
                "TagList": []
            },
            {
                "AppId": 1257780094,
                "InstanceId": "index-gh5rrdhr",
                "SpaceId": "space-0gyg87rx",
                "SpaceName": "price-test",
                "IndexName": "faegagag-0gyg87rx",
                "IndexStorage": 0,
                "IndexCreateTime": "2023-11-23 12:04:48",
                "IndexDocs": 0,
                "Status": 1,
                "IndexSettingsField": {
                    "NumberOfShards": "",
                    "RefreshInterval": "30s"
                },
                "IndexOptionsField": {
                    "ExpireMaxAge": "30d",
                    "TimestampField": "@timestamp"
                },
                "IndexNetworkField": {
                    "Region": "ap-guangzhou",
                    "Zone": "ap-guangzhou-7",
                    "VpcUid": "vpc-444yjczv",
                    "SubnetUid": "subnet-mrezecu2",
                    "Username": "",
                    "Password": ""
                },
                "KibanaUrl": "https://index-gh5rrdhr.kibana.myserverlessindex.com:5601",
                "KibanaPrivateUrl": "",
                "IndexAccessUrl": "index-gh5rrdhr.ap-guangzhou.myserverlessindex.com",
                "StorageType": 0,
                "TagList": []
            },
            {
                "AppId": 1257780094,
                "InstanceId": "index-65q7dsff",
                "SpaceId": "space-0gyg87rx",
                "SpaceName": "price-test",
                "IndexName": "haoa-test3334-0gyg87rx",
                "IndexStorage": 6422689,
                "IndexCreateTime": "2023-11-23 11:53:04",
                "IndexDocs": 0,
                "Status": 1,
                "IndexSettingsField": {
                    "NumberOfShards": "",
                    "RefreshInterval": "30s"
                },
                "IndexOptionsField": {
                    "ExpireMaxAge": "30d",
                    "TimestampField": "@timestamp"
                },
                "IndexNetworkField": {
                    "Region": "ap-guangzhou",
                    "Zone": "ap-guangzhou-7",
                    "VpcUid": "vpc-ld5dkwwx",
                    "SubnetUid": "subnet-267c2gvq",
                    "Username": "",
                    "Password": ""
                },
                "KibanaUrl": "https://index-65q7dsff.kibana.myserverlessindex.com:5601",
                "KibanaPrivateUrl": "",
                "IndexAccessUrl": "index-65q7dsff.ap-guangzhou.myserverlessindex.com",
                "StorageType": 0,
                "TagList": []
            },
            {
                "AppId": 1257780094,
                "InstanceId": "index-irah4s23",
                "SpaceId": "space-mdo5a8bf",
                "SpaceName": "tom-test",
                "IndexName": "cvm-source-mdo5a8bf",
                "IndexStorage": 204964,
                "IndexCreateTime": "2023-11-23 11:39:28",
                "IndexDocs": 0,
                "Status": 1,
                "IndexSettingsField": {
                    "NumberOfShards": "",
                    "RefreshInterval": "30s"
                },
                "IndexOptionsField": {
                    "ExpireMaxAge": "30d",
                    "TimestampField": "@timestamp"
                },
                "IndexNetworkField": {
                    "Region": "ap-guangzhou",
                    "Zone": "ap-guangzhou-7",
                    "VpcUid": "vpc-444yjczv",
                    "SubnetUid": "subnet-mrezecu2",
                    "Username": "",
                    "Password": ""
                },
                "KibanaUrl": "https://index-irah4s23.kibana.myserverlessindex.com:5601",
                "KibanaPrivateUrl": "",
                "IndexAccessUrl": "index-irah4s23.ap-guangzhou.myserverlessindex.com",
                "StorageType": 0,
                "TagList": []
            },
            {
                "AppId": 1257780094,
                "InstanceId": "index-8s7iinrd",
                "SpaceId": "space-0gyg87rx",
                "SpaceName": "price-test",
                "IndexName": "haoa-test44-0gyg87rx",
                "IndexStorage": 6072662,
                "IndexCreateTime": "2023-11-23 11:15:47",
                "IndexDocs": 0,
                "Status": 1,
                "IndexSettingsField": {
                    "NumberOfShards": "",
                    "RefreshInterval": "30s"
                },
                "IndexOptionsField": {
                    "ExpireMaxAge": "30d",
                    "TimestampField": "@timestamp"
                },
                "IndexNetworkField": {
                    "Region": "ap-guangzhou",
                    "Zone": "ap-guangzhou-7",
                    "VpcUid": "vpc-ld5dkwwx",
                    "SubnetUid": "subnet-267c2gvq",
                    "Username": "",
                    "Password": ""
                },
                "KibanaUrl": "https://index-8s7iinrd.kibana.myserverlessindex.com:5601",
                "KibanaPrivateUrl": "",
                "IndexAccessUrl": "index-8s7iinrd.ap-guangzhou.myserverlessindex.com",
                "StorageType": 0,
                "TagList": []
            }
        ],
        "TotalCount": 20,
        "RequestId": "a75f987c-5f03-4fec-bbb8-be132b57666b"
    }
}
```

