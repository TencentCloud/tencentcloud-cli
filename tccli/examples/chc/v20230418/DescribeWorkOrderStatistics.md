**Example 1: 查询工单状态对应的数量**



Input: 

```
tccli chc DescribeWorkOrderStatistics --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "CancelNum": 0,
        "CheckingNum": 0,
        "ConfirmingNum": 0,
        "ExceptionNum": 2748,
        "FinishNum": 297,
        "ProcessingNum": 112,
        "RejectNum": 91,
        "RequestId": "4c2a84c1-61ab-4f4c-b3b3-b38d7e6af4fc",
        "TotalNum": 3248
    }
}
```

