**Example 1: 获取运维任务列表示例**



Input: 

```
tccli bh DescribeOperationTask --cli-unfold-argument  \
    --Name 周期运维任务 \
    --Type 2 \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "wewaq-eqwwd-wesfd-332sfda",
        "OperationTasks": [
            {
                "Id": 10,
                "OperationId": "ops-xzfr5yeg",
                "Name": "周期运维任务",
                "UserName": "dfraw",
                "RealName": "zdfrawhang",
                "Type": 2,
                "Period": 1,
                "FirstTime": "2025-03-14T15:33:34+08:00",
                "NextTime": "2025-03-15T15:33:34+08:00"
            }
        ],
        "TotalCount": 1
    }
}
```

