**Example 1: Associating a Policy with a User**

Associating a policy (ID: 524497) with a user group (ID: 3449)

Input: 

```
tccli cam AttachGroupPolicy --cli-unfold-argument  \
    --PolicyId 524497\
    --AttachGroupId 3449
```

Output: 
```
{
    "Response": {
        "RequestId": "1a21f666-d00e-4df8-92f7-7121f9012e43"
    }
}
```

