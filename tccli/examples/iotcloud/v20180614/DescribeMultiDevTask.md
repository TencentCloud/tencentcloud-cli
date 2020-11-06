**Example 1: 获取创建多设备任务状态**



Input: 

```
tccli iotcloud DescribeMultiDevTask --cli-unfold-argument  \
    --ProductId ABCDE12345 \
    --TaskId abcdefghijklmn
```

Output: 
```
{
    "Response": {
        "TaskId": "abcdefghijklmn",
        "TaskStatus": 1,
        "RequestId": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    }
}
```

