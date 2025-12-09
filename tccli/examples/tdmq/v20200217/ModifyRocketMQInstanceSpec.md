**Example 1: 修改RocketMQ专享实例规格**

对实例进行升降配

Input: 

```
tccli tdmq ModifyRocketMQInstanceSpec --cli-unfold-argument  \
    --InstanceId rocketmq-4k4orqgq \
    --Specification rocket-vip-basic-1 \
    --NodeCount 2 \
    --StorageSize 1000
```

Output: 
```
{
    "Response": {
        "OrderId": "20230720073017608094121",
        "RequestId": "23ca1a58-0388-4d2d-8465-653a53addda7"
    }
}
```

