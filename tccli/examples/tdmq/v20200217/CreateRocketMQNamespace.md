**Example 1: 创建命名空间**

创建命名空间

Input: 

```
tccli tdmq CreateRocketMQNamespace --cli-unfold-argument  \
    --ClusterId rocketmq-2p9vx3ax9jxg \
    --NamespaceId example \
    --Ttl 60000 \
    --RetentionTime 600000 \
    --Remark example
```

Output: 
```
{
    "Response": {
        "RequestId": "bf71e2ae-8b56-4231-87cf-0cbb6f421caa"
    }
}
```

