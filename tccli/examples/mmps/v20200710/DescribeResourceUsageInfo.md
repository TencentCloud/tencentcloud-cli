**Example 1: 查询安全资源使用情况**

查询当前用户的安全资源使用情况

Input: 

```
tccli mmps DescribeResourceUsageInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "5e93a212-ca01-0fdc-eedd-5a1fce5e83e6",
        "Ret": 0,
        "Data": [
            {
                "ResourceName": "sv_mps_detection_public_basic",
                "Total": 10,
                "UnusedCount": 5
            }
        ],
        "Total": 1
    }
}
```

