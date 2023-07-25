**Example 1: 重命名Docker容器**



Input: 

```
tccli lighthouse RenameDockerContainer --cli-unfold-argument  \
    --ContainerId 809e9d4014f08811779c07639ec13a53ee70ba166201611298611c883e553415 \
    --ContainerName test-rename-hello \
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

