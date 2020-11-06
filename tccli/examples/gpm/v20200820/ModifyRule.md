**Example 1: 修改规则示例**



Input: 

```
tccli gpm ModifyRule --cli-unfold-argument  \
    --RuleDesc test \
    --RuleCode rule-v879tr24 \
    --RuleName test \
    --Tags.0.Key 字符串 \
    --Tags.0.Value 字符串
```

Output: 
```
{
    "Response": {
        "RequestId": "c34a20b9-0fba-4c37-8819-c25a271778f6",
        "RuleInfo": {
            "AppId": "1300704415",
            "CreateTime": "2020-09-29 15:15:36",
            "CreateUin": "100012125188",
            "MatchCodeList": [],
            "Region": "ap-shanghai",
            "RuleCode": "rule-v879tr24",
            "RuleDesc": "test",
            "RuleName": "test",
            "RuleScript": "test",
            "Tags": [
                {
                    "Key": "字符串",
                    "Value": "字符串"
                }
            ],
            "Uin": "100012125188"
        }
    }
}
```

