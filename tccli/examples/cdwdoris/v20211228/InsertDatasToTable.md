**Example 1: 插入**



Input: 

```
tccli cdwdoris InsertDatasToTable --cli-unfold-argument  \
    --InstanceId cdwdoris-xx \
    --Database demo1 \
    --Table my_table \
    --CatalogName internal \
    --Columns id name age salary join_date \
    --Rows.0.DataRow 11 'John Doe' 30 7000.50 2024-08-27 \
    --Rows.1.DataRow 21 'Jane Smith' 25 6000.00 2024-08-28 \
    --Types BIGINT VARCHAR(50) INT DECIMAL(10,2) DATE
```

Output: 
```
{
    "Response": {
        "Success": true,
        "Message": "Data inserted successfully.",
        "InsertCount": 2,
        "RequestId": "6b10033a-97da-4171-b40c-xx"
    }
}
```

