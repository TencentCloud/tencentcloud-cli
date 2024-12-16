**Example 1: 获取当月API调用量**

获取当月租户的API调用次数

Input: 

```
tccli tdmq DescribeRocketMQBillingUsage --cli-unfold-argument  \
    --ClusterId rocketmq-xxxxx
```

Output: 
```
{
    "Response": {
        "APIUsage": 1,
        "RequestId": "abc"
    }
}
```

