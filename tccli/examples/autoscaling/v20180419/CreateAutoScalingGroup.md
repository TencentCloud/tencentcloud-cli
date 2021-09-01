**Example 1: 创建伸缩组**

创建伸缩组，VPC网络，配置7层负载均衡器

Input: 

```
tccli as CreateAutoScalingGroup --cli-unfold-argument  \
    --AutoScalingGroupName asg-vpc-7layer-lb \
    --DefaultCooldown 300 \
    --DesiredCapacity 0 \
    --LaunchConfigurationId asc-7vucy6ae \
    --MaxSize 10 \
    --MinSize 0 \
    --ProjectId 0 \
    --VpcId vpc-hy436tmc \
    --SubnetIds subnet-3tmerl37 subnet-b0vxjhot \
    --TerminationPolicies OLDEST_INSTANCE \
    --ForwardLoadBalancers.0.LoadBalancerId lb-23aejgcv \
    --ForwardLoadBalancers.0.ListenerId lbl-ncw704sn \
    --ForwardLoadBalancers.0.LocationId loc-l3hmaev9 \
    --ForwardLoadBalancers.0.Region ap-guangzhou \
    --ForwardLoadBalancers.0.TargetAttributes.0.Port 8080 \
    --ForwardLoadBalancers.0.TargetAttributes.0.Weight 10
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

