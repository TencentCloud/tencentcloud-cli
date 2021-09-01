**Example 1: 切换高危命令规则状态**



Input: 

```
tccli cwp SwitchBashRules --cli-unfold-argument  \
    --Id 100 \
    --Disabled 0
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

