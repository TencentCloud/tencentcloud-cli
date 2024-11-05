**Example 1: 新增/修改高危命令规则**

新增/修改高危命令规则，之前的EditBashRule只支持用户输入单个IP去新增或修改高危命令规则，而该接口EditBashRules支持多服务器选择。

Input: 

```
tccli cwp EditBashRules --cli-unfold-argument  \
    --Name yaxte**** \
    --Level 1 \
    --Rule .* \
    --IsGlobal 0 \
    --Uuids 05f0bcab-726c-4ea4-8109-bcd03d5598f7
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

