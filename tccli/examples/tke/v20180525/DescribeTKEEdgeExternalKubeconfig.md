**Example 1: 获取边缘计算外部访问的kubeconfig**

获取边缘计算外部访问的kubeconfig

Input: 

```
tccli tke DescribeTKEEdgeExternalKubeconfig --cli-unfold-argument  \
    --ClusterId cls-2wds9k9p
```

Output: 
```
{
    "Response": {
        "Kubeconfig": "[REDACTED]",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

