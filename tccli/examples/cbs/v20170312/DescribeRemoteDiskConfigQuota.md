**Example 1: 查询单副本SSD硬盘机型搭配配额**

按机型族和可用区过滤查询单副本SSD硬盘配额。

Input: 

```
tccli cbs DescribeRemoteDiskConfigQuota --cli-unfold-argument  \
    --Filters.0.Name instance-family \
    --Filters.0.Values S5 \
    --Filters.1.Name zone \
    --Filters.1.Values ap-guangzhou-3
```

Output: 
```
{
    "Response": {
        "RequestId": "a0ed56a0-4b9a-4690-bd5e-7aa76fd67b4d"
    }
}
```

