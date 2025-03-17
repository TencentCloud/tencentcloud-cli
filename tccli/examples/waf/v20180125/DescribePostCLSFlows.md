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

