**Example 1: 生成变更超管链接**



Input: 

```
tccli essbasic CreateBatchAdminChangeInvitationsUrl --cli-unfold-argument  \
    --Agent.AppId yDwFoUUckpsomwx1UyhWGhIR2RkhOjw2 \
    --Agent.ProxyOrganizationOpenId ess_open********ation_1 \
    --Agent.ProxyOperator.OpenId kevi****eng \
    --NewAdminName 出** \
    --NewAdminMobile 1320****013 \
    --Endpoint APP \
    --NewAdminIdCardNumber 530823******084610
```

Output: 
```
{
    "Response": {
        "ExpireTime": 1784647929,
        "Url": "pages/guide/index?to=BATCH_CHANGE_SUPER_ADMIN&shortKey=yD3JaU9Tww0plw1zVgf4",
        "RequestId": "2ff2e92e-689a-46b9-96bb-3c5a17ff3c94"
    }
}
```

