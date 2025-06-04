**Example 1: 查询作业事件**

请求参数不包含 "RunningOrderIds"时，接口为查询作业事件接口

Input: 

```
tccli oceanus DescribeJobEvents --cli-unfold-argument  \
    --RunningOrderIds 1 \
    --Types 1 2 \
    --EndTimestamp 1630933910 \
    --StartTimestamp 1630833910 \
    --JobId cql-xxx
```

Output: 
```
{
    "Response": {
        "RunningOrderIds": [
            1
        ],
        "Events": [
            {
                "RunningOrderId": 1,
                "Description": "作业停止事件",
                "Timestamp": 1630933810,
                "Type": "11"
            }
        ],
        "TotalCount": 1,
        "RequestId": "123345be-e89b-52f3-a456-426616274040"
    }
}
```

**Example 2: 查询作业运行实例ID**

请求参数不包含 "RunningOrderIds"时，接口为查询作业实例ID接口

Input: 

```
tccli oceanus DescribeJobEvents --cli-unfold-argument  \
    --WorkSpaceId space-xxxx \
    --JobId cql-xxxx \
    --StartTimestamp 1747994802 \
    --EndTimestamp 1748513202
```

Output: 
```
{
    "Response": {
        "Events": null,
        "RequestId": "a908a65e-aa94-4406-acc4-2aa64edb40c6",
        "RunningOrderIds": [
            10,
            9,
            8,
            7
        ],
        "Versions": [
            1,
            2,
            3
        ],
        "TotalCount": 0
    }
}
```

