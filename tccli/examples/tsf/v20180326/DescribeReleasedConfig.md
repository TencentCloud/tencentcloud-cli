**Example 1: 查询group发布的配置**



Input: 

```
tccli tsf DescribeReleasedConfig --cli-unfold-argument  \
    --GroupId group-jy9re3gy
```

Output: 
```
{
    "Response": {
        "RequestId": "6ec73c01-a942-4c6c-9630-b25e53745a43",
        "Result": "config: enabled\n"
    }
}
```

