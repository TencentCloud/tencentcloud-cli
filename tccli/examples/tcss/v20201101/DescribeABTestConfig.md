**Example 1: 获取用户当前灰度配置**



Input: 

```
tccli tcss DescribeABTestConfig --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Config": [
            {
                "ProjectName": "tcss_pro",
                "Status": true
            },
            {
                "ProjectName": "ban_switch",
                "Status": true
            },
            {
                "ProjectName": "v20200715",
                "Status": true
            }
        ],
        "RequestId": "8fa9bf5e-a0dc-d89d-9ece-d68c2232a4c6"
    }
}
```

