**Example 1: 查看供应链**

查看供应链

Input: 

```
tccli ctem DescribeSupplyChains --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "DownloadLink": "",
        "List": [
            {
                "Content": "",
                "DisplayToolCommon": {
                    "CreateAt": "2024-06-06 19:17:14",
                    "CustomerId": 100081,
                    "CustomerName": "5555",
                    "Detail": "",
                    "EnterpriseName": "",
                    "EnterpriseUid": "",
                    "Ignored": false,
                    "IsDeleted": false,
                    "IsNew": true,
                    "JobId": 0,
                    "JobRecordId": 0,
                    "JobStageId": 0,
                    "Md5": "f124cf8eb8277cdb9ad3e32ac3e9c025",
                    "UpdateAt": "2024-06-06 19:17:14"
                },
                "Id": 3227,
                "Purchaser": "购买方",
                "Source": "test.com",
                "Supplier": "测试企业"
            }
        ],
        "RequestId": "8f9ae785-e501-411a-8cb1-db5205a4b91d",
        "Total": 1
    }
}
```

