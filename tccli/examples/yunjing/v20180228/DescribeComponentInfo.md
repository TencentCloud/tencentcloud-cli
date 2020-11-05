**Example 1: Getting component information**

This example shows you how to get component information.

Input: 

```
tccli yunjing DescribeComponentInfo --cli-unfold-argument  \
    --ComponentId 100010
```

Output: 
```
{
    "Response": {
        "Id": 100010,
        "Description": "description",
        "ComponentName": "Mysql-Server",
        "ComponentType": "WEB",
        "Homepage": "http://example.com",
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

