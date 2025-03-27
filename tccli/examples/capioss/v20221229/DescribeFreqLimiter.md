**Example 1: 查询指定过滤器**

查询apitest下指定过滤器

Input: 

```
tccli capioss DescribeFreqLimiter --cli-unfold-argument  \
    --Data.Module apitest \
    --Data.Name $module.$version.$action.$uin
```

Output: 
```
{
    "Response": {
        "Filter": {
            "Module": "apitest",
            "Name": "$module.$version.$action.$uin",
            "Spec": {
                "KeyPattern": "$module/$version/$action/$uin",
                "Matchers": [
                    {
                        "FrequencyLimit": 2,
                        "Matcher": "apitest/2021-10-30/AddHan2/123"
                    },
                    {
                        "FrequencyLimit": 1,
                        "Matcher": "apitest/2021-10-30/AddHan2/*"
                    },
                    {
                        "FrequencyLimit": -1,
                        "Matcher": "*/*/*/*"
                    },
                    {
                        "FrequencyLimit": 1,
                        "Matcher": "apitest/2017-03-12/InstanceTest/*"
                    }
                ]
            }
        },
        "RequestId": "b39b9138-64a3-4107-8273-3282d82374b7"
    }
}
```

**Example 2: 查询指定接口过滤器**

查询apitest下指定接口过滤器

Input: 

```
tccli capioss DescribeFreqLimiter --cli-unfold-argument  \
    --Data.Module apitest \
    --Data.Name $module.$version.$action.$uin
```

Output: 
```
{
    "Response": {
        "Filter": {
            "Module": "apitest",
            "Name": "$module.$version.$action.$uin",
            "Spec": {
                "KeyPattern": "$module/$version/$action/$uin",
                "Matchers": [
                    {
                        "FrequencyLimit": 1,
                        "Matcher": "apitest/2017-03-12/InstanceTest/*"
                    }
                ]
            }
        },
        "RequestId": "fe9be21f-b267-45b9-99d9-55cce867dd15"
    }
}
```

