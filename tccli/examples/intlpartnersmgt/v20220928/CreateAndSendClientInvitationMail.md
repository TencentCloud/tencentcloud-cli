**Example 1: 创建邀请客户链接**



Input: 

```
tccli intlpartnersmgt CreateAndSendClientInvitationMail --cli-unfold-argument  \
    --Email abc@gmail.com
```

Output: 
```
{
    "Response": {
        "InvitationLink": "https://www.tencentcloud.com/reseller-customer/invitation?RegisterToken=28c******2f",
        "RequestId": "91158930-****-496f-****-8f32f5edabcc"
    }
}
```

