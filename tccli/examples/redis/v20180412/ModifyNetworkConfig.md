**Example 1: 请求修改实例网络配置示例。**

通过该接口修改实例的私有网络。

Input: 

```
tccli redis ModifyNetworkConfig --cli-unfold-argument  \
    --InstanceId crs-5a4p**** \
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
        "TaskId": 0,
        "RequestId": "f1b5aabe-806a-4886-b839-9907baa24c85"
    }
}
```

