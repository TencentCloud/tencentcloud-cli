**Example 1: 伸缩组扩容一台实例**

伸缩组asg-12yqet78扩容一台实例

Input: 

```
tccli as ScaleOutInstances --cli-unfold-argument  \
    --AutoScalingGroupId asg-12yqet78 \
    --ScaleOutNumber 1
```

Output: 
```
{
    "Response": {
        "ActivityId": "asa-k1q8oaz6",
        "RequestId": "6af368fd-35ff-4dcc-b302-35c378f2cccb"
    }
}
```

