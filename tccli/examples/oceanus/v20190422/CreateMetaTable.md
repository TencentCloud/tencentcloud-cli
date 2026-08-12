**Example 1: 创建元数据表**



Input: 

```
tccli oceanus CreateMetaTable --cli-unfold-argument  \
    --CatalogId 0 \
    --DatabaseId 0 \
    --SqlCode Q1JFQVRFIFRBQkxFIFNvdXJjZVRhYmxlICggICAgICBmX3NlcXVlbmNlIElOVCwgICAgICBmX3JhbmRvbSBJTlQsICAgICAgZl9yYW5kb21fc3RyIFNUUklORyAgKSBXSVRIICggICAgICAnY29ubmVjdG9yJyA9ICdteXNxbC1jZGMnLCAgICAgICdkYXRhYmFzZS1uYW1lJyA9ICd0ZXN0JywgICAgICAnaG9zdG5hbWUnID0gJzEwLjAuMC4xNicsICAgICAgJ3Bhc3N3b3JkJyA9ICdRY2xvdWRWNSEnLCAgICAgICdwb3J0JyA9ICczMzA2JywgICAgICAndGFibGUtbmFtZScgPSAnbXlfdGVzdCcsICAgICAgJ3VzZXJuYW1lJyA9ICdyb290JyApIA== \
    --Comment 维表
```

Output: 
```
{
    "Response": {
        "RequestId": "ff2de498-281d-4b26-8f31-f3cdd9904559",
        "TableId": 0
    }
}
```

