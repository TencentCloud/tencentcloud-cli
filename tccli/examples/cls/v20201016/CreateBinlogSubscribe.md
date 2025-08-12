**Example 1: 创建binlog采集**

CreateBinlogSubscribe

Input: 

```
tccli cls CreateBinlogSubscribe --cli-unfold-argument  \
    --Name template_1 \
    --TopicId 715094e3-01b0-4aeb-91f5-ee9f46a4a13c \
    --Type 1 \
    --SqlInfo.AccessMode 1 \
    --SqlInfo.User root \
    --SqlInfo.Password root-3306 \
    --SqlInfo.InstanceId instance-id \
    --InitialPoint.Type 1 \
    --Events DDL \
    --Metadatas position \
    --TimestampType 1 \
    --BlockListStatus 1 \
    --AllowListStatus 1
```

Output: 
```
{
    "Response": {
        "TaskId": "715094e3-01b0-4aeb-91f5-ee9f46a4a13c",
        "RequestId": "715094e3-01b0-4aeb-91f5-ee9f46a4a131"
    }
}
```

