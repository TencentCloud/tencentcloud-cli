**Example 1: 查询集群实例信息**

查询集群实例信息

Input: 

```
tccli tke DescribeClusterInstances --cli-unfold-argument  \
    --ClusterId cls-7ph3twqe
```

Output: 
```
{
    "Response": {
        "InstanceSet": [
            {
                "InstanceAdvancedSettings": {
                    "DockerGraphPath": "/data/docker",
                    "Labels": [
                        {
                            "Name": "key",
                            "Value": "value"
                        }
                    ],
                    "ExtraArgs": {
                        "Kubelet": [
                            "--register-node=true"
                        ]
                    },
                    "Unschedulable": 0,
                    "UserScript": "ZWNobyAiMTAuMTA3LjEwMy41N",
                    "MountTarget": "/var/lib/docker",
                    "DataDisks": [
                        {
                            "DiskPartition": "",
                            "DiskType": "CLOUD_PREMIUM",
                            "DiskSize": 0,
                            "FileSystem": "ext4",
                            "AutoFormatAndMount": true,
                            "MountTarget": "/var/lib/docker"
                        }
                    ]
                },
                "InstanceId": "ins-wggphft5",
                "InstanceRole": "WORKER",
                "LanIP": "10.0.39.19",
                "DrainStatus": "drained",
                "AutoscalingGroupId": "asg-ewqsfgrt",
                "InstanceState": "running",
                "CreatedTime": "2021-02-22T07:14:11Z",
                "NodePoolId": "np-3j4elm0k",
                "FailedReason": "=Ready:True"
            }
        ],
        "TotalCount": 1,
        "RequestId": "f12a6e20-f950-4af9-8f8b-b6329a4961c2"
    }
}
```

