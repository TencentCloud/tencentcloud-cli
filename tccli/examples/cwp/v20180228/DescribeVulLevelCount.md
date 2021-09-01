**Example 1: 查询漏洞数量按等级分布统计**

查询漏洞数量按等级分布统计

Input: 

```
tccli cwp DescribeVulLevelCount --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "4234234",
        "VulLevelList": [
            {
                "VulLevel": 3,
                "Count": 16
            },
            {
                "VulLevel": 2,
                "Count": 16
            },
            {
                "VulLevel": 1,
                "Count": 4
            },
            {
                "VulLevel": 0,
                "Count": 2
            }
        ]
    }
}
```

