**Example 1: demo**



Input: 

```
tccli vpc DeleteDockerInternal --cli-unfold-argument  \
    --DockerRequestSet.0.IntMask 16 \
    --DockerRequestSet.0.Subnet 10.0.0.10 \
    --DockerRequestSet.0.UniqueVpcId vpc-7zayowkt \
    --DockerRequestSet.0.VpcId 16769060
```

Output: 
```
{
    "Response": {
        "RequestId": "35b3feac-c2d9-4d27-b394-26ce72c4bfd7"
    }
}
```

**Example 2: 删除DOCKER**



Input: 

```
tccli vpc DeleteDockerInternal --cli-unfold-argument  \
    --DockerRequestSet.0.IntMask 16 \
    --DockerRequestSet.0.Subnet 10.0.0.0 \
    --DockerRequestSet.0.VpcId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

