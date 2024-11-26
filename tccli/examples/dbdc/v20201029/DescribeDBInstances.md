**Example 1: 查询独享集群内的DB实例列表**



Input: 

```
tccli dbdc DescribeDBInstances --cli-unfold-argument  \
    --InstanceId dbdc-56nsyijj
```

Output: 
```
{
    "Response": {
        "Instances": [
            {
                "Cpu": 2,
                "CreateTime": "2018-05-15 10:30:00",
                "DbEngine": "MariaDB",
                "DbHosts": "svr-buhfdoz8,svr-d5vaw4us,svr-q87ur6lu",
                "DbVersion": "10.0.10",
                "Disk": 50,
                "HostRole": 0,
                "InstanceId": "tdsql-3q78d56r",
                "InstanceName": "tdsql-3q78d56r",
                "Memory": 4,
                "NodeNum": 3,
                "Region": "ap-guangzhou",
                "Shard": 0,
                "ShardNum": 0,
                "Status": 2,
                "StatusDesc": "运行中",
                "UniqueSubnetId": "subnet-dlcm2zne",
                "UniqueVpcId": "vpc-fn7ejibv",
                "Vip": "10.10.100.59",
                "Vport": 3306,
                "Zone": "ap-guangzhou-3"
            }
        ],
        "RequestId": "8cf4daa6-b172-11eb-94d3-525400542aa6",
        "TotalCount": 1
    }
}
```

