**Example 1: Getting the list of vulnerabilities on server**

This example shows you how to get the list of vulnerabilities on a server.

Input: 

```
tccli yunjing DescribeAgentVuls --cli-unfold-argument  \
    --Uuid add4a78a-0d59-11e8-b7ab-00e081e1a5c5 \
    --VulType WEB \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "AgentVuls": [
            {
                "Id": 4,
                "VulId": 1001,
                "MachineIp": "10.10.120.12",
                "Description": "Vulnerability description",
                "VulName": "Vulnerability name",
                "VulLevel": "HIGHT",
                "VulStatus": "UN_OPERATED",
                "LastScanTime": "2018-03-19 17:38:56"
            }
        ],
        "TotalCount": 10
    }
}
```

