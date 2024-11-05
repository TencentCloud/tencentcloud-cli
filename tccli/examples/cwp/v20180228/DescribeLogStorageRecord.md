**Example 1: 获取日志存储量记录**

获取日志存储量记录

Input: 

```
tccli cwp DescribeLogStorageRecord --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Records": [
            {
                "Month": "202410",
                "UsedSize": 53715597787,
                "InquireSize": 53687091200
            }
        ],
        "RequestId": "e5b4724c-49af-46ab-bd84-cdbae897e7e0"
    }
}
```

