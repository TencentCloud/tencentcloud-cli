**Example 1: 获取实例Prometheus信息**



Input: 

```
tccli ckafka DescribePrometheus --cli-unfold-argument  \
    --InstanceId ckafka-test
```

Output: 
```
{
    "Response": {
        "Result": [
            {
                "Type": "jmx_export",
                "SourceIp": "10.0.0.5",
                "SourcePort": 9090,
                "BrokerIp": "10.0.0.30",
                "VpcId": "vpc-test",
                "SubnetId": "subnet-test"
            }
        ],
        "RequestId": "d173b4fb-c6d0-4507-a822-b6f277fc4016"
    }
}
```

