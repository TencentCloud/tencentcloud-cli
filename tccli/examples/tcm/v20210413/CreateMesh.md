**Example 1: CreateMesh**



Input: 

```
tccli tcm CreateMesh --cli-unfold-argument  \
    --DisplayName test \
    --MeshVersion 1.8.1 \
    --Type HOSTED \
    --Config.Istio.OutboundTrafficPolicy ALLOW_ANY \
    --Config.Istio.Tracing.Sampling 1 \
    --ClusterList.0.ClusterId {{clusterId}} \
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
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "MeshId": "mesh-xxxxxxxx"
    }
}
```

