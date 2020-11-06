**Example 1: 银行卡识别示例代码**



Input: 

```
tccli ocr BankCardOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "CardNo": "6225760088888888",
        "BankInfo": "招商银行(03080000)",
        "ValidDate": "08/2022",
        "RequestId": "46ab2e62-11e3-4d04-9fab-0abe18e7c927"
    }
}
```

