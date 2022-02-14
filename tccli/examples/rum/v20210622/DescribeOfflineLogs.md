**Example 1: 获取 rum 离线日志**



Input: 

```
tccli rum DescribeOfflineLogs --cli-unfold-argument  \
    --ProjectKey 'a46hv4vGFds576' \
    --FileIDs '958033435' '958033436'
```

Output: 
```
{
    "Response": {
        "Msg": "success",
        "LogSet": [],
        "RequestId": "65a8fec7-2b39-4b11-893f-3715279d235f"
    }
}
```

