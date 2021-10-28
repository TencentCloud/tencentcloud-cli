**Example 1: 修改订阅组**



Input: 

```
tccli tdmq ModifyRocketMQGroup --cli-unfold-argument  \
    --ClusterId rocketmq-2p9vx3ax9jxg \
    --NamespaceId example \
    --GroupId group-example \
    --Remark modified \
    --ReadEnable true \
    --BroadcastEnable false
```

Output: 
```
{
    "Response": {
        "RequestId": "1f9e837c-aab9-4f93-a373-48e165758529"
    }
}
```

