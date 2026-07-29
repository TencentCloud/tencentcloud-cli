**Example 1: 查询 DB Custom 支持售卖的可用区**



Input: 

```
tccli dbdc DescribeDBCustomZones --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ZoneSet": [
            {
                "Zone": "ap-shanghai-5",
                "ZoneState": "SELL"
            }
        ],
        "RequestId": "ed7daa71-8d68-416d-96a3-e60fb6e357c0"
    }
}
```

