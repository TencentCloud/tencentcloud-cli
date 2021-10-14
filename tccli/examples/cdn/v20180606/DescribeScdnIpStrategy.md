**Example 1: 查询SCDN的IP白名单列表**



Input: 

```
tccli cdn DescribeScdnIpStrategy --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "a4ac88a3-a159-47ac-9b87-19185d7deb09",
        "IpStrategyList": [
            {
                "Domain": "www.test.com",
                "StrategyId": 1,
                "IpList": [
                    "1.1.1.1",
                    "2.2.2.2"
                ],
                "UpdateTime": "2020-09-22 15:00:00",
                "Remark": "test"
            }
        ],
        "TotalCount": 1
    }
}
```

