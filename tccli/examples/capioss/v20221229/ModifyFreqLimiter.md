**Example 1: 修改限频过滤器配置**

修改cvm指定接口限频过滤器配置

Input: 

```
tccli capioss ModifyFreqLimiter --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Module": "cvm",
        "Name": "$module.$version.$action.$uin",
        "RequestId": "e6a07218-57c3-4ad8-ae26-990e3868a4a8",
        "Spec": {
            "KeyPattern": "$module/$version/$action/$uin",
            "Matchers": [
                {
                    "FrequencyLimit": -1,
                    "Matcher": "*/*/*/*"
                },
                {
                    "FrequencyLimit": 100,
                    "Matcher": "cvm/2017-03-12/DescribeZoneCdhInstanceConfigInfos/*"
                }
            ]
        }
    }
}
```

