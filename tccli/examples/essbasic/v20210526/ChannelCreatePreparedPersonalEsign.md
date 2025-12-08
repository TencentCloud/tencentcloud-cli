**Example 1: 通过准备好的个人印章图片创建印章**

通过准备好的个人印章图片创建印章

Input: 

```
tccli essbasic ChannelCreatePreparedPersonalEsign --cli-unfold-argument  \
    --Operator.OpenId UxSq3Yhw6lLHwsZd9RZTCOz69ewqFzXChxs3bMD \
    --Agent.AppId yDwJBUUckpkl05jrUuxCKSQvQxffCN28 \
    --Agent.ProxyOrganizationOpenId org_dianzqin \
    --UserName 印章归属个人姓名 \
    --IdCardType  \
    --IdCardNumber 身份证件号码 \
    --SealImage 印章图片Base64 \
    --SealName 我的印章名称 \
    --Mobile 135*111 \
    --EnableAutoSign True
```

Output: 
```
{
    "Response": {
        "SealId": "yDCYIUUckp7t75mxUxAAGY1B8z3p0AIA",
        "RequestId": "6e3eb9ef-61f9-4884-9874-465eaffc3d64"
    }
}
```

**Example 2: 通过已上传的印章FileId创建印章**

通过已上传的印章FileId创建印章

Input: 

```
tccli essbasic ChannelCreatePreparedPersonalEsign --cli-unfold-argument  \
    --Operator.OpenId UxSq3Yhw6lLHwsZd9RZTCOz69ewqFzXChxs3bMD \
    --Agent.AppId yDwJBUUckpkl05jrUuxCKSQvQxffCN28 \
    --Agent.ProxyOrganizationOpenId org_dianzqin \
    --UserName 印章归属个人姓名 \
    --IdCardType  \
    --IdCardNumber 身份证件号码 \
    --SealImage 印章图片Base64 \
    --SealName 我的印章名称 \
    --Mobile 135*111 \
    --FileId yDwJB******************ddskaSIs \
    --EnableAutoSign True
```

Output: 
```
{
    "Response": {
        "SealId": "yDtOJUUckpftturtURxNEFKShAukAd2b",
        "RequestId": "39f18b2b-03fe-40b8-8d16-dbf4ead3685f"
    }
}
```

