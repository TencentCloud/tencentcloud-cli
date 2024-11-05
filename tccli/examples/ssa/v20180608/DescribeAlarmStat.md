**Example 1: 空数据**

空数据

Input: 

```
tccli ssa DescribeAlarmStat --cli-unfold-argument  \
    --StartTime 2020-09-22 00:00:00 \
    --EndTime 2020-09-22 00:00:00
```

Output: 
```
{
    "Response": {
        "Data": {
            "AttackEvent": [
                {
                    "SsaSrcIp": "1.1.1.1",
                    "SsaDstIp": "1.1.1.2",
                    "SsaDstProvince": "湖北省",
                    "SsaDstCity": "武汉市",
                    "SsaDstCountry": "中国",
                    "SsaSrcProvince": "江苏省",
                    "SsaSrcCountry": "中国",
                    "SsaSrcCity": "南京市"
                }
            ]
        },
        "RequestId": "7fe7e825-cf43-4749-a570-2912f5a62706"
    }
}
```

