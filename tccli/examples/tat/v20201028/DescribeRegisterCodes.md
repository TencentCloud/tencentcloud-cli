**Example 1: 根据注册码ID查询注册码**

根据注册码ID查询注册码。

Input: 

```
tccli tat DescribeRegisterCodes --cli-unfold-argument  \
    --RegisterCodeIds 8cca2d3b-7ac3-422a-98f0-8a5bc17cdc38 \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "RegisterCodeSet": [
            {
                "CreatedTime": "2024-10-26T08:50:45Z",
                "Description": "HAI instance register code, attach hai-8sclmptu",
                "Enabled": false,
                "ExpiredTime": "2024-10-26T12:50:45Z",
                "InstanceNamePrefix": "HAI-Instance-hai-8sclmptu",
                "IpAddressRange": "",
                "RegisterCodeId": "8cca2d3b-7ac3-422a-98f0-8a5bc17cdc38",
                "RegisterLimit": 10,
                "RegisteredCount": 1,
                "UpdatedTime": "2024-10-26T08:50:45Z"
            }
        ],
        "RequestId": "e0f011ac-6949-4726-a7d6-b28540f9d729",
        "TotalCount": 1
    }
}
```

