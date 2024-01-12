**Example 1: 1**

1

Input: 

```
tccli wedata RunForceSucScheduleInstances --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation",
            "Message": "[500] during [POST] to [http://scheduler-gateway-service/api/taskScheduler/instance/batchForceSuc] [ScheduleOpsApi#batchForceSuc(InstanceRequest)]: [{\"timestamp\":\"2023-08-28T08:40:41.514+0000\",\"status\":500,\"error\":\"Internal Server Error\",\"message\":\"获取当前用户选择的项目信息为空，请先选择或者创建项目！\",\"path\":\"/api/taskScheduler/instance/batchForceSuc\"}]"
        },
        "RequestId": "7f5215ed-d304-4feb-895a-449dcfe0576a"
    }
}
```

