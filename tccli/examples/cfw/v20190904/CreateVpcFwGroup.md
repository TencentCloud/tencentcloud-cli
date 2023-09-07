**Example 1: 创建防火墙(组)**

创建防火墙(组)

Input: 

```
tccli cfw CreateVpcFwGroup --cli-unfold-argument  \
    --Name 新的世界 \
    --Mode 0 \
    --VpcFwInstances.0.FwInsId  \
    --VpcFwInstances.0.Name 新的时间 \
    --VpcFwInstances.0.VpcIds vpc-ddddaaaa \
    --VpcFwInstances.0.FwDeploy.DeployRegion ap-guangzhou \
    --VpcFwInstances.0.FwDeploy.Width 1024 \
    --VpcFwInstances.0.FwDeploy.CrossAZone 1 \
    --VpcFwInstances.0.FwDeploy.Zone ap-guangzhou-1 \
    --VpcFwInstances.0.FwDeploy.ZoneBak ap-guangzhou-2 \
    --VpcFwInstances.0.FwDeploy.CdcId abc \
    --SwitchMode 1 \
    --FwVpcCidr auto \
    --CcnId  \
    --FwCidrInfo.FwCidrType  \
    --FwCidrInfo.ComFwCidr abc
```

Output: 
```
{
    "Response": {
        "FwGroupId": "cfwg-12345678",
        "RequestId": "0752de63-570c-4c2e-bbd2-78574e22a1ae"
    }
}
```

