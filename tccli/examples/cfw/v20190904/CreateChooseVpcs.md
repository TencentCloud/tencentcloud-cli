**Example 1: 创建、选择vpc**



Input: 

```
tccli cfw CreateChooseVpcs --cli-unfold-argument  \
    --VpcList xxx \
    --AllZoneList.0.Zone ap-test-5 \
    --AllZoneList.0.Region ap-test
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

