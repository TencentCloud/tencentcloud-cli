**Example 1: 查询知识库组件列表**



Input: 

```
tccli bsca MatchKBPURLList --cli-unfold-argument  \
    --SHA1 7ed845de1dfe070d43511fab321784e6c4118398
```

Output: 
```
{
    "Response": {
        "Hit": true,
        "PURLList": [
            {
                "Name": "log4j-core",
                "Namespace": "org.apache.logging.log4j",
                "Protocol": "maven",
                "Qualifiers": [],
                "Subpath": "",
                "Version": "2.5"
            }
        ],
        "RequestId": "3189252f-aad2-44b2-b11c-b51fccd8bf6d"
    }
}
```

