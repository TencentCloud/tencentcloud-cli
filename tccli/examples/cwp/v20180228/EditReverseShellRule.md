**Example 1: 编辑反弹Shell规则**

编辑反弹Shell规则

Input: 

```
tccli cwp EditReverseShellRule --cli-unfold-argument  \
    --Uuid "xx" \
    --ProcessName bash \
    --IsGlobal 1 \
    --Id 1 \
    --DestIp 127.0.0.1 \
    --Hostip 127.0.0.1 \
    --DestPort 123
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

