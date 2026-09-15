**Example 1: 修改kubelet参数并应用到存量节点**



Input: 

```
tccli tke ModifyClusterNodePool --cli-unfold-argument  \
    --ClusterId cls-7cohhdby \
    --NodePoolId np-prfovafy \
    --ExtraArgs.Kubelet v=3
```

Output: 
```
{
    "Response": {
        "RequestId": "d4eef499-a63b-41ec-a24b-fb6bfcaa6f98"
    }
}
```

