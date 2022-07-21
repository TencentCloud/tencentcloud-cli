**Example 1: 添加DOCKER**



Input: 

```
tccli vpc CreateDockerInternal --cli-unfold-argument  \
    --DockerRequestSet.0.VpcId 1 \
    --DockerRequestSet.0.Subnet 10.0.0.0 \
    --DockerRequestSet.0.IntMask 16
```

Output: 
```
{
    "Response": {
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

