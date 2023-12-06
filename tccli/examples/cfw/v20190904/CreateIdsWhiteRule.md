**Example 1: 入侵防御规则白名单添加示例**

入侵防御规则白名单添加示例

Input: 

```
tccli cfw CreateIdsWhiteRule --cli-unfold-argument  \
    --SrcIp 10.23.33.1 \
    --DstIp 10.23.33.2 \
    --IdsRuleId 20006 \
    --WhiteRuleType srcdst \
    --FwType 4
```

Output: 
```
{
    "Response": {
        "RequestId": "313be273-4993-450e-ae4b-7a4fd1d8c73f",
        "ReturnCode": 0,
        "ReturnMsg": "success",
        "Status": 0
    }
}
```

