**Example 1: 接口请求示例**



Input: 

```
tccli zj GetSmsSignList --cli-unfold-argument  \
    --Status 0 \
    --Offset 0 \
    --Limit 1 \
    --License xsdf
```

Output: 
```
{
    "Response": {
        "Data": {
            "Total": 1,
            "List": [
                {
                    "SignId": 150465,
                    "International": 0,
                    "SignName": "腾讯云智慧零售",
                    "StatusCode": 0,
                    "ReviewReply": "",
                    "CreateTime": 1000
                }
            ]
        },
        "RequestId": "111111"
    }
}
```

