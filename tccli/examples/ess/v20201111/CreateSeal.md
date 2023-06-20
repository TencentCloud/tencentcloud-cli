**Example 1: 创建电子印章**

创建电子印章

Input: 

```
tccli ess CreateSeal --cli-unfold-argument  \
    --Operator.UserId 11234567890123456789012345678901 \
    --SealName 公司印章 \
    --Image imagecontentbase64 \
    --Width 10 \
    --Height 20 \
    --Color Red \
    --SealType OFFICIAL \
    --SealHorizontalText 横向文字 \
    --SealChordText 下弦文字 \
    --SealCentralType Star \
    --FileName 印章图片.png
```

Output: 
```
{
    "Response": {
        "SealId": "429b82b4xxxx0a90d45c715bad7",
        "RequestId": "62DDFFC6xxxxxA6-59152E3D129A"
    }
}
```

