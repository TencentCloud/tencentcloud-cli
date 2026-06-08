**Example 1: 修改NAT CCN集群模式防火墙开关配置**

修改NAT CCN集群防火墙的自动接入VPC列表

Input: 

```
tccli cfw ModifyClusterNatFwSwitch --cli-unfold-argument  \
    --NatCcnSwitch.NatInsId cfwnat-xxxxxxxx \
    --NatCcnSwitch.CcnId ccn-xxxxxxxx \
    --NatCcnSwitch.SwitchMode 1 \
    --NatCcnSwitch.RoutingMode 1 \
    --NatCcnSwitch.LeadVpcCidr 
```

Output: 
```
{
    "Response": {
        "RequestId": "3b3a2e60-1b2c-4d3e-a4f5-6789abcdef01"
    }
}
```

