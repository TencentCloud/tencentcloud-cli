**Example 1: 更新防火墙配置**



Input: 

```
tccli cfw UpdateClusterVpcFw --cli-unfold-argument  \
    --CcnSwitch.CcnId ccn-hunqbq8z \
    --CcnSwitch.SwitchMode 1 \
    --CcnSwitch.RoutingMode 1 \
    --CcnSwitch.RegionCidrConfigs.0.Region eu-frankfurt \
    --CcnSwitch.RegionCidrConfigs.0.CidrMode 1 \
    --CcnSwitch.RegionCidrConfigs.0.CustomCidr  \
    --CcnSwitch.InterconnectPairs.0.GroupA.0.InstanceId vpc-lo1oluf4 \
    --CcnSwitch.InterconnectPairs.0.GroupA.0.InstanceType VPC \
    --CcnSwitch.InterconnectPairs.0.GroupA.0.InstanceRegion ap-seoul \
    --CcnSwitch.InterconnectPairs.0.GroupA.0.AccessCidrMode 1 \
    --CcnSwitch.InterconnectPairs.0.GroupA.0.AccessCidrList 10.24.0.0/16 \
    --CcnSwitch.InterconnectPairs.0.GroupB.0.InstanceId vpc-lo1oluf4 \
    --CcnSwitch.InterconnectPairs.0.GroupB.0.InstanceType VPC \
    --CcnSwitch.InterconnectPairs.0.GroupB.0.InstanceRegion ap-seoul \
    --CcnSwitch.InterconnectPairs.0.GroupB.0.AccessCidrMode 1 \
    --CcnSwitch.InterconnectPairs.0.GroupB.0.AccessCidrList 10.24.0.0/16 \
    --CcnSwitch.InterconnectPairs.0.InterconnectMode FullMesh
```

Output: 
```
{
    "Response": {
        "RequestId": "d6850583-1840-4d17-90d2-59d3fe8988c7"
    }
}
```

