**Example 1: 请求示例**



Input: 

```
tccli redis DescribeInstanceBackups --cli-unfold-argument  \
    --Limit 5 \
    --Offset 0 \
    --InstanceId crs-5a4py64p
```

Output: 
```
{
    "Response": {
        "RequestId": "2d4387ee-2011-449e-a32b-87f9366f3ef4",
        "TotalCount": 2
    }
}
```

