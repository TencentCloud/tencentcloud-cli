**Example 1: 查看第三方节点池列表**



Input: 

```
tccli tke DescribeExternalNodePools --cli-unfold-argument  \
    --ClusterId cls-lm91rql0
```

Output: 
```
{
    "Response": {
        "NodePoolSet": [
            {
                "ClusterCIDR": "172.16.0.0/16",
                "InstanceAdvancedSettings": {
                    "DockerGraphPath": "/var/lib/docker",
                    "ExtraArgs": {
                        "Kubelet": null
                    },
                    "Unschedulable": 0
                },
                "Labels": [
                    {
                        "Name": "lkong1",
                        "Value": "lkong1"
                    },
                    {
                        "Name": "tke.cloud.tencent.com/location",
                        "Value": "gz"
                    }
                ],
                "LifeState": "normal",
                "Name": "IDC节点池",
                "NetworkType": "",
                "NodePoolId": "np-0nwzqj10",
                "RuntimeConfig": {
                    "RuntimeType": "docker",
                    "RuntimeVersion": "19.3"
                },
                "Taints": []
            }
        ],
        "RequestId": "4c6c63c7-b23e-4896-bf3b-6bc44dxxxxxx",
        "TotalCount": 1
    }
}
```

