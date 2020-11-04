**Example 1: 获取用户单个模块配额示例**



Input: 

```
tccli gse DescribeUserQuota --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "QuotaResource": {
            "ExtraInfo": "",
            "HardLimit": 20,
            "Remaining": 10,
            "ResourceType": 1
        },
        "RequestId": "s1585794616012158675"
    }
}
```

