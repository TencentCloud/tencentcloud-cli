**Example 1: 更换公网IP**

更换CVM实例的普通公网IP

Input: 

```
tccli vpc AdjustPublicAddress --cli-unfold-argument  \
    --InstanceId ins-1vogaxgk
```

Output: 
```
{
    "Response": {
        "TaskId": 5513621,
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```

**Example 2: 更换包月带宽的弹性EIP**

更换包月带宽计费模式的弹性EIP

Input: 

```
tccli vpc AdjustPublicAddress --cli-unfold-argument  \
    --AddressId eip-oy67r5oi
```

Output: 
```
{
    "Response": {
        "TaskId": 5312621,
        "RequestId": "6AF60BEC-0142-43AF-CB20-276271FB54A7"
    }
}
```

