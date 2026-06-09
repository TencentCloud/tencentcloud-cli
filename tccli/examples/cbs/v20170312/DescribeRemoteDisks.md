**Example 1: 按条件查询单副本SSD硬盘列表**

按可用区和状态过滤查询单副本SSD硬盘。

Input: 

```
tccli cbs DescribeRemoteDisks --cli-unfold-argument  \
    --Filters.0.Name zone \
    --Filters.0.Values ap-guangzhou-2 \
    --Filters.1.Name remote-disk-state \
    --Filters.1.Values ATTACHED
```

Output: 
```
{
    "Response": {
        "RequestId": "a0ed56a0-4b9a-4690-bd5e-7aa76fd67b4d"
    }
}
```

**Example 2: 查询单副本SSD硬盘列表**



Input: 

```
tccli cbs DescribeRemoteDisks --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "a0ed56a0-4b9a-4690-bd5e-7aa76fd67b4d"
    }
}
```

