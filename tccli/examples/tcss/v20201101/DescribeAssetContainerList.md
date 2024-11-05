**Example 1: 搜索查询容器列表**

搜索查询容器列表

Input: 

```
tccli tcss DescribeAssetContainerList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "CPUUsage": 0,
                "ClusterID": "cls-dfw3e***",
                "ClusterName": "clsfoo***",
                "Cmd": "--controllers=*,-everest-csi-local-volume --leader-elect=true --leader-elect-resource-lock=endpoints --leader-elect-resource-namespace=kube-system --feature-gates=Topology=true,DistributeAttacher=false --provision-with-strict-topology=true --csi-attacher-worker-threads=60 --csi-attacher-detach-worker-threads=60 --csi-attacher-should-reconcile-va=false",
                "ContainerID": "8eaffb2a09728b130020b7fe33d87fe3a45856a2ff39eab57873c34815461b22",
                "ContainerName": "/k8s_everest-csi-controller_everest-csi-controller-7b7df58489-9v9pf_kube-system_3b5f2feb-af96-4c0b-84f0-4e86d0671ae8_2",
                "CreateTime": "2023-08-30 14:48:19",
                "HostID": "ed7bcc17-3ad7-455d-b2f6-1712c005ced0",
                "HostIP": "10.0.4.74",
                "HostName": "ecs-suanfa-0001",
                "ImageID": "sha256:3cdeb1036c11af9e7f906ed2a0535056c71f3f53522242fa24a5aa2022b83f2c",
                "ImageName": "swr.cn-south-1.myhuaweicloud.com/hwofficial/everest:2.1.13",
                "IsolateSource": "source",
                "IsolateTime": "1970-01-01 00:00:01",
                "NetStatus": "NORMAL",
                "NetSubStatus": "NONE",
                "NodeID": "mix-GOmf****",
                "NodeType": "NORMAL",
                "NodeUniqueID": "896e349d-2e7d-4151-a26f-4e9fdafe****",
                "POD": "clife-estate-thirdparty-admin-dm-59785fd6-4****",
                "PodCpu": 0,
                "PodIP": "10.0.1.92",
                "PodMem": 0,
                "PodName": "agent-test-2zrp7",
                "PodUid": "20461430-67c2-455b-932e-6a6c8981****",
                "PublicIp": "116.205.224.125",
                "RamUsage": 99728,
                "RunAs": "paas",
                "Status": "RUNNING",
                "UpdateTime": "2024-07-15 16:05:20"
            }
        ],
        "RequestId": "05844ae1-7f46-41f2-a521-0b6a011cc16d",
        "TotalCount": 1
    }
}
```

