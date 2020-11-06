**Example 1: Modifies server ports in batches**



Input: 

```
tccli clb ModifyTargetGroupInstancesPort --cli-unfold-argument  \
    --TargetGroupId lbtg-815iz538 \
    --TargetGroupInstances.0.BindIP 172.16.0.34 \
    --TargetGroupInstances.0.Port 123 \
    --TargetGroupInstances.0.NewPort 2233
```

Output: 
```
{
    "Response": {
        "RequestId": "15566c73-3881-4762-939f-bae9ecf25808"
    }
}
```

