**Example 1: 创建只读账号**



Input: 

```
tccli keewidb CreateInstanceAccount --cli-unfold-argument  \
    --InstanceId kee-p04nodnb \
    --AccountName test-read-only \
    --AccountPassword Test123456 \
    --ReadonlyPolicy master \
    --Privilege r \
    --Remark 测试只读
```

Output: 
```
{
    "Response": {
        "TaskId": 4294994438,
        "RequestId": "7fa233af-6482-458a-b6cf-a0523b6ff5d4"
    }
}
```

