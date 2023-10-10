**Example 1: 编辑反弹Shell规则（支持多服务器选择）**

编辑反弹Shell规则（支持多服务器选择）

Input: 

```
tccli cwp EditReverseShellRules --cli-unfold-argument  \
    --ProcessName test \
    --DestIp 1.2.3.4 \
    --DestPort 8080 \
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

