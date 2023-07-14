**Example 1: 创建托管集群示例**

创建托管集群

Input: 

```
tccli tke CreateCluster --cli-unfold-argument  \
    --ClusterCIDRSettings.ServiceCIDR xyz \
    --ClusterCIDRSettings.ClaimExpiredSeconds 0 \
    --ClusterCIDRSettings.MaxClusterServiceNum 1 \
    --ClusterCIDRSettings.MaxNodePodNum 1 \
    --ClusterCIDRSettings.EniSubnetIds subnet-abcdef \
    --ClusterCIDRSettings.ClusterCIDR xyz \
    --ClusterCIDRSettings.IgnoreServiceCIDRConflict True \
    --ClusterCIDRSettings.IgnoreClusterCIDRConflict True \
    --ClusterAdvancedSettings.AuditEnabled True \
    --ClusterAdvancedSettings.DeletionProtection True \
    --ClusterAdvancedSettings.RuntimeVersion xyz \
    --ClusterAdvancedSettings.IsDualStack True \
    --ClusterAdvancedSettings.IsNonStaticIpMode True \
    --ClusterAdvancedSettings.KubeProxyMode xyz \
    --ClusterAdvancedSettings.AuditLogTopicId xyz \
    --ClusterAdvancedSettings.ExtraArgs.KubeAPIServer xyz \
    --ClusterAdvancedSettings.ExtraArgs.KubeScheduler xyz \
    --ClusterAdvancedSettings.ExtraArgs.KubeControllerManager xyz \
    --ClusterAdvancedSettings.ExtraArgs.Etcd xyz \
    --ClusterAdvancedSettings.AuditLogsetId xyz \
    --ClusterAdvancedSettings.EnableCustomizedPodCIDR True \
    --ClusterAdvancedSettings.CiliumMode xyz \
    --ClusterAdvancedSettings.AsEnabled True \
    --ClusterAdvancedSettings.ContainerRuntime xyz \
    --ClusterAdvancedSettings.VpcCniType xyz \
    --ClusterAdvancedSettings.NetworkType xyz \
    --ClusterAdvancedSettings.NodeNameType xyz \
    --ClusterAdvancedSettings.IPVS True \
    --ClusterAdvancedSettings.BasePodNumber 0 \
    --ClusterBasicSettings.AutoUpgradeClusterLevel.IsAutoUpgrade True \
    --ClusterBasicSettings.VpcId xyz \
    --ClusterBasicSettings.ClusterVersion xyz \
    --ClusterBasicSettings.TagSpecification.0.ResourceType xyz \
    --ClusterBasicSettings.TagSpecification.0.Tags.0.Value xyz \
    --ClusterBasicSettings.TagSpecification.0.Tags.0.Key xyz \
    --ClusterBasicSettings.ClusterName xyz \
    --ClusterBasicSettings.ProjectId 0 \
    --ClusterBasicSettings.ClusterDescription xyz \
    --ClusterBasicSettings.NeedWorkSecurityGroup True \
    --ClusterBasicSettings.SubnetId xyz \
    --ClusterBasicSettings.OsCustomizeType xyz \
    --ClusterBasicSettings.ClusterLevel xyz \
    --ClusterBasicSettings.ClusterOs xyz \
    --RunInstancesForNode.0.InstanceAdvancedSettingsOverrides.0.PreStartUserScript xyz \
    --RunInstancesForNode.0.InstanceAdvancedSettingsOverrides.0.DockerGraphPath xyz \
    --RunInstancesForNode.0.InstanceAdvancedSettingsOverrides.0.Labels.0.Name xyz \
    --RunInstancesForNode.0.InstanceAdvancedSettingsOverrides.0.Labels.0.Value xyz \
    --RunInstancesForNode.0.InstanceAdvancedSettingsOverrides.0.ExtraArgs.Kubelet xyz \
    --RunInstancesForNode.0.InstanceAdvancedSettingsOverrides.0.Taints.0.Value xyz \
    --RunInstancesForNode.0.InstanceAdvancedSettingsOverrides.0.Taints.0.Key xyz \
    --RunInstancesForNode.0.InstanceAdvancedSettingsOverrides.0.Taints.0.Effect xyz \
    --RunInstancesForNode.0.InstanceAdvancedSettingsOverrides.0.Unschedulable 0 \
    --RunInstancesForNode.0.InstanceAdvancedSettingsOverrides.0.UserScript xyz \
    --RunInstancesForNode.0.InstanceAdvancedSettingsOverrides.0.DesiredPodNumber 0 \
    --RunInstancesForNode.0.InstanceAdvancedSettingsOverrides.0.GPUArgs.MIGEnable True \
    --RunInstancesForNode.0.InstanceAdvancedSettingsOverrides.0.GPUArgs.CustomDriver.Address xyz \
    --RunInstancesForNode.0.InstanceAdvancedSettingsOverrides.0.GPUArgs.Driver.Version xyz \
    --RunInstancesForNode.0.InstanceAdvancedSettingsOverrides.0.GPUArgs.Driver.Name xyz \
    --RunInstancesForNode.0.InstanceAdvancedSettingsOverrides.0.GPUArgs.CUDA.Version xyz \
    --RunInstancesForNode.0.InstanceAdvancedSettingsOverrides.0.GPUArgs.CUDA.Name xyz \
    --RunInstancesForNode.0.InstanceAdvancedSettingsOverrides.0.GPUArgs.CUDNN.DocName xyz \
    --RunInstancesForNode.0.InstanceAdvancedSettingsOverrides.0.GPUArgs.CUDNN.Version xyz \
    --RunInstancesForNode.0.InstanceAdvancedSettingsOverrides.0.GPUArgs.CUDNN.Name xyz \
    --RunInstancesForNode.0.InstanceAdvancedSettingsOverrides.0.GPUArgs.CUDNN.DevName xyz \
    --RunInstancesForNode.0.InstanceAdvancedSettingsOverrides.0.MountTarget xyz \
    --RunInstancesForNode.0.InstanceAdvancedSettingsOverrides.0.DataDisks.0.DiskPartition xyz \
    --RunInstancesForNode.0.InstanceAdvancedSettingsOverrides.0.DataDisks.0.DiskType xyz \
    --RunInstancesForNode.0.InstanceAdvancedSettingsOverrides.0.DataDisks.0.DiskSize 0 \
    --RunInstancesForNode.0.InstanceAdvancedSettingsOverrides.0.DataDisks.0.FileSystem xyz \
    --RunInstancesForNode.0.InstanceAdvancedSettingsOverrides.0.DataDisks.0.AutoFormatAndMount True \
    --RunInstancesForNode.0.InstanceAdvancedSettingsOverrides.0.DataDisks.0.MountTarget xyz \
    --RunInstancesForNode.0.NodeRole xyz \
    --RunInstancesForNode.0.RunInstancesPara {"VirtualPrivateCloud":{"SubnetId":"subnet-xyzx","VpcId":"vpc-xyzx"},"Placement":{"Zone":"ap-region-1","ProjectId":1032509},"InstanceType":"S3.LARGE8","SystemDisk":{"DiskType":"CLOUD_PREMIUM"},"DataDisks":[{"DiskType":"CLOUD_PREMIUM","DiskSize":50}],"InstanceCount":1,"InternetAccessible":{"PublicIpAssigned":true,"InternetMaxBandwidthOut":1},"LoginSettings":{"Password":"YourPassword"},"UserData":"IyEvYmluL3NoCgplY2hvIGFhYQo="} \
    --ExtensionAddons.0.AddonName xyz \
    --ExtensionAddons.0.AddonParam xyz \
    --ClusterType xyz \
    --InstanceAdvancedSettings.PreStartUserScript xyz \
    --InstanceAdvancedSettings.DockerGraphPath xyz \
    --InstanceAdvancedSettings.Labels.0.Name xyz \
    --InstanceAdvancedSettings.Labels.0.Value xyz \
    --InstanceAdvancedSettings.ExtraArgs.Kubelet xyz \
    --InstanceAdvancedSettings.Taints.0.Value xyz \
    --InstanceAdvancedSettings.Taints.0.Key xyz \
    --InstanceAdvancedSettings.Taints.0.Effect xyz \
    --InstanceAdvancedSettings.Unschedulable 0 \
    --InstanceAdvancedSettings.UserScript xyz \
    --InstanceAdvancedSettings.DesiredPodNumber 0 \
    --InstanceAdvancedSettings.GPUArgs.MIGEnable True \
    --InstanceAdvancedSettings.GPUArgs.CustomDriver.Address xyz \
    --InstanceAdvancedSettings.GPUArgs.Driver.Version xyz \
    --InstanceAdvancedSettings.GPUArgs.Driver.Name xyz \
    --InstanceAdvancedSettings.GPUArgs.CUDNN.DocName xyz \
    --InstanceAdvancedSettings.GPUArgs.CUDNN.Version xyz \
    --InstanceAdvancedSettings.GPUArgs.CUDNN.Name xyz \
    --InstanceAdvancedSettings.GPUArgs.CUDNN.DevName xyz \
    --InstanceAdvancedSettings.MountTarget xyz \
    --InstanceAdvancedSettings.DataDisks.0.DiskPartition xyz \
    --InstanceAdvancedSettings.DataDisks.0.DiskType xyz \
    --InstanceAdvancedSettings.DataDisks.0.DiskSize 0 \
    --InstanceAdvancedSettings.DataDisks.0.FileSystem xyz \
    --InstanceAdvancedSettings.DataDisks.0.AutoFormatAndMount True \
    --InstanceAdvancedSettings.DataDisks.0.MountTarget xyz \
    --ExistedInstancesForNode.0.ExistedInstancesPara.InstanceAdvancedSettings.PreStartUserScript xyz \
    --ExistedInstancesForNode.0.ExistedInstancesPara.InstanceAdvancedSettings.DockerGraphPath xyz \
    --ExistedInstancesForNode.0.ExistedInstancesPara.InstanceAdvancedSettings.Labels.0.Name xyz \
    --ExistedInstancesForNode.0.ExistedInstancesPara.InstanceAdvancedSettings.Labels.0.Value xyz \
    --ExistedInstancesForNode.0.ExistedInstancesPara.InstanceAdvancedSettings.ExtraArgs.Kubelet xyz \
    --ExistedInstancesForNode.0.ExistedInstancesPara.InstanceAdvancedSettings.Taints.0.Value xyz \
    --ExistedInstancesForNode.0.ExistedInstancesPara.InstanceAdvancedSettings.Taints.0.Key xyz \
    --ExistedInstancesForNode.0.ExistedInstancesPara.InstanceAdvancedSettings.Taints.0.Effect xyz \
    --ExistedInstancesForNode.0.ExistedInstancesPara.InstanceAdvancedSettings.Unschedulable 0 \
    --ExistedInstancesForNode.0.ExistedInstancesPara.InstanceAdvancedSettings.UserScript xyz \
    --ExistedInstancesForNode.0.ExistedInstancesPara.InstanceAdvancedSettings.DesiredPodNumber 0 \
    --ExistedInstancesForNode.0.ExistedInstancesPara.InstanceAdvancedSettings.GPUArgs.MIGEnable True \
    --ExistedInstancesForNode.0.ExistedInstancesPara.InstanceAdvancedSettings.GPUArgs.CustomDriver.Address xyz \
    --ExistedInstancesForNode.0.ExistedInstancesPara.InstanceAdvancedSettings.GPUArgs.CUDNN.DocName xyz \
    --ExistedInstancesForNode.0.ExistedInstancesPara.InstanceAdvancedSettings.GPUArgs.CUDNN.Version xyz \
    --ExistedInstancesForNode.0.ExistedInstancesPara.InstanceAdvancedSettings.GPUArgs.CUDNN.Name xyz \
    --ExistedInstancesForNode.0.ExistedInstancesPara.InstanceAdvancedSettings.GPUArgs.CUDNN.DevName xyz \
    --ExistedInstancesForNode.0.ExistedInstancesPara.InstanceAdvancedSettings.MountTarget xyz \
    --ExistedInstancesForNode.0.ExistedInstancesPara.InstanceAdvancedSettings.DataDisks.0.DiskPartition xyz \
    --ExistedInstancesForNode.0.ExistedInstancesPara.InstanceAdvancedSettings.DataDisks.0.DiskType xyz \
    --ExistedInstancesForNode.0.ExistedInstancesPara.InstanceAdvancedSettings.DataDisks.0.DiskSize 0 \
    --ExistedInstancesForNode.0.ExistedInstancesPara.InstanceAdvancedSettings.DataDisks.0.FileSystem xyz \
    --ExistedInstancesForNode.0.ExistedInstancesPara.InstanceAdvancedSettings.DataDisks.0.AutoFormatAndMount True \
    --ExistedInstancesForNode.0.ExistedInstancesPara.InstanceAdvancedSettings.DataDisks.0.MountTarget xyz \
    --ExistedInstancesForNode.0.ExistedInstancesPara.HostName xyz \
    --ExistedInstancesForNode.0.ExistedInstancesPara.LoginSettings.Password xyz \
    --ExistedInstancesForNode.0.ExistedInstancesPara.LoginSettings.KeepImageLogin xyz \
    --ExistedInstancesForNode.0.ExistedInstancesPara.LoginSettings.KeyIds xyz \
    --ExistedInstancesForNode.0.ExistedInstancesPara.SecurityGroupIds xyz \
    --ExistedInstancesForNode.0.ExistedInstancesPara.EnhancedService.SecurityService.Enabled True \
    --ExistedInstancesForNode.0.ExistedInstancesPara.EnhancedService.MonitorService.Enabled True \
    --ExistedInstancesForNode.0.ExistedInstancesPara.EnhancedService.AutomationService.Enabled True \
    --ExistedInstancesForNode.0.ExistedInstancesPara.InstanceIds xyz \
    --ExistedInstancesForNode.0.DesiredPodNumbers 0 \
    --ExistedInstancesForNode.0.NodeRole xyz \
    --InstanceDataDiskMountSettings.0.InstanceType xyz \
    --InstanceDataDiskMountSettings.0.Zone xyz \
    --InstanceDataDiskMountSettings.0.DataDisks.0.DiskPartition xyz \
    --InstanceDataDiskMountSettings.0.DataDisks.0.DiskType xyz \
    --InstanceDataDiskMountSettings.0.DataDisks.0.DiskSize 0 \
    --InstanceDataDiskMountSettings.0.DataDisks.0.FileSystem xyz \
    --InstanceDataDiskMountSettings.0.DataDisks.0.AutoFormatAndMount True \
    --InstanceDataDiskMountSettings.0.DataDisks.0.MountTarget xyz
```

Output: 
```
{
    "Response": {
        "ClusterId": "cls-7ph3twqe",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

**Example 2: 创建独立集群示例**

创建独立集群

Input: 

```
tccli tke CreateCluster --cli-unfold-argument  \
    --ClusterCIDRSettings.ClusterCIDR 10.4.0.0/14 \
    --ExtensionAddons.0.AddonName GameApp \
    --ExtensionAddons.0.AddonParam {"kind":"GameApp","apiVersion":"platform.tke/v1","metadata":{"generateName":"ga"},"spec":{"clusterName":"xxx"}} \
    --ClusterType INDEPENDENT_CLUSTER \
    --RunInstancesForNode.0.NodeRole WORKER \
    --RunInstancesForNode.0.RunInstancesPara {"VirtualPrivateCloud":{"SubnetId":"subnet-xxx","VpcId":"vpc-xxx"},"Placement":{"Zone":"ap-region-1","ProjectId":1032509},"InstanceType":"S3.LARGE8","SystemDisk":{"DiskType":"CLOUD_PREMIUM"},"DataDisks":[{"DiskType":"CLOUD_PREMIUM","DiskSize":50}],"InstanceCount":1,"InternetAccessible":{"PublicIpAssigned":true,"InternetMaxBandwidthOut":1},"LoginSettings":{"Password":"YourPassword"},"UserData":"IyEvYmluL3NoCgplY2hvIGFhYQo="} \
    --RunInstancesForNode.1.NodeRole MASTER_ETCD \
    --RunInstancesForNode.1.RunInstancesPara {"VirtualPrivateCloud":{"SubnetId":"subnet-xxx","VpcId":"vpc-xxx"},"Placement":{"Zone":"ap-region-1","ProjectId":1032509},"InstanceType":"S3.LARGE8","SystemDisk":{"DiskType":"CLOUD_PREMIUM"},"DataDisks":[{"DiskType":"CLOUD_PREMIUM","DiskSize":50}],"InstanceCount":3,"InternetAccessible":{"PublicIpAssigned":true,"InternetMaxBandwidthOut":1},"LoginSettings":{"Password":"YourPassword"},"UserData":"IyEvYmluL3NoCgplY2hvIGFhYQo="}
```

Output: 
```
{
    "Response": {
        "ClusterId": "cls-xxx",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

