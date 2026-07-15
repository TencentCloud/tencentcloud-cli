**Example 1: 生成批量变更超管链接**



Input: 

```
tccli ess CreateBatchAdminChangeInvitationsUrl --cli-unfold-argument  \
    --Operator.UserId yDwf3UUckps8dvypUEfH3DjwIpMfa0uw \
    --NewAdminName 典子谦 \
    --NewAdminMobile 1880***000 \
    --NewAdminIdCardType ID_CARD \
    --NewAdminIdCardNumber 640521***113278 \
    --NotifyType NONE \
    --Endpoint APP
```

Output: 
```
{
    "Response": {
        "ExpireTime": 1763963107,
        "Url": "pages/guide/index?to=BATCH_CHANGE_SUPER_ADMIN&shortKey=yDtzZUX5uY7W5lPn8P47",
        "RequestId": "e632a5a0-13aa-4ed1-afdc-5e5714a38fcd"
    }
}
```

