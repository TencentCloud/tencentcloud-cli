**Example 1: 查询Docker容器详情**

查询Docker容器详情

Input: 

```
tccli lighthouse DescribeDockerContainerConfiguration --cli-unfold-argument  \
    --ContainerId 809e9d4014f08811779c07639ec13a53ee70ba166201611298611c883e553415 \
    --InstanceId lhins-nwycpjl3
```

Output: 
```
{
    "Response": {
        "ContainerConfiguration": {
            "Command": "",
            "ContainerImage": "nginx",
            "ContainerName": "mynginx",
            "Envs": [
                {
                    "Key": "Key1",
                    "Value": "Value1"
                }
            ],
            "PublishPorts": [
                {
                    "ContainerPort": 80,
                    "HostPort": 8081
                }
            ],
            "Volumes": [
                {
                    "ContainerPath": "/data/container",
                    "HostPath": "/data/host"
                }
            ]
        },
        "RequestId": "07dded6e-0ce5-4f8f-a6ff-3683f70830f8"
    }
}
```

