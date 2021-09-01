**Example 1: 创建实例名称为cis-dev的容器实例**



Input: 

```
tccli cis CreateContainerInstanceInternal --cli-unfold-argument  \
    --Zone ap-chengdu-1 \
    --VpcId vpc-mjmab5g2 \
    --SubnetId subnet-bwyqjag9 \
    --InstanceName cis-dev \
    --RestartPolicy Never \
    --Containers.0.Name sshd \
    --Containers.0.Image jdeathe/centos-ssh:centos-7 \
    --Containers.0.Cpu 0.25 \
    --Containers.0.Memory 0.25
```

Output: 
```
{
    "Response": {
        "InstanceId": "cis-abcdefgh",
        "RequestId": "701c8a35-ed66-fc79-3795-5a1fa72cdbf1"
    }
}
```

