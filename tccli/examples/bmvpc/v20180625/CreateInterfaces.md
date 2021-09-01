**Example 1: 物理机加入子网**

物理机加入子网

Input: 

```
tccli bmvpc CreateInterfaces --cli-unfold-argument  \
    --VpcId vpc-q1j48dkd \
    --SubnetId subnet-q1j48dkd \
    --InstanceIds cpm-q1j48dkd
```

Output: 
```
{
    "Response": {
        "TaskId": 12312,
        "RequestId": "62735da7-4546-4d63-8d42-36ced3bd3d94"
    }
}
```

