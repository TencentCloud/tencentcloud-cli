**Example 1: 查询命名空间信息**

查询实例内所有的命名空间信息

Input: 

```
tccli tcr DescribeInstanceAllNamespaces --cli-unfold-argument  \
    --Limit 5 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "ResourceId": "tcr-csexdur7/finofliu"
            },
            {
                "ResourceId": "tcr-csexdur7/ns2"
            },
            {
                "ResourceId": "tcr-csexdur7/chart"
            },
            {
                "ResourceId": "tcr-csexdur7/uptime"
            },
            {
                "ResourceId": "tcr-csexdur7/futu"
            }
        ],
        "RequestId": "5df0c1f1-6981-4faa-852c-403bd8ef0ef8",
        "TotalCount": 25
    }
}
```

