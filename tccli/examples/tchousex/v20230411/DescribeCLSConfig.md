**Example 1: 日志投递配置信息**



Input: 

```
tccli tchousex DescribeCLSConfig --cli-unfold-argument  \
    --InstanceId instance-7wxclv93
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "",
        "RequestId": "58c5c250-4a4e-4de7-ad34-40a81d100f04",
        "ReturnData": "[{\"InstanceId\":\"instance-7wxclv93\",\"DeliveryType\":\"impala_log\",\"LogsetId\":\"7bd1caf4-3b8e-42ea-9424-3e550c655431\",\"TopicId\":\"291500cc-32ed-48fb-b8e7-63785dbd2cd7\",\"Reason\":\"\",\"Status\":2,\"StartTime\":\"2025-05-12 11:25:15\",\"EndTime\":\"\"},{\"InstanceId\":\"instance-7wxclv93\",\"DeliveryType\":\"operate_record\",\"LogsetId\":\"7bd1caf4-3b8e-42ea-9424-3e550c655431\",\"TopicId\":\"41213780-0c08-41f6-bae2-d8b08b63bd10\",\"Reason\":\"因用户100012695507修改目标CLS等原因造成异常, 可联系TCHouse-X团队协助排查\",\"Status\":4,\"StartTime\":\"2025-04-29 11:10:27\",\"EndTime\":\"2025-04-29 14:39:31\"},{\"InstanceId\":\"instance-7wxclv93\",\"DeliveryType\":\"spark_log\",\"LogsetId\":\"7bd1caf4-3b8e-42ea-9424-3e550c655431\",\"TopicId\":\"938cd3fc-be54-4552-a513-a1a388f78af8\",\"Reason\":\"\",\"Status\":2,\"StartTime\":\"2025-05-12 11:25:14\",\"EndTime\":\"\"},{\"InstanceId\":\"instance-7wxclv93\",\"DeliveryType\":\"spark_session_record\",\"LogsetId\":\"7bd1caf4-3b8e-42ea-9424-3e550c655431\",\"TopicId\":\"3f2aa8e4-6094-4ee2-91b9-474651d7be32\",\"Reason\":\"因用户100012695507修改目标CLS等原因造成异常, 可联系TCHouse-X团队协助排查\",\"Status\":4,\"StartTime\":\"2025-04-29 11:10:30\",\"EndTime\":\"2025-04-29 14:34:11\"},{\"InstanceId\":\"instance-7wxclv93\",\"DeliveryType\":\"spark_task_record\",\"LogsetId\":\"7bd1caf4-3b8e-42ea-9424-3e550c655431\",\"TopicId\":\"eb0e8a05-45a6-4cd0-9918-5d4d77af9579\",\"Reason\":\"\",\"Status\":2,\"StartTime\":\"2025-05-14 16:43:45\",\"EndTime\":\"\"}]"
    }
}
```

