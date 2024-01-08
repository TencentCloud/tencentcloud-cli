**Example 1: 入侵防御规则白名单查询示例**

入侵防御规则白名单查询示例

Input: 

```
tccli cfw DescribeIdsWhiteRule --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "DstIp": "10.23.33.2",
                "FwType": 4,
                "Id": 63,
                "RuleId": "20006",
                "SrcIp": "10.23.33.1",
                "WhiteRuleType": "srcdst"
            }
        ],
        "RequestId": "88db276f-42d5-4b60-afc1-2c5799250a99",
        "ReturnCode": 0,
        "ReturnMsg": "success",
        "Total": 1
    }
}
```

