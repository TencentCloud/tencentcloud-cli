**Example 1: 修改云数据库实例网络信息**



Input: 

```
tccli mongodb ModifyDBInstanceNetworkAddress --cli-unfold-argument  \
    --InstanceId xx \
    --NetworkAddresses.0.OldIpAddress xx \
    --NetworkAddresses.0.NewIPAddress xx \
    --OldIpExpiredTime 1 \
    --NewUniqVpcId xx \
    --NewUniqSubnetId xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

