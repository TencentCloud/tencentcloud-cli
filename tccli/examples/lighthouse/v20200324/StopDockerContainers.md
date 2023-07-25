**Example 1: 停止Docker容器**



Input: 

```
tccli lighthouse StopDockerContainers --cli-unfold-argument  \
    --ContainerIds 809e9d4014f08811779c07639ec13a53ee70ba166201611298611c883e553415 \
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

