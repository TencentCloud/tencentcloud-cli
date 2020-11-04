**Example 1: 请求修改实例VIP示例**



Input: 

```
tccli redis ModifyNetworkConfig --cli-unfold-argument  \
    --InstanceId crs-5a4py64p\
    --Operation changeVip
```

Output: 
```
{
    "Response": {
        "status": true,
        "vip": "192.168.1.1",
        "vport": 6379,
        "vpcId": 7678,
        "subnetId": 3545,
        "RequestId": "f1b5aabe-806a-4886-b839-9907baa24c85"
    }
}
```

