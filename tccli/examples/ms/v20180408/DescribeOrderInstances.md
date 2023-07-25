**Example 1: 根据订单id查订单资源信息**

根据订单id查订单资源信息

Input: 

```
tccli ms DescribeOrderInstances --cli-unfold-argument  \
    --OrderId 20230602_03702020-0a90-4f46-8f20-XXXXXXXXX
```

Output: 
```
{
    "Response": {
        "Orders": [
            {
                "AppPkgName": "",
                "ApprovalStatus": 1,
                "ApprovalStatusDesc": "审批通过",
                "ApprovalTime": "2023-06-02 17:51:55",
                "Approver": "xxxxxx",
                "CreateTime": "2023-06-02 17:42:06",
                "ExpireTime": "0000-00-00 00:00:00",
                "OrderId": "20230602_03702020-0a90-4f46-8f20-XXXXXXXXX",
                "OrderType": 3,
                "OrderTypeDesc": "按次收费",
                "PlatformType": 1,
                "PlatformTypeDesc": "android安卓加固",
                "ResourceId": "20230602_03702020-0a90-4f46-8f20-XXXXXXXXX_0",
                "ResourceStatus": 1,
                "ResourceStatusDesc": "生效中",
                "TestTimes": 0,
                "TimesTaskFailCount": 6,
                "TimesTaskSuccessCount": 2,
                "TimesTaskTotalCount": 8,
                "ValidTime": "0000-00-00 00:00:00"
            }
        ],
        "RequestId": "c3af1139-4146-4a17-a4f7-395933351a5f",
        "TotalCount": 1
    }
}
```

