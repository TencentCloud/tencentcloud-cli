**Example 1: 绑定弹性伸缩组**



Input: 

```
tccli thpc BindAutoScalingGroup --cli-unfold-argument  \
    --ClusterId hpc-5lyv94lq \
    --LaunchConfigurationId asc-jhf9c1gi \
    --AutoScalingGroupId asg-aesc6pcq \
    --ExpansionBusyTime 120 \
    --ShrinkIdleTime 300 \
    --DryRun false
```

Output: 
```
{
    "Response": {
        "RequestId": "f4d90874-f565-463d-ba1d-c707517eeaa1"
    }
}
```

