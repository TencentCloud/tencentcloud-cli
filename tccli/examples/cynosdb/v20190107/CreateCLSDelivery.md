**Example 1: 创建日志投递**



Input: 

```
tccli cynosdb CreateCLSDelivery --cli-unfold-argument  \
    --InstanceId cynosdbmysql-ins-o971o62r \
    --CLSInfoList.0.TopicId 38b86342-7cb0-4776-9ebd-ff1830035da1 \
    --CLSInfoList.0.TopicOperation reuse \
    --CLSInfoList.0.GroupId 17de6e2a-efd0-4fc2-ba2e-8845bd4f9895 \
    --CLSInfoList.0.Region ap-guangzhou \
    --CLSInfoList.0.GroupOperation reuse
```

Output: 
```
{
    "Response": {
        "TaskId": 123456,
        "RequestId": "347698da-03e4-4078-8d96-9a8b219c01a5"
    }
}
```

