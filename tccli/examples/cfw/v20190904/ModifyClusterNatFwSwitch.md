**Example 1: 修改NAT CCN集群模式防火墙开关配置**

修改NAT CCN集群防火墙的自动接入VPC列表

Input: 

```
tccli cfw ModifyClusterNatFwSwitch --cli-unfold-argument  \
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
        "RequestId": "3ca2bbb3-316f-4255-b169-6e5544c2c70a"
    }
}
```

