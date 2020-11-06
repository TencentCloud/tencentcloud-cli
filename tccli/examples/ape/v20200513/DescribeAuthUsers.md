**Example 1: 查询授权人列表**



Input: 

```
tccli ape DescribeAuthUsers --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "s1589773775497713697",
        "TotalCount": 2,
        "OldUser": false,
        "Users": [
            {
                "Code": "1111",
                "CreateTime": "2020-05-18 11:33:36",
                "Id": "apur-m3tcpxw1",
                "Name": "测试",
                "Type": 1
            }
        ]
    }
}
```

