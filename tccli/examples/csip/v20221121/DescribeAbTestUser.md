**Example 1: 判断用户是否灰度用户**

功能模块灰度

Input: 

```
tccli csip DescribeAbTestUser --cli-unfold-argument  \
    --ProjectName csip_xspm \
    --UserAppIds 17837821
```

Output: 
```
{
    "Response": {
        "AbTestUserList": [
            {
                "AppId": 1234343,
                "IsAbTestUser": false
            }
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

