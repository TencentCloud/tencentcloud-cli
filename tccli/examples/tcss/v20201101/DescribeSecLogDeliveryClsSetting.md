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
                "LogSet": "",
                "LogSetName": "",
                "LogType": "container_bash",
                "Region": "",
                "State": false,
                "TopicID": "",
                "TopicName": ""
            },
            {
                "LogSet": "",
                "LogSetName": "",
                "LogType": "container_launch",
                "Region": "",
                "State": false,
                "TopicID": "",
                "TopicName": ""
            },
            {
                "LogSet": "",
                "LogSetName": "",
                "LogType": "k8s_api",
                "Region": "",
                "State": false,
                "TopicID": "",
                "TopicName": ""
            }
        ],
        "RequestId": "1279ad3b-a5aa-46ea-825d-3124cc19112a"
    }
}
```

