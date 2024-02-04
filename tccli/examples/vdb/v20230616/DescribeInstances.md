**Example 1: 示例1**

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
                "AppId": 251223614,
                "Cpu": 1,
                "CreatedAt": "2023-07-07",
                "Disk": 20,
                "EngineName": "",
                "EngineVersion": "",
                "ExpiredAt": "2023-08-07",
                "Extend": "{\"Port\": \"8100\", \"DiskType\": \"CLOUD_SSD\", \"NodeType\": \"Store\", \"Platform\": \"vdb-cd\", \"NodeSpecs\": \"{\\\"Cpu\\\":1,\\\"Memory\\\":8}\", \"NodeNumber\": \"3\", \"DiskCapacity\": \"20\", \"DiskTypeValue\": \"云硬盘\", \"EngineVersion\": \"v1.0.0\", \"NodeTypeValue\": \"存储型\", \"NodeSpecsValue\": \"S.2SMALL\", \"NodeNumberValue\": \"\", \"DiskCapacityValue\": \"\"}",
                "HealthScore": 0,
                "InstanceId": "vdb-77qt0r46",
                "IsNoExpired": false,
                "Memory": 8,
                "Name": "benyqhuang_测试",
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
                "Project": "vdb",
                "Region": "ap-guangzhou",
                "ReplicaNum": 3,
                "ResourceTags": [],
                "ShardNum": 1,
                "Status": "online",
                "Warning": 0,
                "Zone": "ap-guangzhou-3"
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
                "HealthScore": 0,
                "InstanceId": "vdb-o2ovx6ko",
                "IsNoExpired": false,
                "Memory": 8,
                "Name": "ha-test",
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
                "Project": "vdb",
                "Region": "ap-guangzhou",
                "ReplicaNum": 3,
                "ResourceTags": [],
                "ShardNum": 1,
                "Status": "online",
                "Warning": 0,
                "Zone": "ap-guangzhou-3"
            }
        ],
        "RequestId": "2757e3ad-427f-45dc-9119-8c9cfb4ae614",
        "TotalCount": 2
    }
}
```

