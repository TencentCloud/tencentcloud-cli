**Example 1: 文本内容检测**



Input: 

```
tccli cms TextModeration --cli-unfold-argument  \
    --Content 57uY5aOw57uY6Imy
```

Output: 
```
{
    "Response": {
        "BusinessCode": 0,
        "Data": {
            "EvilType": 20001,
            "EvilFlag": 1,
            "BizType": 2,
            "Score": 72,
            "EvilLabel": "Polity",
            "Suggestion": "Review",
            "Keywords": [
                "傻子"
            ],
            "DetailResult": [
                {
                    "EvilType": 20001,
                    "KeywordsList": [
                        "傻子"
                    ],
                    "Prediction": 72
                }
            ]
        },
        "RequestId": "jlUM5m23JWDeAX1tQirYT9cP"
    },
    "retmsg": "success",
    "retcode": 0
}
```

