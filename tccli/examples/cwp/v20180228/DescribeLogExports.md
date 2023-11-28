**Example 1: 示例**



Input: 

```
tccli cwp DescribeLogExports --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Exports": [
            {
                "ExportId": "export-4b905654-7af5-43c1-a111-04c89e029c2a",
                "Query": "*",
                "FileName": "log_100004506473_c5ad674a-e6cc-4d7d-82e0-e7d7edaae26b_20220629_export-4b905654-7af5-43c1-a111-04c89e029c2a_1656466508.tar.gz",
                "FileSize": 97805,
                "Order": "desc",
                "Format": "json",
                "Count": 2240,
                "Status": "Completed",
                "StartTime": 1656464537652,
                "EndTime": 1656466337652,
                "CosPath": "https://export-gz-1254077820.cos.ap-guangzhou.myqcloud.com/%2Fexport/20220629/log_100004506473_c5ad674a-e6cc-4d7d-82e0-e7d7edaae26b_20220629_export-4b905654-7af5-43c1-a111-04c89e029c2a_1656466508.tar.gz?q-sign-algorithm=sha1&q-ak=xxxxxxxxxxxxPBtQlw86tt&q-sign-time=1656639828%3B1656643428&q-key-time=1656639828%3B1656643428&q-header-list=host&q-url-param-list=&q-signature=e491e72e50afa2258",
                "CreateTime": "2022-06-29 09:35:00"
            },
            {
                "ExportId": "export-9a5f89fc-986b-4b5e-a511-168646949685",
                "Query": "*",
                "FileName": "log_100004506473_c5ad674a-e6cc-4d7d-82e0-e7d7edaae26b_20220628_export-9a5f89fc-986b-4b5e-a511-168646949685_1656415208.tar.gz",
                "FileSize": 9815,
                "Order": "desc",
                "Format": "json",
                "Count": 121,
                "Status": "Completed",
                "StartTime": 1656408311641,
                "EndTime": 1656410111641,
                "CosPath": "https://export-gz-1254077820.cos.ap-guangzhou.myqcloud.com/%2Fexport/20220628/log_100004506473_c5ad674a-e6cc-4d7d-82e0-e7d7edaae26b_20220628_export-9a5f89fc-986b-4b5e-a511-168646949685_1656415208.tar.gz?q-sign-algorithm=sha1&q-ak=xxxxxxxxBtQlw86tt&q-sign-time=1656639828%3B1656643428&q-key-time=1656639828%3B1656643428&q-header-list=host&q-url-param-list=&q-signature=b338dbd1685e5ea3f",
                "CreateTime": "2022-06-28 19:19:46"
            }
        ],
        "RequestId": "05db17be-ba35-467f-b903-51f66d2d1def",
        "TotalCount": 2
    }
}
```

