**Example 1: 获取公网接入点信息**



Input: 

```
tccli tdmq DescribeRocketMQPublicAccessPoint --cli-unfold-argument  \
    --InstanceId rocketmq-jxj3wj5j8e7
```

Output: 
```
{
    "Response": {
        "RequestId": "086e9401-0674-41f1-a381-9c6a8ba702ea",
        "Status": 0,
        "PayStatus": 1,
        "AccessUrl": "rocketmq-jxj3wj5j8e7.mock-test.com",
        "PayMode": 0,
        "Bandwidth": 0,
        "Rules": [
            {
                "IpRule": "0.0.0.0/0",
                "Allow": true,
                "Remark": "test"
            }
        ]
    }
}
```

