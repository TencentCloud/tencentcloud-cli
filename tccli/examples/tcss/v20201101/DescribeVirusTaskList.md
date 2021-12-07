**Example 1: 运行时查询文件查杀任务列表**

运行时查询文件查杀任务列表

Input: 

```
tccli tcss DescribeVirusTaskList --cli-unfold-argument  \
    --TaskId dskaldjskld
```

Output: 
```
{
    "Response": {
        "List": [],
        "RequestId": "ff49ad4b-fe52-4f9d-8810-ba377eab9124",
        "TotalCount": 6
    }
}
```

