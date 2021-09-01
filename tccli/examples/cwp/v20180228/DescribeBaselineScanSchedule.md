**Example 1: 查询检测进度接口**

根据任务id查询基线检测进度

Input: 

```
tccli cwp DescribeBaselineScanSchedule --cli-unfold-argument  \
    --TaskId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "req-566234234",
        "Schedule": 20
    }
}
```

