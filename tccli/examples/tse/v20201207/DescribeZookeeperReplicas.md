**Example 1: 查询 Zookeeper 类型注册引擎实例副本信息**



Input: 

```
tccli tse DescribeZookeeperReplicas --cli-unfold-argument  \
    --InstanceId ers-12345678
```

Output: 
```
{
    "Response": {
        "Replicas": [
            {
                "Name": "abc",
                "Role": "Leader",
                "Status": "running",
                "SubnetId": "subnet-xxx",
                "Zone": "ap-guangzhou-1",
                "ZoneId": "100000",
                "AliasName": "abc",
                "VpcId": "vpc-xxx"
            }
        ],
        "TotalCount": 1,
        "RequestId": "abc"
    }
}
```

