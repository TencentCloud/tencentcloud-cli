**Example 1: 查询操作日志列表**



Input: 

```
tccli dasb DescribeOperationEvent --cli-unfold-argument  \
    --UserName Liam \
    --RealName Noah \
    --StartTime 2020-09-22T00:00:00+00:00 \
    --EndTime 2020-09-22T00:00:00+00:00 \
    --SourceIp 17.25.24.41 \
    --Kind 1 \
    --Result 1 \
    --Offset 1 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "OperationEventSet": [
            {
                "UserName": "Liam",
                "Kind": 1,
                "RealName": "Noah",
                "Result": 1,
                "Time": "2020-09-22T00:00:00+08:00",
                "Operation": "新建用户组",
                "SourceIp": "10.15.42.47"
            }
        ],
        "RequestId": "3bf47843-f8b2-40f7-8963-76d9506eed22"
    }
}
```

