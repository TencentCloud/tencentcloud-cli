**Example 1: 创建一个发票专用章**

1.设置GenerateSource为SealGenerateSourceSystem
2.设置SealType为发票专用章INVOICE
3.设置SealStyle为椭圆形ellipse
4.设置SealSize为40_30

Input: 

```
tccli ess CreateSeal --cli-unfold-argument  \
    --Operator.UserId user-id-xxxx \
    --GenerateSource SealGenerateSourceSystem \
    --SealType INVOICE \
    --SealName 这是一个发票专用章 \
    --SealHorizontalText  \
    --SealStyle ellipse \
    --SealSize SealSize
```

Output: 
```
{
    "Response": {
        "RequestId": "s170xxxxxxxx1760718",
        "SealId": "yDwfwUUgygorm2w0UuS2eARCYT5rtPIi"
    }
}
```

**Example 2: 通过图片创建电子印章**

1.SealImage传递图片的base64编码, GenerateSource不设置
2. 通过图片创建电子印章，需要电子签人工审核

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
    --SealHorizontalText 印章横向文字 \
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

**Example 3: 通过企业印章横向文字创建椭圆形印章**

通过企业印章横向文字创建椭圆形印章

Input: 

```
tccli ess CreateSeal --cli-unfold-argument  \
    --Operator.UserId user-id-xxxx \
    --GenerateSource SealGenerateSourceSystem \
    --SealType OFFICIAL \
    --SealName 这是一个椭圆形电子印章名称 \
    --SealHorizontalText 测试专业用椭圆印章一号 \
    --SealStyle ellipse
```

Output: 
```
{
    "Response": {
        "SealId": "yDxxx1234556677xxx",
        "RequestId": "s1692775850696494255"
    }
}
```

**Example 4: 通过企业印章横向文字创建企业圆形公章**

通过企业印章横向文字创建企业圆形公章

Input: 

```
tccli ess CreateSeal --cli-unfold-argument  \
    --Operator.UserId user-id-xxxx \
    --GenerateSource SealGenerateSourceSystem \
    --SealType OFFICIAL \
    --SealName 这是一个圆形电子印章名称 \
    --SealHorizontalText 测试专业用章圆形横向一号 \
    --SealStyle circle
```

Output: 
```
{
    "Response": {
        "SealId": "yDxxx12345xxx",
        "RequestId": "s1692775850696494235"
    }
}
```

