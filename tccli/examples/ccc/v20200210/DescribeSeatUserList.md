**Example 1: 获取坐席用户列表示例**



Input: 

```
tccli ccc DescribeSeatUserList --cli-unfold-argument  \
    --InstanceId 11 \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "RequestId": "6bb56a09-2787-40bc-80c5-dc6dab783eff",
        "TotalCount": 30,
        "SeatUsers": [
            {
                "Name": "张三",
                "Mail": "zhangsan@qq.com",
                "Phone": "12345678901",
                "Nick": "张三"
            },
            {
                "Name": "李四",
                "Mail": "lisi@qq.com",
                "Phone": "12345678902",
                "Nick": "李四"
            },
            {
                "Name": "王五",
                "Mail": "wangwu@qq.com",
                "Phone": "12345678903",
                "Nick": "王五"
            }
        ]
    }
}
```

