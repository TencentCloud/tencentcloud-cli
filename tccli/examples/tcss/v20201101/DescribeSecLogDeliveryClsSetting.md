**Example 1: 查询安全日志投递Cls配置**



Input: 

```
tccli tcss DescribeSecLogDeliveryClsSetting --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "LogTypeList": [
            {
                "LogSet": "846f4834-7f89-4e97-9c0a-e8623959****",
                "LogSetName": "tcss",
                "LogType": "container_bash",
                "Region": "ap-guangzhou",
                "State": false,
                "TopicID": "72ebf085-f7b7-4efb-961a-6ef37f07****",
                "TopicName": "tcss_log_****"
            },
            {
                "LogSet": "LogSet",
                "LogSetName": "cn",
                "LogType": "container_launch",
                "Region": "ap-guangzhou",
                "State": false,
                "TopicID": "TopicID",
                "TopicName": "TopicName"
            },
            {
                "LogSet": "LogSet",
                "LogSetName": "LogSetName",
                "LogType": "k8s_api",
                "Region": "ap-guangzhou",
                "State": false,
                "TopicID": "TopicID",
                "TopicName": "TopicName"
            }
        ],
        "RequestId": "1279ad3b-a5aa-46ea-825d-3124cc19112a"
    }
}
```

