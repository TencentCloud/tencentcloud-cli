**Example 1: 创建EMR集群实例**



Input: 

```
tccli emr CreateCluster --cli-unfold-argument  \
    --EnableKerberosFlag False \
    --SceneSoftwareConfig.SceneName Hadoop-Default \
    --SceneSoftwareConfig.Software hdfs-3.2.2 yarn-3.2.2 zookeeper-3.6.3 openldap-2.4.44 knox-1.6.1 hive-3.1.3 \
    --MetaDBInfo.MetaType EMR_DEFAULT_META \
    --NeedMasterWan NEED_MASTER_WAN \
    --EnableCbsEncryptFlag False \
    --LoginSettings.Password xxxxxxx \
    --SecurityGroupIds sg-xxx \
    --InstanceChargeType POSTPAID_BY_HOUR \
    --ProductVersion EMR-V3.5.0 \
    --ClientToken xxx \
    --EnableRemoteLoginFlag True \
    --InstanceChargePrepaid.RenewFlag True \
    --InstanceChargePrepaid.Period 1 \
    --InstanceName EMR350-JH6 \
    --EnableSupportHAFlag False \
    --ZoneResourceConfiguration.0.VirtualPrivateCloud.SubnetId subnet-xxx \
    --ZoneResourceConfiguration.0.VirtualPrivateCloud.VpcId vpc-xxx \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.MasterResourceSpec.SystemDisk.0.Count 1 \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.MasterResourceSpec.SystemDisk.0.DiskSize 50 \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.MasterResourceSpec.SystemDisk.0.DiskType CLOUD_HSSD \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.MasterResourceSpec.DataDisk.0.Count 1 \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.MasterResourceSpec.DataDisk.0.DiskSize 100 \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.MasterResourceSpec.DataDisk.0.DiskType CLOUD_SSD \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.MasterResourceSpec.InstanceType S6.2XLARGE32 \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.CoreCount 2 \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.CoreResourceSpec.SystemDisk.0.Count 1 \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.CoreResourceSpec.SystemDisk.0.DiskSize 50 \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.CoreResourceSpec.SystemDisk.0.DiskType CLOUD_SSD \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.CoreResourceSpec.DataDisk.0.Count 1 \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.CoreResourceSpec.DataDisk.0.DiskSize 300 \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.CoreResourceSpec.DataDisk.0.DiskType CLOUD_TSSD \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.CoreResourceSpec.InstanceType SA4.8XLARGE64 \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.TaskCount 0 \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.CommonCount 0 \
    --ZoneResourceConfiguration.0.AllNodeResourceSpec.MasterCount 1 \
    --ZoneResourceConfiguration.0.Placement.ProjectId 0 \
    --ZoneResourceConfiguration.0.Placement.Zone ap-guangzhou-7
```

Output: 
```
{
    "Response": {
        "InstanceId": "emr-rx5",
        "RequestId": "fsafa-232"
    }
}
```

