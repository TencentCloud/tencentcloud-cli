**Example 1: SetNatFwVpcDnsSwitch 防火墙VPC DNS 开关切换**



Input: 

```
tccli cfw ModifyNatFwVpcDnsSwitch --cli-unfold-argument  \
    --NatFwInsId cfwnat-d1580b7b \
    --DnsVpcSwitchLst.0.VpcId vpc-ilbrv877 \
    --DnsVpcSwitchLst.0.Status 0
```

Output: 
```
{
    "Response": {
        "ReturnMsg": "success",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

