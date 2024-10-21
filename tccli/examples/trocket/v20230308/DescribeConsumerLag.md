**Example 1: 正常响应**

查询指定客户端堆积成功

Input: 

```
tccli trocket DescribeConsumerLag --cli-unfold-argument  \
    --InstanceId rmq-24kzek2b \
    --ConsumerGroup test_group
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "ConsumerLag": 260,
        "RequestId": "2b9eef15-a8bc-47a3-9445-9edcafccb459"
    }
}
```

