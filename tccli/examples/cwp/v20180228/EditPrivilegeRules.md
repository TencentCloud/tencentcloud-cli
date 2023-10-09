**Example 1: 新增/修改本地提权规则（支持多服务器选择）**

新增/修改本地提权规则（支持多服务器选择）

Input: 

```
tccli cwp EditPrivilegeRules --cli-unfold-argument  \
    --ProcessName test \
    --SMode 1 \
    --IsGlobal 0 \
    --Uuids 11 12
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

