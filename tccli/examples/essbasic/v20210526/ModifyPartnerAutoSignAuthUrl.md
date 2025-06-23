**Example 1: 修改授权**



Input: 

```
tccli essbasic ModifyPartnerAutoSignAuthUrl --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --AuthorizedOrganizationName 张三示例企业
```

Output: 
```
{
    "Response": {
        "ExpireTime": 1747966900,
        "MiniAppPath": "/pages/guide/index?shortKey=yDttjUsO8wXIPLi8dM02",
        "RequestId": "s1747362100925380930",
        "Url": "https://test.essurl.cn/lrtXUBLTtI"
    }
}
```

