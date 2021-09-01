**Example 1: 新增词条接口示例**



Input: 

```
tccli nlp CreateWordItems --cli-unfold-argument  \
    --DictId udf-066edc3449 \
    --WordItems.0.Text 理想的目标是不再继续下跌了 \
    --WordItems.0.Pos nr
```

Output: 
```
{
    "Response": {
        "RequestId": "fb716d37-6669-405b-93ff-f4187f95576f"
    }
}
```

