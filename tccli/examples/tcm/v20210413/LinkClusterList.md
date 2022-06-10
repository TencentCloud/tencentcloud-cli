**Example 1: LinkClusterList**



Input: 

```
tccli tcm LinkClusterList --cli-unfold-argument  \
    --MeshId xx \
    --ClusterList.0.ClusterId {{clusterId}} \
    --ClusterList.0.DisplayName  \
    --ClusterList.0.Region sh \
    --ClusterList.0.Role MASTER \
    --ClusterList.0.VpcId {{vpcId}} \
    --ClusterList.0.SubnetId {{subnetId}} \
    --ClusterList.0.Config.AutoInjectionNamespaceList default
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

