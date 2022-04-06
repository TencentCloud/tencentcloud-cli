**Example 1: 修改云数据库实例网络信息**

如需修改云数据库实例的网络信息，如基础网络转VPC网络和VPC网络之间的变换。

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

