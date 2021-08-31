**Example 1: 查询检测进度接口**

根据任务id查询检测进度

Input: 

```
tccli cwp DescribeScanSchedule --cli-unfold-argument  \
    --TaskId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "Schedule": 20
    }
}
```

