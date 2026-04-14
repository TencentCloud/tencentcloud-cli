**Example 1: 查看注册节点池列表**

查看注册节点池列表

Input: 

```
tccli tke DescribeExternalNodePools --cli-unfold-argument  \
    --ClusterId cls-edk3h1cs
```

Output: 
```
{
    "Response": {
        "NodePoolSet": [
            {
                "ClusterCIDR": "",
                "DeletionProtection": false,
                "InstanceAdvancedSettings": {
                    "DataDisks": null,
                    "DesiredPodNumber": 0,
                    "DockerGraphPath": "",
                    "ExtraArgs": {
                        "Kubelet": []
                    },
                    "GPUArgs": null,
                    "Labels": null,
                    "MountTarget": "",
                    "PreStartUserScript": "",
                    "Taints": null,
                    "Unschedulable": 0,
                    "UserScript": ""
                },
                "Labels": [
                    {
                        "Name": "tke.cloud.tencent.com/nodepool-id",
                        "Value": "np-rpyicty0"
                    },
                    {
                        "Name": "node.kubernetes.io/instance-type",
                        "Value": "external"
                    },
                    {
                        "Name": "tke.cloud.tencent.com/cbs-mountable",
                        "Value": "false"
                    }
                ],
                "LifeState": "normal",
                "Name": "注册节点池",
                "NetworkType": "",
                "NodePoolId": "np-rpyicty0",
                "NodeType": "CPU",
                "RuntimeConfig": {
                    "RuntimeType": "containerd",
                    "RuntimeVersion": "1.7.28"
                },
                "Taints": []
            }
        ],
        "RequestId": "7526c3f8-4ac5-458a-bf42-cafbc8a92927",
        "TotalCount": 1
    }
}
```

