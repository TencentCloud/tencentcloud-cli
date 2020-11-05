**Example 1: Unassociating a Policy and a User**

Unassociating policy 16313162 and user 3449203261

Input: 

```
tccli cam DetachUserPolicy --cli-unfold-argument  \
    --PolicyId 16313162\
    --DetachUin 3449203261
```

Output: 
```
{
    "Response": {
        "RequestId": "1a21f666-d00e-4df8-92f7-7121f9012e43"
    }
}
```

