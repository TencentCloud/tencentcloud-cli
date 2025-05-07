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
            "Message": "TXT解析记录验证不匹配"
        },
        "RequestId": "26cbf416-0155-411f-93df-7256930245a4"
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

