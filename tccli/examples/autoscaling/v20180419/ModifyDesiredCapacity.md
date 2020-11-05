**Example 1: Modifying the desired capacity of a scaling group**



Input: 

```
tccli as ModifyDesiredCapacity --cli-unfold-argument  \
    --AutoScalingGroupId asg-nvnlpbb8\
    --DesiredCapacity 2
```

Output: 
```
{
    "Response": {
        "RequestId": "2f7c0f11-edfd-4598-a5f6-fb5c10cc9d8e"
    }
}
```

