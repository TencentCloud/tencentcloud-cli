**Example 1: 测试用例**



Input: 

```
tccli waf DescribeLLMSdkAccess --cli-unfold-argument  \
    --InstanceId waf_2l15d14809yfq9sf \
    --Offset 0 \
    --Limit 10 \
    --By UpdateTime \
    --Order ASC
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "ContentRuleCount": 5,
                "ContentRuleStatus": true,
                "CreateTime": 1774247637,
                "Domain": "9000002874",
                "LimitRuleCount": 40,
                "LimitRuleStatus": true,
                "MainStatus": true,
                "Name": "ddptest",
                "Remark": "测试213313",
                "UpdateTime": 1774248650
            }
        ],
        "Total": 1,
        "RequestId": "d5255828-7c5e-4c18-9558-12535caee67e"
    }
}
```

