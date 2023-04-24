**Example 1: 修改RocketMQ专享实例规格**

对实例进行升降配

Input: 

```
tccli tdmq ModifyRocketMQInstanceSpec --cli-unfold-argument  \
    --InstanceId abc \
    --Specification abc \
    --NodeCount 1 \
    --StorageSize 1
```

Output: 
```
{
    "Response": {
        "OrderId": "abc",
        "RequestId": "abc"
    }
}
```

