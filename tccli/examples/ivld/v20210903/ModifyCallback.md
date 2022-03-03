**Example 1: 成功设置回调地址**



Input: 

```
tccli ivld ModifyCallback --cli-unfold-argument  \
    --TaskFinishNotifyURL https://callback.com \
    --MediaFinishNotifyURL https://callback.com
```

Output: 
```
{
    "Response": {
        "RequestId": "705f6aed-f46b-4f43-aeef-31167885d938"
    }
}
```

