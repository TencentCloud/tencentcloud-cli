**Example 1: 查询指定资源**



Input: 

```
tccli cls DescribeResourceGraphEntityDetail --cli-unfold-argument  \
    --EntityId 002b693f4f8cd075e2c6a750e6e58e2c \
    --ResourceGraphId test-yunapi-full \
    --FromTime 1782230000 \
    --ToTime 1782231000
```

Output: 
```
{
    "Response": {
        "RequestId": "21b0ace2-808f-486d-ab90-cf8b5aeb3fcf"
    }
}
```

**Example 2: 查询无数据**



Input: 

```
tccli cls DescribeResourceGraphEntityDetail --cli-unfold-argument  \
    --EntityId 7eca728abe2e4dacc8c687dfaca3d743 \
    --ResourceGraphId test-yunapi-full \
    --FromTime 1782230000 \
    --ToTime 1782231000
```

Output: 
```
{
    "Response": {
        "RequestId": "b2e18bb2-cac6-44e0-b40e-41d61e07ae8d"
    }
}
```

