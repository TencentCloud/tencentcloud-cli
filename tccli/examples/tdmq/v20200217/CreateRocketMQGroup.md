**Example 1: 创建订阅组**



Input: 

```
tccli tdmq CreateRocketMQGroup --cli-unfold-argument  \
    --GroupId group-example \
    --Remark example \
    --ReadEnable true \
    --BroadcastEnable true \
    --ClusterId rocketmq-2p9vx3ax9jxg \
    --Namespaces example
```

Output: 
```
{
    "Response": {
        "RequestId": "0604a303-6d5f-40e6-9dfe-6c4ddd8fe2df"
    }
}
```

