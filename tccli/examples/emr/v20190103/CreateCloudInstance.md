**Example 1: 创建EMR容器实例**

创建EMR容器实例

Input: 

```
tccli emr CreateCloudInstance --cli-unfold-argument  \
    --InstanceName EMR-dzrgkpwq \
    --LoginSettings.Password xxxxxxxxxx \
    --VPCSettings.SubnetId subnet-xxxxo3x0 \
    --VPCSettings.VpcId vpc-xxxxqmqz \
    --CosBucket coslcl-xxxxxxxxxx \
    --CloudResources.0.ComponentName QuorumPeerMain \
    --CloudResources.0.PodNumber 3 \
    --CloudResources.0.LimitCpu 1 \
    --CloudResources.0.LimitMemory 2 \
    --CloudResources.0.Service ZOOKEEPER \
    --CloudResources.0.VolumeDir.VolumeType NEW_PVC \
    --CloudResources.0.VolumeDir.HostPath.Path  \
    --CloudResources.0.VolumeDir.HostPath.Type DirectoryOrCreate \
    --CloudResources.0.Disks.0.DiskType CLOUD_PREMIUM \
    --CloudResources.0.Disks.0.DiskCapacity 100 \
    --CloudResources.0.Disks.0.DiskNumber 1 \
    --CloudResources.1.ComponentName Slapd \
    --CloudResources.1.PodNumber 2 \
    --CloudResources.1.LimitCpu 1 \
    --CloudResources.1.LimitMemory 2 \
    --CloudResources.1.Service OPENLDAP \
    --CloudResources.1.VolumeDir.VolumeType NEW_PVC \
    --CloudResources.1.VolumeDir.HostPath.Path  \
    --CloudResources.1.VolumeDir.HostPath.Type DirectoryOrCreate \
    --CloudResources.1.Disks.0.DiskType CLOUD_PREMIUM \
    --CloudResources.1.Disks.0.DiskCapacity 100 \
    --CloudResources.1.Disks.0.DiskNumber 1 \
    --CloudResources.2.ComponentName HiveServer2Node \
    --CloudResources.2.PodNumber 1 \
    --CloudResources.2.LimitCpu 1 \
    --CloudResources.2.LimitMemory 2 \
    --CloudResources.2.Service HIVESERVER2 \
    --CloudResources.2.VolumeDir.VolumeType NEW_PVC \
    --CloudResources.2.VolumeDir.HostPath.Path  \
    --CloudResources.2.VolumeDir.HostPath.Type DirectoryOrCreate \
    --CloudResources.2.Disks.0.DiskType CLOUD_PREMIUM \
    --CloudResources.2.Disks.0.DiskCapacity 100 \
    --CloudResources.2.Disks.0.DiskNumber 1 \
    --CloudResources.3.ComponentName HiveMetaStoreNode \
    --CloudResources.3.PodNumber 1 \
    --CloudResources.3.LimitCpu 1 \
    --CloudResources.3.LimitMemory 2 \
    --CloudResources.3.Service METASTORE \
    --CloudResources.3.VolumeDir.VolumeType NEW_PVC \
    --CloudResources.3.VolumeDir.HostPath.Path  \
    --CloudResources.3.VolumeDir.HostPath.Type DirectoryOrCreate \
    --CloudResources.3.Disks.0.DiskType CLOUD_PREMIUM \
    --CloudResources.3.Disks.0.DiskCapacity 100 \
    --CloudResources.3.Disks.0.DiskNumber 1 \
    --CloudResources.4.ComponentName SparkJobHistoryServer \
    --CloudResources.4.PodNumber 1 \
    --CloudResources.4.LimitCpu 2 \
    --CloudResources.4.LimitMemory 4 \
    --CloudResources.4.Service SPARK \
    --CloudResources.4.VolumeDir.VolumeType NEW_PVC \
    --CloudResources.4.VolumeDir.HostPath.Path  \
    --CloudResources.4.VolumeDir.HostPath.Type DirectoryOrCreate \
    --CloudResources.4.Disks.0.DiskType CLOUD_PREMIUM \
    --CloudResources.4.Disks.0.DiskCapacity 100 \
    --CloudResources.4.Disks.0.DiskNumber 1 \
    --Tags.0.TagKey test-key \
    --Tags.0.TagValue v1 \
    --MetaDBInfo.MetaType EMR_DEFAULT_META \
    --Software zookeeper-3.6.3 metastore-3.1.3 openldap-2.4.44 hiveserver2-3.1.3 spark-3.3.2 \
    --ClusterClass EMR-TKE \
    --PlatFormType tke \
    --EksClusterId cls-xxxxxl3o \
    --ProductId 60 \
    --SgId sg-1111123nt \
    --ZoneId 1000010
```

Output: 
```
{
    "Response": {
        "RequestId": "d830face-6587-4263-8ab0-56bda2657xxx",
        "InstanceId": "emr-xxxx"
    }
}
```

