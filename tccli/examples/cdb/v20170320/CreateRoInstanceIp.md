**Example 1: 创建云数据库只读实例的独立VIP**



Input: 

```
tccli cdb CreateRoInstanceIp --cli-unfold-argument  \
    --InstanceId cdbro-c1nl9rpv \
    --UniqSubnetId subnet-1typ0s7d
```

Output: 
```
{
    "Response": {
        "RoVpcId": 511512,
        "RoSubnetId": 115839,
        "RoVip": "172.0.0.1",
        "RoVport": 3306,
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```

