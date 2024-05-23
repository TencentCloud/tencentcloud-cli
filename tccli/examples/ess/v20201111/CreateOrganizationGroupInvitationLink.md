**Example 1: 生成建工集团集团加入邀请链接**

生成建工集团集团加入邀请链接

Input: 

```
tccli ess CreateOrganizationGroupInvitationLink --cli-unfold-argument  \
    --Operator.UserId yDR4yUUgyg1qh6szUxt1qOK1Jy90khKS \
    --Operator.ClientIp 8.8.8.8 \
    --ExpireTime 1702366386
```

Output: 
```
{
    "Response": {
        "ExpireTime": 1716683735,
        "JumpUrl": "https://test.essurl.cn/BGgGUBGtln",
        "Link": "https://dyn.test.ess.tencent.cn/imgs/organization/732aaefa78c439d726f541b89c49e022/qrcode/joingroup/yDCZFUUckpyyo8pgUxP8QQ8yRgWF3en4.png",
        "MiniAppPath": "/pages/guide/index?shortKey=yDCZFUyOc8a3FdjP9477",
        "RequestId": "acba9fe30ab0"
    }
}
```

