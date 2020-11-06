**Example 1: 修改伸缩组VPC子网信息**



Input: 

```
tccli as ModifyAutoScalingGroup --cli-unfold-argument  \
    --AutoScalingGroupId asg-ka0s0q80 \
    --VpcId vpc-hy436tmc \
    --SubnetIds subnet-3tmerl37 subnet-b0vxjhot
```

Output: 
```
{
    "Response": {
        "RequestId": "c503ddc6-496c-44c9-8cec-e9f1c3f9c11c"
    }
}
```

**Example 2: 修改伸缩组期望实例、最大实例数、最小实例数**



Input: 

```
tccli as ModifyAutoScalingGroup --cli-unfold-argument  \
    --AutoScalingGroupId asg-ka0s0q80 \
    --DesiredCapacity 3 \
    --MaxSize 10 \
    --MinSize 1
```

Output: 
```
{
    "Response": {
        "RequestId": "b41d8d30-21d4-412c-b7f3-53041879968c"
    }
}
```

