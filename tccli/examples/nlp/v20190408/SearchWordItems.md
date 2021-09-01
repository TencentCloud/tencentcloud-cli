**Example 1: 检索词条接口示例**



Input: 

```
tccli nlp SearchWordItems --cli-unfold-argument  \
    --DictId udf-066edc3449 \
    --WordItems.0.Text 理想型 \
    --WordItems.0.Pos nr
```

Output: 
```
{
    "Response": {
        "RequestId": "fb716d37-6669-405b-93ff-f4187f95576f",
        "Results": [
            {
                "IsExist": 1,
                "Pos": "",
                "MatchText": "理想型",
                "Text": "理想型"
            }
        ]
    }
}
```

