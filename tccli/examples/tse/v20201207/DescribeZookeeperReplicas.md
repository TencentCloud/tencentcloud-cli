**Example 1: 查询consul类型注册引擎实例副本信息**



Input: 

```
tccli tse DescribeZookeeperReplicas --cli-unfold-argument  \
    --InstanceId ers-12345678
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "xx",
        "Replicas": [
            {
                "Status": "xx",
                "Name": "xx",
                "Zone": "xx",
                "ZoneId": "xx",
                "Role": "xx",
                "SubnetId": "xx"
            }
        ]
    }
}
```

