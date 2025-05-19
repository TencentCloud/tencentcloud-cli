**Example 1: 查询工作负载的配置**

查询工作负载的配置

Input: 

```
tccli tke DescribeK8sWorkload --cli-unfold-argument  \
    --ClusterId cls-7chbcyat \
    --Kind Deployment \
    --Name coredns \
    --Namespace kube-system
```

Output: 
```
{
    "Response": {
        "Containers": [
            {
                "Image": "ccr.ccs.tencentyun.com/tkeimages/coredns:1.11.1",
                "Name": "coredns"
            }
        ],
        "RequestId": "f0a09224-0694-4474-bd49-cb884edb617a",
        "Status": {
            "AvailableReplicas": 2,
            "ReadyReplicas": 2,
            "Replicas": 2,
            "UpdatedReplicas": 2
        }
    }
}
```

