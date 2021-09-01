**Example 1: 创建HAVIP**



Input: 

```
tccli ecm CreateHaVip --cli-unfold-argument  \
    --VpcId vpc-m0c2kcun \
    --SubnetId subnet-rtmfkg4w \
    --HaVipName irang_testHaVip
```

Output: 
```
{
    "Response": {
        "HaVip": {
            "AddressIp": "",
            "CreatedTime": "2020-10-29 16:54:45",
            "HaVipId": "havip-kekyk044",
            "HaVipName": "irang_testHaVip",
            "InstanceId": "",
            "NetworkInterfaceId": "",
            "State": "UNBIND",
            "SubnetId": "subnet-rtmfkg4w",
            "Vip": "172.16.0.17",
            "VpcId": "vpc-m0c2kcun",
            "Business": "xx"
        },
        "RequestId": "d7226510-434e-4896-bdcd-fb1234aaafdfa"
    }
}
```

