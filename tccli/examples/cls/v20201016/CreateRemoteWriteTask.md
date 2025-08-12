**Example 1: 创建RemoteWrite 任务**



Input: 

```
tccli cls CreateRemoteWriteTask --cli-unfold-argument  \
    --TopicId xxx-xxx-xxx-xxx \
    --Name test_name \
    --Target prometheus \
    --RemoteWriteURL  \
    --AuthType 0 \
    --NetType 1
```

Output: 
```
{
    "Response": {
        "TaskId": "abc-dec-ff-ee",
        "RequestId": "xxx-x-xx-xx"
    }
}
```

