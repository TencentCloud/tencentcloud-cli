**Example 1: 删除自定义送检用户**

删除自定义送检用户

Input: 

```
tccli gme DeleteScanUser --cli-unfold-argument  \
    --UserId 123 \
    --BizId 1400000000
```

Output: 
```
{
    "Response": {
        "ErrorCode": 0,
        "RequestId": "ec975acd-0b19-4e97-90e2-a9ff7b9c26aa"
    }
}
```

