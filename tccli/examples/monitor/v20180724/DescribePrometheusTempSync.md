**Example 1: 拉取同步目标**

拉取同步目标

Input: 

```
tccli monitor DescribePrometheusTempSync --cli-unfold-argument  \
    --TemplateId "temp-xxx"
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "Targets": [
            {
                "Region": "ap-shanghai",
                "InstanceId": "prom-xxx",
                "ClusterId": "xxx",
                "SyncTime": "2020-02-2"
            }
        ]
    }
}
```

