**Example 1: 印章授权申请下发**

给指定人员下发印章授权

Input: 

```
tccli ess CreateSealPolicy --cli-unfold-argument  \
    --SealId 33eb007cda138df0dc0f8b65f75905bd \
    --Policy  \
    --Operator.UserId 65fb0c591044be8a1f60aa382cc5ed0e \
    --Operator.ClientIp 192.6.5.45 \
    --Operator.Channel string \
    --Operator.OpenId string \
    --Operator.ProxyIp 192.6.5.45 \
    --Expired 123 \
    --Users.0.OpenId xx \
    --Users.0.ClientIp xx \
    --Users.0.UserId xx \
    --Users.0.Channel xx \
    --Users.0.ProxyIp xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "UserIds": []
    }
}
```

