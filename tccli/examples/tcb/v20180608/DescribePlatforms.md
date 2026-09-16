**Example 1: 查询指定平台版资源信息**



Input: 

```
tccli tcb DescribePlatforms --cli-unfold-argument  \
    --PlatformIds pf-2v4plhx1ph2bq
```

Output: 
```
{
    "Response": {
        "PlatformList": [
            {
                "Alias": "",
                "BillStatus": "normal",
                "BillTime": "2026-09-08 21:26:03",
                "ExpireTime": "2026-10-08 23:59:59",
                "IsAutoRenew": 0,
                "PackageId": "default",
                "PlatformId": "pf-2v4plhx1ph2bq",
                "Region": "ap-shanghai",
                "Resources": [
                    {
                        "Detail": "{\"Bucket\":\"b5c5-static-pf-2v4plhx1ph2bq-1258467748\",\"PolicyId\":285688480,\"Region\":\"ap-shanghai\"}",
                        "Id": 84,
                        "PlatformId": 30,
                        "ResName": "b5c5-static-pf-2v4plhx1ph2bq-1258467748",
                        "ResType": "hosting",
                        "Status": 0
                    }
                ],
                "Spec": "{\"credits\":6000,\"envNum\":60}",
                "Status": 0
            }
        ],
        "Total": 1,
        "RequestId": "db08ab1f-fa4b-4c52-bc4d-09149ac24d40"
    }
}
```

