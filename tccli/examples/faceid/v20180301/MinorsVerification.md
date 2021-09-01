**Example 1: 使用手机号进行检查**



Input: 

```
tccli faceid MinorsVerification --cli-unfold-argument  \
    --Type 0 \
    --Mobile 13800138000
```

Output: 
```
{
    "Response": {
        "Result": "-1",
        "Description": "未成年",
        "AgeRange": "[0,8)",
        "RequestId": "c163d210-ed9e-44d0-a4c4-d6bbc1bf6f27"
    }
}
```

**Example 2: 使用姓名身份证号进行检查**



Input: 

```
tccli faceid MinorsVerification --cli-unfold-argument  \
    --Type 1 \
    --IdCard 440111199110100000 \
    --Name 张成年
```

Output: 
```
{
    "Response": {
        "Result": "0",
        "Description": "成年",
        "AgeRange": "[18,+)",
        "RequestId": "7f03975b-957d-47e5-a346-02d7c4b330c6"
    }
}
```

