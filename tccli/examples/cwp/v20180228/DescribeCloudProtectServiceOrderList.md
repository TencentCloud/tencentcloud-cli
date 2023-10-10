**Example 1: 查询云护航服务订单列表**

查询云护航服务订单列表

Input: 

```
tccli cwp DescribeCloudProtectServiceOrderList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "67d7cb74-8055-7704-1610-29786d95e2b1",
        "Data": [
            {
                "ServiceName": "巡检服务",
                "Type": "新购",
                "Config": "巡检服务: 1次",
                "BeginTime": "2022-12-31 00:00:00",
                "ResourceId": "cwpinsp-xxxxxxxx"
            }
        ]
    }
}
```

