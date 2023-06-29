**Example 1: DescribeNamespaceResources**



Input: 

```
tccli iecp DescribeNamespaceResources --cli-unfold-argument  \
    --EdgeUnitID 1 \
    --Namespace test
```

Output: 
```
{
    "Response": {
        "RequestId": "72d540a0-ed11-4370-b977-96c6c224a1d8",
        "Resources": [
            {
                "Type": "workload",
                "Count": 4,
                "Names": [
                    "test",
                    "test-replace",
                    "test-deployment",
                    "wwww"
                ]
            },
            {
                "Type": "grid",
                "Count": 1,
                "Names": [
                    "hrq-test"
                ]
            }
        ]
    }
}
```

