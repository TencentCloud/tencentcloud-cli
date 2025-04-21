**Example 1: null**



Input: 

```
tccli ioa DescribeDeviceTags --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": {
            "DeviceTagList": null
        },
        "RequestId": "a5cff48e-5a0d-4f2c-8a76-ae1c47ebc3bf"
    }
}
```

**Example 2: 测试**

测试

Input: 

```
tccli ioa DescribeDeviceTags --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": {
            "DeviceTagList": [
                {
                    "Id": 1,
                    "TagName": "123456",
                    "UpdateTime": 1725444263
                }
            ]
        },
        "RequestId": "0560fa92-f36e-4c62-b5fc-15a5dc5e3812"
    }
}
```

