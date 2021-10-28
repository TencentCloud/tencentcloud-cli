**Example 1: 设备数据返回**

查询ua_device指标的数据

Input: 

```
tccli cdn DescribeTopData --cli-unfold-argument  \
    --StartTime '2018-09-04 00:00:00' \
    --EndTime '2018-09-04 12:00:00' \
    --Metric ua_device \
    --Filter request \
    --Domains www.test.com www.test.com
```

Output: 
```
{
    "Response": {
        "RequestId": "37aabaa8-c4c1-45ea-a4aa-8bafea1a496d",
        "Data": [
            {
                "Resource": "all",
                "DetailData": [
                    {
                        "Name": "桌面",
                        "Value": 635,
                        "Percent": 0.6642
                    },
                    {
                        "Name": "其他/未知",
                        "Value": 260,
                        "Percent": 0.272
                    },
                    {
                        "Name": "移动",
                        "Value": 61,
                        "Percent": 0.0638
                    }
                ]
            }
        ]
    }
}
```

