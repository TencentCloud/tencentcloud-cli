**Example 1: 印章授权申请下发**

给指定人员下发印章授权

Input: 

```
tccli ess CreateSealPolicy --cli-unfold-argument  \
    --SealId 33eb007cdxxxxxx8b65f75905bd \
    --Policy  \
    --Operator.UserId 65fb0c591xxxaa382cc5ed0e \
    --Expired 123 \
    --Users.0.UserId test
```

Output: 
```
{
    "Response": {
        "RequestId": "test",
        "UserIds": []
    }
}
```

