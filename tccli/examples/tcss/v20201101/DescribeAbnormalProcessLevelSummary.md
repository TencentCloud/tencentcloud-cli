**Example 1: 统计异常进程各威胁等级待处理事件数**



Input: 

```
tccli tcss DescribeAbnormalProcessLevelSummary --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "MediumLevelEventCount": 0,
        "HighLevelEventCount": 0,
        "RequestId": "xx",
        "LowLevelEventCount": 0
    }
}
```

