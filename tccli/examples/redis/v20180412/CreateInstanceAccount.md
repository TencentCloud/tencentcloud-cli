**Example 1: 请求示例**



Input: 

```
tccli redis CreateInstanceAccount --cli-unfold-argument  \
    --InstanceId crs-5a4py64p \
    --AccountName test \
    --AccountPassword 1234567a \
    --ReadonlyPolicy master \
    --Privilege rw
```

Output: 
```
{
    "Response": {
        "TaskId": 123456,
        "RequestId": "0e728fa9-c2e5-4bf8-8d6b-c1c4fab7b6db"
    }
}
```

