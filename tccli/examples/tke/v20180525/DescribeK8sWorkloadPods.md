**Example 1: 查询工作负载的配置**

查询工作负载的配置

Input: 

```
tccli tke DescribeK8sWorkloadPods --cli-unfold-argument  \
    --ClusterId cls-123deabc \
    --Namespace default \
    --Kind Deployment \
    --Name nginx
```

Output: 
```
{
    "Response": {
        "Pods": [
            {
                "Name": "nginx-6898468859-94n7w",
                "Namespace": "default",
                "Status": "Running",
                "CreationTimestamp": "2023-11-20T03:06:08Z"
            }
        ],
        "RequestId": "f55aaa93-c681-47c9-860a-59ae16ade268"
    }
}
```

