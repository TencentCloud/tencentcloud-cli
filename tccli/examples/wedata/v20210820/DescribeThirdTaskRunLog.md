**Example 1: 获取第三方日志成功返回**

获取第三方日志成功返回

Input: 

```
tccli wedata DescribeThirdTaskRunLog --cli-unfold-argument  \
    --TaskId 20230313154400000 \
    --CurRunDate 2023-03-13 15:44:16
```

Output: 
```
{
    "Response": {
        "Data": "third party log",
        "RequestId": "e2669547-161c-46ea-8d69-41863d2ba488"
    }
}
```

