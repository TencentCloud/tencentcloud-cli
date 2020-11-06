**Example 1: Modifying the attributes of a CDH instance**

This example shows you how to modify the `HostName` attribute of a specified CDH instance.

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
        "RequestID": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

