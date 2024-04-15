**Example 1: 查询集群版实例信息**



Input: 

```
tccli cdb DescribeClusterInfo --cli-unfold-argument  \
    --InstanceId cdb-xxx
```

Output: 
```
{
    "Response": {
        "ClusterName": "dbname",
        "ReadWriteAddress": {
            "ResourceId": "cdb-xxx",
            "UniqVpcId": "vpc-xxx",
            "UniqSubnetId": "subnet-xxx",
            "Vip": "192.168.3.4",
            "VPort": 3306,
            "WanDomain": "",
            "WanPort": 0
        },
        "ReadOnlyAddress": [
            {
                "ResourceId": "cdb-xxx|readonly",
                "UniqVpcId": "vpc-xxx",
                "UniqSubnetId": "subnet-xxx",
                "Vip": "192.168.3.5",
                "VPort": 3306,
                "WanDomain": "",
                "WanPort": 0
            }
        ],
        "NodeList": [
            {
                "NodeId": "dbn-xxx",
                "Role": "master",
                "Zone": "ap-guangzhou-1",
                "Weight": 1,
                "Status": "online"
            },
            {
                "NodeId": "dbn-xxx",
                "Role": "slave",
                "Zone": "ap-guangzhou-2",
                "Weight": 1,
                "Status": "online"
            }
        ],
        "ReadonlyLimit": 10,
        "NodeCount": 2,
        "RequestId": "abc"
    }
}
```

