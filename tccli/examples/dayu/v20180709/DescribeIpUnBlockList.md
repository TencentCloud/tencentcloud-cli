**Example 1: 获取IP解封记录**



Input: 

```
tccli dayu DescribeIpUnBlockList --cli-unfold-argument  \
    --BeginTime 2018-09-0111:59:46 \
    --EndTime 2018-09-1011:59:46 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "BeginTime": "2018-09-01 11:59:46",
        "EndTime": "2018-09-10 11:59:46",
        "List": [
            {
                "Ip": "111.230.156.235",
                "BlockTime": "2018-09-07 17:12:10",
                "UnBlockTime": "2018-09-07 17:36:41",
                "ActionType": "user"
            }
        ],
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "Total": 1
    }
}
```

