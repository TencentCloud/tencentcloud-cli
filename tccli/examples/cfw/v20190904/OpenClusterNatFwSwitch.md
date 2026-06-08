**Example 1: 开启NAT CCN集群模式防火墙开关**

以自动接入+策略路由模式开启NAT CCN集群防火墙开关

Input: 

```
tccli cfw OpenClusterNatFwSwitch --cli-unfold-argument  \
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

