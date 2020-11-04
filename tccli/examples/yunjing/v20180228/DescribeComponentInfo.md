**Example 1: 获取组件信息数据**

获取组件信息数据

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

