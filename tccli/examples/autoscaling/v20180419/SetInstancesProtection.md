**Example 1: Setting scale-in protection for CVM instances**



Input: 

```
tccli as SetInstancesProtection --cli-unfold-argument  \
    --AutoScalingGroupId asg-2umy3jbd \
    --InstanceIds ins-b2d33ywt \
    --ProtectedFromScaleIn true
```

Output: 
```
{
    "Response": {
        "RequestId": "5b7168d9-5709-4d69-bd32-880a2f565e33"
    }
}
```

