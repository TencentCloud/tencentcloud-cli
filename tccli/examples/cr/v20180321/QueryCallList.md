**Example 1: 机器人任务查询**



Input: 

```
tccli cr QueryCallList --cli-unfold-argument  \
    --BotId xx \
    --Module xx \
    --FileName xx \
    --BizDate 2020-09-22 \
    --Operation xx \
    --BotName xx
```

Output: 
```
{
    "Response": {
        "CallList": [
            {
                "Status": "xx",
                "CallId": "xx",
                "FileType": "xx",
                "FileName": "xx",
                "TotalCount": 0,
                "BizDate": "2020-09-22"
            }
        ],
        "RequestId": "xx"
    }
}
```

