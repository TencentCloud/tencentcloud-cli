**Example 1: 成功查询用户回调地址**



Input: 

```
tccli ivld QueryCallback --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "705f6aed-f46b-4f43-aeef-31167885d938",
        "TaskFinishNotifyURL": "http://example.com/api/task/callback",
        "MediaFinishNotifyURL": "http://example.com/api/media/callback"
    }
}
```

