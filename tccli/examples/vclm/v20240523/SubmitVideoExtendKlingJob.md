**Example 1: 调用成功示例**



Input: 

```
tccli vclm SubmitVideoExtendKlingJob --cli-unfold-argument  \
    --VideoId 8663489104******** \
    --Prompt 小狗跳舞 \
    --CfgScale 0.5 \
    --CallbackUrl http://*************:808* \
    --LogoAdd 0
```

Output: 
```
{
    "Response": {
        "JobId": "1428951145945636864",
        "RequestId": "b0f2021a-e647-4a6c-bc08-f1013ae9281f"
    }
}
```

