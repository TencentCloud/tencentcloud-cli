**Example 1: 查询nacos服务接口列表**

查询nacos服务接口列表

Input: 

```
tccli tse DescribeNacosServerInterfaces --cli-unfold-argument  \
    --InstanceId ins-123456 \
    --Limit 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Content": [
            {
                "Interface": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

