**Example 1: 计划删除接口请求示例**

指定CMK于累计7天后被删除

Input: 

```
tccli kms ScheduleKeyDeletion --cli-unfold-argument  \
    --KeyId "23e80852-1e38-11e9-b129-5cb9019b4b01" \
    --PendingWindowInDays 7
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "DeletionDate": 1559318399,
        "KeyId": "23e80852-1e38-11e9-b129-5cb9019b4b01"
    }
}
```

