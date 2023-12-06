**Example 1: 入侵防御规则白名单查询示例**

入侵防御规则白名单查询示例

Input: 

```
tccli cfw DescribeIdsWhiteRule --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "88db276f-42d5-4b60-afc1-2c5799250a99",
        "ReturnCode": 0,
        "ReturnMsg": "success",
        "Total": 1
    }
}
```

