**Example 1: 关闭GME应用140000001**



Input: 

```
tccli gme ModifyAppStatus --cli-unfold-argument  \
    --BizId 140000001 \
    --Status close
```

Output: 
```
{
    "Response": {
        "Data": {
            "BizId": 140000001,
            "Status": "close"
        },
        "RequestId": "e2900289-f21e-43a8-a3bf-0b439cdbbbb8"
    }
}
```

