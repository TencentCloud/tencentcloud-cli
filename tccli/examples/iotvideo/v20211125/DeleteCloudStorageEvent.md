**Example 1: 删除云存某一事件**



Input: 

```
tccli iotvideo DeleteCloudStorageEvent --cli-unfold-argument  \
    --ProductId abc \
    --DeviceName abc \
    --EventId abc \
    --StartTime 1 \
    --EndTime 1 \
    --UserId abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

