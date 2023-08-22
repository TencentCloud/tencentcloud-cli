**Example 1: demo1**

查询每分钟统计值，不以status分组

Input: 

```
tccli eb DescribeLogStats --cli-unfold-argument  \
    --StartTime 1600000000000 \
    --EndTime 1600000010000 \
    --EventBusId eb-xxxx \
    --Filter.0.Key host \
    --Filter.0.Operator eq \
    --Filter.0.Value 106.53.106.243
```

Output: 
```
{
    "Response": {
        "Results": [
            {
                "Status": "all",
                "Data": [
                    {
                        "Count": 0,
                        "Timestamp": 0
                    }
                ]
            }
        ],
        "RequestId": "162d46e5-2968-4b4c-9e61-d84ab10f26a6"
    }
}
```

**Example 2: demo2**

查询每分钟统计值，以status分组

Input: 

```
tccli eb DescribeLogStats --cli-unfold-argument  \
    --StartTime 1600000000000 \
    --EndTime 1600000010000 \
    --EventBusId eb-xxx \
    --GroupByStatus 0 1
```

Output: 
```
{
    "Response": {
        "Results": [
            {
                "Status": "abc",
                "Data": [
                    {
                        "Count": 0,
                        "Timestamp": 0
                    }
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

