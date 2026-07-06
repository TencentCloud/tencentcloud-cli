**Example 1: 生成员工手机号变更链接-不指定手机号**



Input: 

```
tccli essbasic CreateEmployeeChangeUrl --cli-unfold-argument  \
    --Agent.AppId yDwFoUUckpsomwx1UyhWGhIR2RkhOjw2 \
    --Agent.ProxyOperator.OpenId kevinlcheng_1 \
    --OpenId kevinlcheng_1 \
    --NewMobile 182****2320
```

Output: 
```
{
    "Response": {
        "ExpireTime": 1741332331,
        "MiniAppPath": "/pages/guide/index?shortKey=yDtSJUde8JFIMAykHz79",
        "RequestId": "s1740727531055190955",
        "LongUrl": "https://res.ess.tencent.cn/cdn/h5-activity********p-mp.html?to=CHANGE_MOBILE&shortKey=yD******************",
        "ShortUrl": "https://test.essurl.cn/z2Wz******"
    }
}
```

**Example 2: 生成员工手机号变更链接-指定手机号**



Input: 

```
tccli essbasic CreateEmployeeChangeUrl --cli-unfold-argument  \
    --Agent.AppId yDwFoUUckpsomwx1UyhWGhIR2RkhOjw2 \
    --Agent.ProxyOperator.OpenId kevinlcheng_1 \
    --OpenId kevinlcheng_1 \
    --NewMobile +12 12345721
```

Output: 
```
{
    "Response": {
        "ExpireTime": 1741332331,
        "MiniAppPath": "/pages/guide/index?shortKey=yDtSJUde8JFIMAykH***",
        "LongUrl": "https://res.ess.tencent.cn/cdn/h5-activity********p-mp.html?to=CHANGE_MOBILE&shortKey=yD******************",
        "ShortUrl": "https://test.essurl.cn/z2Wz******",
        "RequestId": "s1740727531055190955"
    }
}
```

