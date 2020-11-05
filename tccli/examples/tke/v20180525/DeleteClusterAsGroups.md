**Example 1: Deleting cluster scaling group**

This example shows you how to delete a cluster scaling group.

Input: 

```
tccli tke DeleteClusterAsGroups --cli-unfold-argument  \
    --ClusterId cls-xxxxxx\
    --AutoScalingGroupIds asg-xxxxxxxx\
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

