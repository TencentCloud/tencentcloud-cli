**Example 1: 示例**



Input: 

```
tccli cwp DescribeLicenseBindSchedule --cli-unfold-argument  \
    --TaskId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "db15d3f0-5573-4409-a75e-04d54b8c564c",
        "Schedule": 100,
        "TotalCount": 1,
        "List": [
            {
                "Quuid": "xxx-xxxx-xxxx-xxx",
                "Status": 1,
                "ErrMsg": ""
            }
        ]
    }
}
```

