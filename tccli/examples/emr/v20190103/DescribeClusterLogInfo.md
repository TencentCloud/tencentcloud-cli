**Example 1: 用于es serverless获取emr支持的服务日志信息**



Input: 

```
tccli emr DescribeClusterLogInfo --cli-unfold-argument  \
    --InstanceId emr-xffef1j
```

Output: 
```
{
    "Response": {
        "ServiceCvmLogPaths": [
            {
                "ServiceName": "abc",
                "LogPaths": [
                    "abc"
                ],
                "LogIndex": "abc",
                "LogFieldRole": "abc",
                "LogMultiLinePattern": "abc"
            }
        ],
        "CVMInstanceIds": [
            "abc"
        ],
        "LogInfoVersion": "abc",
        "RequestId": "abc"
    }
}
```

