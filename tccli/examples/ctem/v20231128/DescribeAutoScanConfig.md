**Example 1: 查看情报扫描配置**

查看情报扫描配置

Input: 

```
tccli ctem DescribeAutoScanConfig --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "EnableIntelligenceAutoScan": true,
                "Id": 100136,
                "Name": "22"
            },
            {
                "EnableIntelligenceAutoScan": true,
                "Id": 100151,
                "Name": "test123"
            },
            {
                "EnableIntelligenceAutoScan": true,
                "Id": 100162,
                "Name": "test123"
            }
        ],
        "RequestId": "1ee22341-1273-4b11-902c-d34dc05672e4",
        "Total": 3
    }
}
```

