**Example 1: 修改伸缩组VPC子网信息**

修改指定伸缩组的VpcId和SubnetIds参数

Input: 

```
tccli as ModifyAutoScalingGroup --cli-unfold-argument  \
    --AutoScalingGroupId asg-ka0s0q80 \
    --SubnetIds subnet-b0vxjhot subnet-3tmerl37 \
    --VpcId vpc-hy436tmc
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

修改指定伸缩组的期望实例数为3，最大实例数为10，最小实例数为1

Input: 

```
tccli as ModifyAutoScalingGroup --cli-unfold-argument  \
    --AutoScalingGroupId asg-ka0s0q80 \
    --MinSize 1 \
    --MaxSize 10 \
    --DesiredCapacity 3
```

Output: 
```
{
    "Response": {
        "RequestId": "b41d8d30-21d4-412c-b7f3-53041879968c"
    }
}
```

