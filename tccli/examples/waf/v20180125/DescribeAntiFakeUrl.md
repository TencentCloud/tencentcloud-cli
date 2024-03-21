**Example 1: 获取防篡改url**



Input: 

```
tccli waf DescribeAntiFakeUrl --cli-unfold-argument  \
    --Domain www.test.com \
    --PageInfo.PageNumber 0 \
    --PageInfo.PageSize 10
```

Output: 
```
{
    "Response": {
        "List": [],
        "RequestId": "08e8410d-6e80-4d1f-89ff-62669042369d",
        "Total": "0"
    }
}
```

**Example 2: 获取配置的防篡改策略--有数据返回场景**



Input: 

```
tccli waf DescribeAntiFakeUrl --cli-unfold-argument  \
    --Domain www.test.com \
    --PageInfo.PageNumber 0 \
    --PageInfo.PageSize 10
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Domain": "www.test1.com",
                "Id": "135",
                "Name": "test",
                "Protocol": "http",
                "Status": "1",
                "Uri": "http://www.test1.com/a1.html"
            }
        ],
        "RequestId": "0f0d7ca8-2ece-48af-886c-7ef178b5940a",
        "Total": "1"
    }
}
```

