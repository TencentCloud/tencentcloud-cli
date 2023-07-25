**Example 1: 查询Docker容器列表**

查询Docker容器列表

Input: 

```
tccli lighthouse DescribeDockerContainers --cli-unfold-argument  \
    --InstanceId lhins-nwycpjl3
```

Output: 
```
{
    "Response": {
        "DockerContainerSet": [
            {
                "Command": "/docker-entrypoint.sh nginx -g 'daemon off;'",
                "ContainerId": "edbc15ffac7074bf28cbc6071f422f90029154aefd9bf0392f33b247a3577a57",
                "ContainerImage": "nginx",
                "ContainerName": "mynginx",
                "CreatedTime": "2021-07-13T08:09:27Z",
                "PublishPortSet": [
                    {
                        "ContainerPort": 80,
                        "HostPort": 8081,
                        "Ip": "0.0.0.0",
                        "Protocol": "tcp"
                    }
                ],
                "State": "running",
                "Status": "Up 19 hours",
                "VolumeSet": [
                    {
                        "ContainerPath": "/data/container",
                        "HostPath": "/data/host"
                    }
                ]
            }
        ],
        "RequestId": "54ff6139-244a-4074-938a-26b5d321d4c1",
        "TotalCount": 1
    }
}
```

