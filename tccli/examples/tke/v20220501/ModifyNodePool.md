**Example 1: 更新 TKE 节点池**

用户更新节点池

Input: 

```
tccli tke ModifyNodePool --cli-unfold-argument  \
    --ClusterId cls-6sukkvyx \
    --Native.DeletePolicy Newest \
    --Native.EnableAutoscaling True \
    --Native.Scaling.CreatePolicy ZonePriority \
    --Native.Scaling.MaxReplicas 1 \
    --Native.Scaling.MinReplicas 0 \
    --NodePoolId np-00igpu9y
```

Output: 
```
{
    "Response": {
        "RequestId": "9bd42c72-dd16-46bc-9d1e-b4020c59fab8"
    }
}
```

