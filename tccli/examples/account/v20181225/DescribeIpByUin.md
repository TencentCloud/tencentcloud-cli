**Example 1: 示例**



Input: 

```
tccli account DescribeIpByUin --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --AccountIdList 123445
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "IP": "0.0.0.0",
                "Time": "2020-12-12 12:00:00",
                "Type": "login",
                "Uin": 1234455
            }
        ],
        "Total": 1,
        "RequestId": "088b49b1-ea91-4d33-8cd0-43a73ccb602f"
    }
}
```

