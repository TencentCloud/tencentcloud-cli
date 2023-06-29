**Example 1: 企业名称智能匹配示例代码**



Input: 

```
tccli ep SearchEnterprise --cli-unfold-argument  \
    --Name 腾讯 \
    --Limit 5
```

Output: 
```
{
    "Response": {
        "RequestId": "7151cd8f-0cd7-43ca-9c60-062ad0da4dcf",
        "Data": [
            {
                "Name": "深圳市腾讯计算机系统有限公司",
                "SearchName": "深圳市腾讯计算机系统有限公司",
                "SearchNameType": "admin"
            },
            {
                "Name": "深圳市腾讯网域计算机网络有限公司",
                "SearchName": "深圳市腾讯网域计算机网络有限公司",
                "SearchNameType": "admin"
            },
            {
                "Name": "广州市腾讯计算机系统有限公司",
                "SearchName": "广州市腾讯计算机系统有限公司",
                "SearchNameType": "admin"
            }
        ],
        "TotalCount": 35
    }
}
```

