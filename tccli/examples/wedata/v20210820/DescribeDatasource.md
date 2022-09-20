**Example 1: 样例**



Input: 

```
tccli wedata DescribeDatasource --cli-unfold-argument  \
    --Id 1
```

Output: 
```
{
    "Response": {
        "RequestId": "123",
        "Data": {
            "BizParams": "string",
            "Category": "DB",
            "DatabaseName": "string",
            "Description": "string",
            "Display": "string",
            "Name": "string",
            "Params": "string",
            "Status": 1,
            "ID": 1,
            "Type": "CLICKHOUSE",
            "AppId": 1,
            "Region": "string"
        }
    }
}
```

