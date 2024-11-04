**Example 1: 创建企业注销链接**



Input: 

```
tccli essbasic CreateCloseOrganizationUrl --cli-unfold-argument  \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.AppId yDRSRUUgygj6qnwfUuO4zjEwc193c2hH
```

Output: 
```
{
    "Response": {
        "ExpiredOn": 1730257357,
        "LongUrl": "https://res.ess.tencent.cn/cdn/h5-activity-dev/jump-mp.html?to=ENTERPRISE_LOGOUT_LANDING&shortKey=yDCkuUW35EQA3r0aqr88",
        "MiniAppPath": "pages/guide/index?to=ENTERPRISE_LOGOUT_LANDING&shortKey=yDCkuUW35EQA3r0aqr88",
        "QrcodeUrl": "https://dyn.ess.tencent.cn/imgs/qrcode_urls/enterprise_logout_landing/yDCkxUUckp495fo9Ua9wie1hisAGTzhI.png",
        "RequestId": "s1729652557401395967",
        "ShortUrl": "https://essurl.cn/ppiKUBJLt0",
        "WeixinQrcodeUrl": "https://res.ess.tencent.cn/mp-gate/develop/ENTERPRISE_LOGOUT_LANDING?shortKey=yDCkuUW35EQA3r0aqr88"
    }
}
```

