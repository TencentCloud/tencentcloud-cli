**Example 1: 查看etcd可用版本**



Input: 

```
tccli cetcd DescribeEtcdAvailableVersions --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "32daac92-b940-4894-b9d8-1d325f1ee9d1",
        "Versions": [
            {
                "Name": "etcd",
                "Version": "v3.4.9"
            },
            {
                "Name": "etcd",
                "Version": "v3.3.25"
            }
        ]
    }
}
```

