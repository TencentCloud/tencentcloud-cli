**Example 1: 创建匹配示例**



Input: 

```
tccli gpm CreateRule --cli-unfold-argument  \
    --RuleName test \
    --RuleDesc test \
    --RuleScript test \
    --Tags.0.Key 字符串 \
    --Tags.0.Value 字符串
```

Output: 
```
{
    "Response": {
        "RequestId": "d49cff57-ac1e-437e-a89e-5372fd6538ed",
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

