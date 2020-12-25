**Example 1: 获取用户互联网公网地址分配统计信息**



Input: 

```
tccli dc DescribeInternetAddressStatistics --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "InternetAddressStatistics": [
            {
                "Region": "gz",
                "SubnetNum": 1
            }
        ],
        "RequestId": "aac03e7b-3c91-4970-b2bc-c20f0c6bdd38"
    }
}
```

