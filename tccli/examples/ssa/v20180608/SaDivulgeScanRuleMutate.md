**Example 1: 设置规则**

设置规则调用

Input: 

```
tccli ssa SaDivulgeScanRuleMutate --cli-unfold-argument  \
    --Id 1324 \
    --DivulgeSoure github \
    --DivulgeSoureUrl https://url \
    --RuleName 规则577 \
    --RuleWord 规则关键字 \
    --ScanStatus 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Value": "参数",
            "Code": 1,
            "Message": "信息"
        },
        "RequestId": "167a9a4b-a8a6-4a84-a115-23fddfc327b0"
    }
}
```

