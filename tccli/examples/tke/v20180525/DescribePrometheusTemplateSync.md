**Example 1: 拉取同步目标**

拉取同步目标

Input: 

```
tccli tke DescribePrometheusTemplateSync --cli-unfold-argument  \
    --TemplateId "temp-dsffgg"
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "Targets": [
            {
                "Region": "ap-shanghai",
                "InstanceId": "prom-dsdfaf",
                "ClusterId": "cls-dfdfga",
                "SyncTime": "2020-02-2"
            }
        ]
    }
}
```

