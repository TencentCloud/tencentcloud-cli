**Example 1: 校验问答**



Input: 

```
tccli lke VerifyQA --cli-unfold-argument  \
    --LoginUin 600000562455 \
    --LoginSubAccountUin 600000562455 \
    --List.0.QaBizId 161707 \
    --List.0.IsAccepted True \
    --List.0.CateBizId  \
    --List.0.Question  \
    --List.0.Answer  \
    --BotBizId 1696822786072117248
```

Output: 
```
{
    "Response": {
        "RequestId": "9ea25595-b37f-4612-b82b-96616bd75c82"
    }
}
```

