**Example 1: 查看集群中K8S控制器是否开启**



Input: 

```
tccli tke DescribeClusterControllers --cli-unfold-argument  \
    --ClusterId cls-xx
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
        "RequestId": "xx"
    }
}
```

