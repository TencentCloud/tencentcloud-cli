**Example 1: vpc 集群模式防火墙预接入检查**



Input: 

```
tccli cfw CheckClusterVpcFwPreAccess --cli-unfold-argument  \
    --CcnSwitch.0.CcnId ccn-c0qmm031 \
    --CcnSwitch.0.SwitchMode 1 \
    --CcnSwitch.0.RoutingMode 1 \
    --CcnSwitch.0.RegionCidrConfigs.0.Region ap-shanghai \
    --CcnSwitch.0.RegionCidrConfigs.0.CidrMode 2 \
    --CcnSwitch.0.RegionCidrConfigs.0.CustomCidr 10.100.1.0/26 \
    --CcnSwitch.0.InterconnectPairs.0.GroupA.0.InstanceId vpc-fj3e7nr8 \
    --CcnSwitch.0.InterconnectPairs.0.GroupA.0.InstanceType VPC \
    --CcnSwitch.0.InterconnectPairs.0.GroupA.0.InstanceRegion ap-shanghai \
    --CcnSwitch.0.InterconnectPairs.0.GroupA.0.AccessCidrMode 1 \
    --CcnSwitch.0.InterconnectPairs.0.GroupA.0.AccessCidrList 10.15.160.0/22 \
    --CcnSwitch.0.InterconnectPairs.0.GroupB.0.InstanceId vpc-fj3e7nr8 \
    --CcnSwitch.0.InterconnectPairs.0.GroupB.0.InstanceType VPC \
    --CcnSwitch.0.InterconnectPairs.0.GroupB.0.InstanceRegion ap-shanghai \
    --CcnSwitch.0.InterconnectPairs.0.GroupB.0.AccessCidrMode 1 \
    --CcnSwitch.0.InterconnectPairs.0.GroupB.0.AccessCidrList 10.15.160.0/22 \
    --CcnSwitch.0.InterconnectPairs.0.InterconnectMode FullMesh \
    --CcnSwitch.0.FwVpcCidr  \
    --CheckMode open
```

Output: 
```
{
    "Response": {
        "CheckItems": [
            {
                "Description": "带宽配额检查",
                "Stage": "vpc_bandwidth_check"
            }
        ],
        "RequestId": "90fa332b-8ec3-42bb-9ff3-558c9d9ba187"
    }
}
```

