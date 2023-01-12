**Example 1: 创建主题**

创建主题

Input: 

```
tccli tdmq CreateRocketMQTopic --cli-unfold-argument  \
    --Topic example-topic \
    --Type Normal \
    --Remark example \
    --ClusterId rocketmq-2p9vx3ax9jxg \
    --Namespaces example
```

Output: 
```
{
    "Response": {
        "RequestId": "f844f173-93ed-4d89-979e-86e4e1d63b8a"
    }
}
```

