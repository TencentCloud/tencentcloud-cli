**Example 1: 请求demo**



Input: 

```
tccli wedata StopAdhocTask --cli-unfold-argument  \
    --RecordId 111 \
    --InstanceId 222
```

Output: 
```
{
    "Response": {
        "RequestId": "123",
        "Result": "true"
    }
}
```

**Example 2: 终止失败示例**



Input: 

```
tccli wedata StopAdhocTask --cli-unfold-argument  \
    --RecordId 111 \
    --InstanceId 20220218143949840_2022-03-07T14:42:59+08:00
```

Output: 
```
{
    "Response": {
        "RequestId": "b43f2307-0b80-410c-9afd-572263ef18a1",
        "Result": "stop task failed"
    }
}
```

**Example 3: 失败示例**



Input: 

```
tccli wedata StopAdhocTask --cli-unfold-argument  \
    --RecordId 1111 \
    --InstanceId 字符串
```

Output: 
```
{
    "Response": {
        "RequestId": "ce83ca0a-73b3-4b70-a502-0694961a32e6",
        "Result": "stop task failed"
    }
}
```

