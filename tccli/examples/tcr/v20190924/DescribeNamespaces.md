**Example 1: 查询命名空间信息**

查询实例内所有的命名空间信息

Input: 

```
tccli tcr DescribeNamespaces --cli-unfold-argument  \
    --Limit 20 \
    --RegistryId tcr-f7g1ir99 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "NamespaceList": [
            {
                "Public": true,
                "Name": "ns1",
                "CreationTime": "2020-09-22T00:00:00+00:00",
                "NamespaceId": 1,
                "TagSpecification": {
                    "ResourceType": "namespace",
                    "Tags": [
                        {
                            "Value": "tag-value",
                            "Key": "tag-key"
                        }
                    ]
                },
                "Metadata": [
                    {
                        "Key": "prevent_vul",
                        "Value": "false"
                    }
                ],
                "CVEWhitelistItems": [
                    {
                        "CVEID": "1"
                    }
                ],
                "AutoScan": true,
                "PreventVUL": true,
                "Severity": "low"
            }
        ],
        "TotalCount": 2,
        "RequestId": "866bda78-ed75-4b10-8876-e82de555f69b"
    }
}
```

