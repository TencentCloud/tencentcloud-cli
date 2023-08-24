**Example 1: 用于开启自定义密码复杂度功能**



Input: 

```
tccli cynosdb OpenClusterPasswordComplexity --cli-unfold-argument  \
    --ValidatePasswordLength 0 \
    --ValidatePasswordMixedCaseCount 0 \
    --ValidatePasswordDictionary admin \
    --ClusterId cynosdbmysql-abcdxxxx \
    --ValidatePasswordNumberCount 0 \
    --ValidatePasswordSpecialCharCount 0 \
    --ValidatePasswordPolicy MEDIUM
```

Output: 
```
{
    "Response": {
        "RequestId": "128046",
        "FlowId": "123"
    }
}
```

