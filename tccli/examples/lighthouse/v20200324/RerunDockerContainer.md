**Example 1: 重新创建并运行Docker容器**



Input: 

```
tccli lighthouse RerunDockerContainer --cli-unfold-argument  \
    --ContainerConfiguration.Command  \
    --ContainerConfiguration.ContainerImage nginx \
    --ContainerConfiguration.ContainerName mynginx \
    --ContainerConfiguration.Envs.0.Key Key1 \
    --ContainerConfiguration.Envs.0.Value Value1 \
    --ContainerConfiguration.PublishPorts.0.ContainerPort 80 \
    --ContainerConfiguration.PublishPorts.0.HostPort 8081 \
    --ContainerConfiguration.Volumes.0.ContainerPath /data/container \
    --ContainerConfiguration.Volumes.0.HostPath /data/host \
    --ContainerId 809e9d4014f08811779c07639ec13a53ee70ba166201611298611c883e553415 \
    --InstanceId lhins-nwycpjl3
```

Output: 
```
{
    "Response": {
        "DockerActivityId": "lhda-nn82v77w",
        "RequestId": "2c715b55-de1f-4a46-94a8-caeeee86b0f1"
    }
}
```

