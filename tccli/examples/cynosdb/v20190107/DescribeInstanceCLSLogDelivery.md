**Example 1: 查询实例日志投递信息**



Input: 

```
tccli cynosdb DescribeInstanceCLSLogDelivery --cli-unfold-argument  \
    --InstanceId cynosdbmysql-ins-o971o62r
```

Output: 
```
{
    "Response": {
        "InstanceCLSDeliveryInfos": [
            {
                "GroupId": "a5532aba-506f-4ec4-a293-e0ac34b69a4e",
                "GroupName": "cloud_cynos_-test-003_logset",
                "InstanceId": "cynosdbmysql-ins-o971o62r",
                "InstanceName": "cynosdbmysql-ins-o971o62r",
                "Region": "ap-qingyuan",
                "Status": "running",
                "TopicId": "2a289122-0b01-490b-be75-763da79621fe",
                "TopicName": "cloud_cynos_-test-003_topic"
            },
            {
                "GroupId": "2f484392-d3f1-491c-82a0-00ceaad9281a",
                "GroupName": "cloud_cynos_-test-002_logset",
                "InstanceId": "cynosdbmysql-ins-o971o62r",
                "InstanceName": "cynosdbmysql-ins-o971o62r",
                "Region": "ap-qingyuan",
                "Status": "running",
                "TopicId": "83dc6703-f43a-4b95-92ec-267bdf9e48c3",
                "TopicName": "cloud_cynos_-test-002_topic"
            }
        ],
        "RequestId": "347698da-03e4-4078-8d96-9a8b219c01a5",
        "TotalCount": 2
    }
}
```

