**Example 1: Associating a Policy with a User**

Associating a policy (ID: 524497) with user 3449203261

Input: 

```
tccli cam AttachUserPolicy --cli-unfold-argument  \
    --PolicyId 524497 \
    --AttachUin 3449203261
```

Output: 
```
{
    "Response": {
        "RequestId": "1a21f666-d00e-4df8-92f7-7121f9012e43"
    }
}
```

