**Example 1: 命令检索**

命令检索

Input: 

```
tccli bh SearchSessionCommand --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --Cmd pwd \
    --StartTime 2020-01-01T01:01:01+08:00 \
    --EndTime 2020-01-01T01:01:01+08:00
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "27d70f6b-3732-4698-a00f-ee91d3a1fb31"
    }
}
```

