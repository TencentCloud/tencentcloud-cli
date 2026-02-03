**Example 1: DescribeCloudBaseGWAPI示例**



Input: 

```
tccli tcb DescribeCloudBaseGWAPI --cli-unfold-argument  \
    --ServiceId "roy-test-666"
```

Output: 
```
{
    "Response": {
        "APISet": [
            {
                "ServiceId": "roy-test-666",
                "IsShortPath": false,
                "APIId": "3171368e-e641-4788-bd0e-e856aa713995",
                "Path": "/lowcode-datasource",
                "Type": 1,
                "Name": "lowcode-datasource",
                "CreateTime": 1741184090,
                "EnvId": "roy-test-666",
                "EnableAuth": false,
                "Custom": "",
                "AccessType": 13,
                "Domain": "*",
                "UnionStatus": 1,
                "ConflictFlag": false,
                "DomainStatus": 0,
                "PathTransmission": 2,
                "EnableCheckAcrossDomain": 1,
                "StaticFileDirectory": ""
            }
        ],
        "EnableService": true,
        "Limit": 100,
        "Offset": 0,
        "RequestId": "c16af20e-8b15-421a-8c4a-c9269e3eb38a",
        "Total": 1
    }
}
```

