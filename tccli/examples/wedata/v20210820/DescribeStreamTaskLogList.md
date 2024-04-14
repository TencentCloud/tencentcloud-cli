**Example 1: 查询实时任务日志列表**

查询实时任务日志列表

Input: 

```
tccli wedata DescribeStreamTaskLogList --cli-unfold-argument  \
    --ProjectId 1 \
    --TaskId 20230112170349643 \
    --JobId 123213 \
    --Container pod \
    --EndTime 143213 \
    --StartTime 143113 \
    --Limit 1 \
    --OrderType desc \
    --RunningOrderId 1 \
    --Keyword INFO
```

Output: 
```
{
    "Response": {
        "ListOver": true,
        "LogContentList": [
            {
                "Log": "vdscsdcs",
                "PkgId": "1",
                "PkgLogId": "1",
                "Time": 1,
                "ContainerName": "pod"
            }
        ],
        "RequestId": "as1cs2c123asyi23bh213cc"
    }
}
```

