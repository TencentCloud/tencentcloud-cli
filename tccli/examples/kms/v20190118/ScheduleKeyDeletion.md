**Example 1: 计划删除接口请求示例**

指定CMK于累计7天后被删除

Input: 

```
tccli kms ScheduleKeyDeletion --cli-unfold-argument  \
    --PendingWindowInDays 7 \
    --KeyId "23e80852-1e38-11e9-b129-5cb9019b4b01"
```

Output: 
```
{
    "Response": {
        "RequestId": "8e8f23a7-50b2-4c8e-bd23-0a98cb643f88",
        "DeletionDate": 1559318399,
        "KeyId": "23e80852-1e38-11e9-b129-5cb9019b4b01"
    }
}
```

