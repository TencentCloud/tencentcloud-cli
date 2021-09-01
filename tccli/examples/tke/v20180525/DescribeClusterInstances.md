**Example 1: 查询集群实例信息**

查询集群实例信息

Input: 

```
tccli tke DescribeClusterInstances --cli-unfold-argument  \
    --ClusterId cls-xxxxxx
```

Output: 
```
{
    "Response": {
        "InstanceSet": [
            {
                "InstanceAdvancedSettings": {
                    "DockerGraphPath": "xx",
                    "Labels": [
                        {
                            "Name": "xx",
                            "Value": "xx"
                        }
                    ],
                    "ExtraArgs": {
                        "Kubelet": [
                            "xx"
                        ]
                    },
                    "Unschedulable": 0,
                    "UserScript": "xx",
                    "MountTarget": "xx",
                    "DataDisks": [
                        {
                            "DiskPartition": "xx",
                            "DiskType": "xx",
                            "DiskSize": 0,
                            "FileSystem": "xx",
                            "AutoFormatAndMount": true,
                            "MountTarget": "xx"
                        }
                    ]
                },
                "InstanceId": "xx",
                "InstanceRole": "xx",
                "LanIP": "xx",
                "DrainStatus": "xx",
                "AutoscalingGroupId": "xx",
                "InstanceState": "xx",
                "CreatedTime": "xx",
                "NodePoolId": "xx",
                "FailedReason": "xx"
            }
        ],
        "TotalCount": 1,
        "RequestId": "xx"
    }
}
```

