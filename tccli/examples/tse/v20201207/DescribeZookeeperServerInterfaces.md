**Example 1: 查询nacos服务接口列表**

查询nacos服务接口列表

Input: 

```
tccli tse DescribeZookeeperServerInterfaces --cli-unfold-argument  \
    --InstanceId xx \
    --Limit 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "Content": [
            {
                "Interface": "xx"
            }
        ],
        "TotalCount": 1,
        "RequestId": "xx"
    }
}
```

