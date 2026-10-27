**Example 1: CreatePolicy**

CreatePolicy

Input: 

```
tccli cvd CreatePolicy --cli-unfold-argument  \
    --UserIds tom \
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

