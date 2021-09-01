**Example 1: 查询规则示例**



Input: 

```
tccli gpm DescribeRule --cli-unfold-argument  \
    --RuleCode rule-r4x6tk49
```

Output: 
```
{
    "Response": {
        "RequestId": "16a99485-c55a-4202-9302-dc329e710d00",
        "RuleInfo": {
            "AppId": "1300704415",
            "CreateTime": "2020-09-29 10:52:48",
            "CreateUin": "100012125188",
            "MatchCodeList": [
                {
                    "Key": "match-74w0ckl8",
                    "Value": "test"
                }
            ],
            "Region": "ap-shanghai",
            "RuleCode": "rule-r4x6tk49",
            "RuleDesc": "test",
            "RuleName": "test",
            "RuleScript": "1",
            "Tags": [],
            "Uin": "100012125188"
        }
    }
}
```

