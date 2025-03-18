**Example 1: 成功示例**



Input: 

```
tccli vdb DescribeInstances --cli-unfold-argument  \
    --Offset 0 \
    --Limit 50
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "AppId": 251223614,
                "Cpu": 1,
                "CreatedAt": "2023-07-07",
                "Disk": 20,
                "EngineName": "",
                "EngineVersion": "",
                "ExpiredAt": "2023-08-07",
                "Extend": "{\"Port\": \"8100\", \"DiskType\": \"CLOUD_SSD\", \"NodeType\": \"Store\", \"Platform\": \"vdb-cd\", \"NodeSpecs\": \"{\\\"Cpu\\\":1,\\\"Memory\\\":8}\", \"NodeNumber\": \"3\", \"DiskCapacity\": \"20\", \"DiskTypeValue\": \"云硬盘\", \"EngineVersion\": \"v1.0.0\", \"NodeTypeValue\": \"存储型\", \"NodeSpecsValue\": \"S.2SMALL\", \"NodeNumberValue\": \"\", \"DiskCapacityValue\": \"\"}",
                "InstanceId": "vdb-77qt0r46",
                "IsNoExpired": false,
                "Memory": 8,
                "Name": "vector_search",
                "Networks": [
                    {
                        "Port": 8100,
                        "SubnetId": "subnet-02bwnv4i",
                        "Vip": "10.0.7.132",
                        "VpcId": "vpc-kddx224l"
                    }
                ],
                "PayMode": 1,
                "Product": "vdb",
                "Project": "",
                "Region": "ap-guangzhou",
                "ReplicaNum": 3,
                "ResourceTags": [],
                "ShardNum": 1,
                "Status": "online",
                "Zone": ""
            },
            {
                "AppId": 251223614,
                "Cpu": 1,
                "CreatedAt": "2023-07-06",
                "Disk": 20,
                "EngineName": "",
                "EngineVersion": "",
                "ExpiredAt": "2023-08-06",
                "Extend": "{\"Port\": \"8100\", \"DiskType\": \"CLOUD_SSD\", \"NodeType\": \"Store\", \"Platform\": \"vdb-cd\", \"NodeSpecs\": \"{\\\"Cpu\\\":1,\\\"Memory\\\":8}\", \"NodeNumber\": \"3\", \"DiskCapacity\": \"20\", \"DiskTypeValue\": \"云硬盘\", \"EngineVersion\": \"v1.0.0\", \"NodeTypeValue\": \"存储型\", \"NodeSpecsValue\": \"S.2SMALL\", \"NodeNumberValue\": \"\", \"DiskCapacityValue\": \"\"}",
                "InstanceId": "vdb-o2ovx6ko",
                "IsNoExpired": false,
                "Memory": 8,
                "Name": "embedding_search",
                "Networks": [
                    {
                        "Port": 8100,
                        "SubnetId": "subnet-02bwnv4i",
                        "Vip": "10.0.7.115",
                        "VpcId": "vpc-kddx224l"
                    }
                ],
                "PayMode": 1,
                "Product": "vdb",
                "Project": "",
                "Region": "ap-guangzhou",
                "ReplicaNum": 3,
                "ResourceTags": [],
                "ShardNum": 1,
                "Status": "online",
                "Zone": ""
            }
        ],
        "RequestId": "2757e3ad-427f-45dc-9119-8c9cfb4ae614",
        "TotalCount": 2
    }
}
```

**Example 2: 查询实例列表**

查询实例列表

Input: 

```
tccli vdb DescribeInstances --cli-unfold-argument  \
    --Offset 0 \
    --Limit 50
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "ApiVersion": "2.0",
                "AppId": 251255497,
                "AutoRenew": 0,
                "Cpu": 1,
                "CreatedAt": "2025-02-24 19:02:40",
                "Disk": 20,
                "EngineName": "",
                "EngineVersion": "v2.3.0",
                "ExpiredAt": "2025-03-24 19:54:40",
                "Extend": "{\"EngineVersion\":\"v1.0.0\",\"FreeApply\":2,\"Mode\":\"two\",\"Platform\":\"vdb\",\"Port\":\"80\",\"Tag\":\"trade\"}",
                "HealthScore": 0,
                "InstanceId": "vdb-mh653rup",
                "IsNoExpired": false,
                "IsolateAt": "",
                "Memory": 2,
                "Name": "vdb-mh653rup",
                "Networks": [],
                "PayMode": 1,
                "Product": "vdb",
                "Project": "",
                "Region": "ap-chengdu",
                "ReplicaNum": 2,
                "ResourceTags": [],
                "ShardNum": 0,
                "Status": "creating",
                "TaskStatus": 0,
                "WanAddress": "",
                "Warning": 0,
                "Zone": ""
            },
            {
                "ApiVersion": "2.0",
                "AppId": 251255497,
                "AutoRenew": 0,
                "Cpu": 1,
                "CreatedAt": "2025-02-24 19:02:45",
                "Disk": 30,
                "EngineName": "",
                "EngineVersion": "v2.3.0",
                "ExpiredAt": "2025-05-24 19:14:44",
                "Extend": "{\"EngineVersion\":\"v1.0.0\",\"FreeApply\":2,\"Mode\":\"two\",\"Platform\":\"vdb\",\"Port\":\"80\",\"Tag\":\"trade\"}",
                "HealthScore": 0,
                "InstanceId": "vdb-bmz0gqmd",
                "IsNoExpired": false,
                "IsolateAt": "",
                "Memory": 2,
                "Name": "vdb-bmz0gqmd",
                "Networks": [
                    {
                        "ExpireTime": "",
                        "Port": 80,
                        "PreserveDuration": 0,
                        "SubnetId": "subnet-8apk7iir",
                        "Vip": "10.10.16.8",
                        "VpcId": "vpc-n4c3s8u4"
                    }
                ],
                "PayMode": 1,
                "Product": "vdb",
                "Project": "",
                "Region": "ap-chengdu",
                "ReplicaNum": 2,
                "ResourceTags": [],
                "ShardNum": 0,
                "Status": "online",
                "TaskStatus": 0,
                "WanAddress": "",
                "Warning": 0,
                "Zone": ""
            }
        ],
        "RequestId": "ebae613a-d963-4979-9764-588ff0a315e3",
        "TotalCount": 2
    }
}
```

