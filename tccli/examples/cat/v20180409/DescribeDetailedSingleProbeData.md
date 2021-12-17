**Example 1: 列出单次拨测详情数据**



Input: 

```
tccli cat DescribeDetailedSingleProbeData --cli-unfold-argument  \
    --BeginTime 1627345083000 \
    --EndTime 1627363083000 \
    --TaskType xxx \
    --SortField xxx \
    --Ascending True \
    --Offset 0 \
    --Limit 10 \
    --SelectedFields xxx \
    --TaskID task_xxx \
    --Operators xxx \
    --Districts xxx \
    --ErrorTypes xxx
```

Output: 
```
{
    "Response": {
        "TotalNumber": 10,
        "DataSet": [
            {
                "ProbeTime": 1,
                "Labels": [
                    {
                        "ID": 0,
                        "Name": "xxx",
                        "Value": "xxx"
                    }
                ],
                "Fields": [
                    {
                        "ID": 0,
                        "Name": "xxx",
                        "Value": 1
                    }
                ]
            }
        ],
        "RequestId": "xx"
    }
}
```

