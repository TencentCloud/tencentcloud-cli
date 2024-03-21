**Example 1: 查询用户所有地域实例概览。**

查询所有地域的实例概览，包括实例总数，已过期包年包月实例总数，新创建实例总数。

Input: 

```
tccli cvm DescribeInstanceStatistics --cli-unfold-argument ```

Output: 
```
{
    "code": 0,
    "data": {
        "Response": {
            "InstanceStatisticsSet": [
                {
                    "ExpiredInstanceCount": 2,
                    "NewInstanceCount": 0,
                    "Region": "ap-guangzhou",
                    "TotalCount": 131
                },
                "",
                "此处省略部分地域详情",
                "",
                {
                    "ExpiredInstanceCount": 0,
                    "NewInstanceCount": 1,
                    "Region": "ap-shenzhen-fsi",
                    "TotalCount": 6
                }
            ],
            "RequestId": "3385dcf2-e1f0-4ed8-a924-c296721ab65f"
        }
    }
}
```

