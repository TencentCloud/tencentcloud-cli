**Example 1: 请求示例**

查询指定实例的热 Key信息

Input: 

```
tccli redis DescribeInstanceMonitorHotKey --cli-unfold-argument  \
    --InstanceId crs-r34w**** \
    --SpanType 4
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Key": "hello",
                "Type": "string",
                "Count": 110
            }
        ],
        "RequestId": "20d64b80-cbac-49a0-8771-42e326db5c45"
    }
}
```

