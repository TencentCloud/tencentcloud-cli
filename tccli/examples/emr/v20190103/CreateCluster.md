**Example 1: 创建EMR集群实例**



Input: 

```
tccli emr CreateCluster --cli-unfold-argument  \
    --DisasterRecoverGroupIds disa \
    --DependService.0.InstanceId emr-123 \
    --DependService.0.ServiceName zookeeper \
    --ZoneResourceConfiguration.0.VirtualPrivateCloud.SubnetId 12 \
    --ZoneResourceConfiguration.0.VirtualPrivateCloud.VpcId 32 \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.CoreResourceSpec.DataDisk.0.Count 0 \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.CoreResourceSpec.DataDisk.0.DiskSize 0 \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.CoreResourceSpec.DataDisk.0.DiskType CLOUD_SSD \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.CoreResourceSpec.SystemDisk.0.Count 0 \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.CoreResourceSpec.SystemDisk.0.DiskSize 0 \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.CoreResourceSpec.SystemDisk.0.DiskType CLOUD_SSD \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.CoreResourceSpec.LocalDataDisk.0.Count 0 \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.CoreResourceSpec.LocalDataDisk.0.DiskSize 0 \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.CoreResourceSpec.LocalDataDisk.0.DiskType CLOUD_SSD \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.CoreResourceSpec.InstanceType S2.MEDIUM8 \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.CoreResourceSpec.Tags.0.TagKey key \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.CoreResourceSpec.Tags.0.TagValue value \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.CoreCount 0 \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.MasterResourceSpec.InstanceType S2.MEDIUM8 \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.MasterResourceSpec.Tags.0.TagKey key \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.MasterResourceSpec.Tags.0.TagValue value \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.TaskCount 0 \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.TaskResourceSpec.InstanceType S2.MEDIUM8 \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.CommonCount 0 \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.MasterCount 0 \
    --ZoneResourceConfiguration.0.Placement.ProjectId 0 \
    --ZoneResourceConfiguration.0.Placement.Zone GZ \
    --ZoneResourceConfiguration.0.ZoneTag key \
    --ScriptBootstrapActionConfig.0.CosFileName file \
    --ScriptBootstrapActionConfig.0.Args region \
    --ScriptBootstrapActionConfig.0.CosFileURI filefads \
    --ScriptBootstrapActionConfig.0.ExecutionMoment moment \
    --Tags.0.TagKey key \
    --Tags.0.TagValue value \
    --NeedMasterWan 127.0.0.1 \
    --EnableCbsEncryptFlag True \
    --MetaDBInfo.MetaDataPass pass \
    --MetaDBInfo.MetaDataUser user \
    --MetaDBInfo.UnifyMetaInstanceId instance \
    --MetaDBInfo.MetaDataJdbcUrl  \
    --MetaDBInfo.MetaType  \
    --LoginSettings.Password  \
    --LoginSettings.PublicKeyId  \
    --SecurityGroupIds  \
    --InstanceChargeType  \
    --ProductVersion  \
    --ClientToken  \
    --SceneSoftwareConfig.SceneName  \
    --SceneSoftwareConfig.Software  \
    --EnableKerberosFlag True \
    --CustomConf file.xml \
    --InstanceChargePrepaid.RenewFlag True \
    --InstanceChargePrepaid.Period 0 \
    --InstanceName name \
    --EnableRemoteLoginFlag True \
    --EnableSupportHAFlag True
```

Output: 
```
{
    "Response": {
        "InstanceId": "emr-1332",
        "RequestId": "fsafa-232"
    }
}
```

