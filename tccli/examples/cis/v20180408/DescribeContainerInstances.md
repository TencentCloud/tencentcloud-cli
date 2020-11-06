**Example 1: 查询容器实例列表**



Input: 

```
tccli cis DescribeContainerInstances --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --Filters.0.Name InstanceName \
    --Filters.0.ValueList hello
```

Output: 
```
{
    "Response": {
        "ContainerInstanceList": [
            {
                "InstanceId": "cis-h2ud12sa",
                "InstanceName": "helloworld",
                "Zone": "ap-guangzhou-4",
                "VpcId": "vpc-3p4hvnmx",
                "VpcName": "ddtest",
                "VpcCidr": "10.0.0.0/16",
                "SubnetId": "subnet-r0t1xm4e",
                "SubnetName": "zone4",
                "SubnetCidr": "10.0.2.0/24",
                "CreateTime": "2018-05-17 11:14:28",
                "RestartPolicy": "Never",
                "State": "Succeeded",
                "StartTime": "2018-05-17 11:16:23",
                "LanIp": "10.0.2.11",
                "Containers": [
                    {
                        "Command": "echo",
                        "Args": [
                            "hello world"
                        ],
                        "EnvironmentVars": null,
                        "Image": "alpine:latest",
                        "Name": "helloworld",
                        "WorkingDir": null,
                        "Cpu": 0.25,
                        "Memory": 0.25,
                        "ContainerId": "7aa85b70a3e1e1856718cbb7f1de0dba236272380da2854f059dd489d4d967cd",
                        "RestartCount": 0,
                        "CurrentState": {
                            "Reason": "Completed",
                            "StartTime": "2018-05-17 11:16:42",
                            "FinishTime": "2018-05-17 11:16:42",
                            "ExitCode": 0,
                            "State": "Terminated"
                        },
                        "PreviousState": null
                    }
                ]
            },
            {
                "InstanceId": "cis-esmfjhek",
                "InstanceName": "helloworld2",
                "Zone": "ap-guangzhou-4",
                "VpcId": "vpc-3p4hvnmx",
                "VpcName": "ddtest",
                "VpcCidr": "10.0.0.0/16",
                "SubnetId": "subnet-r0t1xm4e",
                "SubnetName": "zone4",
                "SubnetCidr": "10.0.2.0/24",
                "CreateTime": "2018-05-18 14:40:57",
                "RestartPolicy": "Never",
                "State": "Succeeded",
                "StartTime": "2018-05-18 14:40:57",
                "LanIp": "10.0.2.24",
                "Containers": [
                    {
                        "Command": "echo",
                        "Args": [
                            "hello world"
                        ],
                        "EnvironmentVars": null,
                        "Image": "busybox:latest",
                        "Name": "echo",
                        "WorkingDir": null,
                        "Cpu": 0.25,
                        "Memory": 0.25,
                        "ContainerId": "11e66fc00ed8c653e256ede6885a8b428731387443331eeef7f12d7f77ceaf39",
                        "RestartCount": 0,
                        "CurrentState": {
                            "Reason": "Completed",
                            "StartTime": "2018-05-18 14:41:11",
                            "FinishTime": "2018-05-18 14:41:11",
                            "ExitCode": 0,
                            "State": "Terminated"
                        },
                        "PreviousState": null
                    }
                ]
            }
        ],
        "TotalCount": 2,
        "RequestId": "7695ee56-77d2-43b1-bc7d-d85f411d44c6"
    }
}
```

