**Example 1: 使用照片URL进行核验示例**



Input: 

```
tccli faceid IdCardOCRVerification --cli-unfold-argument  \
    --ImageUrl https://www.qq.com/image.jpg
```

Output: 
```
{
    "Response": {
        "Result": "0",
        "Description": "姓名和身份证号一致",
        "Name": "韦小宝",
        "IdCard": "11204416541220243X",
        "Sex": "男",
        "Nation": "汉",
        "Birth": "1654/12/20",
        "Address": "北京市东城区景山前街4号紫禁城敬事房",
        "RequestId": "a62f567c-1eea-4ef3-b51a-a9eb9bd84cd9"
    }
}
```

**Example 2: 使用照片Base64进行核验示例**



Input: 

```
tccli faceid IdCardOCRVerification --cli-unfold-argument  \
    --ImageBase64 /9j/4AAQSkZJRg.....s97n//2Q==
```

Output: 
```
{
    "Response": {
        "Result": "0",
        "Description": "姓名和身份证号一致",
        "Name": "韦小宝",
        "IdCard": "11204416541220243X",
        "Sex": "男",
        "Nation": "汉",
        "Birth": "1654/12/20",
        "Address": "北京市东城区景山前街4号紫禁城敬事房",
        "RequestId": "022ffdd2-67a2-4177-8946-97bc1c4b3347"
    }
}
```

**Example 3: 使用姓名身份证号进行验证示例**



Input: 

```
tccli faceid IdCardOCRVerification --cli-unfold-argument  \
    --IdCard 11204416541220243X \
    --Name 韦小宝
```

Output: 
```
{
    "Response": {
        "Result": "0",
        "Description": "姓名和身份证号一致",
        "Name": "韦小宝",
        "IdCard": "11204416541220243X",
        "Sex": "",
        "Nation": "",
        "Birth": "",
        "Address": "",
        "RequestId": "945c69ad-d86c-47ea-ba33-419b1dc4d242"
    }
}
```

**Example 4: 身份证识别及信息核验失败示例**



Input: 

```
tccli faceid IdCardOCRVerification --cli-unfold-argument  \
    --IdCard 11204416541220243Y \
    --Name 韦小宝
```

Output: 
```
{
    "Response": {
        "Address": "",
        "Birth": "",
        "Description": "非法身份证号（长度、校验位等不正确）",
        "IdCard": "11204416541220243Y",
        "Name": "韦小宝",
        "Nation": "",
        "RequestId": "c528602c-6574-4dd7-a836-895ff62a13ed",
        "Result": "-2",
        "Sex": ""
    }
}
```

