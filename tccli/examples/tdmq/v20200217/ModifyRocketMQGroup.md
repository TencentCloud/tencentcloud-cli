**Example 1: 修改订阅组**



Input: 

```
tccli tdmq ModifyRocketMQGroup --cli-unfold-argument  \
    --Remark modified \
    --BroadcastEnable false \
    --ClusterId rocketmq-2p9vx3ax9jxg \
    --GroupId group-example \
    --RetryMaxTimes 16 \
    --ReadEnable true \
    --NamespaceId example
```

Output: 
```
{
    "Response": {
        "RequestId": "1f9e837c-aab9-4f93-a373-48e165758529"
    }
}
```

