**Example 1: 配置实例访问时间窗**

修改实例的维护时间窗为03:00-06:00

Input: 

```
tccli redis DescribeMaintenanceWindow --cli-unfold-argument  \
    --InstanceId crs-5a4p****
```

Output: 
```
{
    "Response": {
        "StartTime": "03:00",
        "EndTime": "06:00",
        "RequestId": "0e728fa9-c2e5-4bf8-8d6b-c1c4fab7b6db"
    }
}
```

