**Example 1: 获取实例可升级列表**

获取实例可升级列表

Input: 

```
tccli es DescribeUpgrade --cli-unfold-argument  \
    --InstanceId es-f5mwm28u
```

Output: 
```
{
    "Response": {
        "EsVersions": [],
        "EsLicenses": [],
        "RequestId": "783d9290-dc60-4862-9340-10b632605374"
    }
}
```

