**Example 1: 使用姓名身份证号进行验证**



Input: 

```
tccli faceid IdCardOCRVerification --cli-unfold-argument  \
    --IdCard 360*************50 \
    --Name **杰
```

Output: 
```
{
    "Response": {
        "Result": "0",
        "Description": "姓名和身份证号一致",
        "Name": "**杰",
        "IdCard": "360*************50",
        "Sex": "",
        "Nation": "",
        "Birth": "",
        "Address": "",
        "RequestId": "945c69ad-d86c-47ea-ba33-419b1dc4d242"
    }
}
```

**Example 2: 使用照片URL进行核验**



Input: 

```
tccli faceid IdCardOCRVerification --cli-unfold-argument  \
    --ImageUrl https://qq.com/a.jpg
```

Output: 
```
{
    "Response": {
        "Result": "0",
        "Description": "姓名和身份证号一致",
        "Name": "**杰",
        "IdCard": "360*************50",
        "Sex": "男",
        "Nation": "汉",
        "Birth": "1986/11/13",
        "Address": "江西省九江市庐山河南路57号01室",
        "RequestId": "a62f567c-1eea-4ef3-b51a-a9eb9bd84cd9"
    }
}
```

**Example 3: 使用照片Base64进行核验**



Input: 

```
tccli faceid IdCardOCRVerification --cli-unfold-argument  \
    --ImageBase64 <base64字符串>
```

Output: 
```
{
    "Response": {
        "Result": "0",
        "Description": "姓名和身份证号一致",
        "Name": "**杰",
        "IdCard": "360*************50",
        "Sex": "男",
        "Nation": "汉",
        "Birth": "1986/11/13",
        "Address": "江西省九江市庐山河南路57号01室",
        "RequestId": "022ffdd2-67a2-4177-8946-97bc1c4b3347"
    }
}
```

