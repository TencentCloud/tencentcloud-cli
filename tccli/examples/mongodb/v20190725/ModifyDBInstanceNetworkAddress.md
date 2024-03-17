**Example 1: 修改云数据库实例网络信息**

修改云数据库实例的VIP信息

Input: 

```
tccli mongodb ModifyDBInstanceNetworkAddress --cli-unfold-argument  \
    --InstanceId cmgo-9d0p**** \
    --OldIpExpiredTime 1 \
    --NetworkAddresses.0.NewIPAddress 10.0.0.10 \
    --NetworkAddresses.0.OldIpAddress 10.0.0.1 \
    --NewUniqVpcId vpc-gfb3pqo1 \
    --NewUniqSubnetId ins-wsdn61fw
```

Output: 
```
{
    "Response": {
        "FlowId": 1679402995,
        "RequestId": "8279f6c2-db93-4b2e-931b-233d780b1a91"
    }
}
```

