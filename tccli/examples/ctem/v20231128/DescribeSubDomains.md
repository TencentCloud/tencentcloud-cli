**Example 1: 查看子域名数据**

查看子域名数据

Input: 

```
tccli ctem DescribeSubDomains --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "City": "深圳",
                "Country": "中国",
                "DisplayToolCommon": {
                    "CreateAt": "2024-06-06 15:59:09",
                    "CustomerId": 100081,
                    "CustomerName": "5555",
                    "Detail": "",
                    "EnterpriseName": "",
                    "EnterpriseUid": "",
                    "Ignored": false,
                    "JobId": 0,
                    "JobRecordId": 0,
                    "JobStageId": 0,
                    "Md5": "679e65f8583a8a88f5c9e1d6a1e76259",
                    "UpdateAt": "2024-06-06 15:59:09"
                },
                "Id": 63660,
                "Ip": "1.1.1.1",
                "Isp": "电信",
                "Province": "广东",
                "SubDomain": "test.qq.com"
            }
        ],
        "RequestId": "452e1e8f-fb05-45af-b2b0-67d0f211e30c",
        "Total": 1
    }
}
```

