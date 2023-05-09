**Example 1: 升级集群到指定版本**

升级集群到指定版本

Input: 

```
tccli tke UpdateClusterVersion --cli-unfold-argument  \
    --ClusterId cls-xxxxxxxx \
    --DstVersion 1.18.4
```

Output: 
```
{
    "Response": {
        "RequestId": "2ac430cd-f7de-482e-b98e-f78a48e785e8"
    }
}
```

