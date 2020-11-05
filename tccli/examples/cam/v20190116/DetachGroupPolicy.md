**Example 1: Unassociating a Policy and a User Group**

Unassociating a policy (ID: 524497) and a user group (ID: 3449)

Input: 

```
tccli cam DetachGroupPolicy --cli-unfold-argument  \
    --PolicyId 524497\
    --DetachGroupId 3449
```

Output: 
```
{
    "Response": {
        "RequestId": "1a21f666-d00e-4df8-92f7-7121f9012e43"
    }
}
```

