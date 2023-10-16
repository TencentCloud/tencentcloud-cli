**Example 1: 查询知识库组件的版本列表**

查询ristretto组件的版本列表

Input: 

```
tccli bsca DescribeKBComponentVersionList --cli-unfold-argument  \
    --PURL.Name ristretto \
    --PURL.Protocol golang \
    --PURL.Namespace  \
    --PURL.Subpath  \
    --PURL.Version 
```

Output: 
```
{
    "Response": {
        "RequestId": "1df9b437-4e92-4ad5-b422-abeb45bbaf03",
        "VersionList": [
            {
                "LicenseExpression": "apache-2.0",
                "PURL": {
                    "Name": "ristretto",
                    "Namespace": "github.com/sergiub32",
                    "Protocol": "golang",
                    "Qualifiers": [],
                    "Subpath": "",
                    "Version": "v0.2.1"
                }
            }
        ]
    }
}
```

