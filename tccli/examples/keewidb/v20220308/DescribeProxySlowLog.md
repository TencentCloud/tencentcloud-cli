**Example 1: 示例1**



Input: 

```
tccli keewidb DescribeProxySlowLog --cli-unfold-argument  \
    --InstanceId kee-9clk**** \
    --Offset 0 \
    --Limit 100 \
    --BeginTime 2022-03-10 13:22:03 \
    --MinQueryTime 500 \
    --EndTime 2022-03-10 14:22:03
```

Output: 
```
{
    "Response": {
        "InstanceProxySlowLogDetail": [],
        "RequestId": "1bf55864-c4f1-48de-a6fd-b43f756e32f4",
        "TotalCount": 0
    }
}
```

