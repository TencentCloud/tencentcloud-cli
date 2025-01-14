**Example 1: 列出单次拨测详情数据**

列出单次拨测详情数据

Input: 

```
tccli cat DescribeDetailedSingleProbeData --cli-unfold-argument  \
    --BeginTime 1679899994107 \
    --EndTime 1679903594107 \
    --TaskType AnalyzeTaskType_Network \
    --SortField ProbeTime \
    --Ascending True \
    --Offset 0 \
    --Limit 10 \
    --SelectedFields ProbeTime City Operator ProbeIP \
    --TaskID task-p4najqd4 \
    --ScrollID DXF1ZXJ5QW5kRmV0Y2gBAAAAAQEPczgWVU1RMC12VHhSUWlYa1I0dnU4aXlxxx==
```

Output: 
```
{
    "Response": {
        "ScrollID": "DXF1ZXJ5QW5kRmV0Y2gBAAAAAQEPczgWVU1RMC12VHhSUWlYa1I0dnU4aXlxxx==",
        "TotalNumber": 10,
        "DataSet": [
            {
                "ProbeTime": 1,
                "Labels": [
                    {
                        "ID": 0,
                        "Name": "City",
                        "Value": "上海市"
                    }
                ],
                "Fields": [
                    {
                        "ID": 0,
                        "Name": "ProbeTime",
                        "Value": 1679903537000
                    }
                ]
            }
        ],
        "RequestId": "720b3231-5a85-4f05-aaab-c9b9596xxxxx"
    }
}
```

