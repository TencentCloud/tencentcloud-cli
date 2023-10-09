**Example 1: 获取主机安全相关统计**



Input: 

```
tccli cwp DescribeScreenGeneralStat --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Protection": [
            {
                "Name": "xx",
                "Value": 1
            }
        ],
        "RequestId": "xx",
        "Machines": [
            {
                "Name": "xx",
                "Value": 1
            }
        ]
    }
}
```

