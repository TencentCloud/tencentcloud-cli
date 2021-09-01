**Example 1: 伸缩组缩容一台实例**



Input: 

```
tccli as ScaleInInstances --cli-unfold-argument  \
    --AutoScalingGroupId asg-12yqet78 \
    --ScaleInNumber 1
```

Output: 
```
{
    "Response": {
        "ActivityId": "asa-n6w01f6m",
        "RequestId": "c0bb46ea-2b47-471c-9099-e20bf7a23078"
    }
}
```

