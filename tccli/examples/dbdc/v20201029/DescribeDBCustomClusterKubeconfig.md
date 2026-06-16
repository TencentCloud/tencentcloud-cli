**Example 1: 查询 DB Custom 集群 Kubeconfig 配置**



Input: 

```
tccli dbdc DescribeDBCustomClusterKubeconfig --cli-unfold-argument  \
    --ClusterId dbcc-0cj0av3j
```

Output: 
```
{
    "Response": {
        "Kubeconfig": "mock-kubeconfig-for-cls-mock00001",
        "RequestId": "d5830035-cfbf-49bb-b6b3-a22d3b76b897"
    }
}
```

