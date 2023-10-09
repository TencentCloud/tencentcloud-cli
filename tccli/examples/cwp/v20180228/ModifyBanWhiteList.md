**Example 1: 修改阻断白名单列表**



Input: 

```
tccli cwp ModifyBanWhiteList --cli-unfold-argument  \
    --Rules.Id 1 \
    --Rules.Remark test123
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

