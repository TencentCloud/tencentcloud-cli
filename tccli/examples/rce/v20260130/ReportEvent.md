**Example 1: 登录事件信息上报示例**



Input: 

```
tccli rce ReportEvent --cli-unfold-argument  \
    --EventCode login \
    --EventTime 2026-07-07T15:16:31.000+08:00 \
    --SessionId se****************56 \
    --DeviceToken v3:**********************************************************************************************bzxeC9FTtHon0Vq+zEB0iKhM5OGvG \
    --UserIp 192.***.*.100 \
    --EventDetail.Login.UserInfo.UserLevel golden \
    --EventDetail.Login.UserInfo.UserPoint.Point 10 \
    --EventDetail.Login.UserInfo.UserPoint.PointType credit_point \
    --EventDetail.Login.UserInfo.UserType person \
    --EventDetail.Login.UserLoginName u_cuidq \
    --EventDetail.Login.LoginResult.Status success \
    --UserId u*******56 \
    --UserEmail u***********.com \
    --UserPhone +86138******** \
    --Browser.UserAgent Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 \
    --Browser.AcceptLanguage zh-CN,zh;q=0.9,en;q=0.8 \
    --Browser.ContentLanguage zh-CN \
    --App.OS iOS \
    --App.OSVersion 16.0 \
    --App.DeviceManufacturer Apple \
    --App.DeviceModel iPhone 14 Pro \
    --App.DeviceId de*************23 \
    --App.AppName MyShoppingApp \
    --App.AppVersion 3.2.1 \
    --App.ClientLanguage zh-CN \
    --DataAuthorization.DataProviderName **公司 \
    --DataAuthorization.DataRecipientName 腾讯云计算（北京）有限责任公司 \
    --DataAuthorization.UserDataType 1 \
    --DataAuthorization.IsAuthorized True \
    --DataAuthorization.IsOrderHanding True \
    --DataAuthorization.AuthorizationDeadline 1793070635 \
    --DataAuthorization.PrivacyPolicyLink http://*******.com \
    --UserPhoneEncrypt plain \
    --WeChatOpenId ob************************8E \
    --QQOpenId cs****w \
    --QQAppId 1****74
```

Output: 
```
{
    "Response": {
        "RequestId": "374aefc2-99e7-40a1-b92c-9e08a3f3b742"
    }
}
```

