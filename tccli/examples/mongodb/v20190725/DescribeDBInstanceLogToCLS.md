**Example 1: 查询实例日志投递 CLS 的配置**



Input: 

```
tccli mongodb DescribeDBInstanceLogToCLS --cli-unfold-argument  \
    --InstanceId cmgo-2gdv46zn \
    --CLSRegion ap-guangzhou
```

Output: 
```
{
    "Response": {
        "ErrorLog": {
            "CLSRegion": "",
            "LogSetId": "",
            "LogTopicId": "",
            "Status": "OFF"
        },
        "OperationLog": {
            "CLSRegion": "",
            "LogSetId": "",
            "LogTopicId": "",
            "Status": "OFF"
        },
        "SlowLog": {
            "CLSRegion": "ap-guangzhou",
            "LogSetId": "64ae0139-0621-4e59-aba7-f60cd2264ab6",
            "LogTopicId": "6af6a321-879e-415b-b612-64dad8a3c571",
            "Status": "OFF"
        },
        "RequestId": "c11fe4ab-9d7f-4eed-bdcb-671ca55386ee"
    }
}
```

