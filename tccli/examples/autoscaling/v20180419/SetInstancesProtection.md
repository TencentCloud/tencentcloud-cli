**Example 1: 为实例设置保护**



Input: 

```
tccli as SetInstancesProtection --cli-unfold-argument  \
    --AutoScalingGroupId asg-2umy3jbd \
    --ProtectedFromScaleIn true \
    --InstanceIds ins-b2d33ywt
```

Output: 
```
{
    "Response": {
        "RequestId": "5b7168d9-5709-4d69-bd32-880a2f565e33"
    }
}
```

