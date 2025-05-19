**Example 1: 修改工作负载的镜像**

修改工作负载的镜像

Input: 

```
tccli tke ModifyK8sWorkload --cli-unfold-argument  \
    --ClusterId cls-123deabc \
    --Namespace default \
    --Kind Deployment \
    --Name nginx \
    --Containers.0.Name nginx \
    --Containers.0.Image nginx:latest
```

Output: 
```
{
    "Response": {
        "RequestId": "f55aaa93-c681-47c9-860a-59ae16ade268"
    }
}
```

