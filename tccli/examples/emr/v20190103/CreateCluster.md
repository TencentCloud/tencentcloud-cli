**Example 1: 创建EMR集群实例**



Input: 

```
tccli emr CreateCluster --cli-unfold-argument  \
    --DisasterRecoverGroupIds xx \
    --DependService.0.InstanceId xx \
    --DependService.0.ServiceName xx \
    --ZoneResourceConfiguration.0.VirtualPrivateCloud.SubnetId xx \
    --ZoneResourceConfiguration.0.VirtualPrivateCloud.VpcId xx \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.CoreResourceSpec.DataDisk.0.Count 0 \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.CoreResourceSpec.DataDisk.0.DiskSize 0 \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.CoreResourceSpec.DataDisk.0.DiskType xx \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.CoreResourceSpec.SystemDisk.0.Count 0 \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.CoreResourceSpec.SystemDisk.0.DiskSize 0 \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.CoreResourceSpec.SystemDisk.0.DiskType xx \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.CoreResourceSpec.LocalDataDisk.0.Count 0 \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.CoreResourceSpec.LocalDataDisk.0.DiskSize 0 \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.CoreResourceSpec.LocalDataDisk.0.DiskType xx \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.CoreResourceSpec.InstanceType xx \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.CoreResourceSpec.Tags.0.TagKey xx \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.CoreResourceSpec.Tags.0.TagValue xx \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.CoreCount 0 \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.MasterResourceSpec.InstanceType xx \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.MasterResourceSpec.Tags.0.TagKey xx \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.MasterResourceSpec.Tags.0.TagValue xx \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.TaskCount 0 \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.TaskResourceSpec.InstanceType xx \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.CommonCount 0 \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.MasterCount 0 \
    --ZoneResourceConfiguration.0.Placement.ProjectId 0 \
    --ZoneResourceConfiguration.0.Placement.Zone xx \
    --ZoneResourceConfiguration.0.ZoneTag xx \
    --ScriptBootstrapActionConfig.0.CosFileName xx \
    --ScriptBootstrapActionConfig.0.Args xx \
    --ScriptBootstrapActionConfig.0.CosFileURI xx \
    --ScriptBootstrapActionConfig.0.ExecutionMoment xx \
    --Tags.0.TagKey xx \
    --Tags.0.TagValue xx \
    --NeedMasterWan xx \
    --EnableCbsEncryptFlag True \
    --MetaDBInfo.MetaDataPass xx \
    --MetaDBInfo.MetaDataUser xx \
    --MetaDBInfo.UnifyMetaInstanceId xx \
    --MetaDBInfo.MetaDataJdbcUrl xx \
    --MetaDBInfo.MetaType xx \
    --LoginSettings.Password xx \
    --LoginSettings.PublicKeyId xx \
    --SecurityGroupIds xx \
    --InstanceChargeType xx \
    --ProductVersion xx \
    --ClientToken xx \
    --SceneSoftwareConfig.SceneName xx \
    --SceneSoftwareConfig.Software xx \
    --EnableKerberosFlag True \
    --CustomConf xx \
    --InstanceChargePrepaid.RenewFlag True \
    --InstanceChargePrepaid.Period 0 \
    --InstanceName xx \
    --EnableRemoteLoginFlag True \
    --EnableSupportHAFlag True
```

Output: 
```
{
    "Response": {
        "InstanceId": "xx",
        "RequestId": "xx"
    }
}
```

