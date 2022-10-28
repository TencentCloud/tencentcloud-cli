**Example 1: 查询代理商指定月份返佣信息**

查询某代理商在2018年2月份的返佣信息

Input: 

```
tccli partners DescribeRebateInfosNew --cli-unfold-argument  \
    --RebateMonth 2018-02
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03",
        "RebateInfoSet": [
            {
                "Uin": "111111",
                "RebateMonth": "2018-02",
                "Amt": 2682133,
                "MonthSales": "4873578",
                "QuarterSales": "10756003",
                "ExceptionFlag": "NORMAL"
            }
        ],
        "TotalCount": "8"
    }
}
```

