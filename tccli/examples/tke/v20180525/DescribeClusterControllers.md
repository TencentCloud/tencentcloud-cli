**Example 1: 查看集群中K8S控制器是否开启**

查看集群中K8S控制器是否开启

Input: 

```
tccli tke DescribeClusterControllers --cli-unfold-argument  \
    --ClusterId cls-7ph3twqe
```

Output: 
```
{
    "Response": {
        "ControllerStatusSet": [
            {
                "Name": "route-controller",
                "Enabled": true
            },
            {
                "Name": "node-ipam-controller",
                "Enabled": true
            }
        ],
        "RequestId": "f12a6e20-f950-4af9-8f8b-b6329a4961c2"
    }
}
```

