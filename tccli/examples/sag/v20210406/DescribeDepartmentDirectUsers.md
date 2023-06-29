**Example 1: 获取部门直属用户**



Input: 

```
tccli sag DescribeDepartmentDirectUsers --cli-unfold-argument  \
    --DepartmentId 1
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Id": "1",
                "Name": "张三"
            }
        ],
        "RequestId": "xxx"
    }
}
```

