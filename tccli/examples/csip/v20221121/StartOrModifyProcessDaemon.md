**Example 1: 开启机器进程守护**

开启机器进程守护

Input: 

```
tccli csip StartOrModifyProcessDaemon --cli-unfold-argument  \
    --From 1 \
    --Scope 0 \
    --IncludeQuuid d77ca669-e14c-4165-9b53-eb8f42f03609
```

Output: 
```
{
    "Response": {
        "FailedHostCount": 0,
        "RequestId": "b7b001de-252f-481c-b40b-7c275fe6e720"
    }
}
```

