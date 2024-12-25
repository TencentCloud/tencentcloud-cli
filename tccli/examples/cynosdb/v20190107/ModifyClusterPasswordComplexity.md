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
        "RequestId": "51169b54-61d4-4604-a07e-e519a5527923",
        "FlowId": "147283"
    }
}
```

