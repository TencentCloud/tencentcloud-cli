**Example 1: 请求修改实例VIP示例**



Input: 

```
tccli redis ModifyNetworkConfig --cli-unfold-argument  \
    --InstanceId crs-5a4py64p \
    --Operation changeVip
```

Output: 
```
{
    "Response": {
        "Status": true,
        "Vip": "192.168.1.1",
        "VpcId": "vpc-hu6khgap",
        "SubnetId": "subnet-6mt7lir6",
        "RequestId": "f1b5aabe-806a-4886-b839-9907baa24c85"
    }
}
```

