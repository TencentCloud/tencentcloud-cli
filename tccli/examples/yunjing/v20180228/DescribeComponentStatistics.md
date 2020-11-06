**Example 1: 获取组件统计列表**

获取组件统计列表

Input: 

```
tccli yunjing DescribeComponentStatistics --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "ComponentStatistics": [
            {
                "Id": 100010,
                "MachineNum": 10,
                "ComponentName": "machine-name",
                "ComponentType": "WEB",
                "Description": "description"
            }
        ],
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "TotalCount": 100
    }
}
```

