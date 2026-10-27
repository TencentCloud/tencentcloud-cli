**Example 1: UpdatePolicy**



Input: 

```
tccli cvd UpdatePolicy --cli-unfold-argument  \
    --PolicyId policy-12dfew3 \
    --PolicyInfoList.0.PolicyValue 0 \
    --PolicyInfoList.0.PolicyType 0 \
    --Name policy \
    --Description policy
```

Output: 
```
{
    "Response": {
        "RequestId": "2bcfe8b7-8ea8-4488-9d17-f1aeb106eecd"
    }
}
```

