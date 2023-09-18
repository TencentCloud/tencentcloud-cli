**Example 1: 开启公网接入点**



Input: 

```
tccli tdmq SetRocketMQPublicAccessPoint --cli-unfold-argument  \
    --Rules.0.Remark test \
    --Rules.0.IpRule 0.0.0.0/0 \
    --Rules.0.Allow true \
    --PayMode 0 \
    --Bandwidth 10 \
    --InstanceId rocketmq-jxj3wj5j8e7 \
    --Enabled true
```

Output: 
```
{
    "Response": {
        "RequestId": "b28ad6c3-059f-4c38-8a97-a66b3b136a3e"
    }
}
```

