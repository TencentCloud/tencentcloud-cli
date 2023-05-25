**Example 1: 用于修改/开启集群密码复杂度**



Input: 

```
tccli cynosdb ModifyClusterPasswordComplexity --cli-unfold-argument  \
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

