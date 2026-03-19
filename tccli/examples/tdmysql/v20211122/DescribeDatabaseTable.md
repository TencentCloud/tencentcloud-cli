**Example 1: 1**



Input: 

```
tccli tdmysql DescribeDatabaseTable --cli-unfold-argument  \
    --InstanceId tdsql3-01d1c3ed \
    --Table user \
    --DbName my-db
```

Output: 
```
{
    "Response": {
        "Cols": [
            {
                "Col": "Host",
                "Type": "char(60)"
            }
        ],
        "DbName": "mysql",
        "InstanceId": "tdsql3-01d1c3ed",
        "RequestId": "d70d9f4e-80d8-459f-8771-73e87bd553c1",
        "Table": "user"
    }
}
```

**Example 2: 11**



Input: 

```
tccli tdmysql DescribeDatabaseTable --cli-unfold-argument  \
    --InstanceId tdsql3-2123sasd \
    --Table dasf \
    --DbName adsf
```

Output: 
```
{
    "Response": {
        "Cols": null,
        "DbName": "",
        "InstanceId": "",
        "RequestId": "5cdd7082-d8b9-4e4c-87ea-aabe45c91b3e",
        "Table": ""
    }
}
```

