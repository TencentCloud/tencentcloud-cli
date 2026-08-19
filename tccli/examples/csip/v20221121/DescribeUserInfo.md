**Example 1: 获取用户版本和配额信息**



Input: 

```
tccli csip DescribeUserInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "UserInfo": {
            "AccountType": 0,
            "AppID": 260095525,
            "CostQuota": 3,
            "PayType": 2,
            "Providers": [
                "te***nt"
            ],
            "TotalQuota": 16000
        },
        "RequestId": "16e725ad-6742-4216-bf74-b4f04d175c66"
    }
}
```

