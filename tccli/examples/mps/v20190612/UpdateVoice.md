**Example 1: 更新音色信息示例**



Input: 

```
tccli mps UpdateVoice --cli-unfold-argument  \
    --VoiceId v1_bXtKSKkmijRkVuzHpVQMkZ/356N9EYGT6/o0liHuqhTc3l2C93vGsTgoqRZNy9MaTAs= \
    --VoiceFields.Age youth \
    --VoiceFields.Languages zh
```

Output: 
```
{
    "Response": {
        "ErrorCode": 0,
        "Msg": "success",
        "Voice": {
            "Age": "youth",
            "Category": "clone",
            "Description": "This is an updated voice description",
            "Gender": "female",
            "Languages": [
                "zh"
            ],
            "Name": "update-test",
            "VoiceId": "v1_bXtKSKkmijRkVuzHpVQMkZ/356N9EYGT6/o0liHuqhTc3l2C93vGsTgoqRZNy9MaTAs="
        },
        "RequestId": "e8af7402-5b5a-4e32-bb72-55886391d270"
    }
}
```

