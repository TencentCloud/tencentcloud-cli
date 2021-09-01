**Example 1: 获取动线轨迹信息**



Input: 

```
tccli youmall DescribeTrajectoryData --cli-unfold-argument  \
    --CompanyId testCompany1 \
    --ShopId 1 \
    --Limit 10 \
    --Gender 0 \
    --StartDate 2016-10-10 \
    --EndDate 2017-06-01
```

Output: 
```
{
    "Response": {
        "Data": [],
        "CompanyId": "tencent",
        "ShopId": 12345,
        "TotalPerson": 0,
        "TotalTrajectory": 0,
        "Person": 0,
        "Trajectory": 0,
        "RequestId": "7494e219-3387-451b-bd48-6de7a5baf92f"
    }
}
```

