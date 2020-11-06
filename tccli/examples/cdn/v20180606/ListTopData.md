**Example 1: 查询Top Url访问数据**



Input: 

```
tccli cdn ListTopData --cli-unfold-argument  \
    --StartTime '2018-09-04 00:00:00' \
    --EndTime '2018-09-04 12:00:00' \
    --Metric Url \
    --Filter flux \
    --Domains www.test.com www.test.com
```

Output: 
```
{
    "Response": {
        "RequestId": "123",
        "Data": [
            {
                "Resource": "www.test1.com",
                "DetailData": [
                    {
                        "Name": "www.test1.com/1.jpg?abc=123",
                        "Value": 13838
                    }
                ]
            },
            {
                "Resource": "www.test2.com",
                "DetailData": [
                    {
                        "Name": "http://www.test2.com/1.jpg?abc=123",
                        "Value": 2501
                    }
                ]
            }
        ]
    }
}
```

