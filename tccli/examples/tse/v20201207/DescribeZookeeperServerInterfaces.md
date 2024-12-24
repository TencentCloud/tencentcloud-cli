**Example 1: 查询nacos服务接口列表**

查询nacos服务接口列表

Input: 

```
tccli tse DescribeZookeeperServerInterfaces --cli-unfold-argument  \
    --InstanceId abc \
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
                "Interface": "addWatch"
            }
        ],
        "RequestId": "req-id"
    }
}
```

