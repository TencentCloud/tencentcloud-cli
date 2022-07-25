**Example 1: 创建伸缩组**

创建伸缩组，VPC网络，配置7层负载均衡器

Input: 

```
tccli as CreateAutoScalingGroup --cli-unfold-argument  \
    --VpcId vpc-hy436tmc \
    --DesiredCapacity 0 \
    --LaunchConfigurationId asc-7vucy6ae \
    --ProjectId 0 \
    --SubnetIds subnet-b0vxjhot subnet-3tmerl37 \
    --AutoScalingGroupName asg-vpc-7layer-lb \
    --DefaultCooldown 300 \
    --MinSize 0 \
    --MaxSize 10 \
    --TerminationPolicies OLDEST_INSTANCE \
    --ForwardLoadBalancers.0.TargetAttributes.0.Port 8080 \
    --ForwardLoadBalancers.0.TargetAttributes.0.Weight 10 \
    --ForwardLoadBalancers.0.Region ap-guangzhou \
    --ForwardLoadBalancers.0.LocationId loc-l3hmaev9 \
    --ForwardLoadBalancers.0.ListenerId lbl-ncw704sn \
    --ForwardLoadBalancers.0.LoadBalancerId lb-23aejgcv
```

Output: 
```
{
    "Response": {
        "AutoScalingGroupId": "asg-nkdwoui0",
        "RequestId": "a5d66fed-85b9-4f43-8243-597337ba896e"
    }
}
```

