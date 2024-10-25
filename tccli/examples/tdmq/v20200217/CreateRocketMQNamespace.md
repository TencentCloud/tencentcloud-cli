**Example 1: 创建命名空间**

创建命名空间

Input: 

```
tccli tdmq CreateRocketMQNamespace --cli-unfold-argument  \
    --ClusterId rocketmq-2p9vx3ax9jxg \
    --NamespaceId test_namespace \
    --Ttl 259200000 \
    --RetentionTime 259200000 \
    --Remark 测试命名空间
```

Output: 
```
{
    "Response": {
        "RequestId": "bf71e2ae-8b56-4231-87cf-0cbb6f421caa"
    }
}
```

