**Example 1: 获取目标组列表**

获取目标组列表

Input: 

```
tccli clb DescribeTargetGroupList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "TargetGroupSet": [
            {
                "TargetGroupId": "lbtg-pcsv4t9o",
                "VpcId": "vpc-i1cnjuhx",
                "TargetGroupName": "czh_vpc0",
                "Port": 443,
                "CreatedTime": "2019-07-30 16:04:22",
                "UpdatedTime": "2019-07-30 16:04:22",
                "AssociatedRule": null
            },
            {
                "TargetGroupId": "lbtg-5xunivs0",
                "VpcId": "vpc-i1cnjuhx",
                "TargetGroupName": "kkkkk",
                "Port": 19999,
                "CreatedTime": "2019-07-14 16:18:43",
                "UpdatedTime": "2019-07-29 11:37:10",
                "AssociatedRule": null
            }
        ],
        "RequestId": "ed30f949-2bea-48a6-8ba0-7f2f33743d4d"
    }
}
```

