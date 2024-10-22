**Example 1: 修改命名空间信息**

修改命名空间信息

Input: 

```
tccli tdmq ModifyRocketMQNamespace --cli-unfold-argument  \
    --ClusterId rocketmq-xj8kr5apevj7 \
    --NamespaceId test_namespace \
    --Ttl 259200000 \
    --RetentionTime 259200000 \
    --Remark 测试修改 \
    --PublicAccessEnabled True
```

Output: 
```
{
    "Response": {
        "RequestId": "7c995fd0-9a78-4985-8874-244a20a1d47b"
    }
}
```

