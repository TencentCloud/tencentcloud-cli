**Example 1: 查询waf攻击top数据**



Input: 

```
tccli teo DescribeWebManagedRulesTopData --cli-unfold-argument  \
    --MetricName waf_requestNum_cip \
    --PolicyIds 1705 \
    --ZoneIds zone-21xfqlh4qjee \
    --Domains www.baidu.com \
    --Limit 1 \
    --StartTime 2020-09-22T00:00:00+00:00 \
    --EndTime 2020-09-22T00:00:00+00:00 \
    --Area overseas
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "Msg": "success",
        "Data": [
            {
                "Value": [
                    {
                        "Count": 123,
                        "Name": "1.2.3.4"
                    }
                ],
                "Key": "www.baidu.com"
            }
        ],
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707"
    }
}
```

