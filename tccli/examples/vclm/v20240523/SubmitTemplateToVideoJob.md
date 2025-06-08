**Example 1: 成功提交**

成功提交任务

Input: 

```
tccli vclm SubmitTemplateToVideoJob --cli-unfold-argument  \
    --Template hug \
    --Images.0.Url https://test.jpg
```

Output: 
```
{
    "Response": {
        "JobId": "1305518294765740032",
        "RequestId": "2392f73f-6436-4f79-85dc-6283d2ca78ef"
    }
}
```

