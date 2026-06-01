**Example 1: 测试示例**

测试示例

Input: 

```
tccli tchousex DescribeDatabaseList --cli-unfold-argument  \
    --InstanceId warehouse-vgh8kk6k \
    --ExtParameters.0.Name VirtualCluster \
    --ExtParameters.0.Value jimmyzwang \
    --ExtParameters.1.Name UserName \
    --ExtParameters.1.Value root \
    --ExtParameters.2.Name Password \
    --ExtParameters.2.Value Wanghaoran1993 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Databases": [
            {
                "Description": "",
                "ExtParameters": null,
                "Name": "_impala_builtins"
            },
            {
                "Description": "",
                "ExtParameters": null,
                "Name": "default"
            },
            {
                "Description": "",
                "ExtParameters": null,
                "Name": "information_schema"
            },
            {
                "Description": "",
                "ExtParameters": null,
                "Name": "jimmy"
            },
            {
                "Description": "",
                "ExtParameters": null,
                "Name": "mysql"
            },
            {
                "Description": "",
                "ExtParameters": null,
                "Name": "system"
            },
            {
                "Description": "",
                "ExtParameters": null,
                "Name": "test"
            }
        ],
        "RequestId": "c4e0a1e9-8692-44a6-a84d-80679df85380",
        "TotalCount": 7
    }
}
```

