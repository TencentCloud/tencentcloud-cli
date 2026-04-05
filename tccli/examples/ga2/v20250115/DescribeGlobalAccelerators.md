**Example 1: 查询全球加速实例**



Input: 

```
tccli ga2 DescribeGlobalAccelerators --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "GlobalAcceleratorSet": [
            {
                "CreateTime": "2025-02-26 19:51:26",
                "DdosId": "",
                "Description": "zemin_test",
                "GlobalAcceleratorId": "ga-00000kf6",
                "InstanceChargeType": "POSTPAY",
                "Name": "zemin_test",
                "State": "CREATING",
                "Status": "ACTIVE",
                "ListenerCounts": 1,
                "AcceleratorAreaCounts": 2,
                "Cname": "cname"
            }
        ],
        "RequestId": "5a99afb5-277f-4400-a8ed-eb586e946a20",
        "TotalCount": 1
    }
}
```

