**Example 1: 编辑VPC间防火墙(防火墙组)**

编辑VPC间防火墙(防火墙组)

Input: 

```
tccli cfw ModifyVpcFwGroup --cli-unfold-argument  \
    --FwGroupId cfwg-4e14ec17 \
    --Name 防火墙(组)第三个实例 \
    --VpcFwInstances.0.FwInsId cfwew-ace94947 \
    --VpcFwInstances.0.Name 防火墙(组)第三个实例(生死有命) \
    --VpcFwInstances.0.VpcIds vpc-39sc6ru5 \
    --VpcFwInstances.0.FwDeploy.DeployRegion ap-guangzhou \
    --VpcFwInstances.0.FwDeploy.Width 1024 \
    --VpcFwInstances.0.FwDeploy.CrossAZone 1 \
    --VpcFwInstances.0.FwDeploy.Zone ap-guangzhou-1 \
    --VpcFwInstances.0.FwDeploy.ZoneBak ap-guangzhou-2 \
    --VpcFwInstances.0.FwDeploy.CdcId  \
    --FwCidrInfo.FwCidrType Custom \
    --FwCidrInfo.FwCidrLst.0.VpcId vpc-39sc6ru5 \
    --FwCidrInfo.FwCidrLst.0.FwCidr 192.168.1.0/24 \
    --FwCidrInfo.ComFwCidr 
```

Output: 
```
{
    "Response": {
        "RequestId": "570c7dee-1fb5-450e-b5c1-178ac7fe93e8"
    }
}
```

