**Example 1: 重发死信消息**



Input: 

```
tccli tdmq RetryRocketMQDlqMessage --cli-unfold-argument  \
    --NamespaceId test_ns \
    --ClusterId rocketmq-a52qova7x97b \
    --GroupName test_group \
    --MessageIds 01963F0B14BAF09F27077D244F00000000
```

Output: 
```
{
    "Response": {
        "RequestId": "90760e40-5db2-4150-807f-5760c2a03804"
    }
}
```

