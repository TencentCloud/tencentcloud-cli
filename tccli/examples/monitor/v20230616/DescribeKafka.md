**Example 1: 转发kafka连通性查询**



Input: 

```
tccli monitor DescribeKafka --cli-unfold-argument  \
    --Brokers 11.150.215.105:9092
```

Output: 
```
{
    "Response": {
        "KafkaConnectivityList": [
            {
                "Region": "gz",
                "Result": true
            }
        ],
        "RequestId": "f34f0e91-8fe1-42cc-a22d-8a3a5426c668"
    }
}
```

