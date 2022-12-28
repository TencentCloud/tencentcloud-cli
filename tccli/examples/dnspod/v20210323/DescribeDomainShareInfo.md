**Example 1: 获取域名共享信息**

 

Input: 

```
tccli dnspod DescribeDomainShareInfo --cli-unfold-argument  \
    --Domain dnspod.com
```

Output: 
```
{
    "Response": {
        "RequestId": "ab4f1426-ea15-42ea-8183-dc1b44151166",
        "ShareList": [
            {
                "ShareTo": "qcloud_uin_100000014227@qcloud.com",
                "Mode": "r",
                "Status": "enabled"
            }
        ],
        "Owner": "qcloud_uin_100000014226@qcloud.com"
    }
}
```

