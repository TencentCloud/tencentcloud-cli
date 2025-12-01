**Example 1: 创建主题**



Input: 

```
tccli tdmq CreateRocketMQTopicV2 --cli-unfold-argument  \
    --Topic test_topic \
    --Namespace test_namespace \
    --Type Normal \
    --ClusterId rocketmq-xj8kr5apevj7 \
    --Remark 测试主题 \
    --PartitionNum 3
```

Output: 
```
{
    "Response": {
        "RequestId": "f844f173-93ed-4d89-979e-86e4e1d63b8a"
    }
}
```

