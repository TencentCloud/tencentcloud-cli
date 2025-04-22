**Example 1: 获取CKafka投递流任务列表**

获取CKafka投递流任务列表

Input: 

```
tccli waf DescribePostCKafkaFlows --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "a20702ee-7206-4eeb-ba74-d13ecbc29c02",
        "PostCKafkaFlows": [
            {
                "FlowId": 100000,
                "LogType": 1,
                "Status": 1,
                "CKafkaRegion": "ap-guangzhou",
                "CKafkaID": "ckafka-o9gjqonr",
                "Brokers": "11.179.226.202:6016",
                "Version": "2.4.1",
                "Topic": "waf_post_access_log",
                "Compression": "lz4",
                "SASLEnable": 0,
                "SASLUser": "sa",
                "SASLPassword": "sa***",
                "Content": "info"
            }
        ]
    }
}
```

