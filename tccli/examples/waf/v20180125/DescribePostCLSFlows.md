**Example 1: 获取CLS投递流任务列表**

获取CLS投递流任务列表

Input: 

```
tccli waf DescribePostCLSFlows --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "a20702ee-7206-4eeb-ba74-d13ecbc29c02",
        "PostCLSFlows": [
            {
                "FlowId": 100001,
                "LogType": 1,
                "Status": 1,
                "CLSRegion": "ap-guangzhou",
                "LogsetName": "waf-post-logset",
                "LogsetID": "59a61f1a-d606-4a17-8eaf-0881cb656887"
            }
        ]
    }
}
```

**Example 2: 获取CLS投递流任务列表新**

获取CLS投递流任务列表

Input: 

```
tccli waf DescribePostCLSFlows --cli-unfold-argument  \
    --LogType 1
```

Output: 
```
{
    "Response": {
        "PostCLSFlows": [
            {
                "CLSRegion": "ap-guangzhou",
                "FlowId": 16778297,
                "LogTopicID": "3a867828-4e7e-4268-bac4-5f3900e49e46",
                "LogTopicName": "waf_access_logtopic",
                "LogType": 1,
                "LogsetID": "76dc6d58-c4b6-4e39-92dc-0ecf35e09282",
                "LogsetName": "waf_logset",
                "Status": 1,
                "WriteConfig": {
                    "EnableBody": 1,
                    "EnableBot": 0,
                    "EnableHeaders": 1,
                    "EnableResponse": 1
                }
            }
        ],
        "RequestId": "32e9cdf3-05ad-4c7e-b225-d3dfb0efa201"
    }
}
```

