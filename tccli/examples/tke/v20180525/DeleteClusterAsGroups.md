**Example 1: 删除集群伸缩组**

删除集群伸缩组

Input: 

```
tccli tke DeleteClusterAsGroups --cli-unfold-argument  \
    --ClusterId cls-2wds9k9p \
    --AutoScalingGroupIds asg-2wds9k9p \
    --KeepInstance false
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

