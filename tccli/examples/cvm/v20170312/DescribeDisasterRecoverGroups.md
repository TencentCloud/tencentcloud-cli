**Example 1: 查询分散置放群组信息**

查询分散置放群组信息

Input: 

```
tccli cvm DescribeDisasterRecoverGroups --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "DisasterRecoverGroupSet": [
            {
                "DisasterRecoverGroupId": "ps-21q9ibvr",
                "Name": "数据库业务",
                "Type": "RACK",
                "CvmQuotaTotal": 30,
                "CurrentNum": 0,
                "InstanceIds": [],
                "CreateTime": "2018-04-19T02:47:12Z"
            }
        ],
        "TotalCount": 1,
        "RequestId": "c68ce193-be41-4d13-9a9b-2dc031db6477"
    }
}
```

