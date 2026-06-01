**Example 1: 日志投递历史记录**



Input: 

```
tccli tchousex DescribeCLSConfigHistory --cli-unfold-argument  \
    --InstanceId instance-7wxclv93 \
    --DeliveryType spark_task_record \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "",
        "RequestId": "a215325e-fef8-4693-bd12-d8d61183f47c",
        "ReturnData": "{\"total\":12,\"list\":[{\"LogsetId\":\"7bd1caf4-3b8e-42ea-9424-3e550c655431\",\"TopicId\":\"eb0e8a05-45a6-4cd0-9918-5d4d77af9579\",\"Reason\":\"\",\"StartTime\":\"2025-05-14 16:43:45\",\"EndTime\":\"\"},{\"LogsetId\":\"7bd1caf4-3b8e-42ea-9424-3e550c655431\",\"TopicId\":\"6d77bb84-7571-4b8e-9272-f0c5a7dd4102\",\"Reason\":\"用户100006811818操作停止投递\",\"StartTime\":\"2025-05-12 11:25:14\",\"EndTime\":\"2025-05-14 16:41:05\"},{\"LogsetId\":\"7bd1caf4-3b8e-42ea-9424-3e550c655431\",\"TopicId\":\"6d77bb84-7571-4b8e-9272-f0c5a7dd4102\",\"Reason\":\"因用户100012695507修改目标CLS等原因造成异常, 可联系TCHouse-X团队协助排查\",\"StartTime\":\"2025-04-29 15:18:37\",\"EndTime\":\"2025-05-12 11:19:25\"},{\"LogsetId\":\"7bd1caf4-3b8e-42ea-9424-3e550c655431\",\"TopicId\":\"28177491-d030-41ab-9775-d26464e173eb\",\"Reason\":\"因用户100012695507修改目标CLS等原因造成异常, 可联系TCHouse-X团队协助排查\",\"StartTime\":\"2025-04-29 11:10:27\",\"EndTime\":\"2025-04-29 14:34:07\"},{\"LogsetId\":\"7bd1caf4-3b8e-42ea-9424-3e550c655431\",\"TopicId\":\"28177491-d030-41ab-9775-d26464e173eb\",\"Reason\":\"因用户100012695507修改目标CLS等原因造成异常, 可联系TCHouse-X团队协助排查\",\"StartTime\":\"2025-04-25 11:44:38\",\"EndTime\":\"2025-04-29 11:05:01\"},{\"LogsetId\":\"7bd1caf4-3b8e-42ea-9424-3e550c655431\",\"TopicId\":\"28177491-d030-41ab-9775-d26464e173eb\",\"Reason\":\"因用户100012695507修改目标CLS等原因造成异常, 可联系TCHouse-X团队协助排查\",\"StartTime\":\"2025-04-24 16:08:17\",\"EndTime\":\"2025-04-25 11:11:19\"},{\"LogsetId\":\"7bd1caf4-3b8e-42ea-9424-3e550c655431\",\"TopicId\":\"28177491-d030-41ab-9775-d26464e173eb\",\"Reason\":\"因用户100012695507修改目标CLS等原因造成异常, 可联系TCHouse-X团队协助排查\",\"StartTime\":\"2025-04-24 15:20:53\",\"EndTime\":\"2025-04-24 15:36:34\"},{\"LogsetId\":\"7bd1caf4-3b8e-42ea-9424-3e550c655431\",\"TopicId\":\"\",\"Reason\":\"因用户100012695507修改目标CLS等原因造成异常, 可联系TCHouse-X团队协助排查\",\"StartTime\":\"2025-04-23 17:31:24\",\"EndTime\":\"2025-04-24 15:15:25\"},{\"LogsetId\":\"7bd1caf4-3b8e-42ea-9424-3e550c655431\",\"TopicId\":\"\",\"Reason\":\"因用户100012695507修改目标CLS等原因造成异常, 可联系TCHouse-X团队协助排查\",\"StartTime\":\"2025-04-23 15:34:56\",\"EndTime\":\"2025-04-23 17:25:57\"},{\"LogsetId\":\"7bd1caf4-3b8e-42ea-9424-3e550c655431\",\"TopicId\":\"28177491-d030-41ab-9775-d26464e173eb\",\"Reason\":\"因用户100012695507修改目标CLS等原因造成异常, 可联系TCHouse-X团队协助排查\",\"StartTime\":\"2025-04-18 14:37:20\",\"EndTime\":\"2025-04-23 15:02:16\"}]}"
    }
}
```

