**Example 1: 查询资产组列表**



Input: 

```
tccli dasb DescribeDeviceGroups --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "GroupSet": [
            {
                "Department": {
                    "Managers": [
                        "152017428"
                    ],
                    "Id": "1.2.3.4",
                    "Name": "研发部"
                },
                "Id": 1,
                "Name": "运维组"
            }
        ],
        "RequestId": "cf109eee-b651-4313-9b49-073a9f55732f"
    }
}
```

