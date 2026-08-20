**Example 1: 列出 Grafana 可选版本**



Input: 

```
tccli monitor DescribeGrafanaVersions --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Versions": [
            {
                "Version": "v7.4.2",
                "Alias": "v7.4.2"
            }
        ],
        "RequestId": "abc"
    }
}
```

