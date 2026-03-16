**Example 1: DescribeAIMCredentials**

DescribeAIMCredentials

Input: 

```
tccli apis DescribeAIMCredentials --cli-unfold-argument  \
    --Limit 10 \
    --InstanceID ins-a7af1980 \
    --Offset 0 \
    --Keyword teststs \
    --IDs crd-3077f964 \
    --Type sts \
    --Tags testtag
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "AppID": 1300273807,
                    "CreateTime": "2026-03-16T05:32:00.134Z",
                    "ID": "crd-3077f964",
                    "InstanceID": "ins-a7af1980",
                    "LastUpdateTime": "2026-03-16T05:32:00.134Z",
                    "Name": "teststs",
                    "Type": "sts",
                    "Uin": "700001136234"
                }
            ],
            "Total": 1
        },
        "RequestId": "cd166fe2-4a2c-434c-9f35-481821b58ea7"
    }
}
```

