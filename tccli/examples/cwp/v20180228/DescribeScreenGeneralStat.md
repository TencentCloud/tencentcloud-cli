**Example 1: 大屏可视化获取主机相关统计**



Input: 

```
tccli cwp DescribeScreenGeneralStat --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Protection": [
            {
                "Name": "旗舰版",
                "Value": 82
            },
            {
                "Name": "专业版",
                "Value": 0
            }
        ],
        "RequestId": "25d35d95-6e24-4161-f405-ae7a90afe569",
        "Machines": [
            {
                "Name": "在线",
                "Value": 57
            },
            {
                "Name": "离线",
                "Value": 30
            }
        ]
    }
}
```

