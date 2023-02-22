**Example 1: 企业四要素核验示例代码（输入关键字段进行核验）**

企业四要素核验示例代码（输入关键字段进行核验）

Input: 

```
tccli ocr VerifyEnterpriseFourFactors --cli-unfold-argument  \
    --IdCard 610110190001010812 \
    --EnterpriseName 大饼网络工作室 \
    --RealName 李大饼 \
    --EnterpriseMark 92770729JK3A9WAU7J
```

Output: 
```
{
    "Response": {
        "Detail": {
            "Desc": "企业法人/负责人",
            "Result": 7
        },
        "RequestId": "9406f64f-b57d-4d53-b58a-f65e5f1f90f0",
        "State": 1
    }
}
```

