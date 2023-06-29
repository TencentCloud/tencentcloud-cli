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
                "LogSet": "xx",
                "LogType": "xx",
                "State": true,
                "Region": "xx",
                "TopicID": "xx"
            }
        ],
        "RequestId": "29b37d86-f63d-43d1-b21a-640e82965198"
    }
}
```

