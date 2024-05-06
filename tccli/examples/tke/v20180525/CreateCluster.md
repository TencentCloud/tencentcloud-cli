**Example 1: 创建托管集群示例**

创建托管集群

Input: 

```
tccli tke CreateCluster --cli-unfold-argument  \
    --ClusterType MANAGED_CLUSTER \
    --ClusterBasicSettings.ClusterOs centos8.0x86_64 \
    --ClusterBasicSettings.OsCustomizeType GENERAL \
    --ClusterBasicSettings.ClusterVersion 1.26.1 \
    --ClusterBasicSettings.ClusterName test \
    --ClusterBasicSettings.ClusterDescription 测试集群 \
    --ClusterBasicSettings.VpcId vpc-135qxjgs \
    --ClusterBasicSettings.ProjectId 0 \
    --ClusterBasicSettings.NeedWorkSecurityGroup False \
    --ClusterBasicSettings.TagSpecification.0.ResourceType cluster \
    --ClusterBasicSettings.TagSpecification.0.Tags.0.Key aa \
    --ClusterBasicSettings.TagSpecification.0.Tags.0.Value cc \
    --ClusterBasicSettings.ClusterLevel L5 \
    --ClusterBasicSettings.AutoUpgradeClusterLevel.IsAutoUpgrade True \
    --ClusterCIDRSettings.ClusterCIDR 172.24.0.0/16 \
    --ClusterCIDRSettings.IgnoreClusterCIDRConflict False \
    --ClusterCIDRSettings.MaxNodePodNum 64 \
    --ClusterCIDRSettings.MaxClusterServiceNum 1024 \
    --ClusterAdvancedSettings.AsEnabled False \
    --ClusterAdvancedSettings.IPVS True \
    --ClusterAdvancedSettings.ContainerRuntime containerd \
    --ClusterAdvancedSettings.RuntimeVersion 1.6.9 \
    --ClusterAdvancedSettings.NodeNameType lan-ip \
    --ClusterAdvancedSettings.NetworkType GR \
    --ClusterAdvancedSettings.DeletionProtection True \
    --ClusterAdvancedSettings.AuditEnabled True \
    --ClusterAdvancedSettings.AuditLogsetId  \
    --ClusterAdvancedSettings.AuditLogTopicId  \
    --ClusterAdvancedSettings.EnableCustomizedPodCIDR False \
    --ClusterAdvancedSettings.IsDualStack False \
    --ClusterAdvancedSettings.QGPUShareEnable True \
    --InstanceAdvancedSettings.DockerGraphPath /var/lib/containerd \
    --InstanceAdvancedSettings.Unschedulable 0 \
    --InstanceAdvancedSettings.PreStartUserScript  \
    --InstanceAdvancedSettings.UserScript  \
    --InstanceAdvancedSettings.DesiredPodNumber 0 \
    --ExtensionAddons.0.AddonName CBS \
    --ExtensionAddons.0.AddonParam {"kind":"App","spec":{"chart":{"chartName":"cbs","chartVersion":"1.1.3"},"values":{"values":[],"rawValues":"e30=","rawValuesType":"json"}}} \
    --ExtensionAddons.1.AddonName APP \
    --ExtensionAddons.1.AddonParam {"kind":"App","spec":{"chart":{"chartName":"user-group-access-control","chartVersion":"1.0.0"}}} \
    --ExtensionAddons.2.AddonName QGPU \
    --ExtensionAddons.2.AddonParam {"kind":"App","spec":{"chart":{"chartName":"qgpu","chartVersion":"1.0.19"},"values":{"values":["config.priority=binpack","config.nodepriority=spread","config.rootdir=/var/lib/kubelet"]}}} \
    --ExtensionAddons.3.AddonName KMS \
    --ExtensionAddons.3.AddonParam {"kind":"App","spec":{"chart":{"chartName":"tke-kms-plugin","chartVersion":"1.0.0"},"name":"tke-kms-plugin","values":{"values":["keyId=7d90e454-8458-11ee-b601-525400741137","region=ap-guangzhou","resource=secrets"]}}} \
    --RunInstancesForNode.0.NodeRole WORKER \
    --RunInstancesForNode.0.RunInstancesPara {"Version":"2017-03-12","InstanceChargeType":"POSTPAID_BY_HOUR","Placement":{"Zone":"ap-shanghai-1","ProjectId":0},"TagSpecification":[{"ResourceType":"instance","Tags":[{"Key":"aa","Value":"cc"}]}],"InstanceType":"S2.MEDIUM2","ImageId":"img-25szkc8t","SystemDisk":{"DiskType":"CLOUD_BSSD","DiskSize":50},"VirtualPrivateCloud":{"VpcId":"vpc-135qxjgs","SubnetId":"subnet-rtp4p7q3","Ipv6AddressCount":0},"InternetAccessible":{"InternetChargeType":"TRAFFIC_POSTPAID_BY_HOUR","InternetMaxBandwidthOut":1,"PublicIpAssigned":true},"InstanceCount":1,"InstanceName":"","LoginSettings":{"KeyIds":["skey-4h43fuxj"]},"SecurityGroupIds":["sg-hjsb4ai4"],"EnhancedService":{"SecurityService":{"Enabled":true},"MonitorService":{"Enabled":true}},"PurchaseSource":"docker_dashboard","UserData":""} \
    --RunInstancesForNode.0.InstanceAdvancedSettingsOverrides.0.MountTarget  \
    --RunInstancesForNode.0.InstanceAdvancedSettingsOverrides.0.DockerGraphPath /var/lib/containerd \
    --RunInstancesForNode.0.InstanceAdvancedSettingsOverrides.0.Unschedulable 0 \
    --RunInstancesForNode.0.InstanceAdvancedSettingsOverrides.0.PreStartUserScript  \
    --RunInstancesForNode.0.InstanceAdvancedSettingsOverrides.0.UserScript  \
    --RunInstancesForNode.0.InstanceAdvancedSettingsOverrides.0.DesiredPodNumber 0 \
    --RunInstancesForNode.0.InstanceAdvancedSettingsOverrides.0.GPUArgs.MIGEnable False \
    --RunInstancesForNode.0.InstanceAdvancedSettingsOverrides.0.GPUArgs.Driver.Version  \
    --RunInstancesForNode.0.InstanceAdvancedSettingsOverrides.0.GPUArgs.Driver.Name  \
    --RunInstancesForNode.0.InstanceAdvancedSettingsOverrides.0.GPUArgs.CUDA.Version  \
    --RunInstancesForNode.0.InstanceAdvancedSettingsOverrides.0.GPUArgs.CUDA.Name  \
    --RunInstancesForNode.0.InstanceAdvancedSettingsOverrides.0.GPUArgs.CUDNN.Version  \
    --RunInstancesForNode.0.InstanceAdvancedSettingsOverrides.0.GPUArgs.CUDNN.Name  \
    --RunInstancesForNode.0.InstanceAdvancedSettingsOverrides.0.GPUArgs.CUDNN.DocName  \
    --RunInstancesForNode.0.InstanceAdvancedSettingsOverrides.0.GPUArgs.CUDNN.DevName 
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

