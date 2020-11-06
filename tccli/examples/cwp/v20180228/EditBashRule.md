**Example 1: 新增/修改高危命令规则**

新增/修改高危命令规则

Input: 

```
tccli cwp EditBashRule --cli-unfold-argument  \
    --Name 规则名 \
    --Level 1 \
    --Rule .*
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

