**Example 1: 查询容器实例列表**



Input: 

```
tccli cis ListContainerInstance --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ContainerInstanceList": [
            {
                "InstanceId": "cis-ql2xh3x9",
                "InstanceName": "cis-dev233",
                "VpcId": "vpc-mjmab5g2",
                "SubnetId": "subnet-bwyqjag9",
                "CreateTime": "2018-04-18 19:31:07",
                "RestartPolicy": "Never",
                "State": "Running",
                "StartTime": "2018-04-18 19:33:25",
                "Containers": [
                    {
                        "Command": null,
                        "Args": null,
                        "EnvironmentVars": null,
                        "Image": "jdeathe/centos-ssh:centos-7",
                        "Name": "sshd",
                        "Cpu": 1.0,
                        "Memory": 1,
                        "RestartCount": 0,
                        "CurrentState": {
                            "StartTime": "2018-04-18 19:33:41",
                            "State": "Running"
                        },
                        "PreviousState": null
                    }
                ]
            },
            {
                "InstanceId": "cis-mfntr8n3",
                "InstanceName": "cis-dev6",
                "VpcId": "vpc-mjmab5g2",
                "SubnetId": "subnet-bwyqjag9",
                "CreateTime": "2018-04-19 13:34:37",
                "RestartPolicy": "Never",
                "State": "Succeeded",
                "StartTime": "2018-04-19 13:34:36",
                "Containers": [
                    {
                        "Command": [
                            "/bin/sh",
                            "-c",
                            "echo helloworld"
                        ],
                        "Args": [
                            "hi"
                        ],
                        "EnvironmentVars": [
                            {
                                "Name": "TEST",
                                "Value": "cis"
                            }
                        ],
                        "Image": "alpine:latest",
                        "Name": "helloworld",
                        "Cpu": 1.0,
                        "Memory": 1,
                        "RestartCount": 0,
                        "CurrentState": {
                            "Reason": "Completed",
                            "StartTime": "2018-04-19 13:34:40",
                            "FinishTime": "2018-04-19 13:34:40",
                            "ExitCode": 0
                        },
                        "PreviousState": null
                    }
                ]
            },
            {
                "InstanceId": "cis-qlbsyopp",
                "InstanceName": "cis-dev7",
                "VpcId": "vpc-mjmab5g2",
                "SubnetId": "subnet-bwyqjag9",
                "CreateTime": "2018-04-19 21:33:35",
                "RestartPolicy": "Never",
                "State": "Succeeded",
                "StartTime": "2018-04-19 21:33:35",
                "Containers": [
                    {
                        "Command": [
                            "/bin/sh",
                            "-c",
                            "echo helloworld"
                        ],
                        "Args": [
                            "hi"
                        ],
                        "EnvironmentVars": [
                            {
                                "Name": "TEST",
                                "Value": "cis"
                            }
                        ],
                        "Image": "alpine:latest",
                        "Name": "helloworld",
                        "Cpu": 1.0,
                        "Memory": 1,
                        "RestartCount": 0,
                        "CurrentState": {
                            "Reason": "Completed",
                            "StartTime": "2018-04-19 21:33:41",
                            "FinishTime": "2018-04-19 21:33:41",
                            "ExitCode": 0
                        },
                        "PreviousState": null
                    }
                ]
            },
            {
                "InstanceId": "cis-pnc0esgv",
                "InstanceName": "cis-dev2",
                "VpcId": "vpc-mjmab5g2",
                "SubnetId": "subnet-bwyqjag9",
                "CreateTime": "2018-04-20 17:07:36",
                "RestartPolicy": "Never",
                "State": "Running",
                "StartTime": "2018-04-20 17:07:35",
                "Containers": [
                    {
                        "Command": null,
                        "Args": null,
                        "EnvironmentVars": null,
                        "Image": "jdeathe/centos-ssh:centos-7",
                        "Name": "sshd",
                        "Cpu": 1.0,
                        "Memory": 1,
                        "RestartCount": 0,
                        "CurrentState": {
                            "StartTime": "2018-04-20 17:07:36",
                            "State": "Running"
                        },
                        "PreviousState": null
                    }
                ]
            }
        ],
        "RequestId": "12345"
    }
}
```

