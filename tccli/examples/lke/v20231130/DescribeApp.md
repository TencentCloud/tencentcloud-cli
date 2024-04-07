**Example 1: DescribeApp**

获取企业下应用详情

Input: 

```
tccli lke DescribeApp --cli-unfold-argument  \
    --AppBizId 45454545464646 \
    --AppType knowledge_qa
```

Output: 
```
{
    "Response": {
        "AppBizId": "45454545464646",
        "AppType": "knowledge_qa",
        "BaseConfig": {
            "Name": "应用",
            "Avatar": "头像",
            "Desc": "应用描述"
        },
        "AppKey": "app_key",
        "RequestId": "dwec-adsdsdsd-sfsfdsfsf"
    }
}
```

