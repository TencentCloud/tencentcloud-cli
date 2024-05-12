**Example 1: 创建 TKE 节点池**

创建 TKE 节点池

Input: 

```
tccli tke CreateNodePool --cli-unfold-argument  \
    --DeletionProtection True \
    --Name nodepool \
    --Tags.0.ResourceType machine \
    --Tags.0.Tags.0.Value  \
    --Tags.0.Tags.0.Key  \
    --Labels.0.Name  \
    --Labels.0.Value  \
    --ClusterId cls-3g5rc2ts \
    --Taints.0.Value  \
    --Taints.0.Key  \
    --Taints.0.Effect  \
    --Unschedulable True \
    --Type 
```

Output: 
```
{
    "Response": {
        "RequestId": "604fea70-fcc3-43b5-b17c-d2a5c8df4c16",
        "NodePoolId": "np-7cxt3lom"
    }
}
```

