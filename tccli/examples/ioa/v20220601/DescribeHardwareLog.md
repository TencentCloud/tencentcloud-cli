**Example 1: 测试**

测试

Input: 

```
tccli ioa DescribeHardwareLog --cli-unfold-argument  \
    --Mid 75129D715480905B6A9C4569893C7634663C2D68 \
    --Dump False \
    --OsType 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "DownUrl": "",
            "List": [],
            "Paging": {
                "PageCount": 0,
                "PageNum": 1,
                "PageSize": 1000,
                "Total": 0
            }
        },
        "RequestId": "fb453203-3212-42d6-a443-4740185994bc"
    }
}
```

