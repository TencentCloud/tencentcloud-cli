**Example 1: 验证解析记录**

异常返回

Input: 

```
tccli cdn VerifyDomainRecord --cli-unfold-argument  \
    --Domain www.qq.com
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "UnauthorizedOperation.CdnTxtRecordValueNotMatch",
            "Message": "cdn txt record value not match(txt record value not match)"
        },
        "RequestId": "2424"
    }
}
```

**Example 2: 验证解析记录-2**

正常回包

Input: 

```
tccli cdn VerifyDomainRecord --cli-unfold-argument  \
    --Domain www.qq.com
```

Output: 
```
{
    "Response": {
        "RequestId": "b6926bb2-d0b5-42bc-b17f-e4402bdb9e9b",
        "Result": true
    }
}
```

