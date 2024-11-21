**Example 1: 查询集群版实例信息**



Input: 

```
tccli cdb DescribeClusterInfo --cli-unfold-argument  \
    --InstanceId cdb-dctw4edd
```

Output: 
```
{
    "Response": {
        "ClusterName": "dbname",
        "ReadWriteAddress": {
            "ResourceId": "cdb-dctw4edd",
            "UniqVpcId": "vpc-hendkj",
            "UniqSubnetId": "subnet-eushjw",
            "Vip": "192.168.3.4",
            "VPort": 3306,
            "WanDomain": "gz-cdb-*******.sql.tencentcdb.com",
            "WanPort": 23356
        },
        "ReadOnlyAddress": [
            {
                "ResourceId": "cdbro-3a1eccdd",
                "UniqVpcId": "vpc-ehndjs",
                "UniqSubnetId": "subnet-euwhsn",
                "Vip": "192.168.3.5",
                "VPort": 3306,
                "WanDomain": "gz-cdb-*******.sql.tencentcdb.com",
                "WanPort": 23356
            }
        ],
        "NodeList": [
            {
                "NodeId": "dbn-qqeo1111",
                "Role": "master",
                "Zone": "ap-guangzhou-1",
                "Weight": 1,
                "Status": "online"
            },
            {
                "NodeId": "dbn-qqeo2222",
                "Role": "slave",
                "Zone": "ap-guangzhou-2",
                "Weight": 1,
                "Status": "online"
            }
        ],
        "ReadonlyLimit": 10,
        "NodeCount": 2,
        "RequestId": "mnksadas-cb0d-4943-9b17-c3306ed3d"
    }
}
```

