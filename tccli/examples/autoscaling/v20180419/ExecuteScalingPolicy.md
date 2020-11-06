**Example 1: Triggering a scaling policy**

This example shows you how to trigger an alarm scaling policy.

Input: 

```
tccli as ExecuteScalingPolicy --cli-unfold-argument  \
    --AutoScalingPolicyId asp-f59pppuh \
    --HonorCooldown false
```

Output: 
```
{
    "Response": {
        "ActivityId": "asa-o4v87ae9",
        "RequestId": "116213d6-2269-44cc-af76-c4a8dc7dbdf9"
    }
}
```

