**Example 1: 查询DLC Catalog授权列表**

查询DLC Catalog授权列表

Input: 

```
tccli dlc DescribeDLCCatalogAccess --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 20,
        "Rows": [
            {
                "VpcId": "vpc-12345",
                "Product": "EMR",
                "Description": "EMR生产集群",
                "CreateTime": "2024年10月01日"
            }
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

