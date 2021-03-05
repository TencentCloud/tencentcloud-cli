**Example 1: 查询集群详情**



Input: 

```
tccli cynosdb DescribeClusterDetail --cli-unfold-argument  \
    --ClusterId cynosdbpg-5804k48e
```

Output: 
```
{
    "Response": {
        "Detail": {
            "UsedStorage": 129417216,
            "VpcId": "vpc-1ptuei0b",
            "SubnetId": "subnet-1tmw9t4o",
            "Vport": 5432,
            "ClusterId": "cynosdbpg-962bpoek",
            "DbType": "POSTGRESQL",
            "SubnetName": "cynosdb-test",
            "CreateTime": "2018-12-03 17:04:07",
            "Charset": "UTF8",
            "Vip": "10.0.1.5",
            "Region": "ap-guangzhou",
            "ClusterName": "funnyTest",
            "StatusDesc": "运行中",
            "DbVersion": "10.0",
            "Status": "running",
            "InstanceSet": [
                {
                    "InstanceStatus": "running",
                    "InstanceCpu": 2,
                    "InstanceStatusDesc": "运行中",
                    "InstanceMemory": 4,
                    "InstanceStorage": 100,
                    "InstanceName": "tom-test11111111",
                    "InstanceType": "POSTGRESQL"
                }
            ],
            "VpcName": "cynosdb"
        },
        "RequestId": "101880"
    }
}
```

