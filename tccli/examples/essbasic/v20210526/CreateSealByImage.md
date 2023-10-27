**Example 1: 系统生成印章**

GenerateSource为SealGenerateSourceSystem表示系统生成印章

Input: 

```
tccli essbasic CreateSealByImage --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId  \
    --SealName 合同专用章 \
    --GenerateSource SealGenerateSourceSystem \
    --SealType FINANCE \
    --SealHorizontalText 印章横向文字在这里
```

Output: 
```
{
    "Response": {
        "SealId": "yDwi8UUckpo5z4omUyleFeZeadKwB=1Hm",
        "ImageUrl": "https://file.test.ess.tencent.cn/bresource/resource/resource/0/0.PNG?hkey=a6c****66264",
        "RequestId": "477f4d46-062c-4d72-a2e0-94e5b52b0cc5"
    }
}
```

**Example 2: 通过图片创建电子印章**

1.SealImage传递图片的base64编码, GenerateSource不设置
2. 通过图片创建电子印章，需要电子签人工审核

Input: 

```
tccli essbasic CreateSealByImage --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId  \
    --SealName 人事专用章 \
    --SealImage iVBORw0KGgoAAAANSUhEUgAAAGwAAABuCAYAAADCrvbGAAABW2lDZXE15yz3uZ6TErkJggg....(图片base64省略) \
    --SealType PERSONNEL
```

Output: 
```
{
    "Response": {
        "SealId": "yDwi8UUckpo5z4k1UyleFeZEcAE49vb6",
        "ImageUrl": "",
        "RequestId": "62378bbc-2384-499c-89f6-7835040b24a1"
    }
}
```

