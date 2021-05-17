**Example 1: 企业四要素核验示例代码（输入关键字段进行核验）**



Input: 

```
tccli ocr VerifyEnterpriseFourFactors --cli-unfold-argument  \
    --RealName xxxxx \
    --IdCard xxxxx \
    --EnterpriseName xxxxx \
    --EnterpriseMark xxxxx
```

Output: 
```
{
    "Response": {
        "State": 2,
        "Detail": {
            "Result": -22,
            "Desc": "姓名不一致"
        },
        "RequestId": "8d9627c4-eb52-4a8d-8565-5b07ad436c9f"
    }
}
```

