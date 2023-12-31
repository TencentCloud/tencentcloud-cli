**Example 1: QueryUser**



Input: 

```
tccli taop QueryUser --cli-unfold-argument  \
    --Req.Page.CurPage 1 \
    --Req.Page.PageSize 100
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Id": "391825450327883776",
                "Name": "100000558876",
                "PlatName": "",
                "SubAccountUin": "100000558876",
                "Position": "医生",
                "Department": "外科",
                "Mobile": "13838373776",
                "Role": 2,
                "CreateTime": "2021-06-24T14:48:30Z"
            }
        ],
        "RequestId": "2a253a69-c941-483f-be7e-6e476d324e3b"
    }
}
```

