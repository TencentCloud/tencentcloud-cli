**Example 1: 根据AppSid对扫描实例进行删除**

通过传入AppSid集合删除1个或者多个扫描实例

Input: 

```
tccli ms DeleteScanInstances --cli-unfold-argument  \
    --AppSids xyuu-csu-ee78236l hhussxu-hui2677-kk
```

Output: 
```
{
    "Response": {
        "RequestId": "5e93a212-ca01-0fdc-eedd-5a1fce5e83e6",
        "Progress": 1
    }
}
```

