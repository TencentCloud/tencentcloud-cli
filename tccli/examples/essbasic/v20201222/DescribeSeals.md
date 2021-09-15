**Example 1: 查询电子印章**



Input: 

```
tccli essbasic DescribeSeals --cli-unfold-argument  \
    --Caller.ApplicationId c17bdf9c2a7bdcb32611f4d0200fee3d \
    --Caller.SubOrganizationId  \
    --Caller.OperatorId a08c79b56afcd3b64317b33bee00ce12 \
    --SealIds 4fecde8c3137d320e8a3c8136bdbb7e5 \
    --UserId 
```

Output: 
```
{
    "Response": {
        "RequestId": "s1609901021649919245",
        "Seals": [
            {
                "CreatedOn": 1609901021,
                "Creator": {
                    "ApplicationId": "c17bdf9c2a7bdcb32611f4d0200fee3d",
                    "OperatorId": "9990ccd83a8cf53376c557c538f9e9d3",
                    "SubOrganizationId": ""
                },
                "FileUrl": {
                    "Index": 0,
                    "Option": "{}",
                    "FlowId": "xxx",
                    "Url": "https://dev.file.ess.myqcloud.com/bfile/SEAL/4fecde8c3137d320e8a3c8136bdbb7e5/0/0.PNG?key=B%1A%87%1B%24%F7%D2j%FBw%B0K%3A%BE%B3%06L%CDQ%26S%1BHF%C5%98v%B1%BFf%E3qDp%8AU%BA%04E%CB%F0%DC%CC%11Wd%E0%A8c%AE%24%9F%C2%C3%8F%F18%22%EE%AE%93%A7R%8E%96%94C%AA%5Bs%C1%F6%F7%8F%B0%99Y%AA%06%0A%1F%9DRU%E7%0C%0C%DC%25R%8F%E32u%0F%CD"
                },
                "SealId": "4fecde8c3137d320e8a3c8136bdbb7e5",
                "SealName": "图片base64创建印章",
                "SealSource": "CREATE",
                "SealType": "OFFICIAL",
                "UserId": ""
            }
        ]
    }
}
```

