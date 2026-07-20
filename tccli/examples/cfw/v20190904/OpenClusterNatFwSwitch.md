**Example 1: 开启NAT CCN集群模式防火墙开关**

以自动接入+策略路由模式开启NAT CCN集群防火墙开关

Input: 

```
tccli cfw OpenClusterNatFwSwitch --cli-unfold-argument  \
    --NatCcnSwitch.NatInsId nat-3mc7mjzd \
    --NatCcnSwitch.CcnId ccn-c0qmm031 \
    --NatCcnSwitch.SwitchMode 1 \
    --NatCcnSwitch.RoutingMode 1 \
    --NatCcnSwitch.AccessInstanceList.0.InstanceId vpc-henonw6y \
    --NatCcnSwitch.AccessInstanceList.0.InstanceType VPC \
    --NatCcnSwitch.AccessInstanceList.0.InstanceRegion ap-tokyo \
    --NatCcnSwitch.AccessInstanceList.0.AccessCidrMode 1 \
    --NatCcnSwitch.AccessInstanceList.0.AccessCidrList 10.241.0.0/16 \
    --NatCcnSwitch.LeadVpcCidr 
```

Output: 
```
{
    "Response": {
        "RequestId": "9c31338b-27dd-44f2-82e5-84c2c77582a8"
    }
}
```

