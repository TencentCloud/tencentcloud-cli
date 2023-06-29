**Example 1: 示例1**

新购订单发货中

Input: 

```
tccli keewidb DescribeInstanceDealDetail --cli-unfold-argument  \
    --DealIds 138172054
```

Output: 
```
{
    "Response": {
        "DealDetails": [
            {
                "CreatTime": "2023-03-13 11:28:10",
                "Creater": "100xxxxxxxxx",
                "DealId": "138172054",
                "DealName": "20230313xxxxxxxxxxxxxxx",
                "Description": "发货中",
                "EndTime": "",
                "GoodsNum": 1,
                "InstanceIds": [
                    "kee-w7xxxxxx"
                ],
                "OverdueTime": "2023-03-28 11:28:09",
                "Price": 0,
                "Status": 3,
                "ZoneId": 100006
            }
        ],
        "RequestId": "b835a553-b98c-49bd-be22-e3e1ce465438"
    }
}
```

