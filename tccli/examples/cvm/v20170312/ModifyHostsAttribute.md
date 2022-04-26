**Example 1: 修改CDH实例的属性**

本示例用于用户修改指定CDH实例的HostName属性。

Input: 

```
tccli cvm ModifyHostsAttribute --cli-unfold-argument  \
    --HostIds host-ey16rkyg \
    --HostName webserver
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

