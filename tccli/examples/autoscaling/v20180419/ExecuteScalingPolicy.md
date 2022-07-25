**Example 1: 触发伸缩策略**

触发告警伸缩策略

Input: 

```
tccli as ExecuteScalingPolicy --cli-unfold-argument  \
    --HonorCooldown false \
    --AutoScalingPolicyId asp-f59pppuh
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

