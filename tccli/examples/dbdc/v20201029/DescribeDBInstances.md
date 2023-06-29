**Example 1: 查询独享集群内的DB实例列表**



Input: 

```
tccli dbdc DescribeDBInstances --cli-unfold-argument  \
    --InstanceId dbdc-test
```

Output: 
```
{
    "Response": {
        "Instances": [
            {
                "InstanceId": "dbdc-test",
                "InstanceName": "test",
                "Status": 1,
                "StatusDesc": "运行中",
                "DbVersion": "5.7.17",
                "DbEngine": "MySQL",
                "Vip": "10.0.0.1",
                "Vport": 3306,
                "UniqueVpcId": "vpc-test",
                "UniqueSubnetId": "subnet-test",
                "Shard": 0,
                "NodeNum": 2,
                "Cpu": 2,
                "Memory": 10,
                "Disk": 10,
                "ShardNum": 0,
                "Region": "ap-guangzhou",
                "Zone": "ap-guangzhou-1",
                "DbHosts": "svr-test1|svr-test2",
                "HostRole": 0,
                "CreateTime": "2022-05-20 12:00:00"
            }
        ],
        "RequestId": "8cf4daa6-b172-11eb-94d3-525400542aa6",
        "TotalCount": 1
    }
}
```

