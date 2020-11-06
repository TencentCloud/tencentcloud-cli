**Example 1: 获取实时拉取端口任务状态**

获取实时拉取端口任务状态

Input: 

```
tccli yunjing DescribeOpenPortTaskStatus --cli-unfold-argument  \
    --Uuid 6b6cd843-6bc1-4011-a74c-dc3fd26a7dd1
```

Output: 
```
{
    "Response": {
        "Status": "COMPLETE",
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

