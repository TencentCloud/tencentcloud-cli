**Example 1: 查询saas和clb域名信息**



Input: 

```
tccli waf DescribeUserDomainInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "b4f13899-561b-46a0-a045-6ba6b72c38f2",
        "UsersInfo": [
            {
                "Appid": 251197211,
                "Domain": "2333.douban.com",
                "DomainId": "45bdad0d-bb98-4cb3-8e5a-ab6e2992",
                "InstanceId": "Swaf_0000001g0",
                "InstanceName": "",
                "Edition": "",
                "Level": "1",
                "WriteConfig": "{\"EnableHeaders\": 1,\"EnableBody\": 1}",
                "Cls": 0,
                "CloudType": ""
            },
            {
                "Appid": 251197211,
                "Domain": "engine_test_dev2.qcloudwaf.com",
                "DomainId": "205eeb7e-1a5c-4f54-aec9-00c97d49",
                "InstanceId": "abc",
                "InstanceName": "",
                "Edition": "",
                "Level": "4",
                "WriteConfig": "{\"EnableBody\": 0}",
                "Cls": 1,
                "CloudType": ""
            },
            {
                "Appid": 251197211,
                "Domain": "413001.qcloudwaf.com",
                "DomainId": "c6458fdaa4bf5045bf069c2b549b5f08",
                "InstanceId": "yuyuyuyuyu",
                "InstanceName": "ModifyName",
                "Edition": "sparta-waf",
                "Level": "1",
                "WriteConfig": "{\"EnableHeaders\": 1,\"EnableBody\": 1}",
                "Cls": 0,
                "CloudType": ""
            }
        ]
    }
}
```

