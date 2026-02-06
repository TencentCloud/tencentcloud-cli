**Example 1: 成功调用**



Input: 

```
tccli wedata DescribeDataSourceAuthority --cli-unfold-argument  \
    --Id 65388
```

Output: 
```
{
    "Response": {
        "Data": {
            "AuthProjectIds": null,
            "AuthUsers": [
                "3057820876712648704_700002172673",
                "3057820876712648704_700002050586",
                "3057820876712648704_700002259781",
                "3057820876712648704_700002130525"
            ]
        },
        "RequestId": "046b8bfb-d3fb-44af-b183-87f10d9388cd"
    }
}
```

