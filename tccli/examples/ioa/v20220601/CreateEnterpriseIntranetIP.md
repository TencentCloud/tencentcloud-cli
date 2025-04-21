**Example 1: test**

test

Input: 

```
tccli ioa CreateEnterpriseIntranetIP --cli-unfold-argument  \
    --IntranetIP.Name 999999999 \
    --IntranetIP.Type IP \
    --IntranetIP.IP 127.0.0.1
```

Output: 
```
{
    "Response": {
        "RequestId": "9bc22ddb-fe6f-42a0-919d-74cfc75c67eb"
    }
}
```

**Example 2: 测试**

测试

Input: 

```
tccli ioa CreateEnterpriseIntranetIP --cli-unfold-argument  \
    --IntranetIP.Name 测试2 \
    --IntranetIP.Type IPSegment \
    --IntranetIP.IPSegment.0.StartIP 127.0.0.1 \
    --IntranetIP.IPSegment.0.EndIP 127.0.0.2
```

Output: 
```
{
    "Response": {
        "RequestId": "ed9a12e0-9acb-45ff-866b-bcbfb31cda57"
    }
}
```

