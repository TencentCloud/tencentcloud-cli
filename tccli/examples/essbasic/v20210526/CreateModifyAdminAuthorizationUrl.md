**Example 1: 重新上传超管授权书**

平台审核因为照片不清晰原因，拒绝了超管授权书，
此时用户重新上传超管授权书。
生成的链接是小程序链接

Input: 

```
tccli essbasic CreateModifyAdminAuthorizationUrl --cli-unfold-argument  \
    --Agent.ProxyOperator.OpenId dianziqian \
    --Agent.ProxyOrganizationOpenId dianziqian_org \
    --Agent.AppId yDwFoUUckpsomwx1UyhWGhIR2RkhOjw2 \
    --AuthorizationId yDt3sUUckpxzou8bUuFrZIdxeP9YoXeP \
    --Endpoint HTTP
```

Output: 
```
{
    "Response": {
        "RequestId": "1245a2a3537e",
        "Url": "https://res.ess.tencent.cn/cdn/h5-activity-dev/jump-mp.html?to=REGISTER_ENTERPRISE_FOR_UPDATE_AUTH_FILE&AuthorizationId=yDt3sUUckpxzou8bUuFrZIdxeP9YoXeP"
    }
}
```

