**Example 1: 示例**



Input: 

```
tccli dsgc DescribeDSPASupportedMetas --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "c7af630e-81c2-4340-9535-5afa8b8e88b1",
        "Metas": [
            {
                "MetaType": "cdb",
                "Regions": [
                    "ap-chengdu",
                    "ap-guangzhou"
                ],
                "SupportedAuthTypes": [
                    "account",
                    "automatic"
                ]
            },
            {
                "MetaType": "dcdb",
                "Regions": [
                    "ap-guangzhou"
                ],
                "SupportedAuthTypes": [
                    "account",
                    "automatic"
                ]
            },
            {
                "MetaType": "mariadb",
                "Regions": [
                    "ap-guangzhou"
                ],
                "SupportedAuthTypes": [
                    "account",
                    "automatic"
                ]
            },
            {
                "MetaType": "postgres",
                "Regions": [
                    "ap-guangzhou"
                ],
                "SupportedAuthTypes": [
                    "account"
                ]
            },
            {
                "MetaType": "cynosdbmysql",
                "Regions": [
                    "ap-guangzhou"
                ],
                "SupportedAuthTypes": [
                    "account"
                ]
            },
            {
                "MetaType": "cos",
                "Regions": [
                    "ap-guangzhou"
                ],
                "SupportedAuthTypes": null
            },
            {
                "MetaType": "mysql_like_proto",
                "Regions": [
                    "ap-guangzhou"
                ],
                "SupportedAuthTypes": [
                    "account"
                ]
            },
            {
                "MetaType": "postgre_like_proto",
                "Regions": [
                    "ap-guangzhou"
                ],
                "SupportedAuthTypes": [
                    "account"
                ]
            }
        ]
    }
}
```

