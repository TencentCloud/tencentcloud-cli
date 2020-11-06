**Example 1: 创建黑石DOCKER子网**

创建黑石DOCKER子网，DOCKER子网专门用于部署DOCKER。会分配VlanId给DOCKER子网。DOCKER子网是关闭分布式网关的，DOCKER子网最好限制于在一个物理机上使用

Input: 

```
tccli bmvpc CreateDockerSubnetWithVlan --cli-unfold-argument  \
    --VpcId vpc-44cxlz7z \
    --SubnetSet.0.SubnetName ownDocker1 \
    --SubnetSet.0.CidrBlock 10.10.246.0/26 \
    --SubnetSet.1.SubnetName ownDocker2 \
    --SubnetSet.1.CidrBlock 10.10.246.64/26
```

Output: 
```
{
    "Response": {
        "TaskId": 1234,
        "RequestId": "09186e64-d19e-4ca1-968f-df4fc8139192"
    }
}
```

