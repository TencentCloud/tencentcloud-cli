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
        "TotalCount": 4,
        "InstanceSet": [
            {
                "CreatedTime": "2023-08-17 13:17:57 +0000 UTC",
                "External": {
                    "CPU": 2,
                    "K8SVersion": "v1.26.1-tke.1",
                    "Memory": 1,
                    "Name": "node-10.0.6.x"
                },
                "FailedReason": "",
                "InstanceId": "node-10.0.6.x",
                "InstanceRole": "WORKER",
                "InstanceState": "running",
                "LanIP": "10.0.6.x",
                "Native": null,
                "NodePoolId": "np-4h43fuxj",
                "NodeType": "External",
                "Regular": null,
                "Super": null,
                "Unschedulable": false
            },
            {
                "CreatedTime": "2023-08-17 20:47:35 +0800 CST",
                "External": null,
                "FailedReason": null,
                "InstanceId": "eklet-subnet-4h43fuxjx-yyyy",
                "InstanceRole": "WORKER",
                "InstanceState": "running",
                "LanIP": "a.b.c.d",
                "Native": null,
                "NodePoolId": "np-yyyyy",
                "NodeType": "Super",
                "Regular": null,
                "Super": {
                    "ActiveAt": null,
                    "AutoRenewFlag": null,
                    "CPU": null,
                    "ExpireAt": null,
                    "InstanceAttribute": null,
                    "MaxCPUScheduledPod": null,
                    "Memory": null,
                    "Name": "",
                    "ResourceType": null,
                    "SubnetId": "subnet-4h43fuxj",
                    "UsedCPU": null,
                    "UsedMemory": null,
                    "VpcId": null,
                    "Zone": null
                },
                "Unschedulable": false
            },
            {
                "CreatedTime": "2023-08-17 12:46:40 +0000 UTC",
                "External": null,
                "FailedReason": "=",
                "InstanceId": "np-4h43fuxj-4h43fuxj",
                "InstanceRole": "WORKER",
                "InstanceState": "running",
                "LanIP": "10.0.0.x",
                "Native": {
                    "CPU": 2,
                    "CreatedAt": "2023-08-17 20:46:39",
                    "DataDisks": [
                        {
                            "AutoFormatAndMount": true,
                            "DiskPartition": "",
                            "DiskSize": 50,
                            "DiskType": "CLOUD_PREMIUM",
                            "FileSystem": "ext4",
                            "MountTarget": "/data"
                        }
                    ],
                    "DisplayName": "tke-np-4h43fuxj-worker",
                    "ExpiredTime": "",
                    "GPU": 0,
                    "GPUParams": {
                        "CUDA": "",
                        "CUDNN": "",
                        "Driver": "",
                        "Fabric": false,
                        "MIGEnable": false
                    },
                    "InstanceChargeType": "POSTPAID_BY_HOUR",
                    "InstanceFamily": "S2",
                    "InstanceType": "S2.MEDIUM2",
                    "InternetAccessible": {
                        "BandwidthPackageId": "",
                        "ChargeType": "",
                        "MaxBandwidthOut": 0
                    },
                    "IsProtectedFromScaleIn": false,
                    "KeyIds": [
                        "skey-ccccc"
                    ],
                    "LanIp": "10.0.0.x",
                    "LoginStatus": "Opened",
                    "MachineName": "np-4h43fuxj-4h43fuxj",
                    "MachineState": "Running",
                    "Memory": 2,
                    "OsImage": "TencentOS Server 3.1 (Final)",
                    "PayMode": "POSTPAID_BY_HOUR",
                    "RenewFlag": "",
                    "SecurityGroupIDs": [
                        "sg-ccccc"
                    ],
                    "SubnetId": "subnet-nqx1ymwm",
                    "SystemDisk": {
                        "AutoFormatAndMount": false,
                        "DiskSize": 50,
                        "DiskType": "CLOUD_PREMIUM",
                        "FileSystem": "",
                        "MountTarget": ""
                    },
                    "VpcId": "vpc-zzzzz",
                    "WanIp": "",
                    "Zone": "ap-guangzhou-3"
                },
                "NodePoolId": "np-4h43fuxj",
                "NodeType": "Native",
                "Regular": null,
                "Super": null,
                "Unschedulable": false
            },
            {
                "CreatedTime": "2023-08-17 12:35:42 +0000 UTC",
                "External": null,
                "FailedReason": "=Ready:True",
                "InstanceId": "ins-aaaaaa",
                "InstanceRole": "WORKER",
                "InstanceState": "running",
                "LanIP": "10.0.0.x",
                "Native": null,
                "NodePoolId": "",
                "NodeType": "Regular",
                "Regular": {
                    "AutoscalingGroupId": "",
                    "InstanceAdvancedSettings": {
                        "DesiredPodNumber": 64,
                        "ExtraArgs": {
                            "Kubelet": null
                        },
                        "PreStartUserScript": null,
                        "RuntimeConfig": null,
                        "UserScript": ""
                    }
                },
                "Super": null,
                "Unschedulable": false
            }
        ],
        "Errors": [],
        "RequestId": "42c27fd7-e2ca-48b2-9f4e-acdb9eef6ee7"
    }
}
```

