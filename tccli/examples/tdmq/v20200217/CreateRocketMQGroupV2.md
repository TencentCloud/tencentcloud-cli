**Example 1: 创建消费组**



Input: 

```
tccli tdmq CreateRocketMQGroupV2 --cli-unfold-argument  \
    --Remark 测试创建 \
    --BroadcastEnable false \
    --ClusterId rocketmq-2p9vx3ax9jxg \
    --RetryMaxTimes 16 \
    --Namespace test_namespace \
    --ReadEnable true \
    --GroupType TCP \
    --GroupId test_group
```

Output: 
```
{
    "Response": {
        "RequestId": "0604a303-6d5f-40e6-9dfe-6c4ddd8fe2df"
    }
}
```

