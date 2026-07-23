**Example 1: nat 集群防火墙预接入检查**



Input: 

```
tccli cfw CheckClusterNatFwPreAccess --cli-unfold-argument  \
    --NatCcnSwitch.NatInsId nat-mqpcoqs3 \
    --NatCcnSwitch.CcnId ccn-c0qmm031 \
    --NatCcnSwitch.SwitchMode 1 \
    --NatCcnSwitch.RoutingMode 1 \
    --NatCcnSwitch.AccessInstanceList.0.InstanceId vpc-fj3e7nr8 \
    --NatCcnSwitch.AccessInstanceList.0.InstanceType VPC \
    --NatCcnSwitch.AccessInstanceList.0.InstanceRegion ap-shanghai \
    --NatCcnSwitch.AccessInstanceList.0.AccessCidrMode 1 \
    --NatCcnSwitch.AccessInstanceList.0.AccessCidrList 10.15.160.0/22 \
    --NatCcnSwitch.LeadVpcCidr 10.136.0.0/26 \
    --CheckMode open
```

Output: 
```
{
    "Response": {
        "CheckItems": [
            {
                "Description": "开关状态检查",
                "Stage": "switch_status_check"
            }
        ],
        "RequestId": "16d22cb2-0183-4a15-a13d-5795adff279f"
    }
}
```

