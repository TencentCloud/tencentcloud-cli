**Example 1: 修改集群运行时配置**



Input: 

```
tccli tke ModifyClusterRuntimeConfig --cli-unfold-argument  \
    --ClusterId clx-o8hjuza0 \
    --DstK8SVersion 1.24.4 \
    --ClusterRuntimeConfig.RuntimeType containerd \
    --ClusterRuntimeConfig.RuntimeVersion 1.6.9 \
    --NodePoolRuntimeConfig.0.NodePoolId np-3z37njiu \
    --NodePoolRuntimeConfig.0.RuntimeType containerd \
    --NodePoolRuntimeConfig.0.RuntimeVersion 1.6.9 \
    --NodePoolRuntimeConfig.0.NodePoolName np-test
```

Output: 
```
{
    "Response": {
        "RequestId": "fb370cb6-df57-4077-hjxk-758225788b9b"
    }
}
```

