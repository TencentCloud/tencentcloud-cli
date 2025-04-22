**Example 1: 获取cIntlInfo表信息**

同步账号数据binlog时，cIntlInfo表数据乱码，新增接口解决问题

Input: 

```
tccli tencentcloudintl GetIntlInfo --cli-unfold-argument  \
    --AccountUin 100001308635
```

Output: 
```
{
    "Response": {
        "Address": "广东省深圳市",
        "City": "深圳市",
        "CompanyName": "长木集团",
        "FullName": "长木集团",
        "RequestId": "asdf",
        "State": "南山区",
        "Uin": "100001308635",
        "UpdateTime": "2023-12-08 17:25:46",
        "UserType": "2"
    }
}
```

