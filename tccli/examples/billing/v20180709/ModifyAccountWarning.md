**Example 1: 云api查余额告警阈值接口示例**



Input: 

```
tccli billing ModifyAccountWarning --cli-unfold-argument  \
    --Threshold 10 \
    --Open 1
```

Output: 
```
{
    "Response": {
        "Threshold": "10",
        "Open": "1",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

