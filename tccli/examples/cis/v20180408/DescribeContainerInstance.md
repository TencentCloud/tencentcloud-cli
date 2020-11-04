**Example 1: 获取容器实例sshdlogt的详细信息**



Input: 

```
tccli cis DescribeContainerInstance --cli-unfold-argument  \
    --InstanceName sshdlog
```

Output: 
```
{
    "Response": {
        "ContainerInstance": {
            "InstanceId": "cis-1a082ocw",
            "InstanceName": "sshdlog",
            "Zone": "ap-guangzhou-4",
            "VpcId": "vpc-3p4hvnmx",
            "VpcName": "ddtest",
            "VpcCidr": "10.0.0.0/16",
            "SubnetId": "subnet-r0t1xm4e",
            "SubnetName": "zone4",
            "SubnetCidr": "10.0.2.0/24",
            "CreateTime": "2018-05-18 14:33:40",
            "RestartPolicy": "Never",
            "State": "Running",
            "StartTime": "2018-05-18 14:33:40",
            "LanIp": "10.0.2.20",
            "Containers": [
                {
                    "Command": null,
                    "Args": null,
                    "EnvironmentVars": null,
                    "Image": "jdeathe/centos-ssh:centos-7",
                    "Name": "sshd",
                    "WorkingDir": null,
                    "Cpu": 0.25,
                    "Memory": 0.25,
                    "ContainerId": "c782aa6a7dd3df431ed2094256e90b82f59f39733a794ea294ed11037e4e2477",
                    "RestartCount": 0,
                    "CurrentState": {
                        "StartTime": "2018-05-18 14:34:03",
                        "State": "Running"
                    },
                    "PreviousState": null
                }
            ]
        },
        "RequestId": "07b9d257-ba2c-4a4f-b78a-600d225eb3b2"
    }
}
```

