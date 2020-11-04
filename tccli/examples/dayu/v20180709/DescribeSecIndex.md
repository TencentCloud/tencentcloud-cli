**Example 1: 获取安全统计**



Input: 

```
tccli dayu DescribeSecIndex --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "BeginDate": "2018-10-01 00:00:00",
        "EndDate": "2018-10-31 23:59:59",
        "Data": [
            {
                "Key": "AttackIpCount",
                "Value": "0"
            },
            {
                "Key": "AttackCount",
                "Value": "0"
            },
            {
                "Key": "BlockCount",
                "Value": "0"
            },
            {
                "Key": "MaxMbps",
                "Value": "0"
            },
            {
                "Key": "IpNum",
                "Value": "0"
            }
        ],
        "RequestId": "f264b10e-da87-456e-8398-3389b69e39fb"
    }
}
```

