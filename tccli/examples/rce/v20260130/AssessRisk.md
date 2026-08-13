**Example 1: 登录事件示例**



Input: 

```
tccli rce AssessRisk --cli-unfold-argument  \
    --EventCode login \
    --EventTime 2026-07-08T15:56:31.000+08:00 \
    --SessionId se****************56 \
    --DeviceToken v3:******************************************************************bzxeC9FTtHon0Vq+zEB0iKhM5OGvG \
    --UserIp 192.***.*.100 \
    --EventDetail.Login.UserInfo.UserLevel golden \
    --EventDetail.Login.UserInfo.UserPoint.Point 10 \
    --EventDetail.Login.UserInfo.UserPoint.PointType credit_point \
    --EventDetail.Login.UserInfo.UserType person \
    --EventDetail.Login.UserLoginName u_dscv \
    --EventDetail.Login.LoginResult.Status success \
    --EventDetail.Login.Cust.0.Key registration_channel \
    --EventDetail.Login.Cust.0.Value web \
    --UserId u********6 \
    --UserEmail u***********.com \
    --UserPhone +86138******** \
    --Browser.UserAgent Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 \
    --Browser.AcceptLanguage zh-CN,zh;q=0.9,en;q=0.8 \
    --Browser.ContentLanguage zh-CN \
    --App.OS iOS \
    --App.OSVersion 16.0 \
    --App.DeviceManufacturer Apple \
    --App.DeviceModel iPhone 14 Pro \
    --App.DeviceId de**************3 \
    --App.AppName MyShoppingApp \
    --App.AppVersion 3.2.1 \
    --App.ClientLanguage zh-CN \
    --DataAuthorization.DataProviderName **公司 \
    --DataAuthorization.DataRecipientName 腾讯云计算（北京）有限责任公司 \
    --DataAuthorization.UserDataType 1 \
    --DataAuthorization.IsAuthorized True \
    --DataAuthorization.IsOrderHanding True \
    --UserPhoneEncrypt plain \
    --WeChatOpenId ob************************8E \
    --QQOpenId c*****w \
    --QQAppId 10****4
```

Output: 
```
{
    "Response": {
        "Data": {
            "Decision": {
                "DecisionResult": "reject"
            },
            "ExtraInfo": [
                {
                    "Key": "DeviceId",
                    "Value": "weffdsdffdff"
                }
            ],
            "Score": {
                "RiskLabels": [],
                "RiskScore": 20
            }
        },
        "RequestId": "65af642d-f2df-4e03-b93d-8c7820f4deda"
    }
}
```

