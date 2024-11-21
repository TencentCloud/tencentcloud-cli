**Example 1: 创建防火墙(组)**

创建防火墙(组)

Input: 

```
tccli cfw CreateVpcFwGroup --cli-unfold-argument  \
    --Name 新防火墙 \
    --Mode 0 \
    --VpcFwInstances.0.FwInsId cfwew-wxecrvrtb \
    --VpcFwInstances.0.Name 新防火墙实例 \
    --VpcFwInstances.0.VpcIds vpc-0752de63 \
    --VpcFwInstances.0.FwDeploy.DeployRegion ap-guangzhou \
    --VpcFwInstances.0.FwDeploy.Width 1024 \
    --VpcFwInstances.0.FwDeploy.CrossAZone 1 \
    --VpcFwInstances.0.FwDeploy.Zone ap-guangzhou-1 \
    --VpcFwInstances.0.FwDeploy.ZoneBak ap-guangzhou-2 \
    --VpcFwInstances.0.FwDeploy.CdcId cluster-0752de63 \
    --SwitchMode 1 \
    --FwVpcCidr auto \
    --CcnId ccn-wxecrevtb \
    --FwCidrInfo.FwCidrType Custom \
    --FwCidrInfo.FwCidrLst.0.VpcId vpc-39sc6ru5 \
    --FwCidrInfo.FwCidrLst.0.FwCidr 192.168.1.0/24 \
    --FwCidrInfo.ComFwCidr 192.168.2.0/24
```

Output: 
```
{
    "Response": {
        "FwGroupId": "cfwg-0752de63",
        "RequestId": "0752de63-570c-4c2e-bbd2-78574e22a1ae"
    }
}
```

