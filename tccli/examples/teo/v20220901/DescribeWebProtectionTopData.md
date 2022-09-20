**Example 1: 查询CC防护Top数据**



Input: 

```
tccli teo DescribeWebProtectionTopData --cli-unfold-argument  \
    --QueryCondition.0.Operator equals \
    --QueryCondition.0.Value drop \
    --QueryCondition.0.Key action \
    --Interval min \
    --ZoneIds zone-21xfqlh4qjee \
    --Limit 1 \
    --StartTime 2020-09-22T00:00:00+00:00 \
    --Domains www.baidu.com \
    --EndTime 2020-09-22T00:00:00+00:00 \
    --MetricName waf_requestNum_cip \
    --Area overseas
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Data": [
            {
                "Value": [
                    {
                        "Count": 123,
                        "Name": "udp"
                    }
                ],
                "Key": "waf_requestNum_cip"
            }
        ],
        "RequestId": "d6182c0c-08c5-448e-9cc8-abb00bbe5fe5"
    }
}
```

