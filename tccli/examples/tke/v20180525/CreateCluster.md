**Example 1: 创建托管集群示例**

创建托管集群

Input: 

```
tccli tke CreateCluster --cli-unfold-argument  \
    --ClusterType MANAGED_CLUSTER \
    --ClusterCIDRSettings.ClusterCIDR 10.4.0.0/14 \
    --RunInstancesForNode.0.NodeRole WORKER \
    --RunInstancesForNode.0.RunInstancesPara {"VirtualPrivateCloud":{"SubnetId":"subnet-xxx","VpcId":"vpc-xxx"},"Placement":{"Zone":"ap-region-1","ProjectId":1032509},"InstanceType":"S3.LARGE8","SystemDisk":{"DiskType":"CLOUD_PREMIUM"},"DataDisks":[{"DiskType":"CLOUD_PREMIUM","DiskSize":50}],"InstanceCount":1,"InternetAccessible":{"PublicIpAssigned":true,"InternetMaxBandwidthOut":1},"LoginSettings":{"Password":"YourPassword"},"UserData":"IyEvYmluL3NoCgplY2hvIGFhYQo \
    --ExtensionAddons.0.AddonName GameApp \
    --ExtensionAddons.0.AddonParam {"kind":"GameApp","apiVersion":"platform.tke/v1","metadata":{"generateName":"ga"},"spec":{"clusterName":"xxx"}}
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

**Example 2: 创建独立集群示例**

创建独立集群

Input: 

```
tccli tke CreateCluster --cli-unfold-argument  \
    --ClusterType INDEPENDENT_CLUSTER \
    --ClusterCIDRSettings.ClusterCIDR 10.4.0.0/14 \
    --RunInstancesForNode.0.NodeRole MASTER_ETCD \
    --RunInstancesForNode.0.RunInstancesPara {"VirtualPrivateCloud":{"SubnetId":"subnet-xxx","VpcId":"vpc-xxx"},"Placement":{"Zone":"ap-region-1","ProjectId":1032509},"InstanceType":"S3.LARGE8","SystemDisk":{"DiskType":"CLOUD_PREMIUM"},"DataDisks":[{"DiskType":"CLOUD_PREMIUM","DiskSize":50}],"InstanceCount":3,"InternetAccessible":{"PublicIpAssigned":true,"InternetMaxBandwidthOut":1},"LoginSettings":{"Password":"YourPassword"},"UserData":"IyEvYmluL3NoCgplY2hvIGFhYQo \
    --RunInstancesForNode.1.NodeRole WORKER \
    --RunInstancesForNode.1.RunInstancesPara {"VirtualPrivateCloud":{"SubnetId":"subnet-xxx","VpcId":"vpc-xxx"},"Placement":{"Zone":"ap-region-1","ProjectId":1032509},"InstanceType":"S3.LARGE8","SystemDisk":{"DiskType":"CLOUD_PREMIUM"},"DataDisks":[{"DiskType":"CLOUD_PREMIUM","DiskSize":50}],"InstanceCount":1,"InternetAccessible":{"PublicIpAssigned":true,"InternetMaxBandwidthOut":1},"LoginSettings":{"Password":"YourPassword"},"UserData":"IyEvYmluL3NoCgplY2hvIGFhYQo \
    --ExtensionAddons.0.AddonName GameApp \
    --ExtensionAddons.0.AddonParam {"kind":"GameApp","apiVersion":"platform.tke/v1","metadata":{"generateName":"ga"},"spec":{"clusterName":"xxx"}}
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

