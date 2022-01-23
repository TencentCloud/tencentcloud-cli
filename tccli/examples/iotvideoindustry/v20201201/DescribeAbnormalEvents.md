**Example 1: 获取异常事件统计**



Input: 

```
tccli iotvideoindustry DescribeAbnormalEvents --cli-unfold-argument  \
    --StartTime 1622520250 \
    --EndTime 1624248250
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Date": "2021-06-01",
                "Info": [
                    {
                        "Key": 4,
                        "Count": 0
                    },
                    {
                        "Key": 5,
                        "Count": 0
                    },
                    {
                        "Key": 6,
                        "Count": 0
                    }
                ]
            },
            {
                "Date": "2021-06-02",
                "Info": [
                    {
                        "Key": 4,
                        "Count": 0
                    },
                    {
                        "Key": 5,
                        "Count": 0
                    },
                    {
                        "Key": 6,
                        "Count": 0
                    }
                ]
            }
        ],
        "RequestId": "1111"
    }
}
```

