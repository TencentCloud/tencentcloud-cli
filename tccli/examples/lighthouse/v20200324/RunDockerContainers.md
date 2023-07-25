**Example 1: 创建并运行Docker容器**



Input: 

```
tccli lighthouse RunDockerContainers --cli-unfold-argument  \
    --Containers.0.Command  \
    --Containers.0.ContainerImage nginx \
    --Containers.0.ContainerName mynginx \
    --Containers.0.Envs.0.Key Key1 \
    --Containers.0.Envs.0.Value Value1 \
    --Containers.0.PublishPorts.0.ContainerPort 80 \
    --Containers.0.PublishPorts.0.HostPort 8081 \
    --Containers.0.Volumes.0.ContainerPath /data/container \
    --Containers.0.Volumes.0.HostPath /data/host \
    --InstanceId lhins-nwycpjl3
```

Output: 
```
{
    "Response": {
        "DockerActivitySet": [
            "lhda-9qq8eu91"
        ],
        "RequestId": "cd373a49-2506-42f6-a205-c2f5ae467849"
    }
}
```

