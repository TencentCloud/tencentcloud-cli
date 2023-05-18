**Example 1: 文本续写调用示例**

对中文文本进行续写。

Input: 

```
tccli nlp TextWriting --cli-unfold-argument  \
    --Text 今天天气不错 \
    --SourceLang zh \
    --Number 2 \
    --Domain general \
    --Style xuanhuan_wuxia
```

Output: 
```
{
    "Response": {
        "RequestId": "40abc589-8603-458b-82a7-fe174e799085",
        "WritingList": [
            {
                "PrefixText": "此事还得从这说起，",
                "TargetText": "此事还得从这说起，他一路行来，不知不觉已到了洛阳城，这一日，他来到一处客栈，打听一下萧月生的消息。“师父，他来了！”江南云忽然开口，声音清脆悦耳，仿"
            },
            {
                "PrefixText": "此事还得从这说起，",
                "TargetText": "此事还得从这说起，那日在山东大会上，萧月生一眼看出，这个赵小四是武林中人，心中不由一动，觉得此人极有可能是华山派的弟子。“师父，他的轻功如何？”江南"
            }
        ]
    }
}
```

